# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_customerservice20231228 import models as customer_service_20231228_models
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
        self._endpoint = self.get_endpoint('customerservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_download_url_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_id):
            body['fileId'] = request.file_id
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.free_order_apply_code):
            body['freeOrderApplyCode'] = request.free_order_apply_code
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDownloadUrl',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/file/getDownloadUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.GetDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_download_url_with_options(request, headers, runtime)

    def get_enterprise_support_plan_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.free_order_apply_codes):
            body['freeOrderApplyCodes'] = request.free_order_apply_codes
        if not UtilClient.is_unset(request.order_ids):
            body['orderIds'] = request.order_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseSupportPlanDetail',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/enterpriseSupport/getEnterpriseSupportPlanDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.GetEnterpriseSupportPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_support_plan_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_enterprise_support_plan_detail_with_options(request, headers, runtime)

    def get_pre_view_url_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_code):
            body['applyCode'] = request.apply_code
        if not UtilClient.is_unset(request.file_id):
            body['fileId'] = request.file_id
        if not UtilClient.is_unset(request.file_key):
            body['fileKey'] = request.file_key
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPreViewUrl',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/file/getPreViewUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.GetPreViewUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pre_view_url(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pre_view_url_with_options(request, headers, runtime)

    def get_service_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_code):
            body['applyCode'] = request.apply_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceDetail',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/expert/service/getServiceDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.GetServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_detail_with_options(request, headers, runtime)

    def get_yun_qi_task_by_record_id_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['recordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetYunQiTaskByRecordId',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/record/getYunQiTaskByRecordId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.GetYunQiTaskByRecordIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_yun_qi_task_by_record_id(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_yun_qi_task_by_record_id_with_options(request, headers, runtime)

    def list_docs_group_by_year_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_codes):
            body['applyCodes'] = request.apply_codes
        if not UtilClient.is_unset(request.file_name_keyword):
            body['fileNameKeyword'] = request.file_name_keyword
        if not UtilClient.is_unset(request.order_ids):
            body['orderIds'] = request.order_ids
        if not UtilClient.is_unset(request.product_code):
            body['productCode'] = request.product_code
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDocsGroupByYear',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/file/listDocsGroupByYear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.ListDocsGroupByYearResponse(),
            self.call_api(params, req, runtime)
        )

    def list_docs_group_by_year(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_docs_group_by_year_with_options(request, headers, runtime)

    def list_enterprise_support_plan_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEnterpriseSupportPlan',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/enterpriseSupport/listEnterpriseSupportPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.ListEnterpriseSupportPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def list_enterprise_support_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_enterprise_support_plan_with_options(request, headers, runtime)

    def list_enterprise_support_plan_simple_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEnterpriseSupportPlanSimple',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/enterpriseSupport/listEnterpriseSupportPlanSimple',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.ListEnterpriseSupportPlanSimpleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_enterprise_support_plan_simple(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_enterprise_support_plan_simple_with_options(request, headers, runtime)

    def list_service_apply_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_type):
            body['applyType'] = request.apply_type
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            body['productCode'] = request.product_code
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceApply',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/expert/service/listServiceApply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.ListServiceApplyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_apply(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_apply_with_options(request, headers, runtime)

    def list_yun_qi_task_by_uid_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['createTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['createTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.free_order_apply_codes):
            body['freeOrderApplyCodes'] = request.free_order_apply_codes
        if not UtilClient.is_unset(request.free_order_apply_ids):
            body['freeOrderApplyIds'] = request.free_order_apply_ids
        if not UtilClient.is_unset(request.order_ids):
            body['orderIds'] = request.order_ids
        if not UtilClient.is_unset(request.page_num):
            body['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListYunQiTaskByUid',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/record/listYunQiTaskByUid',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.ListYunQiTaskByUidResponse(),
            self.call_api(params, req, runtime)
        )

    def list_yun_qi_task_by_uid(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_yun_qi_task_by_uid_with_options(request, headers, runtime)

    def mark_file_readed_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_code):
            body['applyCode'] = request.apply_code
        if not UtilClient.is_unset(request.file_id):
            body['fileId'] = request.file_id
        if not UtilClient.is_unset(request.order_id):
            body['orderId'] = request.order_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MarkFileReaded',
            version='2023-12-28',
            protocol='HTTPS',
            pathname='/customerWorkbench/pop/api/file/markFileReaded',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            customer_service_20231228_models.MarkFileReadedResponse(),
            self.call_api(params, req, runtime)
        )

    def mark_file_readed(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.mark_file_readed_with_options(request, headers, runtime)
