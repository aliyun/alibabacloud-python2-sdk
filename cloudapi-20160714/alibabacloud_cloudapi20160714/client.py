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
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AbolishApiResponse(),
            self.call_api(params, req, runtime)
        )

    def abolish_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    def add_ip_control_policy_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CidrIp'] = request.cidr_ip
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ip_control_policy_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ip_control_policy_item_with_options(request, runtime)

    def add_traffic_special_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SpecialKey'] = request.special_key
        query['SpecialType'] = request.special_type
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    def add_traffic_special_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    def attach_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PluginId'] = request.plugin_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AttachPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AttachPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_plugin_with_options(request, runtime)

    def batch_abolish_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Api'] = request.api
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Api'] = request.api
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeployApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchDeployApisResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_deploy_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_deploy_apis_with_options(request, runtime)

    def create_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AllowSignatureMethod'] = request.allow_signature_method
        query['ApiName'] = request.api_name
        query['AppCodeAuthType'] = request.app_code_auth_type
        query['AuthType'] = request.auth_type
        query['ConstantParameters'] = request.constant_parameters
        query['Description'] = request.description
        query['DisableInternet'] = request.disable_internet
        query['ErrorCodeSamples'] = request.error_code_samples
        query['FailResultSample'] = request.fail_result_sample
        query['ForceNonceCheck'] = request.force_nonce_check
        query['GroupId'] = request.group_id
        query['OpenIdConnectConfig'] = request.open_id_connect_config
        query['RequestConfig'] = request.request_config
        query['RequestParameters'] = request.request_parameters
        query['ResultBodyModel'] = request.result_body_model
        query['ResultDescriptions'] = request.result_descriptions
        query['ResultSample'] = request.result_sample
        query['ResultType'] = request.result_type
        query['SecurityToken'] = request.security_token
        query['ServiceConfig'] = request.service_config
        query['ServiceParameters'] = request.service_parameters
        query['ServiceParametersMap'] = request.service_parameters_map
        query['SystemParameters'] = request.system_parameters
        query['Visibility'] = request.visibility
        query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiResponse(),
            self.call_api(params, req, runtime)
        )

    def create_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    def create_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BasePath'] = request.base_path
        query['Description'] = request.description
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageId'] = request.stage_id
        query['StageRouteModel'] = request.stage_route_model
        query['SupportRoute'] = request.support_route
        query['VariableName'] = request.variable_name
        query['VariableValue'] = request.variable_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_api_stage_variable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_api_stage_variable_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['Source'] = request.source
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['ChargeType'] = request.charge_type
        query['Duration'] = request.duration
        query['HttpsPolicy'] = request.https_policy
        query['InstanceName'] = request.instance_name
        query['InstanceSpec'] = request.instance_spec
        query['PricingCycle'] = request.pricing_cycle
        query['Token'] = request.token
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIntranetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['IpControlName'] = request.ip_control_name
        query['IpControlPolicys'] = request.ip_control_policys
        query['IpControlType'] = request.ip_control_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ip_control_with_options(request, runtime)

    def create_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        query['SlsLogStore'] = request.sls_log_store
        query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    def create_monitor_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Auth'] = request.auth
        query['GroupId'] = request.group_id
        query['RawMonitorGroupId'] = request.raw_monitor_group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMonitorGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['PluginData'] = request.plugin_data
        query['PluginName'] = request.plugin_name
        query['PluginType'] = request.plugin_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreatePluginResponse(),
            self.call_api(params, req, runtime)
        )

    def create_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_plugin_with_options(request, runtime)

    def create_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureKey'] = request.signature_key
        query['SignatureName'] = request.signature_name
        query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def create_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_signature_with_options(request, runtime)

    def create_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiDefault'] = request.api_default
        query['AppDefault'] = request.app_default
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['TrafficControlName'] = request.traffic_control_name
        query['TrafficControlUnit'] = request.traffic_control_unit
        query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    def delete_all_traffic_special_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_all_traffic_special_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    def delete_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    def delete_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    def delete_api_stage_variable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageId'] = request.stage_id
        query['VariableName'] = request.variable_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApiStageVariable',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiStageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_api_stage_variable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_stage_variable_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CertificateId'] = request.certificate_id
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['InstanceId'] = request.instance_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_control_with_options(request, runtime)

    def delete_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    def delete_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PluginId'] = request.plugin_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeletePluginResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_plugin_with_options(request, runtime)

    def delete_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_signature_with_options(request, runtime)

    def delete_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    def delete_traffic_special_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SpecialKey'] = request.special_key
        query['SpecialType'] = request.special_type
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_traffic_special_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    def deploy_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeployApiResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    def describe_abolish_api_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAbolishApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAbolishApiTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_abolish_api_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_abolish_api_task_with_options(request, runtime)

    def describe_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    def describe_api_doc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiDocResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_doc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    def describe_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_with_options(request, runtime)

    def describe_api_group_vpc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Sort'] = request.sort
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    def describe_api_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiHistories',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_histories_with_options(request, runtime)

    def describe_api_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['HistoryVersion'] = request.history_version
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiHistory',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_history_with_options(request, runtime)

    def describe_api_ip_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_ip_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_ip_controls_with_options(request, runtime)

    def describe_api_latency_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiLatencyData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiLatencyDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_latency_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_latency_data_with_options(request, runtime)

    def describe_api_market_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiMarketAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiMarketAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_market_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_market_attributes_with_options(request, runtime)

    def describe_api_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiQpsData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_qps_data_with_options(request, runtime)

    def describe_api_signatures_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_signatures(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_signatures_with_options(request, runtime)

    def describe_api_traffic_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_traffic_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_controls_with_options(request, runtime)

    def describe_api_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['EndTime'] = request.end_time
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApiTrafficData',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_data_with_options(request, runtime)

    def describe_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['CatalogId'] = request.catalog_id
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    def describe_apis_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiName'] = request.api_name
        query['ApiUid'] = request.api_uid
        query['AppId'] = request.app_id
        query['Method'] = request.method
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Path'] = request.path
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    def describe_apis_by_ip_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_ip_control_with_options(request, runtime)

    def describe_apis_by_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisBySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisBySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_signature_with_options(request, runtime)

    def describe_apis_by_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApisByTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis_by_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_traffic_control_with_options(request, runtime)

    def describe_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['AppCode'] = request.app_code
        query['AppId'] = request.app_id
        query['AppKey'] = request.app_key
        query['AppName'] = request.app_name
        query['EnableTagAuth'] = request.enable_tag_auth
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['Sort'] = request.sort
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppAttributes',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_attributes_with_options(request, runtime)

    def describe_app_security_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppOwner'] = request.app_owner
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    def describe_authorized_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_authorized_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apis_with_options(request, runtime)

    def describe_authorized_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppId'] = request.app_id
        query['AppName'] = request.app_name
        query['AppOwnerId'] = request.app_owner_id
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAuthorizedApps',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_authorized_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apps_with_options(request, runtime)

    def describe_deploy_api_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployApiTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['EnableTagAuth'] = request.enable_tag_auth
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deployed_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    def describe_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    def describe_history_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeHistoryApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_history_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    def describe_ip_control_policy_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PolicyItemId'] = request.policy_item_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpControlPolicyItems',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlPolicyItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_control_policy_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_control_policy_items_with_options(request, runtime)

    def describe_ip_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['IpControlName'] = request.ip_control_name
        query['IpControlType'] = request.ip_control_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeIpControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_controls_with_options(request, runtime)

    def describe_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DomainName'] = request.domain_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMarketRemainsQuota',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['ModelId'] = request.model_id
        query['ModelName'] = request.model_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeModels',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_models_with_options(request, runtime)

    def describe_plugin_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginSchemas',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Language'] = request.language
        query['PluginName'] = request.plugin_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginTemplates',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PluginId'] = request.plugin_id
        query['PluginName'] = request.plugin_name
        query['PluginType'] = request.plugin_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePlugins',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugins(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_with_options(request, runtime)

    def describe_plugins_by_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePluginsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_plugins_by_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_by_api_with_options(request, runtime)

    def describe_purchased_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_signatures_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['SignatureName'] = request.signature_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSignatures',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_signatures(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_with_options(request, runtime)

    def describe_signatures_by_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSignaturesByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesByApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_signatures_by_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_by_api_with_options(request, runtime)

    def describe_system_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSystemParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_system_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    def describe_traffic_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_traffic_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    def describe_traffic_controls_by_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControlsByApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_traffic_controls_by_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_by_api_with_options(request, runtime)

    def describe_update_vpc_info_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OperationUid'] = request.operation_uid
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUpdateVpcInfoTask',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SecurityToken'] = request.security_token
        query['VpcAccessId'] = request.vpc_access_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeVpcAccesses',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def dry_run_swagger_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.DryRunSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        query['DataFormat'] = request.data_format
        query['GlobalCondition'] = request.global_condition_shrink
        query['GroupId'] = request.group_id
        query['Overwrite'] = request.overwrite
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
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

    def import_swagger_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloud_api20160714_models.ImportSwaggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.global_condition):
            request.global_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.global_condition, 'GlobalCondition', 'json')
        query = {}
        query['DataFormat'] = request.data_format
        query['DryRun'] = request.dry_run
        query['GlobalCondition'] = request.global_condition_shrink
        query['GroupId'] = request.group_id
        query['Overwrite'] = request.overwrite
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
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
        runtime = util_models.RuntimeOptions()
        return self.import_swagger_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AllowSignatureMethod'] = request.allow_signature_method
        query['ApiId'] = request.api_id
        query['ApiName'] = request.api_name
        query['AppCodeAuthType'] = request.app_code_auth_type
        query['AuthType'] = request.auth_type
        query['ConstantParameters'] = request.constant_parameters
        query['Description'] = request.description
        query['DisableInternet'] = request.disable_internet
        query['ErrorCodeSamples'] = request.error_code_samples
        query['FailResultSample'] = request.fail_result_sample
        query['ForceNonceCheck'] = request.force_nonce_check
        query['GroupId'] = request.group_id
        query['OpenIdConnectConfig'] = request.open_id_connect_config
        query['RequestConfig'] = request.request_config
        query['RequestParameters'] = request.request_parameters
        query['ResultBodyModel'] = request.result_body_model
        query['ResultDescriptions'] = request.result_descriptions
        query['ResultSample'] = request.result_sample
        query['ResultType'] = request.result_type
        query['SecurityToken'] = request.security_token
        query['ServiceConfig'] = request.service_config
        query['ServiceParameters'] = request.service_parameters
        query['ServiceParametersMap'] = request.service_parameters_map
        query['SystemParameters'] = request.system_parameters
        query['Visibility'] = request.visibility
        query['WebSocketApiType'] = request.web_socket_api_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    def modify_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BasePath'] = request.base_path
        query['CompatibleFlags'] = request.compatible_flags
        query['CustomTraceConfig'] = request.custom_trace_config
        query['CustomerConfigs'] = request.customer_configs
        query['DefaultDomain'] = request.default_domain
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['PassthroughHeaders'] = request.passthrough_headers
        query['RpcPattern'] = request.rpc_pattern
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        query['UserLogConfig'] = request.user_log_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    def modify_api_group_vpc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['VpcIds'] = request.vpc_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApiGroupVpcWhitelist',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppName'] = request.app_name
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AutoPay'] = request.auto_pay
        query['InstanceId'] = request.instance_id
        query['InstanceSpec'] = request.instance_spec
        query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_ip_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['IpControlId'] = request.ip_control_id
        query['IpControlName'] = request.ip_control_name
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyIpControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_with_options(request, runtime)

    def modify_ip_control_policy_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CidrIp'] = request.cidr_ip
        query['IpControlId'] = request.ip_control_id
        query['PolicyItemId'] = request.policy_item_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ip_control_policy_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_policy_item_with_options(request, runtime)

    def modify_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['LogType'] = request.log_type
        query['SecurityToken'] = request.security_token
        query['SlsLogStore'] = request.sls_log_store
        query['SlsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyLogConfig',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['ModelName'] = request.model_name
        query['NewModelName'] = request.new_model_name
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyModel',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['PluginData'] = request.plugin_data
        query['PluginId'] = request.plugin_id
        query['PluginName'] = request.plugin_name
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyPlugin',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_plugin_with_options(request, runtime)

    def modify_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['SignatureKey'] = request.signature_key
        query['SignatureName'] = request.signature_name
        query['SignatureSecret'] = request.signature_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySignature',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifySignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_signature_with_options(request, runtime)

    def modify_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiDefault'] = request.api_default
        query['AppDefault'] = request.app_default
        query['Description'] = request.description
        query['SecurityToken'] = request.security_token
        query['TrafficControlId'] = request.traffic_control_id
        query['TrafficControlName'] = request.traffic_control_name
        query['TrafficControlUnit'] = request.traffic_control_unit
        query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

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
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.OpenApiGatewayServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_gateway_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_api_gateway_service_with_options(runtime)

    def reactivate_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReactivateDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ReactivateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def reactivate_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reactivate_domain_with_options(request, runtime)

    def remove_apis_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['AppId'] = request.app_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_apis_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_apis_authorities_with_options(request, runtime)

    def remove_apps_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppIds'] = request.app_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_apps_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_apps_authorities_with_options(request, runtime)

    def remove_ip_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_ip_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_apis_with_options(request, runtime)

    def remove_ip_control_policy_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['IpControlId'] = request.ip_control_id
        query['PolicyItemIds'] = request.policy_item_ids
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveIpControlPolicyItem',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlPolicyItemResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_ip_control_policy_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_policy_item_with_options(request, runtime)

    def remove_signature_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_signature_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_signature_apis_with_options(request, runtime)

    def remove_traffic_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_traffic_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_control_apis_with_options(request, runtime)

    def remove_vpc_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NeedBatchWork'] = request.need_batch_work
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_vpc_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_with_options(request, runtime)

    def remove_vpc_access_and_abolish_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['NeedBatchWork'] = request.need_batch_work
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveVpcAccessAndAbolishApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['AppCode'] = request.app_code
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAppCode',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['AppKey'] = request.app_key
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAppSecret',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppSecretResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_app_secret_with_options(request, runtime)

    def sdk_generate_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SdkGenerateByApp',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def sdk_generate_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_app_with_options(request, runtime)

    def sdk_generate_by_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['GroupId'] = request.group_id
        query['Language'] = request.language
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SdkGenerateByGroup',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def sdk_generate_by_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_group_with_options(request, runtime)

    def set_apis_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['AppId'] = request.app_id
        query['AuthValidTime'] = request.auth_valid_time
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetApisAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetApisAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_apis_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_apis_authorities_with_options(request, runtime)

    def set_apps_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['AppIds'] = request.app_ids
        query['AuthValidTime'] = request.auth_valid_time
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAppsAuthorities',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetAppsAuthoritiesResponse(),
            self.call_api(params, req, runtime)
        )

    def set_apps_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_apps_authorities_with_options(request, runtime)

    def set_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['BindStageName'] = request.bind_stage_name
        query['CustomDomainType'] = request.custom_domain_type
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['IsForce'] = request.is_force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['CaCertificateBody'] = request.ca_certificate_body
        query['CertificateBody'] = request.certificate_body
        query['CertificateName'] = request.certificate_name
        query['CertificatePrivateKey'] = request.certificate_private_key
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    def set_domain_web_socket_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ActionValue'] = request.action_value
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDomainWebSocketStatus',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainWebSocketStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_web_socket_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_web_socket_status_with_options(request, runtime)

    def set_ip_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['IpControlId'] = request.ip_control_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetIpControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetIpControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def set_ip_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_ip_control_apis_with_options(request, runtime)

    def set_signature_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['SignatureId'] = request.signature_id
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSignatureApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetSignatureApisResponse(),
            self.call_api(params, req, runtime)
        )

    def set_signature_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_signature_apis_with_options(request, runtime)

    def set_traffic_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ApiIds'] = request.api_ids
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetTrafficControlApis',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetTrafficControlApisResponse(),
            self.call_api(params, req, runtime)
        )

    def set_traffic_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_traffic_control_apis_with_options(request, runtime)

    def set_vpc_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['Port'] = request.port
        query['SecurityToken'] = request.security_token
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetVpcAccess',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DomainName'] = request.domain_name
        query['GroupId'] = request.group_id
        query['SecurityToken'] = request.security_token
        query['WildcardDomainPatterns'] = request.wildcard_domain_patterns
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetWildcardDomainPatterns',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        UtilClient.validate_model(request)
        query = {}
        query['ApiId'] = request.api_id
        query['Description'] = request.description
        query['GroupId'] = request.group_id
        query['HistoryVersion'] = request.history_version
        query['SecurityToken'] = request.security_token
        query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SwitchApiResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['SecurityToken'] = request.security_token
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['ResourceType'] = request.resource_type
        query['SecurityToken'] = request.security_token
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160714_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
