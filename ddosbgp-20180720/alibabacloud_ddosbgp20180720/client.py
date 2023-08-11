# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddosbgp20180720 import models as ddosbgp_20180720_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'ddosbgp.aliyuncs.com',
            'cn-beijing': 'ddosbgp.aliyuncs.com',
            'cn-zhangjiakou': 'ddosbgp.aliyuncs.com',
            'cn-huhehaote': 'ddosbgp.aliyuncs.com',
            'cn-hangzhou': 'ddosbgp.aliyuncs.com',
            'cn-shanghai': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen': 'ddosbgp.aliyuncs.com',
            'ap-northeast-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'ddosbgp.aliyuncs.com',
            'eu-central-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-shanghai-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-north-2-gov-1': 'ddosbgp.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddosbgp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIp',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AddIpResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    def check_access_log_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccessLogAuth',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CheckAccessLogAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def check_access_log_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_access_log_auth_with_options(request, runtime)

    def check_grant_with_options(self, request, runtime):
        """
        Indicates whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account. Valid values:
        *   **1**: Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        *   **0**: Anti-DDoS Origin is not authorized to obtain information about the assets within the current Alibaba Cloud account.
        

        @param request: CheckGrantRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckGrantResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckGrant',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CheckGrantResponse(),
            self.call_api(params, req, runtime)
        )

    def check_grant(self, request):
        """
        Indicates whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account. Valid values:
        *   **1**: Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        *   **0**: Anti-DDoS Origin is not authorized to obtain information about the assets within the current Alibaba Cloud account.
        

        @param request: CheckGrantRequest

        @return: CheckGrantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    def config_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not UtilClient.is_unset(request.rule_condition_cnt):
            query['RuleConditionCnt'] = request.rule_condition_cnt
        if not UtilClient.is_unset(request.rule_condition_kpps):
            query['RuleConditionKpps'] = request.rule_condition_kpps
        if not UtilClient.is_unset(request.rule_condition_mbps):
            query['RuleConditionMbps'] = request.rule_condition_mbps
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_undo_begin_time):
            query['RuleUndoBeginTime'] = request.rule_undo_begin_time
        if not UtilClient.is_unset(request.rule_undo_end_time):
            query['RuleUndoEndTime'] = request.rule_undo_end_time
        if not UtilClient.is_unset(request.rule_undo_mode):
            query['RuleUndoMode'] = request.rule_undo_mode
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def config_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_schedrule_on_demand_with_options(request, runtime)

    def create_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not UtilClient.is_unset(request.rule_condition_cnt):
            query['RuleConditionCnt'] = request.rule_condition_cnt
        if not UtilClient.is_unset(request.rule_condition_kpps):
            query['RuleConditionKpps'] = request.rule_condition_kpps
        if not UtilClient.is_unset(request.rule_condition_mbps):
            query['RuleConditionMbps'] = request.rule_condition_mbps
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_undo_begin_time):
            query['RuleUndoBeginTime'] = request.rule_undo_begin_time
        if not UtilClient.is_unset(request.rule_undo_end_time):
            query['RuleUndoEndTime'] = request.rule_undo_end_time
        if not UtilClient.is_unset(request.rule_undo_mode):
            query['RuleUndoMode'] = request.rule_undo_mode
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CreateSchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def create_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_schedrule_on_demand_with_options(request, runtime)

    def delete_blackhole_with_options(self, request, runtime):
        """
        You can call the DeleteBlackhole operation to deactivate blackhole filtering for a protected IP address.
        Before you call this operation, you can call the [DescribePackIpList](~~118701~~) operation to query the protection status of the IP addresses that are protected by your Anti-DDoS Origin instance. For example, you can query whether blackhole filtering is triggered for an IP address.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteBlackholeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBlackholeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBlackhole',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteBlackholeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_blackhole(self, request):
        """
        You can call the DeleteBlackhole operation to deactivate blackhole filtering for a protected IP address.
        Before you call this operation, you can call the [DescribePackIpList](~~118701~~) operation to query the protection status of the IP addresses that are protected by your Anti-DDoS Origin instance. For example, you can query whether blackhole filtering is triggered for an IP address.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteBlackholeRequest

        @return: DeleteBlackholeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    def delete_ip_with_options(self, request, runtime):
        """
        The ID of the Anti-DDoS Origin Enterprise instance.
        >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin Enterprise instances.
        

        @param request: DeleteIpRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIp',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteIpResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip(self, request):
        """
        The ID of the Anti-DDoS Origin Enterprise instance.
        >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin Enterprise instances.
        

        @param request: DeleteIpRequest

        @return: DeleteIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    def delete_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_schedrule_on_demand_with_options(request, runtime)

    def describe_ddos_event_with_options(self, request, runtime):
        """
        The number of entries to return on each page.
        

        @param request: DescribeDdosEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDdosEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosEvent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeDdosEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ddos_event(self, request):
        """
        The number of entries to return on each page.
        

        @param request: DescribeDdosEventRequest

        @return: DescribeDdosEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    def describe_excpetion_count_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *DescribeExcpetionCount**.
        

        @param request: DescribeExcpetionCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExcpetionCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExcpetionCount',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeExcpetionCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_excpetion_count(self, request):
        """
        The operation that you want to perform. Set the value to *DescribeExcpetionCount**.
        

        @param request: DescribeExcpetionCountRequest

        @return: DescribeExcpetionCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_excpetion_count_with_options(request, runtime)

    def describe_instance_list_with_options(self, request, runtime):
        """
        The status of the instance. Valid values:
        *   **1**: normal
        *   **2**: expired
        *   **3**: released
        

        @param request: DescribeInstanceListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.orderdire):
            query['Orderdire'] = request.orderdire
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_list(self, request):
        """
        The status of the instance. Valid values:
        *   **1**: normal
        *   **2**: expired
        *   **3**: released
        

        @param request: DescribeInstanceListRequest

        @return: DescribeInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    def describe_instance_specs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_specs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    def describe_on_demand_ddos_event_with_options(self, request, runtime):
        """
        The ID of the resource group.
        

        @param request: DescribeOnDemandDdosEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOnDemandDdosEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnDemandDdosEvent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_on_demand_ddos_event(self, request):
        """
        The ID of the resource group.
        

        @param request: DescribeOnDemandDdosEventRequest

        @return: DescribeOnDemandDdosEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_ddos_event_with_options(request, runtime)

    def describe_on_demand_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnDemandInstanceStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_on_demand_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_instance_status_with_options(request, runtime)

    def describe_op_entities_with_options(self, request, runtime):
        """
        The start time. Operation logs that were generated after this time are queried.*** This value is a UNIX timestamp. Unit: milliseconds.
        

        @param request: DescribeOpEntitiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_dir):
            query['OrderDir'] = request.order_dir
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOpEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_op_entities(self, request):
        """
        The start time. Operation logs that were generated after this time are queried.*** This value is a UNIX timestamp. Unit: milliseconds.
        

        @param request: DescribeOpEntitiesRequest

        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    def describe_pack_ip_list_with_options(self, request, runtime):
        """
        The number of entries to return on each page.
        

        @param request: DescribePackIpListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePackIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackIpList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribePackIpListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pack_ip_list(self, request):
        """
        The number of entries to return on each page.
        

        @param request: DescribePackIpListRequest

        @return: DescribePackIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_ip_list_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_traffic_with_options(self, request, runtime):
        """
        The bandwidth of attack traffic. Unit: bit/s.
        >  This parameter is returned only if attack traffic exists.
        

        @param request: DescribeTrafficRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ipnet):
            query['Ipnet'] = request.ipnet
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraffic',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_traffic(self, request):
        """
        The bandwidth of attack traffic. Unit: bit/s.
        >  This parameter is returned only if attack traffic exists.
        

        @param request: DescribeTrafficRequest

        @return: DescribeTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    def get_sls_open_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSlsOpenStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.GetSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sls_open_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sls_open_status_with_options(request, runtime)

    def list_opened_access_log_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOpenedAccessLogInstances',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_opened_access_log_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_opened_access_log_instances_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        The ID of the region where the Anti-DDoS Origin instance resides.
        >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        The ID of the region where the Anti-DDoS Origin instance resides.
        >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_remark_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *ModifyRemark**.
        

        @param request: ModifyRemarkRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRemark',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_remark(self, request):
        """
        The operation that you want to perform. Set the value to *ModifyRemark**.
        

        @param request: ModifyRemarkRequest

        @return: ModifyRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_remark_with_options(request, runtime)

    def query_schedrule_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.QuerySchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def query_schedrule_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_schedrule_on_demand_with_options(request, runtime)

    def set_instance_mode_on_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceModeOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.SetInstanceModeOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    def set_instance_mode_on_demand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_instance_mode_on_demand_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        The ID of Anti-DDoS Origin Instance N to which you want to add tags.
        >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        The ID of Anti-DDoS Origin Instance N to which you want to add tags.
        >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
