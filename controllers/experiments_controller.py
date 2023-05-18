from crypt import methods
from flask import Blueprint, abort, request, jsonify
from models.experiment import Experiment  # noqa: E501
from services.exercise_service import get_next_random_exercise
from services.experiment_service import get_experiment_by_name_service

experiments_endpoint = Blueprint('experiments_endpoint', __name__)

@experiments_endpoint.route('/experiments/<experiment_name>', methods=['GET'])
def get_experiment_information_endpoint(experiment_name):
    """
    Get the information for one experiment
    """
    experiment_info = get_experiment_by_name_service(experiment_name)

    # if result is None than there is no experiment for the experimentid and userid
    if experiment_info is None:
        abort(404, "No experiment found with provided parameters")
    # if result is () than there are no more exercises to answer
    elif not experiment_info:
        return ('', 204)
    
    # bring response in the required format
    experiment = {
        "introduction": experiment_info["Introduction"],
        "nextButtonText": experiment_info["NextText"],
        "numOfExercises": experiment_info["NumberOfExercises"]
    }

    return jsonify(experiment)