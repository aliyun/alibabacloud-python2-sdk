# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloud_siem20220616 import models as cloud_siem_20220616_models
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
        self._endpoint = self.get_endpoint('cloud-siem', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_job_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobCheck',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_job_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_job_check_with_options(request, runtime)

    def batch_job_submit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_config):
            body['JsonConfig'] = request.json_config
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchJobSubmit',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.BatchJobSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_job_submit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_job_submit_with_options(request, runtime)

    def close_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.CloseDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def close_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_delivery_with_options(request, runtime)

    def delete_automate_response_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutomateResponseConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteAutomateResponseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_automate_response_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_automate_response_config_with_options(request, runtime)

    def delete_customize_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_customize_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_customize_rule_with_options(request, runtime)

    def delete_quick_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_name):
            body['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quick_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quick_query_with_options(request, runtime)

    def delete_white_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DeleteWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_white_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_white_rule_list_with_options(request, runtime)

    def describe_aggregate_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAggregateFunction',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAggregateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aggregate_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aggregate_function_with_options(request, runtime)

    def describe_alert_scene_by_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSceneByEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSceneByEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_scene_by_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_scene_by_event_with_options(request, runtime)

    def describe_alert_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_source_with_options(request, runtime)

    def describe_alert_source_with_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertSourceWithEvent',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertSourceWithEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_source_with_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_source_with_event_with_options(request, runtime)

    def describe_alert_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertType',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alert_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_type_with_options(request, runtime)

    def describe_alerts_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAlertsCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAlertsCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_alerts_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_alerts_count_with_options(request, runtime)

    def describe_attack_time_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_name):
            body['AssetName'] = request.asset_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAttackTimeLine',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAttackTimeLineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_attack_time_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_time_line_with_options(request, runtime)

    def describe_automate_response_config_counter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigCounter',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigCounterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_automate_response_config_counter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_counter_with_options(request, runtime)

    def describe_automate_response_config_feature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigFeature',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_automate_response_config_feature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_feature_with_options(request, runtime)

    def describe_automate_response_config_play_books_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAutomateResponseConfigPlayBooks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeAutomateResponseConfigPlayBooksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_automate_response_config_play_books(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_automate_response_config_play_books_with_options(request, runtime)

    def describe_cloud_siem_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_type):
            body['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemAssets',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_siem_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_assets_with_options(request, runtime)

    def describe_cloud_siem_assets_counter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemAssetsCounter',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemAssetsCounterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_siem_assets_counter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_assets_counter_with_options(request, runtime)

    def describe_cloud_siem_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemEventDetail',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_siem_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_event_detail_with_options(request, runtime)

    def describe_cloud_siem_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asset_id):
            body['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.thread_level):
            body['ThreadLevel'] = request.thread_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCloudSiemEvents',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCloudSiemEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_siem_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_siem_events_with_options(request, runtime)

    def describe_customize_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_customize_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_with_options(request, runtime)

    def describe_customize_rule_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleCount',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_customize_rule_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_count_with_options(request, runtime)

    def describe_customize_rule_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_customize_rule_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_test_with_options(request, runtime)

    def describe_customize_rule_test_histogram_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCustomizeRuleTestHistogram',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeCustomizeRuleTestHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_customize_rule_test_histogram(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_customize_rule_test_histogram_with_options(request, runtime)

    def describe_dispose_and_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisposeAndPlaybook',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDisposeAndPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dispose_and_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dispose_and_playbook_with_options(request, runtime)

    def describe_dispose_strategy_playbook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDisposeStrategyPlaybook',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeDisposeStrategyPlaybookResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dispose_strategy_playbook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dispose_strategy_playbook_with_options(request, runtime)

    def describe_entity_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEntityInfo',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEntityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_entity_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_entity_info_with_options(request, runtime)

    def describe_event_count_by_threat_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEventCountByThreatLevel',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEventCountByThreatLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_count_by_threat_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_count_by_threat_level_with_options(request, runtime)

    def describe_event_dispose_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEventDispose',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeEventDisposeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_dispose(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_dispose_with_options(request, runtime)

    def describe_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.submit_id):
            body['SubmitId'] = request.submit_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_job_status_with_options(request, runtime)

    def describe_log_fields_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogFields',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_fields(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_fields_with_options(request, runtime)

    def describe_log_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogSource',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_source_with_options(request, runtime)

    def describe_log_store_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogStore',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_store(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_with_options(request, runtime)

    def describe_log_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeLogType',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeLogTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_type_with_options(request, runtime)

    def describe_operators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOperators',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeOperatorsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_operators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_operators_with_options(request, runtime)

    def describe_scope_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeScopeUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeScopeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scope_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_scope_users_with_options(request, runtime)

    def describe_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_with_options(request, runtime)

    def describe_waf_scope_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWafScope',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DescribeWafScopeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_waf_scope(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_scope_with_options(request, runtime)

    def do_quick_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.index):
            body['Index'] = request.index
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            body['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DoQuickField',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DoQuickFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def do_quick_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_quick_field_with_options(request, runtime)

    def do_self_delegate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.delegate_or_not):
            body['DelegateOrNot'] = request.delegate_or_not
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DoSelfDelegate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.DoSelfDelegateResponse(),
            self.call_api(params, req, runtime)
        )

    def do_self_delegate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_self_delegate_with_options(request, runtime)

    def get_capacity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_capacity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_capacity_with_options(request, runtime)

    def get_histograms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetHistogramsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_histograms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_histograms_with_options(request, runtime)

    def get_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse_or_not):
            body['ReverseOrNot'] = request.reverse_or_not
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.total):
            body['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_logs_with_options(request, runtime)

    def get_quick_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_name):
            body['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quick_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quick_query_with_options(request, runtime)

    def get_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.GetStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_storage_with_options(request, runtime)

    def list_automate_response_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutomateResponseConfigs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListAutomateResponseConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_automate_response_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_automate_response_configs_with_options(request, runtime)

    def list_cloud_siem_customize_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCloudSiemCustomizeRules',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCloudSiemCustomizeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cloud_siem_customize_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_siem_customize_rules_with_options(request, runtime)

    def list_cloud_siem_predefined_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCloudSiemPredefinedRules',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCloudSiemPredefinedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cloud_siem_predefined_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_siem_predefined_rules_with_options(request, runtime)

    def list_customize_rule_test_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCustomizeRuleTestResult',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListCustomizeRuleTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    def list_customize_rule_test_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_customize_rule_test_result_with_options(request, runtime)

    def list_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_with_options(request, runtime)

    def list_dispose_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.effective_status):
            body['EffectiveStatus'] = request.effective_status
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.entity_identity):
            body['EntityIdentity'] = request.entity_identity
        if not UtilClient.is_unset(request.entity_type):
            body['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.order_field):
            body['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.playbook_name):
            body['PlaybookName'] = request.playbook_name
        if not UtilClient.is_unset(request.playbook_types):
            body['PlaybookTypes'] = request.playbook_types
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sophon_task_id):
            body['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDisposeStrategy',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListDisposeStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dispose_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dispose_strategy_with_options(request, runtime)

    def list_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOperation',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListOperationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_operation_with_options(request, runtime)

    def list_quick_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ListQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quick_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quick_query_with_options(request, runtime)

    def open_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.log_code):
            body['LogCode'] = request.log_code
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenDelivery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.OpenDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def open_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_delivery_with_options(request, runtime)

    def post_automate_response_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_config):
            body['ActionConfig'] = request.action_config
        if not UtilClient.is_unset(request.action_type):
            body['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.auto_response_type):
            body['AutoResponseType'] = request.auto_response_type
        if not UtilClient.is_unset(request.execution_condition):
            body['ExecutionCondition'] = request.execution_condition
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sub_user_id):
            body['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostAutomateResponseConfig',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostAutomateResponseConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def post_automate_response_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_automate_response_config_with_options(request, runtime)

    def post_customize_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.alert_type_mds):
            body['AlertTypeMds'] = request.alert_type_mds
        if not UtilClient.is_unset(request.event_transfer_ext):
            body['EventTransferExt'] = request.event_transfer_ext
        if not UtilClient.is_unset(request.event_transfer_switch):
            body['EventTransferSwitch'] = request.event_transfer_switch
        if not UtilClient.is_unset(request.event_transfer_type):
            body['EventTransferType'] = request.event_transfer_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.log_source):
            body['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.log_source_mds):
            body['LogSourceMds'] = request.log_source_mds
        if not UtilClient.is_unset(request.log_type):
            body['LogType'] = request.log_type
        if not UtilClient.is_unset(request.log_type_mds):
            body['LogTypeMds'] = request.log_type_mds
        if not UtilClient.is_unset(request.query_cycle):
            body['QueryCycle'] = request.query_cycle
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_condition):
            body['RuleCondition'] = request.rule_condition
        if not UtilClient.is_unset(request.rule_desc):
            body['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_group):
            body['RuleGroup'] = request.rule_group
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_threshold):
            body['RuleThreshold'] = request.rule_threshold
        if not UtilClient.is_unset(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostCustomizeRule',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostCustomizeRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def post_customize_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_customize_rule_with_options(request, runtime)

    def post_customize_rule_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.simulated_data):
            body['SimulatedData'] = request.simulated_data
        if not UtilClient.is_unset(request.test_type):
            body['TestType'] = request.test_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    def post_customize_rule_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_customize_rule_test_with_options(request, runtime)

    def post_event_dispose_and_whiterule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_dispose):
            body['EventDispose'] = request.event_dispose
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.receiver_info):
            body['ReceiverInfo'] = request.receiver_info
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostEventDisposeAndWhiteruleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostEventDisposeAndWhiteruleListResponse(),
            self.call_api(params, req, runtime)
        )

    def post_event_dispose_and_whiterule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_event_dispose_and_whiterule_list_with_options(request, runtime)

    def post_event_whiterule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.whiterule_list):
            body['WhiteruleList'] = request.whiterule_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostEventWhiteruleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostEventWhiteruleListResponse(),
            self.call_api(params, req, runtime)
        )

    def post_event_whiterule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_event_whiterule_list_with_options(request, runtime)

    def post_finish_customize_rule_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostFinishCustomizeRuleTest',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostFinishCustomizeRuleTestResponse(),
            self.call_api(params, req, runtime)
        )

    def post_finish_customize_rule_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_finish_customize_rule_test_with_options(request, runtime)

    def post_rule_status_change_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostRuleStatusChange',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.PostRuleStatusChangeResponse(),
            self.call_api(params, req, runtime)
        )

    def post_rule_status_change(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_rule_status_change_with_options(request, runtime)

    def restore_capacity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreCapacity',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.RestoreCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    def restore_capacity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_capacity_with_options(request, runtime)

    def save_quick_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveQuickQuery',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SaveQuickQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def save_quick_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_quick_query_with_options(request, runtime)

    def set_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetStorage',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.SetStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def set_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_storage_with_options(request, runtime)

    def show_quick_analysis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ShowQuickAnalysis',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.ShowQuickAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    def show_quick_analysis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.show_quick_analysis_with_options(request, runtime)

    def update_automate_response_config_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.in_use):
            body['InUse'] = request.in_use
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutomateResponseConfigStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.UpdateAutomateResponseConfigStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_automate_response_config_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_automate_response_config_status_with_options(request, runtime)

    def update_white_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.white_rule_id):
            body['WhiteRuleId'] = request.white_rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWhiteRuleList',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_siem_20220616_models.UpdateWhiteRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def update_white_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_white_rule_list_with_options(request, runtime)
