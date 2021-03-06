# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_bandwidth_profile_type import TapiCommonBandwidthProfileType  # noqa: F401,E501
from tapi_server.models.tapi_common_capacity_value import TapiCommonCapacityValue  # noqa: F401,E501
from tapi_server import util


class TapiCommonBandwidthProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, committed_information_rate=None, coupling_flag=False, bw_profile_type=None, peak_information_rate=None, committed_burst_size=None, peak_burst_size=None, color_aware=False):  # noqa: E501
        """TapiCommonBandwidthProfile - a model defined in OpenAPI

        :param committed_information_rate: The committed_information_rate of this TapiCommonBandwidthProfile.  # noqa: E501
        :type committed_information_rate: TapiCommonCapacityValue
        :param coupling_flag: The coupling_flag of this TapiCommonBandwidthProfile.  # noqa: E501
        :type coupling_flag: bool
        :param bw_profile_type: The bw_profile_type of this TapiCommonBandwidthProfile.  # noqa: E501
        :type bw_profile_type: TapiCommonBandwidthProfileType
        :param peak_information_rate: The peak_information_rate of this TapiCommonBandwidthProfile.  # noqa: E501
        :type peak_information_rate: TapiCommonCapacityValue
        :param committed_burst_size: The committed_burst_size of this TapiCommonBandwidthProfile.  # noqa: E501
        :type committed_burst_size: TapiCommonCapacityValue
        :param peak_burst_size: The peak_burst_size of this TapiCommonBandwidthProfile.  # noqa: E501
        :type peak_burst_size: TapiCommonCapacityValue
        :param color_aware: The color_aware of this TapiCommonBandwidthProfile.  # noqa: E501
        :type color_aware: bool
        """
        self.openapi_types = {
            'committed_information_rate': TapiCommonCapacityValue,
            'coupling_flag': bool,
            'bw_profile_type': TapiCommonBandwidthProfileType,
            'peak_information_rate': TapiCommonCapacityValue,
            'committed_burst_size': TapiCommonCapacityValue,
            'peak_burst_size': TapiCommonCapacityValue,
            'color_aware': bool
        }

        self.attribute_map = {
            'committed_information_rate': 'committed-information-rate',
            'coupling_flag': 'coupling-flag',
            'bw_profile_type': 'bw-profile-type',
            'peak_information_rate': 'peak-information-rate',
            'committed_burst_size': 'committed-burst-size',
            'peak_burst_size': 'peak-burst-size',
            'color_aware': 'color-aware'
        }

        self._committed_information_rate = committed_information_rate
        self._coupling_flag = coupling_flag
        self._bw_profile_type = bw_profile_type
        self._peak_information_rate = peak_information_rate
        self._committed_burst_size = committed_burst_size
        self._peak_burst_size = peak_burst_size
        self._color_aware = color_aware

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonBandwidthProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.BandwidthProfile of this TapiCommonBandwidthProfile.  # noqa: E501
        :rtype: TapiCommonBandwidthProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def committed_information_rate(self):
        """Gets the committed_information_rate of this TapiCommonBandwidthProfile.


        :return: The committed_information_rate of this TapiCommonBandwidthProfile.
        :rtype: TapiCommonCapacityValue
        """
        return self._committed_information_rate

    @committed_information_rate.setter
    def committed_information_rate(self, committed_information_rate):
        """Sets the committed_information_rate of this TapiCommonBandwidthProfile.


        :param committed_information_rate: The committed_information_rate of this TapiCommonBandwidthProfile.
        :type committed_information_rate: TapiCommonCapacityValue
        """

        self._committed_information_rate = committed_information_rate

    @property
    def coupling_flag(self):
        """Gets the coupling_flag of this TapiCommonBandwidthProfile.

        none  # noqa: E501

        :return: The coupling_flag of this TapiCommonBandwidthProfile.
        :rtype: bool
        """
        return self._coupling_flag

    @coupling_flag.setter
    def coupling_flag(self, coupling_flag):
        """Sets the coupling_flag of this TapiCommonBandwidthProfile.

        none  # noqa: E501

        :param coupling_flag: The coupling_flag of this TapiCommonBandwidthProfile.
        :type coupling_flag: bool
        """

        self._coupling_flag = coupling_flag

    @property
    def bw_profile_type(self):
        """Gets the bw_profile_type of this TapiCommonBandwidthProfile.


        :return: The bw_profile_type of this TapiCommonBandwidthProfile.
        :rtype: TapiCommonBandwidthProfileType
        """
        return self._bw_profile_type

    @bw_profile_type.setter
    def bw_profile_type(self, bw_profile_type):
        """Sets the bw_profile_type of this TapiCommonBandwidthProfile.


        :param bw_profile_type: The bw_profile_type of this TapiCommonBandwidthProfile.
        :type bw_profile_type: TapiCommonBandwidthProfileType
        """

        self._bw_profile_type = bw_profile_type

    @property
    def peak_information_rate(self):
        """Gets the peak_information_rate of this TapiCommonBandwidthProfile.


        :return: The peak_information_rate of this TapiCommonBandwidthProfile.
        :rtype: TapiCommonCapacityValue
        """
        return self._peak_information_rate

    @peak_information_rate.setter
    def peak_information_rate(self, peak_information_rate):
        """Sets the peak_information_rate of this TapiCommonBandwidthProfile.


        :param peak_information_rate: The peak_information_rate of this TapiCommonBandwidthProfile.
        :type peak_information_rate: TapiCommonCapacityValue
        """

        self._peak_information_rate = peak_information_rate

    @property
    def committed_burst_size(self):
        """Gets the committed_burst_size of this TapiCommonBandwidthProfile.


        :return: The committed_burst_size of this TapiCommonBandwidthProfile.
        :rtype: TapiCommonCapacityValue
        """
        return self._committed_burst_size

    @committed_burst_size.setter
    def committed_burst_size(self, committed_burst_size):
        """Sets the committed_burst_size of this TapiCommonBandwidthProfile.


        :param committed_burst_size: The committed_burst_size of this TapiCommonBandwidthProfile.
        :type committed_burst_size: TapiCommonCapacityValue
        """

        self._committed_burst_size = committed_burst_size

    @property
    def peak_burst_size(self):
        """Gets the peak_burst_size of this TapiCommonBandwidthProfile.


        :return: The peak_burst_size of this TapiCommonBandwidthProfile.
        :rtype: TapiCommonCapacityValue
        """
        return self._peak_burst_size

    @peak_burst_size.setter
    def peak_burst_size(self, peak_burst_size):
        """Sets the peak_burst_size of this TapiCommonBandwidthProfile.


        :param peak_burst_size: The peak_burst_size of this TapiCommonBandwidthProfile.
        :type peak_burst_size: TapiCommonCapacityValue
        """

        self._peak_burst_size = peak_burst_size

    @property
    def color_aware(self):
        """Gets the color_aware of this TapiCommonBandwidthProfile.

        none  # noqa: E501

        :return: The color_aware of this TapiCommonBandwidthProfile.
        :rtype: bool
        """
        return self._color_aware

    @color_aware.setter
    def color_aware(self, color_aware):
        """Sets the color_aware of this TapiCommonBandwidthProfile.

        none  # noqa: E501

        :param color_aware: The color_aware of this TapiCommonBandwidthProfile.
        :type color_aware: bool
        """

        self._color_aware = color_aware
