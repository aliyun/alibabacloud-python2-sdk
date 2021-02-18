# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_geoip20200101 import models as geoip_20200101_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('geoip', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_geoip_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeGeoipInstanceResponse().from_map(
            self.do_rpcrequest('DescribeGeoipInstance', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_geoip_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_geoip_instance_with_options(request, runtime)

    def describe_geoip_instance_data_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeGeoipInstanceDataInfosResponse().from_map(
            self.do_rpcrequest('DescribeGeoipInstanceDataInfos', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_geoip_instance_data_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_geoip_instance_data_infos_with_options(request, runtime)

    def describe_geoip_instance_data_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeGeoipInstanceDataUrlResponse().from_map(
            self.do_rpcrequest('DescribeGeoipInstanceDataUrl', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_geoip_instance_data_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_geoip_instance_data_url_with_options(request, runtime)

    def describe_geoip_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeGeoipInstancesResponse().from_map(
            self.do_rpcrequest('DescribeGeoipInstances', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_geoip_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_geoip_instances_with_options(request, runtime)

    def describe_geoip_instance_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeGeoipInstanceStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeGeoipInstanceStatistics', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_geoip_instance_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_geoip_instance_statistics_with_options(request, runtime)

    def describe_ipv_4location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeIpv4LocationResponse().from_map(
            self.do_rpcrequest('DescribeIpv4Location', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_4location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_4location_with_options(request, runtime)

    def describe_ipv_6location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return geoip_20200101_models.DescribeIpv6LocationResponse().from_map(
            self.do_rpcrequest('DescribeIpv6Location', '2020-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6location_with_options(request, runtime)
