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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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

    def ape_inner_common_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApeInnerCommonApi',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.ApeInnerCommonApiResponse(),
            self.call_api(params, req, runtime)
        )

    def ape_inner_common_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.ape_inner_common_api_with_options(request, runtime)

    def historical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['OrderId'] = request.order_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['Station'] = request.station
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='Historical',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.HistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    def historical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.historical_with_options(request, runtime)

    def station_day_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OrderId'] = request.order_id
        query['StartForecast'] = request.start_forecast
        query['Station'] = request.station
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StationDay',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.StationDayResponse(),
            self.call_api(params, req, runtime)
        )

    def station_day(self, request):
        runtime = util_models.RuntimeOptions()
        return self.station_day_with_options(request, runtime)

    def weatherforecast_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Lat'] = request.lat
        query['Lon'] = request.lon
        query['OrderId'] = request.order_id
        query['StartForecast'] = request.start_forecast
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='Weatherforecast',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastResponse(),
            self.call_api(params, req, runtime)
        )

    def weatherforecast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.weatherforecast_with_options(request, runtime)

    def weatherforecast_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurHour'] = request.cur_hour
        query['Lat'] = request.lat
        query['Lon'] = request.lon
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='WeatherforecastTime',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeatherforecastTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def weatherforecast_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.weatherforecast_time_with_options(request, runtime)

    def weathermonitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CurHour'] = request.cur_hour
        query['OrderId'] = request.order_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='Weathermonitor',
            version='2021-09-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            aliyunape_20210908_models.WeathermonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def weathermonitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.weathermonitor_with_options(request, runtime)
