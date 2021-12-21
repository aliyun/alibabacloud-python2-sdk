# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vdc20201214 import models as vdc_20201214_models
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
        self._endpoint = self.get_endpoint('vdc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def delete_app_exp_metric_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_exp_metric_rule_with_options(request, headers, runtime)

    def delete_app_exp_metric_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppExpMetricRule',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/deleteAppExpMetricRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DeleteAppExpMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_follow_call_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_follow_call_rule_with_options(request, headers, runtime)

    def delete_app_follow_call_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppFollowCallRule',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/deleteAppFollowCallRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DeleteAppFollowCallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_config(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_config_with_options(request, headers, runtime)

    def describe_app_config_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/describeAppConfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_exp_metric_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_exp_metric_rule_with_options(request, headers, runtime)

    def describe_app_exp_metric_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppExpMetricRule',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/describeAppExpMetricRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppExpMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_exp_metric_rule_list(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_exp_metric_rule_list_with_options(headers, runtime)

    def describe_app_exp_metric_rule_list_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppExpMetricRuleList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/describeAppExpMetricRuleList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppExpMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_follow_call_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_follow_call_rule_with_options(request, headers, runtime)

    def describe_app_follow_call_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppFollowCallRule',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/describeAppFollowCallRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppFollowCallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_follow_call_rule_list(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_follow_call_rule_list_with_options(headers, runtime)

    def describe_app_follow_call_rule_list_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppFollowCallRuleList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/describeAppFollowCallRuleList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeAppFollowCallRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_call(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_with_options(request, headers, runtime)

    def describe_call_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not UtilClient.is_unset(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCall',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeCall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_call_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_list_with_options(request, headers, runtime)

    def describe_call_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_status):
            query['CallStatus'] = request.call_status
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeCallList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_call_list_test(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_list_test_with_options(request, headers, runtime)

    def describe_call_list_test_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallListTest',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeCallListTest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallListTestResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_call_user_exp(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_call_user_exp_with_options(request, headers, runtime)

    def describe_call_user_exp_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallUserExp',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeCallUserExp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeCallUserExpResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_area_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_area_distribution_stat_data_with_options(request, headers, runtime)

    def describe_channel_area_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAreaDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeChannelAreaDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_distribution_stat_data_with_options(request, headers, runtime)

    def describe_channel_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeChannelDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_join_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_join_info_with_options(request, headers, runtime)

    def describe_channel_join_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelJoinInfo',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeChannelJoinInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelJoinInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_overall_data_with_options(request, headers, runtime)

    def describe_channel_overall_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelOverallData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeChannelOverallData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_top_pub_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_top_pub_user_list_with_options(request, headers, runtime)

    def describe_channel_top_pub_user_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelTopPubUserList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeChannelTopPubUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelTopPubUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_user_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_channel_user_metrics_with_options(request, headers, runtime)

    def describe_channel_user_metrics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUserMetrics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeChannelUserMetrics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeChannelUserMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_end_point_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_end_point_event_list_with_options(request, headers, runtime)

    def describe_end_point_event_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointEventList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeEndPointEventList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeEndPointEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_end_point_metric_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_end_point_metric_data_with_options(request, headers, runtime)

    def describe_end_point_metric_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not UtilClient.is_unset(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointMetricData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeEndPointMetricData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeEndPointMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_factor_distribution_stat(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_factor_distribution_stat_with_options(request, headers, runtime)

    def describe_fault_diagnosis_factor_distribution_stat_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisFactorDistributionStat',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/diagnosis/describeFaultDiagnosisFactorDistributionStat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_overall_data_with_options(request, headers, runtime)

    def describe_fault_diagnosis_overall_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisOverallData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/diagnosis/describeFaultDiagnosisOverallData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_user_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_user_detail_with_options(request, headers, runtime)

    def describe_fault_diagnosis_user_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.fault_type):
            query['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserDetail',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/diagnosis/describeFaultDiagnosisUserDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_fault_diagnosis_user_list_with_options(request, headers, runtime)

    def describe_fault_diagnosis_user_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/diagnosis/describeFaultDiagnosisUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeFaultDiagnosisUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ice_dur_period_by_day_sub_type(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ice_dur_period_by_day_sub_type_with_options(request, headers, runtime)

    def describe_ice_dur_period_by_day_sub_type_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIceDurPeriodByDaySubType',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/ice/describeIceDurPeriodByDaySubType',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeIceDurPeriodByDaySubTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ice_dur_summary_overview(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ice_dur_summary_overview_with_options(request, headers, runtime)

    def describe_ice_dur_summary_overview_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cur_ts):
            query['CurTs'] = request.cur_ts
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIceDurSummaryOverview',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/ice/describeIceDurSummaryOverview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeIceDurSummaryOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pub_user_list_by_sub_user(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pub_user_list_by_sub_user_with_options(request, headers, runtime)

    def describe_pub_user_list_by_sub_user_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePubUserListBySubUser',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describePubUserListBySubUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribePubUserListBySubUserResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_qoe_metric_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_qoe_metric_data_with_options(request, headers, runtime)

    def describe_qoe_metric_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQoeMetricData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeQoeMetricData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQoeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_area_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_area_distribution_stat_data_with_options(request, headers, runtime)

    def describe_quality_area_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityAreaDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/quality/describeQualityAreaDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_distribution_stat_data_with_options(request, headers, runtime)

    def describe_quality_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/quality/describeQualityDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_os_sdk_version_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_os_sdk_version_distribution_stat_data_with_options(request, headers, runtime)

    def describe_quality_os_sdk_version_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOsSdkVersionDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/quality/describeQualityOsSdkVersionDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_quality_overall_data_with_options(request, headers, runtime)

    def describe_quality_overall_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOverallData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/quality/describeQualityOverallData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeQualityOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_channel_details(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_details_with_options(request, headers, runtime)

    def describe_rtc_channel_details_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelDetails',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeRtcChannelDetails',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_channel_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_list_with_options(request, headers, runtime)

    def describe_rtc_channel_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeRtcChannelList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_channel_metric_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_metric_list_with_options(request, headers, runtime)

    def describe_rtc_channel_metric_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.pub_uid):
            query['PubUid'] = request.pub_uid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_uid):
            query['SubUid'] = request.sub_uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelMetricList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeRtcChannelMetricList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_channel_users(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_channel_users_with_options(request, headers, runtime)

    def describe_rtc_channel_users_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/channel/describeRtcChannelUsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcChannelUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_record_metric_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_record_metric_data_with_options(request, headers, runtime)

    def describe_rtc_record_metric_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcRecordMetricData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/record/describeRtcRecordMetricData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcRecordMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_user_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rtc_user_event_list_with_options(request, headers, runtime)

    def describe_rtc_user_event_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcUserEventList',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/call/describeRtcUserEventList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeRtcUserEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_area_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_area_distribution_stat_data_with_options(request, headers, runtime)

    def describe_usage_area_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageAreaDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/usage/describeUsageAreaDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_distribution_stat_data_with_options(request, headers, runtime)

    def describe_usage_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/usage/describeUsageDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_os_sdk_version_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_os_sdk_version_distribution_stat_data_with_options(request, headers, runtime)

    def describe_usage_os_sdk_version_distribution_stat_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOsSdkVersionDistributionStatData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/usage/describeUsageOsSdkVersionDistributionStatData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_usage_overall_data_with_options(request, headers, runtime)

    def describe_usage_overall_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOverallData',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/usage/describeUsageOverallData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.DescribeUsageOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_exp_metric_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_exp_metric_rule_with_options(request, headers, runtime)

    def update_app_exp_metric_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppExpMetricRule',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/updateAppExpMetricRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.UpdateAppExpMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_follow_call_rule(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_follow_call_rule_with_options(request, headers, runtime)

    def update_app_follow_call_rule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppFollowCallRule',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/api/config/updateAppFollowCallRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            vdc_20201214_models.UpdateAppFollowCallRuleResponse(),
            self.call_api(params, req, runtime)
        )
