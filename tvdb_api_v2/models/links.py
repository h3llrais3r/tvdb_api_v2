# coding: utf-8

"""
    TheTVDB API v2

    API v2 targets v1 functionality with a few minor additions. The API is accessible via https://api.thetvdb.com and provides the following REST endpoints in JSON format.   How to use this API documentation ----------------   You may browse the API routes without authentication, but if you wish to send requests to the API and see response data, then you must authenticate. 1. Obtain a JWT token by `POST`ing  to the `/login` route in the `Authentication` section with your API key and credentials. 1. Paste the JWT token from the response into the \"JWT Token\" field at the top of the page and click the 'Add Token' button.   You will now be able to use the remaining routes to send requests to the API and get a response.   Language Selection ----------------   Language selection is done via the `Accept-Language` header. At the moment, you may only pass one language abbreviation in the header at a time. Valid language abbreviations can be found at the `/languages` route..   Authentication ----------------   Authentication to use the API is similar to the How-to section above. Users must `POST` to the `/login` route with their API key and credentials in the following format in order to obtain a JWT token.  `{\"apikey\":\"APIKEY\",\"username\":\"USERNAME\",\"userkey\":\"USERKEY\"}`  Note that the username and key are ONLY required for the `/user` routes. The user's key is labled `Account Identifier` in the account section of the main site. The token is then used in all subsequent requests by providing it in the `Authorization` header. The header will look like: `Authorization: Bearer <yourJWTtoken>`. Currently, the token expires after 24 hours. You can `GET` the `/refresh_token` route to extend that expiration date.   Versioning ----------------   You may request a different version of the API by including an `Accept` header in your request with the following format: `Accept:application/vnd.thetvdb.v$VERSION`. This documentation automatically uses the version seen at the top and bottom of the page.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first': 'int',
        'last': 'int',
        'next': 'int',
        'previous': 'int'
    }

    attribute_map = {
        'first': 'first',
        'last': 'last',
        'next': 'next',
        'previous': 'previous'
    }

    def __init__(self, first=None, last=None, next=None, previous=None):
        """
        Links - a model defined in Swagger
        """

        self._first = None
        self._last = None
        self._next = None
        self._previous = None

        if first is not None:
          self.first = first
        if last is not None:
          self.last = last
        if next is not None:
          self.next = next
        if previous is not None:
          self.previous = previous

    @property
    def first(self):
        """
        Gets the first of this Links.

        :return: The first of this Links.
        :rtype: int
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this Links.

        :param first: The first of this Links.
        :type: int
        """

        self._first = first

    @property
    def last(self):
        """
        Gets the last of this Links.

        :return: The last of this Links.
        :rtype: int
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this Links.

        :param last: The last of this Links.
        :type: int
        """

        self._last = last

    @property
    def next(self):
        """
        Gets the next of this Links.

        :return: The next of this Links.
        :rtype: int
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this Links.

        :param next: The next of this Links.
        :type: int
        """

        self._next = next

    @property
    def previous(self):
        """
        Gets the previous of this Links.

        :return: The previous of this Links.
        :rtype: int
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this Links.

        :param previous: The previous of this Links.
        :type: int
        """

        self._previous = previous

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
