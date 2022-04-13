# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cgcs20211111 import models as cgcs20211111_models
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
        self._endpoint = self.get_endpoint('cgcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def adapt_create_service_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.AdaptCreateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.adapt_target):
            request.adapt_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.adapt_target), 'AdaptTarget', 'json')
        body = {}
        if not UtilClient.is_unset(request.adapt_target_shrink):
            body['AdaptTarget'] = request.adapt_target_shrink
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AdaptCreateService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AdaptCreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def adapt_create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.adapt_create_service_with_options(request, runtime)

    def adapt_get_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AdaptGetService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AdaptGetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def adapt_get_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.adapt_get_service_with_options(request, runtime)

    def app_create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppCreateService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppCreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_create_service_with_options(request, runtime)

    def app_delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppDeleteService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppDeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_delete_service_with_options(request, runtime)

    def app_get_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppGetService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppGetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_get_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_get_service_with_options(request, runtime)

    def app_list_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppListService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppListServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_list_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_list_service_with_options(request, runtime)

    def app_modify_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppModifyService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppModifyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_modify_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_modify_service_with_options(request, runtime)

    def app_version_create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        if not UtilClient.is_unset(request.file_address):
            body['FileAddress'] = request.file_address
        if not UtilClient.is_unset(request.file_size):
            body['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_upload_type):
            body['FileUploadType'] = request.file_upload_type
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppVersionCreateService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppVersionCreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_version_create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_version_create_service_with_options(request, runtime)

    def app_version_delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppVersionDeleteService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppVersionDeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_version_delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_version_delete_service_with_options(request, runtime)

    def app_version_get_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppVersionGetService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppVersionGetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_version_get_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_version_get_service_with_options(request, runtime)

    def app_version_list_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppVersionListService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppVersionListServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_version_list_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_version_list_service_with_options(request, runtime)

    def app_version_modify_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppVersionModifyService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppVersionModifyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_version_modify_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_version_modify_service_with_options(request, runtime)

    def app_version_query_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppVersionQueryService',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppVersionQueryServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def app_version_query_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.app_version_query_service_with_options(request, runtime)

    def applied_consum_stat_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.AppliedConsumStatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.applied_id):
            request.applied_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.applied_id, 'AppliedId', 'json')
        body = {}
        if not UtilClient.is_unset(request.applied_id_shrink):
            body['AppliedId'] = request.applied_id_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.query_end_date):
            body['QueryEndDate'] = request.query_end_date
        if not UtilClient.is_unset(request.query_start_date):
            body['QueryStartDate'] = request.query_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppliedConsumStat',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppliedConsumStatResponse(),
            self.call_api(params, req, runtime)
        )

    def applied_consum_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.applied_consum_stat_with_options(request, runtime)

    def applied_near_real_stat_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.AppliedNearRealStatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.applied_version_id):
            request.applied_version_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.applied_version_id, 'AppliedVersionId', 'json')
        body = {}
        if not UtilClient.is_unset(request.applied_version_id_shrink):
            body['AppliedVersionId'] = request.applied_version_id_shrink
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppliedNearRealStat',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppliedNearRealStatResponse(),
            self.call_api(params, req, runtime)
        )

    def applied_near_real_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.applied_near_real_stat_with_options(request, runtime)

    def applied_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.query_end_date):
            body['QueryEndDate'] = request.query_end_date
        if not UtilClient.is_unset(request.query_start_date):
            body['QueryStartDate'] = request.query_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppliedStat',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.AppliedStatResponse(),
            self.call_api(params, req, runtime)
        )

    def applied_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.applied_stat_with_options(request, runtime)

    def create_app_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_with_options(request, runtime)

    def create_app_session_batch_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.custom_task_id):
            query['CustomTaskId'] = request.custom_task_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_session_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_batch_with_options(request, runtime)

    def create_upload_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.file_address):
            body['FileAddress'] = request.file_address
        if not UtilClient.is_unset(request.file_size):
            body['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.progress):
            body['Progress'] = request.progress
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.upload_tool_version):
            body['UploadToolVersion'] = request.upload_tool_version
        if not UtilClient.is_unset(request.upload_type):
            body['UploadType'] = request.upload_type
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUploadTask',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateUploadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_upload_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upload_task_with_options(request, runtime)

    def get_app_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAppList',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_list(self):
        runtime = util_models.RuntimeOptions()
        return self.get_app_list_with_options(runtime)

    def get_app_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_session_with_options(request, runtime)

    def get_need_upload_file_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.hash_list):
            body['HashList'] = request.hash_list
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNeedUploadFileList',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetNeedUploadFileListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_need_upload_file_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_need_upload_file_list_with_options(request, runtime)

    def get_oss_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOssInfo',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetOssInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oss_info(self):
        runtime = util_models.RuntimeOptions()
        return self.get_oss_info_with_options(runtime)

    def get_tenant_id_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetTenantId',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetTenantIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tenant_id(self):
        runtime = util_models.RuntimeOptions()
        return self.get_tenant_id_with_options(runtime)

    def get_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bucket):
            body['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    def get_upload_tool_url_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetUploadToolUrl',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetUploadToolUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_upload_tool_url(self):
        runtime = util_models.RuntimeOptions()
        return self.get_upload_tool_url_with_options(runtime)

    def has_activate_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='HasActivate',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.HasActivateResponse(),
            self.call_api(params, req, runtime)
        )

    def has_activate(self):
        runtime = util_models.RuntimeOptions()
        return self.has_activate_with_options(runtime)

    def list_app_sessions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.custom_session_ids):
            query['CustomSessionIds'] = request.custom_session_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_session_ids):
            query['PlatformSessionIds'] = request.platform_session_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSessions',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_sessions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_sessions_with_options(request, runtime)

    def page_query_resource_package_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_valid_type):
            body['QueryValidType'] = request.query_valid_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PageQueryResourcePackageList',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.PageQueryResourcePackageListResponse(),
            self.call_api(params, req, runtime)
        )

    def page_query_resource_package_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.page_query_resource_package_list_with_options(request, runtime)

    def query_adapt_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.request_app):
            body['RequestApp'] = request.request_app
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAdaptRecords',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.QueryAdaptRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_adapt_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_adapt_records_with_options(request, runtime)

    def query_upload_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.query_upload_progress_requests):
            body['QueryUploadProgressRequests'] = request.query_upload_progress_requests
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryUploadProgress',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.QueryUploadProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def query_upload_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_upload_progress_with_options(request, runtime)

    def record_finished_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.file_fingerprint_dtolist):
            body['FileFingerprintDTOList'] = request.file_fingerprint_dtolist
        if not UtilClient.is_unset(request.file_size):
            body['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.tool_version):
            body['ToolVersion'] = request.tool_version
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecordFinishedFile',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.RecordFinishedFileResponse(),
            self.call_api(params, req, runtime)
        )

    def record_finished_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.record_finished_file_with_options(request, runtime)

    def replicate_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.source_version_id):
            body['SourceVersionId'] = request.source_version_id
        if not UtilClient.is_unset(request.target_version_id):
            body['TargetVersionId'] = request.target_version_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReplicateVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReplicateVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def replicate_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replicate_version_with_options(request, runtime)

    def report_upload_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.progress):
            body['Progress'] = request.progress
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUploadProgress',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReportUploadProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def report_upload_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_upload_progress_with_options(request, runtime)

    def report_upload_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.file_fingerprint_dtolist):
            body['FileFingerprintDTOList'] = request.file_fingerprint_dtolist
        if not UtilClient.is_unset(request.file_size):
            body['FileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.tool_version):
            body['ToolVersion'] = request.tool_version
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUploadResult',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReportUploadResultResponse(),
            self.call_api(params, req, runtime)
        )

    def report_upload_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_upload_result_with_options(request, runtime)

    def report_upload_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.version_id):
            body['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReportUploadStatus',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReportUploadStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def report_upload_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.report_upload_status_with_options(request, runtime)

    def stop_app_session_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_app_session(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_app_session_with_options(request, runtime)

    def total_applied_consum_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.query_end_date):
            body['QueryEndDate'] = request.query_end_date
        if not UtilClient.is_unset(request.query_start_date):
            body['QueryStartDate'] = request.query_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TotalAppliedConsumStat',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.TotalAppliedConsumStatResponse(),
            self.call_api(params, req, runtime)
        )

    def total_applied_consum_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.total_applied_consum_stat_with_options(request, runtime)

    def total_applied_near_real_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TotalAppliedNearRealStat',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.TotalAppliedNearRealStatResponse(),
            self.call_api(params, req, runtime)
        )

    def total_applied_near_real_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.total_applied_near_real_stat_with_options(request, runtime)

    def total_query_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operator_id):
            body['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TotalQueryResourcePackage',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.TotalQueryResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def total_query_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.total_query_resource_package_with_options(request, runtime)
