from flask import current_app
from datalayers.experiment_datalayer import load_user_experiment, get_experiment_by_name, store_experiment_participation, store_experiment_exercises, update_experiment_endtime
from models.experiment import Experiment
from services.exercise_service import get_exercises, get_experiment_exercises
from services.user_service import find_user_by_id

def create_experiment(experiment: Experiment):
    """
    implements the logic to create a new experiment. This means that first the user-experiment connection
    is established by inserting a userexperiment in the database. 
    After positive, random 12 questions of each task are loaded and stored into the database.
    """
    experiment_id = get_experiment_by_name(experiment.experiment_name)

    if(experiment_id is None):
        return None
    
    # the user-experiment connection is stored with the corresponding foreign keys.
    result = store_experiment_participation(experiment, experiment_id)

    # save the generated participation id into the experiment object
    experiment.id = result
    
    exercises = get_experiment_exercises(current_app.config["NUMBER_OF_EXERCISES"], experiment_id)
    
    store_experiment_exercises(exercises, experiment)
    
    return result

def update_experiment(experiment: Experiment):
    """
    implements the logic to update an existing experiment. This means that first it is checked whether the experiment participation exists and has this experiment.
    After that all allowed updated are executed.
    """
    # UPDATE endtime of experiment when the endtime is not set yet (logic in SQL Statement)
    result = update_experiment_endtime(experiment)

    return result