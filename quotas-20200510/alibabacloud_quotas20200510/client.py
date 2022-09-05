# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quotas20200510 import models as quotas_20200510_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('quotas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_quota_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not UtilClient.is_unset(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not UtilClient.is_unset(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quota_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quota_alarm_with_options(request, runtime)

    def create_quota_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audit_mode):
            body['AuditMode'] = request.audit_mode
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_quota_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_quota_application_with_options(request, runtime)

    def create_template_quota_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.CreateTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template_quota_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_quota_item_with_options(request, runtime)

    def delete_quota_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_quota_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_quota_alarm_with_options(request, runtime)

    def delete_template_quota_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.DeleteTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template_quota_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_quota_item_with_options(request, runtime)

    def get_product_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProductQuota',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_product_quota_with_options(request, runtime)

    def get_product_quota_dimension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dependent_dimensions):
            body['DependentDimensions'] = request.dependent_dimensions
        if not UtilClient.is_unset(request.dimension_key):
            body['DimensionKey'] = request.dimension_key
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProductQuotaDimension',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetProductQuotaDimensionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_product_quota_dimension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_product_quota_dimension_with_options(request, runtime)

    def get_quota_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quota_alarm_with_options(request, runtime)

    def get_quota_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaApplication',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quota_application_with_options(request, runtime)

    def get_quota_template_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_directory_id):
            body['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQuotaTemplateServiceStatus',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.GetQuotaTemplateServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_quota_template_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_quota_template_service_status_with_options(request, runtime)

    def list_alarm_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListAlarmHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alarm_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    def list_dependent_quotas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDependentQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListDependentQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dependent_quotas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dependent_quotas_with_options(request, runtime)

    def list_product_dimension_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductDimensionGroups',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductDimensionGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_dimension_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_dimension_groups_with_options(request, runtime)

    def list_product_quota_dimensions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProductQuotaDimensions',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotaDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_quota_dimensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_quota_dimensions_with_options(request, runtime)

    def list_product_quotas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.group_code):
            body['GroupCode'] = request.group_code
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProductQuotas',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_quotas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_quotas_with_options(request, runtime)

    def list_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    def list_quota_alarms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_dimensions):
            body['QuotaDimensions'] = request.quota_dimensions
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaAlarms',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quota_alarms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quota_alarms_with_options(request, runtime)

    def list_quota_application_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplicationTemplates',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quota_application_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quota_application_templates_with_options(request, runtime)

    def list_quota_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.key_word):
            body['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        if not UtilClient.is_unset(request.quota_category):
            body['QuotaCategory'] = request.quota_category
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListQuotaApplications',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ListQuotaApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quota_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_quota_applications_with_options(request, runtime)

    def modify_quota_template_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyQuotaTemplateServiceStatus',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ModifyQuotaTemplateServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_quota_template_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_quota_template_service_status_with_options(request, runtime)

    def modify_template_quota_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desire_value):
            body['DesireValue'] = request.desire_value
        if not UtilClient.is_unset(request.dimensions):
            body['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.env_language):
            body['EnvLanguage'] = request.env_language
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.notice_type):
            body['NoticeType'] = request.notice_type
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.quota_action_code):
            body['QuotaActionCode'] = request.quota_action_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTemplateQuotaItem',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.ModifyTemplateQuotaItemResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_template_quota_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_template_quota_item_with_options(request, runtime)

    def update_quota_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alarm_id):
            body['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.alarm_name):
            body['AlarmName'] = request.alarm_name
        if not UtilClient.is_unset(request.threshold):
            body['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.threshold_percent):
            body['ThresholdPercent'] = request.threshold_percent
        if not UtilClient.is_unset(request.threshold_type):
            body['ThresholdType'] = request.threshold_type
        if not UtilClient.is_unset(request.web_hook):
            body['WebHook'] = request.web_hook
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateQuotaAlarm',
            version='2020-05-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quotas_20200510_models.UpdateQuotaAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def update_quota_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_quota_alarm_with_options(request, runtime)
