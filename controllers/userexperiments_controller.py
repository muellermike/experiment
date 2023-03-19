from crypt import methods
from unittest import result
import six
from flask import Blueprint, abort, request, jsonify
from models.experiment import Experiment  # noqa: E501
import util
from services.exercise_service import get_next_random_exercise
from services.experiment_service import create_experiment, update_experiment

experiments_endpoint = Blueprint('experiments_endpoint', __name__)

@experiments_endpoint.route('/experiment-participations', methods=['POST'])
def add_experiment_participation():  # noqa: E501
    """Add a new experiment to a user

     # noqa: E501

    :param body: Experiment object that needs to be added to a user.
    :type body: dict | bytes

    :rtype: None
    """
    print(request.get_json())
    body = Experiment.from_dict(request.get_json())  # noqa: E501
    result = create_experiment(body)

    if not result:
        abort(404)

    return jsonify(result)

@experiments_endpoint.route('/experiment-participations/<experiment_id>', methods=['PUT'])
def update_experiment_endpoint(experiment_id):
    # it is only allowed to update the endtime of the experiment
    body = Experiment.from_dict(request.get_json())
    body.id = experiment_id
    
    result = update_experiment(body)

    if result is None:
        abort(404)
    elif result is False:
        abort(409)

    result = True
    return jsonify(result)

@experiments_endpoint.route('/experiment-participations/<experiment_id>/exercises/next', methods=['GET'])
def get_next_exercise(experiment_id):  # noqa: E501
    """Get next exercise for this specific experiment of this user

     # noqa: E501

    :param experimentId: Experiment ID to retrieve
    :type experimentId: int

    :rtype: Exercise
    """

    result = get_next_random_exercise(experiment_id)

    # if result is None than there is no experiment for the experimentid and userid
    if result is None:
        abort(404, "No experiment found with provided parameters")
    # if result is () than there are no more exercises to answer
    elif not result:
        return ('', 204)
    
    print(result)
    # bring response in the required format
    exercise = {
        "text": {
            "textId": result["TextID"],
            "text": result["Text"],
        },
        "image": {
            "imageId": result["ImageID"],
            "mimeType": result["Mimetype"],
            "encodedString": result["EncodedString"]
        }
    }

    return jsonify(exercise)
