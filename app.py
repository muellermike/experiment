import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, make_response, current_app, flash
from flask_cors import CORS
from controllers.users_controller import users_endpoint
from controllers.exercises_controller import exercises_endpoint
from controllers.userexperiments_controller import experiments_endpoint
from services.experiment_service import download_experiment_data

app = Flask(__name__)
app.register_blueprint(users_endpoint)
app.register_blueprint(exercises_endpoint)
app.register_blueprint(experiments_endpoint)

CORS(app)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/download', methods=['POST'])
def download():
   name = request.form.get('experimentname')
   password = request.form.get('password')
   
   if (password != current_app.config["DATA_PW"]):
       #flash('Cannot load experiment data')
       return redirect('/')


   df = download_experiment_data(name)

   return create_csv(df)
   #if name:
   #    print('Request for hello page received with name=%s' % name)
   #    return render_template('hello.html', name = name)
   #else:
   #    print('Request for hello page received with no name or blank name -- redirecting')
   #    return redirect(url_for('index'))

def create_csv(df):
    csv_data = df.to_csv(index=False)
    response = make_response(csv_data)
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers['Content-Type'] = 'text/csv'
    return response

if __name__ == '__main__':
    app.run()