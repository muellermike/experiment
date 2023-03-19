# coding: utf-8

from __future__ import absolute_import
from datetime import datetime

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class ExerciseAnswer(Model):

    def __init__(self, answer: str=None, experiment_id: int=None, text_id: int=None, image_id: int=None, time: datetime=None, time_to_click: int=None, time_to_submit: int=None):  # noqa: E501
        """ExerciseAnswer - a model defined in Swagger

        :param answer: The answer of this Experiment Exercise.  # noqa: E501
        :type answer: string
        :param experiment_id: The experiment_id of this Recording.  # noqa: E501
        :type experiment_id: int
        :param image_id: The image_id of this Recording.  # noqa: E501
        :type image_id: int
        :param text_id: The text_id of this Recording.  # noqa: E501
        :type text_id: int
        """
        self.swagger_types = {
            'answer': str,
            'experiment_id': int,
            'text_id': int,
            'image_id': int,
            'time': datetime,
            'time_to_click': int,
            'time_to_submit': int
        }

        self.attribute_map = {
            'answer': 'answer',
            'experiment_id': 'experimentId',
            'image_id': 'imageId',
            'text_id': 'textId',
            'time': 'time',
            'time_to_click': 'timeToClick',
            'time_to_submit': 'timeToSubmit'
        }

        self._answer = answer
        self._experiment_id = experiment_id
        self._image_id = image_id
        self._text_id = text_id
        self._time = time
        self._time_to_click = time_to_click
        self._time_to_submit = time_to_submit

    @classmethod
    def from_dict(cls, dikt) -> 'ExerciseAnswer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExerciseAnswer of this ExerciseAnswer.  # noqa: E501
        :rtype: ExerciseAnswer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def answer(self) -> str:
        """Gets the answer of this ExerciseAnswer.


        :return: The answer of this ExerciseAnswer.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Sets the anser of this ExerciseAnswer.


        :param answer: The answer of this ExerciseAnswer.
        :type answer: str
        """
        if answer is None:
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer

    @property
    def experiment_id(self) -> int:
        """Gets the experiment_id of this ExerciseAnswer.


        :return: The experiment_id of this ExerciseAnswer.
        :rtype: int
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id: int):
        """Sets the experiment_id of this ExerciseAnswer.


        :param experiment_id: The experiment_id of this ExerciseAnswer.
        :type experiment_id: int
        """

        self._experiment_id = experiment_id

    @property
    def image_id(self) -> int:
        """Gets the image_id of this ExerciseAnswer.


        :return: The image_id of this ExerciseAnswer.
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id: int):
        """Sets the image_id of this ExerciseAnswer.


        :param image_id: The image_id of this ExerciseAnswer.
        :type image_id: int
        """

        self._image_id = image_id

    @property
    def text_id(self) -> int:
        """Gets the text_id of this ExerciseAnswer.


        :return: The text_id of this ExerciseAnswer.
        :rtype: int
        """
        return self._text_id

    @text_id.setter
    def text_id(self, text_id: int):
        """Sets the text_id of this ExerciseAnswer.


        :param text_id: The text_id of this ExerciseAnswer.
        :type text_id: int
        """

        self._text_id = text_id

    @property
    def time(self) -> datetime:
        """Gets the time of this ExerciseAnswer.


        :return: The time of this ExerciseAnswer.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this ExerciseAnswer.


        :param end: The time of this ExerciseAnswer.
        :type time: datetime
        """

        self._time = time

    @property
    def time_to_click(self) -> int:
        """Gets the time to click of this ExerciseAnswer.


        :return: The time to click of this ExerciseAnswer.
        :rtype: int
        """
        return self._time_to_click

    @time_to_click.setter
    def time_to_click(self, time_to_click: int):
        """Sets the time to click of this ExerciseAnswer.


        :param time to click: The time to click of this ExerciseAnswer.
        :type time to click: int
        """

        self._time_to_click = time_to_click

    @property
    def time_to_submit(self) -> int:
        """Gets the time to submit of this ExerciseAnswer.


        :return: The time to submit of this ExerciseAnswer.
        :rtype: int
        """
        return self._time_to_submit

    @time_to_submit.setter
    def time_to_submit(self, time_to_submit: int):
        """Sets the time to submit of this ExerciseAnswer.


        :param time to submit: The time to submit of this ExerciseAnswer.
        :type time to submit: int
        """

        self._time_to_submit = time_to_submit