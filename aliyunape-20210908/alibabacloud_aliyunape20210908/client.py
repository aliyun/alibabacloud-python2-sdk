# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aliyunape20210908 import models as aliyunape_20210908_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aliyunape', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def weathermonitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorResponse(),
            self.do_rpcrequest('Weathermonitor', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def weathermonitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.weathermonitor_with_options(request, runtime)

    def weatherforecast_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastTimeResponse(),
            self.do_rpcrequest('WeatherforecastTime', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def weatherforecast_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.weatherforecast_time_with_options(request, runtime)

    def station_day_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.StationDayResponse(),
            self.do_rpcrequest('StationDay', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def station_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.station_day_with_options(request, runtime)

    def weatherforecast_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastResponse(),
            self.do_rpcrequest('Weatherforecast', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def weatherforecast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.weatherforecast_with_options(request, runtime)

    def historical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.HistoricalResponse(),
            self.do_rpcrequest('Historical', '2021-09-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def historical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.historical_with_options(request, runtime)
