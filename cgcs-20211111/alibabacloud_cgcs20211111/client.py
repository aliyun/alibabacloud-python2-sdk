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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cgcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_adaptation_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAdaptationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.adapt_target):
            request.adapt_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.adapt_target), 'AdaptTarget', 'json')
        body = {}
        if not UtilClient.is_unset(request.adapt_target_shrink):
            body['AdaptTarget'] = request.adapt_target_shrink
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdaptation',
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
            cgcs20211111_models.CreateAdaptationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_adaptation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adaptation_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
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
            cgcs20211111_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_app_session_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.result_store):
            request.result_store_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.result_store), 'ResultStore', 'json')
        if not UtilClient.is_unset(tmp_req.start_parameters_v2):
            request.start_parameters_v2shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_parameters_v2, 'StartParametersV2', 'json')
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
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.enable_postpaid):
            query['EnablePostpaid'] = request.enable_postpaid
        if not UtilClient.is_unset(request.result_store_shrink):
            query['ResultStore'] = request.result_store_shrink
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.start_parameters_v2shrink):
            query['StartParametersV2'] = request.start_parameters_v2shrink
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
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

    def create_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppVersion',
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
            cgcs20211111_models.CreateAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_version_with_options(request, runtime)

    def create_dataset_deploy_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_param):
            query['CustomParam'] = request.custom_param
        if not UtilClient.is_unset(request.need_unzip):
            query['NeedUnzip'] = request.need_unzip
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_file_path):
            query['OssFilePath'] = request.oss_file_path
        if not UtilClient.is_unset(request.oss_region_id):
            query['OssRegionId'] = request.oss_region_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatasetDeployTask',
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
            cgcs20211111_models.CreateDatasetDeployTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dataset_deploy_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_deploy_task_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
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
            cgcs20211111_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppVersion',
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
            cgcs20211111_models.DeleteAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_version_with_options(request, runtime)

    def get_adaptation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.adapt_apply_id):
            body['AdaptApplyId'] = request.adapt_apply_id
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAdaptation',
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
            cgcs20211111_models.GetAdaptationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_adaptation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_adaptation_with_options(request, runtime)

    def get_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
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
            cgcs20211111_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

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

    def get_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppVersion',
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
            cgcs20211111_models.GetAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_version_with_options(request, runtime)

    def get_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataset',
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
            cgcs20211111_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    def list_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApp',
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
            cgcs20211111_models.ListAppResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_with_options(request, runtime)

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

    def list_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppVersion',
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
            cgcs20211111_models.ListAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_version_with_options(request, runtime)

    def modify_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApp',
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
            cgcs20211111_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    def modify_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppVersion',
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
            cgcs20211111_models.ModifyAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_version_with_options(request, runtime)

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
