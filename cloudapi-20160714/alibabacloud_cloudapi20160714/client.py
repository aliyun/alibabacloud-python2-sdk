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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AbolishApiResponse(),
            self.do_rpcrequest('AbolishApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abolish_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    def add_ip_control_policy_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddIpControlPolicyItemResponse(),
            self.do_rpcrequest('AddIpControlPolicyItem', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_ip_control_policy_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ip_control_policy_item_with_options(request, runtime)

    def add_traffic_special_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AddTrafficSpecialControlResponse(),
            self.do_rpcrequest('AddTrafficSpecialControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_traffic_special_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    def attach_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.AttachPluginResponse(),
            self.do_rpcrequest('AttachPlugin', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_plugin_with_options(request, runtime)

    def batch_abolish_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchAbolishApisResponse(),
            self.do_rpcrequest('BatchAbolishApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_abolish_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_abolish_apis_with_options(request, runtime)

    def batch_deploy_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.BatchDeployApisResponse(),
            self.do_rpcrequest('BatchDeployApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_deploy_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_deploy_apis_with_options(request, runtime)

    def create_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiResponse(),
            self.do_rpcrequest('CreateApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    def create_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiGroupResponse(),
            self.do_rpcrequest('CreateApiGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_api_group_with_options(request, runtime)

    def create_api_stage_variable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateApiStageVariableResponse(),
            self.do_rpcrequest('CreateApiStageVariable', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_api_stage_variable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_api_stage_variable_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateAppResponse(),
            self.do_rpcrequest('CreateApp', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateInstanceResponse(),
            self.do_rpcrequest('CreateInstance', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_intranet_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIntranetDomainResponse(),
            self.do_rpcrequest('CreateIntranetDomain', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intranet_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intranet_domain_with_options(request, runtime)

    def create_ip_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateIpControlResponse(),
            self.do_rpcrequest('CreateIpControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ip_control_with_options(request, runtime)

    def create_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateLogConfigResponse(),
            self.do_rpcrequest('CreateLogConfig', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_log_config_with_options(request, runtime)

    def create_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateModelResponse(),
            self.do_rpcrequest('CreateModel', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_model_with_options(request, runtime)

    def create_monitor_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateMonitorGroupResponse(),
            self.do_rpcrequest('CreateMonitorGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_monitor_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    def create_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreatePluginResponse(),
            self.do_rpcrequest('CreatePlugin', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_plugin_with_options(request, runtime)

    def create_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateSignatureResponse(),
            self.do_rpcrequest('CreateSignature', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_signature_with_options(request, runtime)

    def create_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.CreateTrafficControlResponse(),
            self.do_rpcrequest('CreateTrafficControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    def delete_all_traffic_special_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAllTrafficSpecialControlResponse(),
            self.do_rpcrequest('DeleteAllTrafficSpecialControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_all_traffic_special_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    def delete_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiResponse(),
            self.do_rpcrequest('DeleteApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    def delete_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiGroupResponse(),
            self.do_rpcrequest('DeleteApiGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    def delete_api_stage_variable_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteApiStageVariableResponse(),
            self.do_rpcrequest('DeleteApiStageVariable', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_api_stage_variable(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_api_stage_variable_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainResponse(),
            self.do_rpcrequest('DeleteDomain', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteDomainCertificateResponse(),
            self.do_rpcrequest('DeleteDomainCertificate', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_certificate_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteInstanceResponse(),
            self.do_rpcrequest('DeleteInstance', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_ip_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteIpControlResponse(),
            self.do_rpcrequest('DeleteIpControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_control_with_options(request, runtime)

    def delete_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteLogConfigResponse(),
            self.do_rpcrequest('DeleteLogConfig', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_log_config_with_options(request, runtime)

    def delete_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteModelResponse(),
            self.do_rpcrequest('DeleteModel', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_model_with_options(request, runtime)

    def delete_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeletePluginResponse(),
            self.do_rpcrequest('DeletePlugin', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_plugin_with_options(request, runtime)

    def delete_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteSignatureResponse(),
            self.do_rpcrequest('DeleteSignature', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_signature_with_options(request, runtime)

    def delete_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficControlResponse(),
            self.do_rpcrequest('DeleteTrafficControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    def delete_traffic_special_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeleteTrafficSpecialControlResponse(),
            self.do_rpcrequest('DeleteTrafficSpecialControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_traffic_special_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    def deploy_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DeployApiResponse(),
            self.do_rpcrequest('DeployApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    def describe_abolish_api_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAbolishApiTaskResponse(),
            self.do_rpcrequest('DescribeAbolishApiTask', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_abolish_api_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_abolish_api_task_with_options(request, runtime)

    def describe_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiResponse(),
            self.do_rpcrequest('DescribeApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    def describe_api_doc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiDocResponse(),
            self.do_rpcrequest('DescribeApiDoc', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_doc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    def describe_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupResponse(),
            self.do_rpcrequest('DescribeApiGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_with_options(request, runtime)

    def describe_api_group_vpc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupVpcWhitelistResponse(),
            self.do_rpcrequest('DescribeApiGroupVpcWhitelist', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_group_vpc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_vpc_whitelist_with_options(request, runtime)

    def describe_api_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiGroupsResponse(),
            self.do_rpcrequest('DescribeApiGroups', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    def describe_api_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoriesResponse(),
            self.do_rpcrequest('DescribeApiHistories', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_histories_with_options(request, runtime)

    def describe_api_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiHistoryResponse(),
            self.do_rpcrequest('DescribeApiHistory', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_history_with_options(request, runtime)

    def describe_api_ip_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiIpControlsResponse(),
            self.do_rpcrequest('DescribeApiIpControls', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_ip_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_ip_controls_with_options(request, runtime)

    def describe_api_latency_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiLatencyDataResponse(),
            self.do_rpcrequest('DescribeApiLatencyData', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_latency_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_latency_data_with_options(request, runtime)

    def describe_api_market_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiMarketAttributesResponse(),
            self.do_rpcrequest('DescribeApiMarketAttributes', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_market_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_market_attributes_with_options(request, runtime)

    def describe_api_qps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiQpsDataResponse(),
            self.do_rpcrequest('DescribeApiQpsData', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_qps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_qps_data_with_options(request, runtime)

    def describe_api_signatures_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiSignaturesResponse(),
            self.do_rpcrequest('DescribeApiSignatures', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_signatures(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_signatures_with_options(request, runtime)

    def describe_api_stage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiStageResponse(),
            self.do_rpcrequest('DescribeApiStage', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_stage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_stage_with_options(request, runtime)

    def describe_api_traffic_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficControlsResponse(),
            self.do_rpcrequest('DescribeApiTrafficControls', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_traffic_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_controls_with_options(request, runtime)

    def describe_api_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApiTrafficDataResponse(),
            self.do_rpcrequest('DescribeApiTrafficData', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_data_with_options(request, runtime)

    def describe_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisResponse(),
            self.do_rpcrequest('DescribeApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    def describe_apis_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByAppResponse(),
            self.do_rpcrequest('DescribeApisByApp', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apis_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    def describe_apis_by_ip_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByIpControlResponse(),
            self.do_rpcrequest('DescribeApisByIpControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apis_by_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_ip_control_with_options(request, runtime)

    def describe_apis_by_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisBySignatureResponse(),
            self.do_rpcrequest('DescribeApisBySignature', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apis_by_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_signature_with_options(request, runtime)

    def describe_apis_by_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeApisByTrafficControlResponse(),
            self.do_rpcrequest('DescribeApisByTrafficControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apis_by_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_traffic_control_with_options(request, runtime)

    def describe_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppResponse(),
            self.do_rpcrequest('DescribeApp', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_with_options(request, runtime)

    def describe_app_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppAttributesResponse(),
            self.do_rpcrequest('DescribeAppAttributes', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_attributes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_attributes_with_options(request, runtime)

    def describe_app_security_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppSecurityResponse(),
            self.do_rpcrequest('DescribeAppSecurity', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_security(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_security_with_options(request, runtime)

    def describe_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAppsResponse(),
            self.do_rpcrequest('DescribeApps', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    def describe_authorized_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedApisResponse(),
            self.do_rpcrequest('DescribeAuthorizedApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_authorized_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apis_with_options(request, runtime)

    def describe_authorized_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeAuthorizedAppsResponse(),
            self.do_rpcrequest('DescribeAuthorizedApps', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_authorized_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_authorized_apps_with_options(request, runtime)

    def describe_deploy_api_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployApiTaskResponse(),
            self.do_rpcrequest('DescribeDeployApiTask', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deploy_api_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deploy_api_task_with_options(request, runtime)

    def describe_deployed_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApiResponse(),
            self.do_rpcrequest('DescribeDeployedApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deployed_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_api_with_options(request, runtime)

    def describe_deployed_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDeployedApisResponse(),
            self.do_rpcrequest('DescribeDeployedApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deployed_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    def describe_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeDomainResponse(),
            self.do_rpcrequest('DescribeDomain', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    def describe_history_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeHistoryApisResponse(),
            self.do_rpcrequest('DescribeHistoryApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_history_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    def describe_ip_control_policy_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlPolicyItemsResponse(),
            self.do_rpcrequest('DescribeIpControlPolicyItems', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_control_policy_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_control_policy_items_with_options(request, runtime)

    def describe_ip_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeIpControlsResponse(),
            self.do_rpcrequest('DescribeIpControls', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ip_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_controls_with_options(request, runtime)

    def describe_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeLogConfigResponse(),
            self.do_rpcrequest('DescribeLogConfig', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_config_with_options(request, runtime)

    def describe_market_remains_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeMarketRemainsQuotaResponse(),
            self.do_rpcrequest('DescribeMarketRemainsQuota', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_market_remains_quota(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_market_remains_quota_with_options(request, runtime)

    def describe_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeModelsResponse(),
            self.do_rpcrequest('DescribeModels', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_models_with_options(request, runtime)

    def describe_plugin_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginSchemasResponse(),
            self.do_rpcrequest('DescribePluginSchemas', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_plugin_schemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_schemas_with_options(request, runtime)

    def describe_plugin_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginTemplatesResponse(),
            self.do_rpcrequest('DescribePluginTemplates', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_plugin_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugin_templates_with_options(request, runtime)

    def describe_plugins_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsResponse(),
            self.do_rpcrequest('DescribePlugins', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_plugins(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_with_options(request, runtime)

    def describe_plugins_by_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePluginsByApiResponse(),
            self.do_rpcrequest('DescribePluginsByApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_plugins_by_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_plugins_by_api_with_options(request, runtime)

    def describe_purchased_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupResponse(),
            self.do_rpcrequest('DescribePurchasedApiGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_purchased_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_group_with_options(request, runtime)

    def describe_purchased_api_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApiGroupsResponse(),
            self.do_rpcrequest('DescribePurchasedApiGroups', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_purchased_api_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_groups_with_options(request, runtime)

    def describe_purchased_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribePurchasedApisResponse(),
            self.do_rpcrequest('DescribePurchasedApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_purchased_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_apis_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_signatures_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesResponse(),
            self.do_rpcrequest('DescribeSignatures', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_signatures(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_with_options(request, runtime)

    def describe_signatures_by_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSignaturesByApiResponse(),
            self.do_rpcrequest('DescribeSignaturesByApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_signatures_by_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_signatures_by_api_with_options(request, runtime)

    def describe_system_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeSystemParametersResponse(),
            self.do_rpcrequest('DescribeSystemParameters', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_system_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    def describe_traffic_controls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsResponse(),
            self.do_rpcrequest('DescribeTrafficControls', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_traffic_controls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    def describe_traffic_controls_by_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeTrafficControlsByApiResponse(),
            self.do_rpcrequest('DescribeTrafficControlsByApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_traffic_controls_by_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_by_api_with_options(request, runtime)

    def describe_update_vpc_info_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeUpdateVpcInfoTaskResponse(),
            self.do_rpcrequest('DescribeUpdateVpcInfoTask', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_update_vpc_info_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_vpc_info_task_with_options(request, runtime)

    def describe_vpc_accesses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeVpcAccessesResponse(),
            self.do_rpcrequest('DescribeVpcAccesses', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_accesses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_accesses_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.DryRunSwaggerResponse(),
            self.do_rpcrequest('DryRunSwagger', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ImportSwaggerResponse(),
            self.do_rpcrequest('ImportSwagger', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_swagger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_swagger_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiResponse(),
            self.do_rpcrequest('ModifyApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    def modify_api_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupResponse(),
            self.do_rpcrequest('ModifyApiGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_api_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    def modify_api_group_vpc_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyApiGroupVpcWhitelistResponse(),
            self.do_rpcrequest('ModifyApiGroupVpcWhitelist', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_api_group_vpc_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_vpc_whitelist_with_options(request, runtime)

    def modify_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyAppResponse(),
            self.do_rpcrequest('ModifyApp', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyInstanceSpecResponse(),
            self.do_rpcrequest('ModifyInstanceSpec', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_ip_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlResponse(),
            self.do_rpcrequest('ModifyIpControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ip_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_with_options(request, runtime)

    def modify_ip_control_policy_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyIpControlPolicyItemResponse(),
            self.do_rpcrequest('ModifyIpControlPolicyItem', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ip_control_policy_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_control_policy_item_with_options(request, runtime)

    def modify_log_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyLogConfigResponse(),
            self.do_rpcrequest('ModifyLogConfig', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_log_config_with_options(request, runtime)

    def modify_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyModelResponse(),
            self.do_rpcrequest('ModifyModel', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_model_with_options(request, runtime)

    def modify_plugin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyPluginResponse(),
            self.do_rpcrequest('ModifyPlugin', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_plugin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_plugin_with_options(request, runtime)

    def modify_signature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifySignatureResponse(),
            self.do_rpcrequest('ModifySignature', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_signature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_signature_with_options(request, runtime)

    def modify_traffic_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ModifyTrafficControlResponse(),
            self.do_rpcrequest('ModifyTrafficControl', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_traffic_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

    def open_api_gateway_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cloud_api20160714_models.OpenApiGatewayServiceResponse(),
            self.do_rpcrequest('OpenApiGatewayService', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_api_gateway_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_api_gateway_service_with_options(runtime)

    def reactivate_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ReactivateDomainResponse(),
            self.do_rpcrequest('ReactivateDomain', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reactivate_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reactivate_domain_with_options(request, runtime)

    def remove_apis_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveApisAuthoritiesResponse(),
            self.do_rpcrequest('RemoveApisAuthorities', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_apis_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_apis_authorities_with_options(request, runtime)

    def remove_apps_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveAppsAuthoritiesResponse(),
            self.do_rpcrequest('RemoveAppsAuthorities', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_apps_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_apps_authorities_with_options(request, runtime)

    def remove_ip_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlApisResponse(),
            self.do_rpcrequest('RemoveIpControlApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_ip_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_apis_with_options(request, runtime)

    def remove_ip_control_policy_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveIpControlPolicyItemResponse(),
            self.do_rpcrequest('RemoveIpControlPolicyItem', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_ip_control_policy_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_ip_control_policy_item_with_options(request, runtime)

    def remove_signature_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveSignatureApisResponse(),
            self.do_rpcrequest('RemoveSignatureApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_signature_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_signature_apis_with_options(request, runtime)

    def remove_traffic_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveTrafficControlApisResponse(),
            self.do_rpcrequest('RemoveTrafficControlApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_traffic_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_traffic_control_apis_with_options(request, runtime)

    def remove_vpc_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessResponse(),
            self.do_rpcrequest('RemoveVpcAccess', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_vpc_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_with_options(request, runtime)

    def remove_vpc_access_and_abolish_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.RemoveVpcAccessAndAbolishApisResponse(),
            self.do_rpcrequest('RemoveVpcAccessAndAbolishApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_vpc_access_and_abolish_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vpc_access_and_abolish_apis_with_options(request, runtime)

    def reset_app_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppCodeResponse(),
            self.do_rpcrequest('ResetAppCode', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_app_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_app_code_with_options(request, runtime)

    def reset_app_secret_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.ResetAppSecretResponse(),
            self.do_rpcrequest('ResetAppSecret', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_app_secret(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_app_secret_with_options(request, runtime)

    def sdk_generate_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByAppResponse(),
            self.do_rpcrequest('SdkGenerateByApp', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sdk_generate_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_app_with_options(request, runtime)

    def sdk_generate_by_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SdkGenerateByGroupResponse(),
            self.do_rpcrequest('SdkGenerateByGroup', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sdk_generate_by_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sdk_generate_by_group_with_options(request, runtime)

    def set_apis_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetApisAuthoritiesResponse(),
            self.do_rpcrequest('SetApisAuthorities', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_apis_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_apis_authorities_with_options(request, runtime)

    def set_apps_authorities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetAppsAuthoritiesResponse(),
            self.do_rpcrequest('SetAppsAuthorities', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_apps_authorities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_apps_authorities_with_options(request, runtime)

    def set_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainResponse(),
            self.do_rpcrequest('SetDomain', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_with_options(request, runtime)

    def set_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainCertificateResponse(),
            self.do_rpcrequest('SetDomainCertificate', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    def set_domain_web_socket_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetDomainWebSocketStatusResponse(),
            self.do_rpcrequest('SetDomainWebSocketStatus', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain_web_socket_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_web_socket_status_with_options(request, runtime)

    def set_ip_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetIpControlApisResponse(),
            self.do_rpcrequest('SetIpControlApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_ip_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_ip_control_apis_with_options(request, runtime)

    def set_signature_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetSignatureApisResponse(),
            self.do_rpcrequest('SetSignatureApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_signature_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_signature_apis_with_options(request, runtime)

    def set_traffic_control_apis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetTrafficControlApisResponse(),
            self.do_rpcrequest('SetTrafficControlApis', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_traffic_control_apis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_traffic_control_apis_with_options(request, runtime)

    def set_vpc_access_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetVpcAccessResponse(),
            self.do_rpcrequest('SetVpcAccess', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vpc_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vpc_access_with_options(request, runtime)

    def set_wildcard_domain_patterns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SetWildcardDomainPatternsResponse(),
            self.do_rpcrequest('SetWildcardDomainPatterns', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_wildcard_domain_patterns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_wildcard_domain_patterns_with_options(request, runtime)

    def switch_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.SwitchApiResponse(),
            self.do_rpcrequest('SwitchApi', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloud_api20160714_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2016-07-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
