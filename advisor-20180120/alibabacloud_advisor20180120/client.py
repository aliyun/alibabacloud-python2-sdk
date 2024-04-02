# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_advisor20180120 import models as advisor_20180120_models
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
        self._endpoint = self.get_endpoint('advisor', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_advices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.exclude_advice_id):
            query['ExcludeAdviceId'] = request.exclude_advice_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_advices_with_options(request, runtime)

    def describe_advices_flat_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvicesFlatPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeAdvicesFlatPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advices_flat_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_advices_flat_page_with_options(request, runtime)

    def describe_advices_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvicesPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeAdvicesPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advices_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_advices_page_with_options(request, runtime)

    def describe_advisor_checks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorChecks',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeAdvisorChecksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advisor_checks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_checks_with_options(request, runtime)

    def describe_advisor_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorResources',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeAdvisorResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advisor_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_resources_with_options(request, runtime)

    def describe_cost_check_advices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostCheckAdvicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostCheckAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeCostCheckAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cost_check_advices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_check_advices_with_options(request, runtime)

    def describe_cost_check_results_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostCheckResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_ids):
            request.check_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostCheckResults',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.DescribeCostCheckResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cost_check_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_check_results_with_options(request, runtime)

    def get_history_advices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.GetHistoryAdvicesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_history_advices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_history_advices_with_options(request, runtime)

    def get_task_status_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatusById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.GetTaskStatusByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_status_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_by_id_with_options(request, runtime)

    def refresh_advisor_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorCheck',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.RefreshAdvisorCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_advisor_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_advisor_check_with_options(request, runtime)

    def refresh_advisor_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorResource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.RefreshAdvisorResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_advisor_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_advisor_resource_with_options(request, runtime)

    def report_biz_alert_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.ReportBizAlertInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_uid):
            request.alert_uid_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_uid, 'AlertUid', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_description):
            query['AlertDescription'] = request.alert_description
        if not UtilClient.is_unset(request.alert_detail):
            query['AlertDetail'] = request.alert_detail
        if not UtilClient.is_unset(request.alert_grade):
            query['AlertGrade'] = request.alert_grade
        if not UtilClient.is_unset(request.alert_labels):
            query['AlertLabels'] = request.alert_labels
        if not UtilClient.is_unset(request.alert_scene):
            query['AlertScene'] = request.alert_scene
        if not UtilClient.is_unset(request.alert_token):
            query['AlertToken'] = request.alert_token
        if not UtilClient.is_unset(request.alert_uid_shrink):
            query['AlertUid'] = request.alert_uid_shrink
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportBizAlertInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            advisor_20180120_models.ReportBizAlertInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def report_biz_alert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_biz_alert_info_with_options(request, runtime)
