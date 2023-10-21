# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudapi20160714 import models as cloud_api20160714_models
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
            'cn-qingdao': 'apigateway.cn-qingdao.aliyuncs.com',
            'cn-beijing': 'apigateway.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'apigateway.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'apigateway.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'apigateway.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'apigateway.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'apigateway.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'apigateway.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'apigateway.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'apigateway.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'apigateway.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'apigateway.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'apigateway.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'apigateway.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'apigateway.eu-west-1.aliyuncs.com',
            'us-west-1': 'apigateway.us-west-1.aliyuncs.com',
            'us-east-1': 'apigateway.us-east-1.aliyuncs.com',
            'eu-central-1': 'apigateway.eu-central-1.aliyuncs.com',
            'me-east-1': 'apigateway.me-east-1.aliyuncs.com',
            'ap-south-1': 'apigateway.ap-south-1.aliyuncs.com',
            'cn-north-2-gov-1': 'apigateway.cn-north-2-gov-1.aliyuncs.com',
            'cn-hangzhou-finance': 'apigateway.aliyuncs.com',
            'cn-shenzhen-finance-1': 'apigateway.aliyuncs.com',
            'cn-shanghai-finance-1': 'apigateway.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abolish_api_with_options(self, request, runtime):
        """
        This operation is intended for API providers and is the opposite of DeployApi.
        *   An API can be unpublished from a specified runtime environment in under 5 seconds.
        *   An unpublished API cannot be called in the specified runtime environment.
        

        @param request: AbolishApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AbolishApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AbolishApiResponse(),
            self.call_api(params, req, runtime)
        )

    def abolish_api(self, request):
        """
        This operation is intended for API providers and is the opposite of DeployApi.
        *   An API can be unpublished from a specified runtime environment in under 5 seconds.
        *   An unpublished API cannot be called in the specified runtime environment.
        

        @param request: AbolishApiRequest

        @return: AbolishApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    def add_access_control_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccessControlListEntry',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_access_control_list_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_access_control_list_entry_with_options(request, runtime)

    def add_ip_control_policy_item_with_options(self, request, runtime):
        """
        When you call this operation, note that:
        *   This operation is intended for API providers.
        *   An added policy immediately takes effect on all APIs that are bound to the access control list (ACL).
        *   A maximum of 100 policies can be added to an ACL.
        

        @param request: AddIpControlPolicyItemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddIpControlPolicyItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ip_control_policy_item(self, request):
        """
        When you call this operation, note that:
        *   This operation is intended for API providers.
        *   An added policy immediately takes effect on all APIs that are bound to the access control list (ACL).
        *   A maximum of 100 policies can be added to an ACL.
        

        @param request: AddIpControlPolicyItemRequest

        @return: AddIpControlPolicyItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_ip_control_policy_item_with_options(request, runtime)

    def add_traffic_special_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   If the input SpecialKey already exists, the previous configuration is overwritten. Use caution when calling this operation.
        *   Special throttling policies must be added to an existing throttling policy, and can take effect on all the APIs to which the throttling policy is bound.
        

        @param request: AddTrafficSpecialControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTrafficSpecialControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    def add_traffic_special_control(self, request):
        """
        This API is intended for API providers.
        *   If the input SpecialKey already exists, the previous configuration is overwritten. Use caution when calling this operation.
        *   Special throttling policies must be added to an existing throttling policy, and can take effect on all the APIs to which the throttling policy is bound.
        

        @param request: AddTrafficSpecialControlRequest

        @return: AddTrafficSpecialControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    def attach_api_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not UtilClient.is_unset(request.apis):
            query['Apis'] = request.apis
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachApiProduct',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AttachApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_api_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_api_product_with_options(request, runtime)

    def attach_plugin_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   You can only bind plug-ins to published APIs.
        *   The plug-in takes effect immediately after it is bound to an API.
        *   If you bind a different plug-in to an API, this plug-in takes effect immediately.
        

        @param request: AttachPluginRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AttachPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_plugin(self, request):
        """
        This operation is intended for API providers.
        *   You can only bind plug-ins to published APIs.
        *   The plug-in takes effect immediately after it is bound to an API.
        *   If you bind a different plug-in to an API, this plug-in takes effect immediately.
        

        @param request: AttachPluginRequest

        @return: AttachPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_plugin_with_options(request, runtime)

    def batch_abolish_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchAbolishApisResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_abolish_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_abolish_apis_with_options(request, runtime)

    def batch_deploy_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeployApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchDeployApisResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_deploy_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_deploy_apis_with_options(request, runtime)

    def create_access_control_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessControlList',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_control_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_control_list_with_options(request, runtime)

    def create_api_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   The name of each API within the same group must be unique.
        *   Each request path within the same group must be unique.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: CreateApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.backend_enable):
            query['BackendEnable'] = request.backend_enable
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        body = {}
        if not UtilClient.is_unset(request.constant_parameters):
            body['ConstantParameters'] = request.constant_parameters
        if not UtilClient.is_unset(request.error_code_samples):
            body['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            body['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.request_parameters):
            body['RequestParameters'] = request.request_parameters
        if not UtilClient.is_unset(request.result_descriptions):
            body['ResultDescriptions'] = request.result_descriptions
        if not UtilClient.is_unset(request.result_sample):
            body['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.service_parameters):
            body['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            body['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.system_parameters):
            body['SystemParameters'] = request.system_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiResponse(),
            self.call_api(params, req, runtime)
        )

    def create_api(self, request):
        """
        This operation is intended for API providers.
        *   The name of each API within the same group must be unique.
        *   Each request path within the same group must be unique.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: CreateApiRequest

        @return: CreateApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    def create_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_path):
            query['BasePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_api_group_with_options(request, runtime)

    def create_api_stage_variable_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        

        @param request: CreateApiStageVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateApiStageVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.stage_route_model):
            query['StageRouteModel'] = request.stage_route_model
        if not UtilClient.is_unset(request.support_route):
            query['SupportRoute'] = request.support_route
        if not UtilClient.is_unset(request.variable_name):
            query['VariableName'] = request.variable_name
        if not UtilClient.is_unset(request.variable_value):
            query['VariableValue'] = request.variable_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_api_stage_variable(self, request):
        """
        This operation is intended for API providers.
        

        @param request: CreateApiStageVariableRequest

        @return: CreateApiStageVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_api_stage_variable_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   Each application has a key-value pair which is used for identity verification when you call an API.
        *   An application must be authorized to call an API.
        *   Each application has only one key-value pair, which can be reset if the pair is leaked.
        *   A maximum of 1,000 applications can be created for each Alibaba Cloud account.
        *   You can call this operation up to 50 times per second per account.
        

        @param request: CreateAppRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        """
        This operation is intended for API callers.
        *   Each application has a key-value pair which is used for identity verification when you call an API.
        *   An application must be authorized to call an API.
        *   Each application has only one key-value pair, which can be reset if the pair is leaked.
        *   A maximum of 1,000 applications can be created for each Alibaba Cloud account.
        *   You can call this operation up to 50 times per second per account.
        

        @param request: CreateAppRequest

        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_backend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_name):
            query['BackendName'] = request.backend_name
        if not UtilClient.is_unset(request.backend_type):
            query['BackendType'] = request.backend_type
        if not UtilClient.is_unset(request.create_event_bridge_service_linked_role):
            query['CreateEventBridgeServiceLinkedRole'] = request.create_event_bridge_service_linked_role
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackend',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateBackendResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backend_with_options(request, runtime)

    def create_backend_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.backend_model_data):
            query['BackendModelData'] = request.backend_model_data
        if not UtilClient.is_unset(request.backend_type):
            query['BackendType'] = request.backend_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackendModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateBackendModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_backend_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backend_model_with_options(request, runtime)

    def create_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.dataset_type):
            query['DatasetType'] = request.dataset_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    def create_dataset_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatasetItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateDatasetItemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dataset_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_item_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.https_policy):
            query['HttpsPolicy'] = request.https_policy
        if not UtilClient.is_unset(request.instance_cidr):
            query['InstanceCidr'] = request.instance_cidr
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_vpc_id):
            query['UserVpcId'] = request.user_vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_vswitch_security_group):
            query['ZoneVSwitchSecurityGroup'] = request.zone_vswitch_security_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_intranet_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntranetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIntranetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_intranet_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intranet_domain_with_options(request, runtime)

    def create_ip_control_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   An ACL must be bound to an API to take effect. After an ACL is bound to an API, the ACL takes effect on the API immediately.
        *   You can add policies to an ACL when you create the ACL.
        *   If an ACL does not have any policy, the ACL is ineffective.
        

        @param request: CreateIpControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateIpControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.ip_control_policys):
            query['IpControlPolicys'] = request.ip_control_policys
        if not UtilClient.is_unset(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ip_control(self, request):
        """
        This operation is intended for API providers.
        *   An ACL must be bound to an API to take effect. After an ACL is bound to an API, the ACL takes effect on the API immediately.
        *   You can add policies to an ACL when you create the ACL.
        *   If an ACL does not have any policy, the ACL is ineffective.
        

        @param request: CreateIpControlRequest

        @return: CreateIpControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ip_control_with_options(request, runtime)

    def create_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_log_config_with_options(request, runtime)

    def create_model_with_options(self, request, runtime):
        """
        For more information about the model definition, see [JSON Schema Draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04?spm=a2c4g.11186623.2.10.2e977ff7p4BpQd).
        *   JSON Schema supports only element attributes of the Object type.
        

        @param request: CreateModelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model(self, request):
        """
        For more information about the model definition, see [JSON Schema Draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04?spm=a2c4g.11186623.2.10.2e977ff7p4BpQd).
        *   JSON Schema supports only element attributes of the Object type.
        

        @param request: CreateModelRequest

        @return: CreateModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    def create_monitor_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.raw_monitor_group_id):
            query['RawMonitorGroupId'] = request.raw_monitor_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    def create_plugin_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   The number of plug-ins of the same type that each user can create is limited. Different limits apply to different plug-in types.
        *   The plug-in definitions for advanced features are restricted.
        *   Plug-ins must be bound to APIs to take effect. After a plug-in is bound, it takes effect on that API immediately.
        

        @param request: CreatePluginRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.plugin_data):
            query['PluginData'] = request.plugin_data
        if not UtilClient.is_unset(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not UtilClient.is_unset(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreatePluginResponse(),
            self.call_api(params, req, runtime)
        )

    def create_plugin(self, request):
        """
        This operation is intended for API providers.
        *   The number of plug-ins of the same type that each user can create is limited. Different limits apply to different plug-in types.
        *   The plug-in definitions for advanced features are restricted.
        *   Plug-ins must be bound to APIs to take effect. After a plug-in is bound, it takes effect on that API immediately.
        

        @param request: CreatePluginRequest

        @return: CreatePluginResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_plugin_with_options(request, runtime)

    def create_signature_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The API operation only creates a key policy. You must call the binding operation to bind the key to an API.
        *   After the key is bound to the API, requests sent from API Gateway to the backend service contain signature strings. You can specify whether your backend service verifies these signature strings.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: CreateSignatureRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSignatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_key):
            query['SignatureKey'] = request.signature_key
        if not UtilClient.is_unset(request.signature_name):
            query['SignatureName'] = request.signature_name
        if not UtilClient.is_unset(request.signature_secret):
            query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def create_signature(self, request):
        """
        This API is intended for API providers.
        *   The API operation only creates a key policy. You must call the binding operation to bind the key to an API.
        *   After the key is bound to the API, requests sent from API Gateway to the backend service contain signature strings. You can specify whether your backend service verifies these signature strings.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: CreateSignatureRequest

        @return: CreateSignatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_signature_with_options(request, runtime)

    def create_traffic_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   Throttling policies must be bound to APIs to take effect. After a policy is bound to an API, it goes into effect on that API immediately.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: CreateTrafficControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTrafficControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_traffic_control(self, request):
        """
        This API is intended for API providers.
        *   Throttling policies must be bound to APIs to take effect. After a policy is bound to an API, it goes into effect on that API immediately.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: CreateTrafficControlRequest

        @return: CreateTrafficControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    def delete_access_control_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessControlList',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_control_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_control_list_with_options(request, runtime)

    def delete_all_traffic_special_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        

        @param request: DeleteAllTrafficSpecialControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAllTrafficSpecialControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_all_traffic_special_control(self, request):
        """
        This API is intended for API providers.
        

        @param request: DeleteAllTrafficSpecialControlRequest

        @return: DeleteAllTrafficSpecialControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    def delete_api_with_options(self, request, runtime):
        """
        This operation is intended for API providers and cannot be undone after it is complete.
        *   An API that is running in the runtime environment must be unpublished before you can delete the API.****\
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api(self, request):
        """
        This operation is intended for API providers and cannot be undone after it is complete.
        *   An API that is running in the runtime environment must be unpublished before you can delete the API.****\
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteApiRequest

        @return: DeleteApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    def delete_api_group_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   An API group that contains APIs cannot be deleted. To delete the API group, you must first delete its APIs.
        *   After an API group is deleted, the second-level domain name bound to the API group is automatically invalidated.
        *   If the specified API group does not exist, a success response is returned.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteApiGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteApiGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api_group(self, request):
        """
        This operation is intended for API providers.
        *   An API group that contains APIs cannot be deleted. To delete the API group, you must first delete its APIs.
        *   After an API group is deleted, the second-level domain name bound to the API group is automatically invalidated.
        *   If the specified API group does not exist, a success response is returned.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteApiGroupRequest

        @return: DeleteApiGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    def delete_api_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiProduct',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_product_with_options(request, runtime)

    def delete_api_stage_variable_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        

        @param request: DeleteApiStageVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteApiStageVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_id):
            query['StageId'] = request.stage_id
        if not UtilClient.is_unset(request.variable_name):
            query['VariableName'] = request.variable_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api_stage_variable(self, request):
        """
        This operation is intended for API providers.
        

        @param request: DeleteApiStageVariableRequest

        @return: DeleteApiStageVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_api_stage_variable_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   After an application is deleted, the application and its API authorization cannot be restored.
        *   You can call this operation up to 50 times per second per account.
        

        @param request: DeleteAppRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        """
        This operation is intended for API callers.
        *   After an application is deleted, the application and its API authorization cannot be restored.
        *   You can call this operation up to 50 times per second per account.
        

        @param request: DeleteAppRequest

        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_backend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackend',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteBackendResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backend_with_options(request, runtime)

    def delete_backend_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.backend_model_id):
            query['BackendModelId'] = request.backend_model_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackendModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteBackendModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_backend_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backend_model_with_options(request, runtime)

    def delete_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    def delete_dataset_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatasetItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDatasetItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dataset_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_item_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   If the specified domain name does not exist, a successful response will still appear.
        *   Unbinding a domain name from an API group will affect access to the APIs in the group. Exercise caution when using this operation.
        

        @param request: DeleteDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        """
        This operation is intended for API providers.
        *   If the specified domain name does not exist, a successful response will still appear.
        *   Unbinding a domain name from an API group will affect access to the APIs in the group. Exercise caution when using this operation.
        

        @param request: DeleteDomainRequest

        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_certificate_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_ip_control_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   If the ACL is bound to an API, you must unbind the ACL from the API before you can delete the ACL. Otherwise, an error is returned.
        *   If you call this operation on an ACL that does not exist, a success message is returned.
        

        @param request: DeleteIpControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIpControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip_control(self, request):
        """
        This operation is intended for API providers.
        *   If the ACL is bound to an API, you must unbind the ACL from the API before you can delete the ACL. Otherwise, an error is returned.
        *   If you call this operation on an ACL that does not exist, a success message is returned.
        

        @param request: DeleteIpControlRequest

        @return: DeleteIpControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_control_with_options(request, runtime)

    def delete_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_log_config_with_options(request, runtime)

    def delete_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    def delete_monitor_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.raw_monitor_group_id):
            query['RawMonitorGroupId'] = request.raw_monitor_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMonitorGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_monitor_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_monitor_group_with_options(request, runtime)

    def delete_plugin_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   You must first unbind the plug-in from the API. Otherwise, an error is reported when you delete the plug-in.
        

        @param request: DeletePluginRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeletePluginResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_plugin(self, request):
        """
        This operation is intended for API providers.
        *   You must first unbind the plug-in from the API. Otherwise, an error is reported when you delete the plug-in.
        

        @param request: DeletePluginRequest

        @return: DeletePluginResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_plugin_with_options(request, runtime)

    def delete_signature_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This API operation deletes an existing backend signature key.
        *   You cannot delete a key that is bound to an API. To delete the key, you must unbind it first.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteSignatureRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSignatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_signature(self, request):
        """
        This API is intended for API providers.
        *   This API operation deletes an existing backend signature key.
        *   You cannot delete a key that is bound to an API. To delete the key, you must unbind it first.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteSignatureRequest

        @return: DeleteSignatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_signature_with_options(request, runtime)

    def delete_traffic_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   If the throttling policy you want to delete is bound to APIs, you need to unbind the policy first. Otherwise, an error is reported when you delete the policy.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteTrafficControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTrafficControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_traffic_control(self, request):
        """
        This API is intended for API providers.
        *   If the throttling policy you want to delete is bound to APIs, you need to unbind the policy first. Otherwise, an error is reported when you delete the policy.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeleteTrafficControlRequest

        @return: DeleteTrafficControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    def delete_traffic_special_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   You can obtain the input parameters required in this operation by calling other APIs.
        

        @param request: DeleteTrafficSpecialControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTrafficSpecialControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_traffic_special_control(self, request):
        """
        This API is intended for API providers.
        *   You can obtain the input parameters required in this operation by calling other APIs.
        

        @param request: DeleteTrafficSpecialControlRequest

        @return: DeleteTrafficSpecialControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    def deploy_api_with_options(self, request, runtime):
        """
        This operation is intended for API providers. Only the API that you have defined and published to a runtime environment can be called.
        *   An API is published to a cluster in under 5 seconds.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeployApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeployApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeployApiResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_api(self, request):
        """
        This operation is intended for API providers. Only the API that you have defined and published to a runtime environment can be called.
        *   An API is published to a cluster in under 5 seconds.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: DeployApiRequest

        @return: DeployApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    def describe_abolish_api_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAbolishApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAbolishApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_abolish_api_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_abolish_api_task_with_options(request, runtime)

    def describe_access_control_list_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlListAttribute',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_control_list_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_list_attribute_with_options(request, runtime)

    def describe_access_control_lists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlLists',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAccessControlListsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_control_lists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_lists_with_options(request, runtime)

    def describe_api_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        

        @param request: DescribeApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api(self, request):
        """
        This operation is intended for API providers.
        

        @param request: DescribeApiRequest

        @return: DescribeApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    def describe_api_doc_with_options(self, request, runtime):
        """
        For API callers, the specified API must be a public or authorized private API that has been published to a runtime environment.****************\
        *   When you call this operation as an API caller, the service information, parameter definitions, and other details of the API you specify are returned.
        *   When you call this operation as an API provider, the definition of the specified API running in the specified runtime environment is returned. The returned definition takes effect in the runtime environment, and may be different from the definition of the API you modify.
        *   Before you call this operation as an API provider, ensure that the API to be queried is a public one or that your application has been authorized to call the API, because authentication on API callers is required.
        

        @param request: DescribeApiDocRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiDocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiDocResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_doc(self, request):
        """
        For API callers, the specified API must be a public or authorized private API that has been published to a runtime environment.****************\
        *   When you call this operation as an API caller, the service information, parameter definitions, and other details of the API you specify are returned.
        *   When you call this operation as an API provider, the definition of the specified API running in the specified runtime environment is returned. The returned definition takes effect in the runtime environment, and may be different from the definition of the API you modify.
        *   Before you call this operation as an API provider, ensure that the API to be queried is a public one or that your application has been authorized to call the API, because authentication on API callers is required.
        

        @param request: DescribeApiDocRequest

        @return: DescribeApiDocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    def describe_api_group_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        

        @param request: DescribeApiGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_group(self, request):
        """
        This operation is intended for API providers.
        

        @param request: DescribeApiGroupRequest

        @return: DescribeApiGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_with_options(request, runtime)

    def describe_api_group_vpc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_group_vpc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_vpc_whitelist_with_options(request, runtime)

    def describe_api_groups_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        

        @param request: DescribeApiGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_groups(self, request):
        """
        This operation is intended for API providers.
        

        @param request: DescribeApiGroupsRequest

        @return: DescribeApiGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    def describe_api_histories_with_options(self, request, runtime):
        """
        This operation is intended for API providers. Only APIs that have been published have historical version records.
        *   This operation allows you to obtain the historical versions of an API. This operation is always called by other operations.
        

        @param request: DescribeApiHistoriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiHistoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiHistories',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_histories(self, request):
        """
        This operation is intended for API providers. Only APIs that have been published have historical version records.
        *   This operation allows you to obtain the historical versions of an API. This operation is always called by other operations.
        

        @param request: DescribeApiHistoriesRequest

        @return: DescribeApiHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_histories_with_options(request, runtime)

    def describe_api_history_with_options(self, request, runtime):
        """
        Queries the details of a specified historical version of a specified API definition.
        *   This API is intended for API providers.
        *   API Gateway records the time and definition of an API every time the API is published. You can use the version number obtained from other operations to query definition details at a certain publication.
        

        @param request: DescribeApiHistoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiHistory',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_history(self, request):
        """
        Queries the details of a specified historical version of a specified API definition.
        *   This API is intended for API providers.
        *   API Gateway records the time and definition of an API every time the API is published. You can use the version number obtained from other operations to query definition details at a certain publication.
        

        @param request: DescribeApiHistoryRequest

        @return: DescribeApiHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_history_with_options(request, runtime)

    def describe_api_ip_controls_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   If an optional parameter is not specified, all results are returned on separate pages.
        ·
        

        @param request: DescribeApiIpControlsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiIpControlsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_ip_controls(self, request):
        """
        This operation is intended for API callers.
        *   If an optional parameter is not specified, all results are returned on separate pages.
        ·
        

        @param request: DescribeApiIpControlsRequest

        @return: DescribeApiIpControlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_ip_controls_with_options(request, runtime)

    def describe_api_latency_data_with_options(self, request, runtime):
        """
        You can call this operation to query the latency metrics in milliseconds for a specified API.
        *   This API is intended for API providers.
        *   Only statistics for API calls made in the release environment are collected by default.
        

        @param request: DescribeApiLatencyDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiLatencyDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiLatencyData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiLatencyDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_latency_data(self, request):
        """
        You can call this operation to query the latency metrics in milliseconds for a specified API.
        *   This API is intended for API providers.
        *   Only statistics for API calls made in the release environment are collected by default.
        

        @param request: DescribeApiLatencyDataRequest

        @return: DescribeApiLatencyDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_latency_data_with_options(request, runtime)

    def describe_api_market_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiMarketAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiMarketAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_market_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_market_attributes_with_options(request, runtime)

    def describe_api_product_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiProductApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiProductApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_product_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_product_apis_with_options(request, runtime)

    def describe_api_products_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiProductsByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiProductsByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_products_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_products_by_app_with_options(request, runtime)

    def describe_api_qps_data_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   Only statistics for API calls made in the release environment are collected by default.
        

        @param request: DescribeApiQpsDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiQpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiQpsData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_qps_data(self, request):
        """
        This API is intended for API providers.
        *   Only statistics for API calls made in the release environment are collected by default.
        

        @param request: DescribeApiQpsDataRequest

        @return: DescribeApiQpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_qps_data_with_options(request, runtime)

    def describe_api_signatures_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The ApiIds parameter is optional. If this parameter is not specified, all results in the specified environment of an API group are returned.
        

        @param request: DescribeApiSignaturesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiSignaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_signatures(self, request):
        """
        This API is intended for API providers.
        *   The ApiIds parameter is optional. If this parameter is not specified, all results in the specified environment of an API group are returned.
        

        @param request: DescribeApiSignaturesRequest

        @return: DescribeApiSignaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_signatures_with_options(request, runtime)

    def describe_api_traffic_controls_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The ApiIds parameter is optional. If this parameter is not specified, all results in the specified environment of an API group are returned.
        

        @param request: DescribeApiTrafficControlsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiTrafficControlsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_traffic_controls(self, request):
        """
        This API is intended for API providers.
        *   The ApiIds parameter is optional. If this parameter is not specified, all results in the specified environment of an API group are returned.
        

        @param request: DescribeApiTrafficControlsRequest

        @return: DescribeApiTrafficControlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_controls_with_options(request, runtime)

    def describe_api_traffic_data_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   Only statistics for API calls made in the release environment are collected by default.
        

        @param request: DescribeApiTrafficDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_traffic_data(self, request):
        """
        This API is intended for API providers.
        *   Only statistics for API calls made in the release environment are collected by default.
        

        @param request: DescribeApiTrafficDataRequest

        @return: DescribeApiTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_data_with_options(request, runtime)

    def describe_apis_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   This operation returns a list of all APIs that are being defined. The basic information about these APIs is also returned in the list.
        *   This operation returns all APIs that are being edited, regardless of their environments. The returned definitions may be different from the definitions in the environments.
        

        @param request: DescribeApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_method):
            query['ApiMethod'] = request.api_method
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.un_deployed):
            query['UnDeployed'] = request.un_deployed
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis(self, request):
        """
        This operation is intended for API callers.
        *   This operation returns a list of all APIs that are being defined. The basic information about these APIs is also returned in the list.
        *   This operation returns all APIs that are being edited, regardless of their environments. The returned definitions may be different from the definitions in the environments.
        

        @param request: DescribeApisRequest

        @return: DescribeApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    def describe_apis_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    def describe_apis_by_backend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByBackend',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByBackendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_backend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_backend_with_options(request, runtime)

    def describe_apis_by_ip_control_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   You can specify PageNumber to obtain the result on the specified page.
        

        @param request: DescribeApisByIpControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApisByIpControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_ip_control(self, request):
        """
        This operation is intended for API callers.
        *   You can specify PageNumber to obtain the result on the specified page.
        

        @param request: DescribeApisByIpControlRequest

        @return: DescribeApisByIpControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_ip_control_with_options(request, runtime)

    def describe_apis_by_signature_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The results are returned on separate pages. You can specify PageNumber to obtain the result on the specified page.
        

        @param request: DescribeApisBySignatureRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApisBySignatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisBySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisBySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_signature(self, request):
        """
        This API is intended for API providers.
        *   The results are returned on separate pages. You can specify PageNumber to obtain the result on the specified page.
        

        @param request: DescribeApisBySignatureRequest

        @return: DescribeApisBySignatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_signature_with_options(request, runtime)

    def describe_apis_by_traffic_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   You can specify PageNumber to obtain the result on the specified page.
        

        @param request: DescribeApisByTrafficControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApisByTrafficControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_traffic_control(self, request):
        """
        This API is intended for API providers.
        *   You can specify PageNumber to obtain the result on the specified page.
        

        @param request: DescribeApisByTrafficControlRequest

        @return: DescribeApisByTrafficControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_traffic_control_with_options(request, runtime)

    def describe_apis_with_stage_name_integrated_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisWithStageNameIntegratedByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisWithStageNameIntegratedByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_with_stage_name_integrated_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_stage_name_integrated_by_app_with_options(request, runtime)

    def describe_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_with_options(request, runtime)

    def describe_app_attributes_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   AppId is optional.
        

        @param request: DescribeAppAttributesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAppAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_attributes(self, request):
        """
        This operation is intended for API callers.
        *   AppId is optional.
        

        @param request: DescribeAppAttributesRequest

        @return: DescribeAppAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_attributes_with_options(request, runtime)

    def describe_app_security_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppSecurityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_security(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_security_with_options(request, runtime)

    def describe_apps_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   API providers can use the app IDs or their Apsara Stack tenant accounts to query app information.
        *   Each provider can call this operation for a maximum of 200 times every day in a region.
        

        @param request: DescribeAppsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_owner):
            query['AppOwner'] = request.app_owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apps(self, request):
        """
        This API is intended for API providers.
        *   API providers can use the app IDs or their Apsara Stack tenant accounts to query app information.
        *   Each provider can call this operation for a maximum of 200 times every day in a region.
        

        @param request: DescribeAppsRequest

        @return: DescribeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    def describe_apps_by_api_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsByApiProduct',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppsByApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apps_by_api_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_by_api_product_with_options(request, runtime)

    def describe_authorized_apis_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   The specified application can call all APIs included in the responses.
        

        @param request: DescribeAuthorizedApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthorizedApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_authorized_apis(self, request):
        """
        This operation is intended for API callers.
        *   The specified application can call all APIs included in the responses.
        

        @param request: DescribeAuthorizedApisRequest

        @return: DescribeAuthorizedApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apis_with_options(request, runtime)

    def describe_authorized_apps_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   All applications included in the responses have access to the specified API.
        

        @param request: DescribeAuthorizedAppsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthorizedAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_owner_id):
            query['AppOwnerId'] = request.app_owner_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_authorized_apps(self, request):
        """
        This operation is intended for API providers.
        *   All applications included in the responses have access to the specified API.
        

        @param request: DescribeAuthorizedAppsRequest

        @return: DescribeAuthorizedAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apps_with_options(request, runtime)

    def describe_backend_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackendInfo',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeBackendInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backend_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backend_info_with_options(request, runtime)

    def describe_backend_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_name):
            query['BackendName'] = request.backend_name
        if not UtilClient.is_unset(request.backend_type):
            query['BackendType'] = request.backend_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackendList',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeBackendListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_backend_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backend_list_with_options(request, runtime)

    def describe_dataset_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatasetInfo',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDatasetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dataset_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dataset_info_with_options(request, runtime)

    def describe_dataset_item_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatasetItemInfo',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDatasetItemInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dataset_item_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dataset_item_info_with_options(request, runtime)

    def describe_dataset_item_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_item_ids):
            query['DatasetItemIds'] = request.dataset_item_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatasetItemList',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDatasetItemListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dataset_item_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dataset_item_list_with_options(request, runtime)

    def describe_dataset_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_ids):
            query['DatasetIds'] = request.dataset_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatasetList',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDatasetListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dataset_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dataset_list_with_options(request, runtime)

    def describe_deploy_api_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deploy_api_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deploy_api_task_with_options(request, runtime)

    def describe_deployed_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deployed_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_api_with_options(request, runtime)

    def describe_deployed_apis_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        

        @param request: DescribeDeployedApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDeployedApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_method):
            query['ApiMethod'] = request.api_method
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.enable_tag_auth):
            query['EnableTagAuth'] = request.enable_tag_auth
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deployed_apis(self, request):
        """
        This API is intended for API providers.
        

        @param request: DescribeDeployedApisRequest

        @return: DescribeDeployedApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    def describe_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    def describe_group_qps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupQps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeGroupQpsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_qps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_group_qps_with_options(request, runtime)

    def describe_history_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeHistoryApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_history_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    def describe_import_oastask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImportOASTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeImportOASTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_import_oastask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_import_oastask_with_options(request, runtime)

    def describe_instance_drop_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDropConnections',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceDropConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_drop_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_drop_connections_with_options(request, runtime)

    def describe_instance_drop_packet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceDropPacket',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceDropPacketResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_drop_packet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_drop_packet_with_options(request, runtime)

    def describe_instance_http_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceHttpCode',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceHttpCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_http_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_http_code_with_options(request, runtime)

    def describe_instance_latency_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLatency',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceLatencyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_latency(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_latency_with_options(request, runtime)

    def describe_instance_new_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceNewConnections',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceNewConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_new_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_new_connections_with_options(request, runtime)

    def describe_instance_packets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancePackets',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstancePacketsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_packets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_packets_with_options(request, runtime)

    def describe_instance_qps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceQps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceQpsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_qps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_qps_with_options(request, runtime)

    def describe_instance_slb_connect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sbc_name):
            query['SbcName'] = request.sbc_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSlbConnect',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceSlbConnectResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_slb_connect(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_slb_connect_with_options(request, runtime)

    def describe_instance_traffic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTraffic',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstanceTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_traffic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_traffic_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_tag_authorization):
            query['EnableTagAuthorization'] = request.enable_tag_authorization
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_ip_control_policy_items_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   You can filter the query results by policy ID.
        

        @param request: DescribeIpControlPolicyItemsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeIpControlPolicyItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpControlPolicyItems',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlPolicyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_control_policy_items(self, request):
        """
        This operation is intended for API providers.
        *   You can filter the query results by policy ID.
        

        @param request: DescribeIpControlPolicyItemsRequest

        @return: DescribeIpControlPolicyItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_control_policy_items_with_options(request, runtime)

    def describe_ip_controls_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   This operation is used to query the ACLs in a Region. Region is a system parameter.
        *   You can filter the query results by ACL ID, name, or type.
        *   This operation cannot be used to query specific policies. If you want to query specific policies, use the DescribeIpControlPolicyItems operation.
        

        @param request: DescribeIpControlsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeIpControlsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.ip_control_type):
            query['IpControlType'] = request.ip_control_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_controls(self, request):
        """
        This operation is intended for API providers.
        *   This operation is used to query the ACLs in a Region. Region is a system parameter.
        *   You can filter the query results by ACL ID, name, or type.
        *   This operation cannot be used to query specific policies. If you want to query specific policies, use the DescribeIpControlPolicyItems operation.
        

        @param request: DescribeIpControlsRequest

        @return: DescribeIpControlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_controls_with_options(request, runtime)

    def describe_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_config_with_options(request, runtime)

    def describe_market_remains_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMarketRemainsQuota',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeMarketRemainsQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_market_remains_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_market_remains_quota_with_options(request, runtime)

    def describe_models_with_options(self, request, runtime):
        """
        Fuzzy queries are supported.
        

        @param request: DescribeModelsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeModelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModels',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_models(self, request):
        """
        Fuzzy queries are supported.
        

        @param request: DescribeModelsRequest

        @return: DescribeModelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_models_with_options(request, runtime)

    def describe_plugin_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePluginApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugin_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_apis_with_options(request, runtime)

    def describe_plugin_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePluginSchemas',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugin_schemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_schemas_with_options(request, runtime)

    def describe_plugin_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePluginTemplates',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugin_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_templates_with_options(request, runtime)

    def describe_plugins_with_options(self, request, runtime):
        """
        This operation supports pagination.
        *   This operation allows you to query plug-ins by business type.
        *   This operation allows you to query plug-ins by ID.
        *   This operation allows you to query plug-ins by name.
        

        @param request: DescribePluginsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not UtilClient.is_unset(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlugins',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugins(self, request):
        """
        This operation supports pagination.
        *   This operation allows you to query plug-ins by business type.
        *   This operation allows you to query plug-ins by ID.
        *   This operation allows you to query plug-ins by name.
        

        @param request: DescribePluginsRequest

        @return: DescribePluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_with_options(request, runtime)

    def describe_plugins_by_api_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   This operation supports pagination.
        

        @param request: DescribePluginsByApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePluginsByApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePluginsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugins_by_api(self, request):
        """
        This operation is intended for API callers.
        *   This operation supports pagination.
        

        @param request: DescribePluginsByApiRequest

        @return: DescribePluginsByApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_by_api_with_options(request, runtime)

    def describe_purchased_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_purchased_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_group_with_options(request, runtime)

    def describe_purchased_api_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_purchased_api_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_groups_with_options(request, runtime)

    def describe_purchased_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_purchased_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_apis_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        """
        This operation queries regions in which API Gateway is available.
        *   This operation is intended for API providers and callers.
        

        @param request: DescribeRegionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        """
        This operation queries regions in which API Gateway is available.
        *   This operation is intended for API providers and callers.
        

        @param request: DescribeRegionsRequest

        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_signatures_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This operation is used to query the backend signature keys in a Region. Region is a system parameter.
        

        @param request: DescribeSignaturesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSignaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.signature_name):
            query['SignatureName'] = request.signature_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_signatures(self, request):
        """
        This API is intended for API providers.
        *   This operation is used to query the backend signature keys in a Region. Region is a system parameter.
        

        @param request: DescribeSignaturesRequest

        @return: DescribeSignaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_with_options(request, runtime)

    def describe_signatures_by_api_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        

        @param request: DescribeSignaturesByApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSignaturesByApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSignaturesByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesByApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_signatures_by_api(self, request):
        """
        This API is intended for API providers.
        

        @param request: DescribeSignaturesByApiRequest

        @return: DescribeSignaturesByApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_by_api_with_options(request, runtime)

    def describe_summary_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummaryData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSummaryDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_summary_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_summary_data_with_options(request, runtime)

    def describe_system_parameters_with_options(self, request, runtime):
        """
        This API is intended for API callers.
        *   The response of this API contains the system parameters that are optional in API definitions.
        

        @param request: DescribeSystemParametersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSystemParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSystemParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_parameters(self, request):
        """
        This API is intended for API callers.
        *   The response of this API contains the system parameters that are optional in API definitions.
        

        @param request: DescribeSystemParametersRequest

        @return: DescribeSystemParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    def describe_traffic_controls_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This API can be used to query all existing throttling policies (including special throttling policies) and their details.
        *   You can specify query conditions. For example, you can query the throttling policies bound to a specified API or in a specified environment.
        

        @param request: DescribeTrafficControlsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTrafficControlsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_traffic_controls(self, request):
        """
        This API is intended for API providers.
        *   This API can be used to query all existing throttling policies (including special throttling policies) and their details.
        *   You can specify query conditions. For example, you can query the throttling policies bound to a specified API or in a specified environment.
        

        @param request: DescribeTrafficControlsRequest

        @return: DescribeTrafficControlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    def describe_traffic_controls_by_api_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        

        @param request: DescribeTrafficControlsByApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTrafficControlsByApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControlsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_traffic_controls_by_api(self, request):
        """
        This API is intended for API providers.
        

        @param request: DescribeTrafficControlsByApiRequest

        @return: DescribeTrafficControlsByApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_by_api_with_options(request, runtime)

    def describe_update_backend_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpdateBackendTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeUpdateBackendTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_update_backend_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_backend_task_with_options(request, runtime)

    def describe_update_vpc_info_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_uid):
            query['OperationUid'] = request.operation_uid
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpdateVpcInfoTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_update_vpc_info_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_vpc_info_task_with_options(request, runtime)

    def describe_vpc_accesses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_access_id):
            query['VpcAccessId'] = request.vpc_access_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcAccesses',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeVpcAccessesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vpc_accesses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_accesses_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def detach_api_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_product_id):
            query['ApiProductId'] = request.api_product_id
        if not UtilClient.is_unset(request.apis):
            query['Apis'] = request.apis
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachApiProduct',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DetachApiProductResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_api_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_api_product_with_options(request, runtime)

    def detach_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DetachPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_plugin_with_options(request, runtime)

    def disable_instance_access_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstanceAccessControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DisableInstanceAccessControlResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_instance_access_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_access_control_with_options(request, runtime)

    def dry_run_swagger_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.DryRunSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.global_condition_shrink):
            query['GlobalCondition'] = request.global_condition_shrink
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DryRunSwagger',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DryRunSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    def dry_run_swagger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dry_run_swagger_with_options(request, runtime)

    def enable_instance_access_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstanceAccessControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.EnableInstanceAccessControlResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_instance_access_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_access_control_with_options(request, runtime)

    def import_oaswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.backend_name):
            query['BackendName'] = request.backend_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ignore_warning):
            query['IgnoreWarning'] = request.ignore_warning
        if not UtilClient.is_unset(request.oasversion):
            query['OASVersion'] = request.oasversion
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.request_mode):
            query['RequestMode'] = request.request_mode
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.skip_dry_run):
            query['SkipDryRun'] = request.skip_dry_run
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportOAS',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ImportOASResponse(),
            self.call_api(params, req, runtime)
        )

    def import_oas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_oaswith_options(request, runtime)

    def import_swagger_with_options(self, tmp_req, runtime):
        """
        Alibaba Cloud supports extensions based on Swagger 2.0.
        *   Alibaba Cloud supports Swagger configuration files in JSON and YAML formats.
        

        @param tmp_req: ImportSwaggerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportSwaggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.ImportSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.global_condition_shrink):
            query['GlobalCondition'] = request.global_condition_shrink
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportSwagger',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ImportSwaggerResponse(),
            self.call_api(params, req, runtime)
        )

    def import_swagger(self, request):
        """
        Alibaba Cloud supports extensions based on Swagger 2.0.
        *   Alibaba Cloud supports Swagger configuration files in JSON and YAML formats.
        

        @param request: ImportSwaggerRequest

        @return: ImportSwaggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_swagger_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        The Tag.N.Key and Tag.N.Value parameters constitute a key-value pair.
        *   ResourceId.N must meet all the key-value pairs that are entered. If you enter multiple key-value pairs, resources that contain the specified key-value pairs are returned.
        *   This operation is used to query resource tags based on conditions. If no relationship matches the conditions, an empty list is returned.
        *   You can query both user tags and visible system tags.
        *   In addition to the required parameters, you can also specify ResourceId.N to query the visible resource tags of a specified resource in a region.
        *   You can also specify Tag.N.Key to query the visible keys of a specified key in a region.
        *   At least one of ResourceId.N, Tag.N.Key, and Tag.N.Value exists.
        *   You can query tags of the same type or different types in a single operation.
        *   You can query all your user tags and visible system tags.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        The Tag.N.Key and Tag.N.Value parameters constitute a key-value pair.
        *   ResourceId.N must meet all the key-value pairs that are entered. If you enter multiple key-value pairs, resources that contain the specified key-value pairs are returned.
        *   This operation is used to query resource tags based on conditions. If no relationship matches the conditions, an empty list is returned.
        *   You can query both user tags and visible system tags.
        *   In addition to the required parameters, you can also specify ResourceId.N to query the visible resource tags of a specified resource in a region.
        *   You can also specify Tag.N.Key to query the visible keys of a specified key in a region.
        *   At least one of ResourceId.N, Tag.N.Key, and Tag.N.Value exists.
        *   You can query tags of the same type or different types in a single operation.
        *   You can query all your user tags and visible system tags.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_api_with_options(self, request, runtime):
        """
        *This operation is intended for API providers.**\
        *   This API operation requires a full update. Updates of partial parameters are not supported.
        *   When you modify an API name, make sure that the name of each API within the same group is unique.
        *   When you modify the request path, make sure that each request path within the same group is unique.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifyApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.backend_enable):
            query['BackendEnable'] = request.backend_enable
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.constant_parameters):
            query['ConstantParameters'] = request.constant_parameters
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.open_id_connect_config):
            query['OpenIdConnectConfig'] = request.open_id_connect_config
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_parameters):
            query['RequestParameters'] = request.request_parameters
        if not UtilClient.is_unset(request.result_body_model):
            query['ResultBodyModel'] = request.result_body_model
        if not UtilClient.is_unset(request.result_descriptions):
            query['ResultDescriptions'] = request.result_descriptions
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.system_parameters):
            query['SystemParameters'] = request.system_parameters
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.web_socket_api_type):
            query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_api(self, request):
        """
        *This operation is intended for API providers.**\
        *   This API operation requires a full update. Updates of partial parameters are not supported.
        *   When you modify an API name, make sure that the name of each API within the same group is unique.
        *   When you modify the request path, make sure that each request path within the same group is unique.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifyApiRequest

        @return: ModifyApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    def modify_api_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_signature_method):
            query['AllowSignatureMethod'] = request.allow_signature_method
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.app_code_auth_type):
            query['AppCodeAuthType'] = request.app_code_auth_type
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.backend_name):
            query['BackendName'] = request.backend_name
        if not UtilClient.is_unset(request.body_format):
            query['BodyFormat'] = request.body_format
        if not UtilClient.is_unset(request.body_model):
            query['BodyModel'] = request.body_model
        if not UtilClient.is_unset(request.content_type_category):
            query['ContentTypeCategory'] = request.content_type_category
        if not UtilClient.is_unset(request.content_type_value):
            query['ContentTypeValue'] = request.content_type_value
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_internet):
            query['DisableInternet'] = request.disable_internet
        if not UtilClient.is_unset(request.error_code_samples):
            query['ErrorCodeSamples'] = request.error_code_samples
        if not UtilClient.is_unset(request.fail_result_sample):
            query['FailResultSample'] = request.fail_result_sample
        if not UtilClient.is_unset(request.force_nonce_check):
            query['ForceNonceCheck'] = request.force_nonce_check
        if not UtilClient.is_unset(request.function_compute_config):
            query['FunctionComputeConfig'] = request.function_compute_config
        if not UtilClient.is_unset(request.http_config):
            query['HttpConfig'] = request.http_config
        if not UtilClient.is_unset(request.mock_config):
            query['MockConfig'] = request.mock_config
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.oss_config):
            query['OssConfig'] = request.oss_config
        if not UtilClient.is_unset(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not UtilClient.is_unset(request.request_http_method):
            query['RequestHttpMethod'] = request.request_http_method
        if not UtilClient.is_unset(request.request_mode):
            query['RequestMode'] = request.request_mode
        if not UtilClient.is_unset(request.request_parameters):
            query['RequestParameters'] = request.request_parameters
        if not UtilClient.is_unset(request.request_path):
            query['RequestPath'] = request.request_path
        if not UtilClient.is_unset(request.request_protocol):
            query['RequestProtocol'] = request.request_protocol
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not UtilClient.is_unset(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not UtilClient.is_unset(request.use_backend_service):
            query['UseBackendService'] = request.use_backend_service
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        if not UtilClient.is_unset(request.vpc_config):
            query['VpcConfig'] = request.vpc_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiConfiguration',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_api_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_configuration_with_options(request, runtime)

    def modify_api_group_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifyApiGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyApiGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_path):
            query['BasePath'] = request.base_path
        if not UtilClient.is_unset(request.compatible_flags):
            query['CompatibleFlags'] = request.compatible_flags
        if not UtilClient.is_unset(request.custom_trace_config):
            query['CustomTraceConfig'] = request.custom_trace_config
        if not UtilClient.is_unset(request.customer_configs):
            query['CustomerConfigs'] = request.customer_configs
        if not UtilClient.is_unset(request.default_domain):
            query['DefaultDomain'] = request.default_domain
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.passthrough_headers):
            query['PassthroughHeaders'] = request.passthrough_headers
        if not UtilClient.is_unset(request.rpc_pattern):
            query['RpcPattern'] = request.rpc_pattern
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.support_sse):
            query['SupportSSE'] = request.support_sse
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_log_config):
            query['UserLogConfig'] = request.user_log_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_api_group(self, request):
        """
        This operation is intended for API providers.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifyApiGroupRequest

        @return: ModifyApiGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    def modify_api_group_vpc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_api_group_vpc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_vpc_whitelist_with_options(request, runtime)

    def modify_app_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   **AppName** or **Description** can be modified. If these parameters are not specified, no modifications are made and the operation will directly return a success response.
        *   You can call this operation up to 50 times per second per account.
        

        @param request: ModifyAppRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app(self, request):
        """
        This operation is intended for API callers.
        *   **AppName** or **Description** can be modified. If these parameters are not specified, no modifications are made and the operation will directly return a success response.
        *   You can call this operation up to 50 times per second per account.
        

        @param request: ModifyAppRequest

        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    def modify_backend_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.backend_name):
            query['BackendName'] = request.backend_name
        if not UtilClient.is_unset(request.backend_type):
            query['BackendType'] = request.backend_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackend',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyBackendResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backend(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backend_with_options(request, runtime)

    def modify_backend_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_id):
            query['BackendId'] = request.backend_id
        if not UtilClient.is_unset(request.backend_model_data):
            query['BackendModelData'] = request.backend_model_data
        if not UtilClient.is_unset(request.backend_model_id):
            query['BackendModelId'] = request.backend_model_id
        if not UtilClient.is_unset(request.backend_type):
            query['BackendType'] = request.backend_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackendModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyBackendModelResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_backend_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backend_model_with_options(request, runtime)

    def modify_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataset',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dataset_with_options(request, runtime)

    def modify_dataset_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.dataset_item_id):
            query['DatasetItemId'] = request.dataset_item_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatasetItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyDatasetItemResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_dataset_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dataset_item_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.modify_action):
            query['ModifyAction'] = request.modify_action
        if not UtilClient.is_unset(request.skip_wait_switch):
            query['SkipWaitSwitch'] = request.skip_wait_switch
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_intranet_domain_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_intranet_enable):
            query['VpcIntranetEnable'] = request.vpc_intranet_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIntranetDomainPolicy',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIntranetDomainPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_intranet_domain_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_intranet_domain_policy_with_options(request, runtime)

    def modify_ip_control_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   This operation allows you to modify only the name and description of an ACL. You cannot modify the type of the ACL.
        

        @param request: ModifyIpControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyIpControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.ip_control_name):
            query['IpControlName'] = request.ip_control_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_control(self, request):
        """
        This operation is intended for API providers.
        *   This operation allows you to modify only the name and description of an ACL. You cannot modify the type of the ACL.
        

        @param request: ModifyIpControlRequest

        @return: ModifyIpControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_with_options(request, runtime)

    def modify_ip_control_policy_item_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   The modification immediately takes effect on all the APIs that are bound to the policy.
        *   This operation causes a full modification of the content of a policy.
        

        @param request: ModifyIpControlPolicyItemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyIpControlPolicyItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cidr_ip):
            query['CidrIp'] = request.cidr_ip
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.policy_item_id):
            query['PolicyItemId'] = request.policy_item_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_control_policy_item(self, request):
        """
        This operation is intended for API providers.
        *   The modification immediately takes effect on all the APIs that are bound to the policy.
        *   This operation causes a full modification of the content of a policy.
        

        @param request: ModifyIpControlPolicyItemRequest

        @return: ModifyIpControlPolicyItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_policy_item_with_options(request, runtime)

    def modify_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sls_log_store):
            query['SlsLogStore'] = request.sls_log_store
        if not UtilClient.is_unset(request.sls_project):
            query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_config_with_options(request, runtime)

    def modify_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.new_model_name):
            query['NewModelName'] = request.new_model_name
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyModelResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_model_with_options(request, runtime)

    def modify_plugin_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   The name of the plug-in must be unique.
        

        @param request: ModifyPluginRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.plugin_data):
            query['PluginData'] = request.plugin_data
        if not UtilClient.is_unset(request.plugin_id):
            query['PluginId'] = request.plugin_id
        if not UtilClient.is_unset(request.plugin_name):
            query['PluginName'] = request.plugin_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_plugin(self, request):
        """
        This operation is intended for API providers.
        *   The name of the plug-in must be unique.
        

        @param request: ModifyPluginRequest

        @return: ModifyPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_plugin_with_options(request, runtime)

    def modify_signature_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This API operation modifies the name, Key value, and Secret value of an existing signature key.
        *   Note that the modification takes effect immediately. If the key has been bound to an API, you must adjust the backend signature verification based on the new key accordingly.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifySignatureRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySignatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.signature_key):
            query['SignatureKey'] = request.signature_key
        if not UtilClient.is_unset(request.signature_name):
            query['SignatureName'] = request.signature_name
        if not UtilClient.is_unset(request.signature_secret):
            query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_signature(self, request):
        """
        This API is intended for API providers.
        *   This API operation modifies the name, Key value, and Secret value of an existing signature key.
        *   Note that the modification takes effect immediately. If the key has been bound to an API, you must adjust the backend signature verification based on the new key accordingly.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifySignatureRequest

        @return: ModifySignatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_signature_with_options(request, runtime)

    def modify_traffic_control_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The modifications take effect on the bound APIs instantly.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifyTrafficControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyTrafficControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_traffic_control(self, request):
        """
        This API is intended for API providers.
        *   The modifications take effect on the bound APIs instantly.
        *   The QPS limit on this operation is 50 per user.
        

        @param request: ModifyTrafficControlRequest

        @return: ModifyTrafficControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

    def modify_vpc_access_and_update_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.refresh):
            query['Refresh'] = request.refresh
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_target_host_name):
            query['VpcTargetHostName'] = request.vpc_target_host_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcAccessAndUpdateApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyVpcAccessAndUpdateApisResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vpc_access_and_update_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_access_and_update_apis_with_options(request, runtime)

    def open_api_gateway_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenApiGatewayService',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.OpenApiGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_gateway_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_api_gateway_service_with_options(runtime)

    def query_request_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_log_id):
            query['RequestLogId'] = request.request_log_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRequestLogs',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.QueryRequestLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_request_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_request_logs_with_options(request, runtime)

    def reactivate_domain_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   You must solve the problem that is mentioned in the domain name exception prompt before you can reactivate the domain name.
        *   A typical reason why a custom domain name becomes abnormal is that the domain name does not have an ICP filing or the domain name is included in a blacklist by the administration. When a custom domain name is abnormal, users cannot use it to access APIs.
        *   You can call this operation to reactivate the domain name to resume normal access.
        

        @param request: ReactivateDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReactivateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReactivateDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ReactivateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def reactivate_domain(self, request):
        """
        This operation is intended for API providers.
        *   You must solve the problem that is mentioned in the domain name exception prompt before you can reactivate the domain name.
        *   A typical reason why a custom domain name becomes abnormal is that the domain name does not have an ICP filing or the domain name is included in a blacklist by the administration. When a custom domain name is abnormal, users cannot use it to access APIs.
        *   You can call this operation to reactivate the domain name to resume normal access.
        

        @param request: ReactivateDomainRequest

        @return: ReactivateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reactivate_domain_with_options(request, runtime)

    def remove_access_control_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessControlListEntry',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_access_control_list_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_access_control_list_entry_with_options(request, runtime)

    def remove_api_products_authorities_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.RemoveApiProductsAuthoritiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_product_ids):
            request.api_product_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_product_ids, 'ApiProductIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.api_product_ids_shrink):
            query['ApiProductIds'] = request.api_product_ids_shrink
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApiProductsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveApiProductsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_api_products_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_api_products_authorities_with_options(request, runtime)

    def remove_apis_authorities_with_options(self, request, runtime):
        """
        This operation is intended for API providers and callers.
        *   Before you revoke access permissions, check by whom the permissions were granted. API providers can only revoke permissions granted by a Provider, and API callers can only revoke permissions granted by a Consumer.
        

        @param request: RemoveApisAuthoritiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveApisAuthoritiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_apis_authorities(self, request):
        """
        This operation is intended for API providers and callers.
        *   Before you revoke access permissions, check by whom the permissions were granted. API providers can only revoke permissions granted by a Provider, and API callers can only revoke permissions granted by a Consumer.
        

        @param request: RemoveApisAuthoritiesRequest

        @return: RemoveApisAuthoritiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_apis_authorities_with_options(request, runtime)

    def remove_apps_authorities_with_options(self, request, runtime):
        """
        This operation is intended for API providers and callers.
        *   Before you revoke access permissions, check by whom the permissions were granted. API providers can only revoke permissions granted by a Provider, and API callers can only revoke permissions granted by a Consumer.
        

        @param request: RemoveAppsAuthoritiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveAppsAuthoritiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_apps_authorities(self, request):
        """
        This operation is intended for API providers and callers.
        *   Before you revoke access permissions, check by whom the permissions were granted. API providers can only revoke permissions granted by a Provider, and API callers can only revoke permissions granted by a Consumer.
        

        @param request: RemoveAppsAuthoritiesRequest

        @return: RemoveAppsAuthoritiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_apps_authorities_with_options(request, runtime)

    def remove_ip_control_apis_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   The unbinding takes effect immediately. After the API is unbound from the ACL, the corresponding environment does not have any IP address access control in place for the API.
        

        @param request: RemoveIpControlApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveIpControlApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_ip_control_apis(self, request):
        """
        This operation is intended for API callers.
        *   The unbinding takes effect immediately. After the API is unbound from the ACL, the corresponding environment does not have any IP address access control in place for the API.
        

        @param request: RemoveIpControlApisRequest

        @return: RemoveIpControlApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_apis_with_options(request, runtime)

    def remove_ip_control_policy_item_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        

        @param request: RemoveIpControlPolicyItemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveIpControlPolicyItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.policy_item_ids):
            query['PolicyItemIds'] = request.policy_item_ids
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_ip_control_policy_item(self, request):
        """
        This operation is intended for API providers.
        

        @param request: RemoveIpControlPolicyItemRequest

        @return: RemoveIpControlPolicyItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_policy_item_with_options(request, runtime)

    def remove_signature_apis_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The operation takes effect immediately. The request sent from API Gateway to the backend service does not contain the signature string. The corresponding verification step can be removed from the backend.
        

        @param request: RemoveSignatureApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveSignatureApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_signature_apis(self, request):
        """
        This API is intended for API providers.
        *   The operation takes effect immediately. The request sent from API Gateway to the backend service does not contain the signature string. The corresponding verification step can be removed from the backend.
        

        @param request: RemoveSignatureApisRequest

        @return: RemoveSignatureApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_signature_apis_with_options(request, runtime)

    def remove_traffic_control_apis_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This API allows you to unbind a specified throttling policy from up to 100 APIs at a time.
        

        @param request: RemoveTrafficControlApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveTrafficControlApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_traffic_control_apis(self, request):
        """
        This API is intended for API providers.
        *   This API allows you to unbind a specified throttling policy from up to 100 APIs at a time.
        

        @param request: RemoveTrafficControlApisRequest

        @return: RemoveTrafficControlApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_control_apis_with_options(request, runtime)

    def remove_vpc_access_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   Revokes the permissions of API Gateway to access your VPC instance.
        >  Deleting an authorization affects the associated API. Before you delete the authorization, make sure that it is not used by the API.
        

        @param request: RemoveVpcAccessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveVpcAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_vpc_access(self, request):
        """
        This API is intended for API providers.
        *   Revokes the permissions of API Gateway to access your VPC instance.
        >  Deleting an authorization affects the associated API. Before you delete the authorization, make sure that it is not used by the API.
        

        @param request: RemoveVpcAccessRequest

        @return: RemoveVpcAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_with_options(request, runtime)

    def remove_vpc_access_and_abolish_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.need_batch_work):
            query['NeedBatchWork'] = request.need_batch_work
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccessAndAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_vpc_access_and_abolish_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_and_abolish_apis_with_options(request, runtime)

    def reset_app_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.new_app_code):
            query['NewAppCode'] = request.new_app_code
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppCode',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_app_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_app_code_with_options(request, runtime)

    def reset_app_secret_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   A new secret is automatically generated after you have called this operation. This secret cannot be customized.
        *   The results returned by this operation do not contain the application secret. You can obtain the secret by calling DescribeAppSecurity.
        

        @param request: ResetAppSecretRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResetAppSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.new_app_key):
            query['NewAppKey'] = request.new_app_key
        if not UtilClient.is_unset(request.new_app_secret):
            query['NewAppSecret'] = request.new_app_secret
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppSecret',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_app_secret(self, request):
        """
        This operation is intended for API callers.
        *   A new secret is automatically generated after you have called this operation. This secret cannot be customized.
        *   The results returned by this operation do not contain the application secret. You can obtain the secret by calling DescribeAppSecurity.
        

        @param request: ResetAppSecretRequest

        @return: ResetAppSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_app_secret_with_options(request, runtime)

    def sdk_generate_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def sdk_generate_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_app_with_options(request, runtime)

    def sdk_generate_by_app_for_region_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByAppForRegion',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByAppForRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def sdk_generate_by_app_for_region(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_app_for_region_with_options(request, runtime)

    def sdk_generate_by_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SdkGenerateByGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def sdk_generate_by_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_group_with_options(request, runtime)

    def set_access_control_list_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessControlListAttribute',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_access_control_list_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_access_control_list_attribute_with_options(request, runtime)

    def set_api_products_authorities_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.SetApiProductsAuthoritiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.api_product_ids):
            request.api_product_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.api_product_ids, 'ApiProductIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.api_product_ids_shrink):
            query['ApiProductIds'] = request.api_product_ids_shrink
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApiProductsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetApiProductsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_api_products_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_api_products_authorities_with_options(request, runtime)

    def set_apis_authorities_with_options(self, request, runtime):
        """
        This operation is intended for API providers and callers.
        *   API providers can authorize any apps to call their APIs.
        *   API callers can authorize their own apps to call the APIs that they have purchased.
        

        @param request: SetApisAuthoritiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetApisAuthoritiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_apis_authorities(self, request):
        """
        This operation is intended for API providers and callers.
        *   API providers can authorize any apps to call their APIs.
        *   API callers can authorize their own apps to call the APIs that they have purchased.
        

        @param request: SetApisAuthoritiesRequest

        @return: SetApisAuthoritiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_apis_authorities_with_options(request, runtime)

    def set_apps_authorities_with_options(self, request, runtime):
        """
        This operation is intended for API providers and callers.
        *   API providers can authorize any apps to call their APIs.
        *   API callers can authorize their own apps to call the APIs that they have purchased.
        

        @param request: SetAppsAuthoritiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetAppsAuthoritiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.auth_valid_time):
            query['AuthValidTime'] = request.auth_valid_time
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_apps_authorities(self, request):
        """
        This operation is intended for API providers and callers.
        *   API providers can authorize any apps to call their APIs.
        *   API callers can authorize their own apps to call the APIs that they have purchased.
        

        @param request: SetAppsAuthoritiesRequest

        @return: SetAppsAuthoritiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_apps_authorities_with_options(request, runtime)

    def set_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_stage_name):
            query['BindStageName'] = request.bind_stage_name
        if not UtilClient.is_unset(request.custom_domain_type):
            query['CustomDomainType'] = request.custom_domain_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_force):
            query['IsForce'] = request.is_force
        if not UtilClient.is_unset(request.is_http_redirect_to_https):
            query['IsHttpRedirectToHttps'] = request.is_http_redirect_to_https
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_with_options(request, runtime)

    def set_domain_certificate_with_options(self, request, runtime):
        """
        This operation is intended for API providers.
        *   The SSL certificate must match the custom domain name.
        *   After the SSL certificate is bound, HTTPS-based API services become available.
        

        @param request: SetDomainCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificate_body):
            query['CaCertificateBody'] = request.ca_certificate_body
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_private_key):
            query['CertificatePrivateKey'] = request.certificate_private_key
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.ssl_verify_depth):
            query['SslVerifyDepth'] = request.ssl_verify_depth
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_certificate(self, request):
        """
        This operation is intended for API providers.
        *   The SSL certificate must match the custom domain name.
        *   After the SSL certificate is bound, HTTPS-based API services become available.
        

        @param request: SetDomainCertificateRequest

        @return: SetDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    def set_domain_web_socket_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_value):
            query['ActionValue'] = request.action_value
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.wssenable):
            query['WSSEnable'] = request.wssenable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainWebSocketStatus',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainWebSocketStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_web_socket_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_web_socket_status_with_options(request, runtime)

    def set_group_auth_app_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_app_code):
            query['AuthAppCode'] = request.auth_app_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGroupAuthAppCode',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetGroupAuthAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_group_auth_app_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_group_auth_app_code_with_options(request, runtime)

    def set_ip_control_apis_with_options(self, request, runtime):
        """
        This operation is intended for API callers.
        *   A maximum of 100 APIs can be bound at a time.
        

        @param request: SetIpControlApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetIpControlApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip_control_id):
            query['IpControlId'] = request.ip_control_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def set_ip_control_apis(self, request):
        """
        This operation is intended for API callers.
        *   A maximum of 100 APIs can be bound at a time.
        

        @param request: SetIpControlApisRequest

        @return: SetIpControlApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_ip_control_apis_with_options(request, runtime)

    def set_signature_apis_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This operation allows you to bind a signature key to an API. You can bind signature keys for up to 100 APIs at a time.
        

        @param request: SetSignatureApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetSignatureApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.signature_id):
            query['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    def set_signature_apis(self, request):
        """
        This API is intended for API providers.
        *   This operation allows you to bind a signature key to an API. You can bind signature keys for up to 100 APIs at a time.
        

        @param request: SetSignatureApisRequest

        @return: SetSignatureApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_signature_apis_with_options(request, runtime)

    def set_traffic_control_apis_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   This API allows you to bind a specific throttling policy to up to 100 APIs at a time.
        

        @param request: SetTrafficControlApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetTrafficControlApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def set_traffic_control_apis(self, request):
        """
        This API is intended for API providers.
        *   This API allows you to bind a specific throttling policy to up to 100 APIs at a time.
        

        @param request: SetTrafficControlApisRequest

        @return: SetTrafficControlApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_traffic_control_apis_with_options(request, runtime)

    def set_vpc_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_target_host_name):
            query['VpcTargetHostName'] = request.vpc_target_host_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    def set_vpc_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vpc_access_with_options(request, runtime)

    def set_wildcard_domain_patterns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.wildcard_domain_patterns):
            query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWildcardDomainPatterns',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetWildcardDomainPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_wildcard_domain_patterns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_wildcard_domain_patterns_with_options(request, runtime)

    def switch_api_with_options(self, request, runtime):
        """
        This API is intended for API providers.
        *   The historical version can be obtained by calling the **DescribeHistoryApis** operation.
        *   Only APIs that have been published more than once have historical versions.
        *   This operation can only be performed on running APIs. Exercise caution when you perform this operation because the operation cannot be undone. The operation takes up to 5 seconds.
        *   The switch operation is essentially a publish operation. A reason for this operation must be provided.
        

        @param request: SwitchApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SwitchApiResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_api(self, request):
        """
        This API is intended for API providers.
        *   The historical version can be obtained by calling the **DescribeHistoryApis** operation.
        *   Only APIs that have been published more than once have historical versions.
        *   This operation can only be performed on running APIs. Exercise caution when you perform this operation because the operation cannot be undone. The operation takes up to 5 seconds.
        *   The switch operation is essentially a publish operation. A reason for this operation must be provided.
        

        @param request: SwitchApiRequest

        @return: SwitchApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        All tags (key-value pairs) are applied to all resources of a specified ResourceId, with each resource specified as ResourceId.N.
        *   Tag.N is a resource tag consisting of a key-value pair: Tag.N.Key and Tag.N.Value.
        *   If you call this operation to tag multiple resources simultaneously, either all or none of the resources will be tagged.
        *   If you specify Tag.1.Value in addition to required parameters, you must also specify Tag.1.Key. Otherwise, an InvalidParameter.TagKey error is reported. A tag that has a value must have the corresponding key, but the key can be an empty string.
        *   If a tag with the same key has been bound to a resource, the new tag will overwrite the existing one.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        All tags (key-value pairs) are applied to all resources of a specified ResourceId, with each resource specified as ResourceId.N.
        *   Tag.N is a resource tag consisting of a key-value pair: Tag.N.Key and Tag.N.Value.
        *   If you call this operation to tag multiple resources simultaneously, either all or none of the resources will be tagged.
        *   If you specify Tag.1.Value in addition to required parameters, you must also specify Tag.1.Key. Otherwise, an InvalidParameter.TagKey error is reported. A tag that has a value must have the corresponding key, but the key can be an empty string.
        *   If a tag with the same key has been bound to a resource, the new tag will overwrite the existing one.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        If you call this operation to untag multiple resources simultaneously, either all or none of the resources will be untagged.
        *   If you specify resource IDs without specifying tag keys and set the All parameter to true, all tags bound to the specified resources will be deleted. If a resource does not have any tags, the request is not processed but a success is returned.
        *   If you specify resource IDs without specifying tag keys and set the All parameter to false, the request is not processed but a success is returned.
        *   When tag keys are specified, the All parameter is invalid.
        *   When multiple resources and key-value pairs are specified, the specified tags bound to the resources are deleted.
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        If you call this operation to untag multiple resources simultaneously, either all or none of the resources will be untagged.
        *   If you specify resource IDs without specifying tag keys and set the All parameter to true, all tags bound to the specified resources will be deleted. If a resource does not have any tags, the request is not processed but a success is returned.
        *   If you specify resource IDs without specifying tag keys and set the All parameter to false, the request is not processed but a success is returned.
        *   When tag keys are specified, the All parameter is invalid.
        *   When multiple resources and key-value pairs are specified, the specified tags bound to the resources are deleted.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def validate_vpc_connectivity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_access_id):
            query['VpcAccessId'] = request.vpc_access_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateVpcConnectivity',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ValidateVpcConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_vpc_connectivity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_vpc_connectivity_with_options(request, runtime)
