# coding: utf-8

from __future__ import absolute_import

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, unique_id: int=None, gender: str=None, age: int=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param gender: The gender of this User.  # noqa: E501
        :type gender: string
        :param age: The age of this User.  # noqa: E501
        :type age: int
        """
        self.swagger_types = {
            'id': str,
            'unique_id': int,
            'gender': str,
            'age': int
        }

        self.attribute_map = {
            'id': 'id',
            'unique_id': 'uniqueId',
            'gender': 'gender',
            'age': 'age'
        }

        self._id = id
        self._unique_id = unique_id
        self._gender = gender
        self._age = age

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def unique_id(self) -> int:
        """Gets the unique_id of this User.


        :return: The unique_id of this User.
        :rtype: int
        """
        return self._unique_id

    @id.setter
    def unique_id(self, unique_id: int):
        """Sets the unique_id of this User.


        :param id: The unique_id of this User.
        :type unique_id: int
        """

        self._unique_id = unique_id

    @property
    def gender(self) -> str:
        """Gets the gender of this User.


        :return: The gender of this User.
        :rtype: string
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this User.


        :param gender: The gender of this User.
        :type gender: string
        """

        self._gender = gender

    @property
    def age(self) -> int:
        """Gets the age of this User.


        :return: The age of this User.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this User.


        :param age: The age of this User.
        :type age: int
        """

        self._age = age