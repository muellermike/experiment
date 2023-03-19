from cgitb import reset
from unittest import result
import six

from flask import Blueprint, request, jsonify
from services.exercise_service import update_exercise_answer
from models.exercise_answer import ExerciseAnswer
import util

exercises_endpoint = Blueprint('exercises_endpoint', __name__)

@exercises_endpoint.route('/exercises', methods=['PUT'])
def update_exercise():  # noqa: E501
    """Update the experiment exercise with the provided answer

     # noqa: E501

    :param body: ExerciseAnswer object that needs to be added to a experiment exercise.
    :type body: dict | bytes

    :rtype: None
    """
    body = ExerciseAnswer.from_dict(request.get_json())  # noqa: E501

    result = update_exercise_answer(body)
    
    return jsonify(result)
