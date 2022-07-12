# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_antiddos_public20170518 import models as antiddos_public_20170518_models
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
        self._endpoint = self.get_endpoint('antiddos-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_bgp_pack_by_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBgpPackByIp',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeBgpPackByIpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bgp_pack_by_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_pack_by_ip_with_options(request, runtime)

    def describe_cap_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.beg_time):
            query['BegTime'] = request.beg_time
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCap',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeCapResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cap(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cap_with_options(request, runtime)

    def describe_ddos_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosCount',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_count_with_options(request, runtime)

    def describe_ddos_credit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosCredit',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosCreditResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_credit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_credit_with_options(request, runtime)

    def describe_ddos_event_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosEventList',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_list_with_options(request, runtime)

    def describe_ddos_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeDdosThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_threshold_with_options(request, runtime)

    def describe_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    def describe_instance_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_status):
            query['DdosStatus'] = request.ddos_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ip):
            query['InstanceIp'] = request.instance_ip
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpAddress',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeInstanceIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_ip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ip_address_with_options(request, runtime)

    def describe_ip_ddos_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.ddos_type):
            query['DdosType'] = request.ddos_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpDdosThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeIpDdosThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_ddos_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_ddos_threshold_with_options(request, runtime)

    def describe_ip_location_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpLocationService',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeIpLocationServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_location_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_location_service_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def modify_ddos_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDdosStatus',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.ModifyDdosStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ddos_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ddos_status_with_options(request, runtime)

    def modify_defense_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bps):
            query['Bps'] = request.bps
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_ip):
            query['InternetIp'] = request.internet_ip
        if not UtilClient.is_unset(request.is_auto):
            query['IsAuto'] = request.is_auto
        if not UtilClient.is_unset(request.pps):
            query['Pps'] = request.pps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefenseThreshold',
            version='2017-05-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            antiddos_public_20170518_models.ModifyDefenseThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_defense_threshold(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_defense_threshold_with_options(request, runtime)
