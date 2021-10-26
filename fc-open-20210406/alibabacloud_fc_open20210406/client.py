# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
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
            'ap-northeast-1': 'account-id.ap-northeast-1.fc.aliyuncs.com',
            'ap-south-1': 'account-id.ap-south-1.fc.aliyuncs.com',
            'ap-southeast-1': 'account-id.ap-southeast-1.fc.aliyuncs.com',
            'ap-southeast-2': 'account-id.ap-southeast-2.fc.aliyuncs.com',
            'ap-southeast-3': 'account-id.ap-southeast-3.fc.aliyuncs.com',
            'ap-southeast-5': 'account-id.ap-southeast-5.fc.aliyuncs.com',
            'cn-beijing': 'account-id.cn-beijing.fc.aliyuncs.com',
            'cn-chengdu': 'account-id.cn-chengdu.fc.aliyuncs.com',
            'cn-hangzhou': 'account-id.cn-hangzhou.fc.aliyuncs.com',
            'cn-hangzhou-finance': 'account-id.cn-hangzhou-finance.fc.aliyuncs.com',
            'cn-hongkong': 'account-id.cn-hongkong.fc.aliyuncs.com',
            'cn-huhehaote': 'account-id.cn-huhehaote.fc.aliyuncs.com',
            'cn-north-2-gov-1': 'account-id.cn-north-2-gov-1.fc.aliyuncs.com',
            'cn-qingdao': 'account-id.cn-qingdao.fc.aliyuncs.com',
            'cn-shanghai': 'account-id.cn-shanghai.fc.aliyuncs.com',
            'cn-shenzhen': 'account-id.cn-shenzhen.fc.aliyuncs.com',
            'cn-zhangjiakou': 'account-id.cn-zhangjiakou.fc.aliyuncs.com',
            'eu-central-1': 'account-id.eu-central-1.fc.aliyuncs.com',
            'eu-west-1': 'account-id.eu-west-1.fc.aliyuncs.com',
            'us-east-1': 'account-id.us-east-1.fc.aliyuncs.com',
            'us-west-1': 'account-id.us-west-1.fc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('fc-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_alias(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_alias_with_options(service_name, request, headers, runtime)

    def create_alias_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.additional_version_weight):
            body['additionalVersionWeight'] = request.additional_version_weight
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateAliasResponse(),
            self.do_roarequest('CreateAlias', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/aliases' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def create_custom_domain(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_custom_domain_with_options(request, headers, runtime)

    def create_custom_domain_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_config):
            body['certConfig'] = request.cert_config
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.route_config):
            body['routeConfig'] = request.route_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateCustomDomainResponse(),
            self.do_roarequest('CreateCustomDomain', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/custom-domains', 'json', req, runtime)
        )

    def create_function(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.CreateFunctionHeaders()
        return self.create_function_with_options(service_name, request, headers, runtime)

    def create_function_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.ca_port):
            body['caPort'] = request.ca_port
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.custom_container_config):
            body['customContainerConfig'] = request.custom_container_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_variables):
            body['environmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.function_name):
            body['functionName'] = request.function_name
        if not UtilClient.is_unset(request.handler):
            body['handler'] = request.handler
        if not UtilClient.is_unset(request.initialization_timeout):
            body['initializationTimeout'] = request.initialization_timeout
        if not UtilClient.is_unset(request.initializer):
            body['initializer'] = request.initializer
        if not UtilClient.is_unset(request.instance_concurrency):
            body['instanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.instance_lifecycle_config):
            body['instanceLifecycleConfig'] = request.instance_lifecycle_config
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.layers):
            body['layers'] = request.layers
        if not UtilClient.is_unset(request.memory_size):
            body['memorySize'] = request.memory_size
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['x-fc-code-checksum'] = headers.x_fc_code_checksum
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateFunctionResponse(),
            self.do_roarequest('CreateFunction', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/functions' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def create_layer_version(self, layer_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_version_with_options(layer_name, request, headers, runtime)

    def create_layer_version_with_options(self, layer_name, request, headers, runtime):
        UtilClient.validate_model(request)
        layer_name = OpenApiUtilClient.get_encode_param(layer_name)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.compatible_runtime):
            body['compatibleRuntime'] = request.compatible_runtime
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateLayerVersionResponse(),
            self.do_roarequest('CreateLayerVersion', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/layers/%s/versions' % TeaConverter.to_unicode(layer_name), 'json', req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    def create_service_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.internet_access):
            body['internetAccess'] = request.internet_access
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.nas_config):
            body['nasConfig'] = request.nas_config
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.tracing_config):
            body['tracingConfig'] = request.tracing_config
        if not UtilClient.is_unset(request.vpc_config):
            body['vpcConfig'] = request.vpc_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateServiceResponse(),
            self.do_roarequest('CreateService', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services', 'json', req, runtime)
        )

    def create_trigger(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(service_name, function_name, request, headers, runtime)

    def create_trigger_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.invocation_role):
            body['invocationRole'] = request.invocation_role
        if not UtilClient.is_unset(request.qualifier):
            body['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.source_arn):
            body['sourceArn'] = request.source_arn
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_name):
            body['triggerName'] = request.trigger_name
        if not UtilClient.is_unset(request.trigger_type):
            body['triggerType'] = request.trigger_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateTriggerResponse(),
            self.do_roarequest('CreateTrigger', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/functions/%s/triggers' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def create_vpc_binding(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_vpc_binding_with_options(service_name, request, headers, runtime)

    def create_vpc_binding_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.CreateVpcBindingResponse(),
            self.do_roarequest('CreateVpcBinding', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/bindings' % TeaConverter.to_unicode(service_name), 'none', req, runtime)
        )

    def delete_alias(self, service_name, alias_name):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteAliasHeaders()
        return self.delete_alias_with_options(service_name, alias_name, headers, runtime)

    def delete_alias_with_options(self, service_name, alias_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        alias_name = OpenApiUtilClient.get_encode_param(alias_name)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteAliasResponse(),
            self.do_roarequest('DeleteAlias', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/aliases/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(alias_name)), 'none', req, runtime)
        )

    def delete_custom_domain(self, domain_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_custom_domain_with_options(domain_name, headers, runtime)

    def delete_custom_domain_with_options(self, domain_name, headers, runtime):
        domain_name = OpenApiUtilClient.get_encode_param(domain_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteCustomDomainResponse(),
            self.do_roarequest('DeleteCustomDomain', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/custom-domains/%s' % TeaConverter.to_unicode(domain_name), 'none', req, runtime)
        )

    def delete_function(self, service_name, function_name):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionHeaders()
        return self.delete_function_with_options(service_name, function_name, headers, runtime)

    def delete_function_with_options(self, service_name, function_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionResponse(),
            self.do_roarequest('DeleteFunction', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/functions/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'none', req, runtime)
        )

    def delete_function_async_invoke_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_async_invoke_config_with_options(service_name, function_name, request, headers, runtime)

    def delete_function_async_invoke_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionAsyncInvokeConfigResponse(),
            self.do_roarequest('DeleteFunctionAsyncInvokeConfig', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/functions/%s/async-invoke-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'none', req, runtime)
        )

    def delete_function_on_demand_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteFunctionOnDemandConfigHeaders()
        return self.delete_function_on_demand_config_with_options(service_name, function_name, request, headers, runtime)

    def delete_function_on_demand_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteFunctionOnDemandConfigResponse(),
            self.do_roarequest('DeleteFunctionOnDemandConfig', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/functions/%s/on-demand-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'none', req, runtime)
        )

    def delete_layer_version(self, layer_name, version):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_version_with_options(layer_name, version, headers, runtime)

    def delete_layer_version_with_options(self, layer_name, version, headers, runtime):
        layer_name = OpenApiUtilClient.get_encode_param(layer_name)
        version = OpenApiUtilClient.get_encode_param(version)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteLayerVersionResponse(),
            self.do_roarequest('DeleteLayerVersion', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/layers/%s/versions/%s' % (TeaConverter.to_unicode(layer_name), TeaConverter.to_unicode(version)), 'none', req, runtime)
        )

    def delete_service(self, service_name):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteServiceHeaders()
        return self.delete_service_with_options(service_name, headers, runtime)

    def delete_service_with_options(self, service_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteServiceResponse(),
            self.do_roarequest('DeleteService', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s' % TeaConverter.to_unicode(service_name), 'none', req, runtime)
        )

    def delete_service_version(self, service_name, version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_version_with_options(service_name, version_id, headers, runtime)

    def delete_service_version_with_options(self, service_name, version_id, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        version_id = OpenApiUtilClient.get_encode_param(version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteServiceVersionResponse(),
            self.do_roarequest('DeleteServiceVersion', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/versions/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(version_id)), 'none', req, runtime)
        )

    def delete_trigger(self, service_name, function_name, trigger_name):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.DeleteTriggerHeaders()
        return self.delete_trigger_with_options(service_name, function_name, trigger_name, headers, runtime)

    def delete_trigger_with_options(self, service_name, function_name, trigger_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        trigger_name = OpenApiUtilClient.get_encode_param(trigger_name)
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteTriggerResponse(),
            self.do_roarequest('DeleteTrigger', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/functions/%s/triggers/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(trigger_name)), 'none', req, runtime)
        )

    def delete_vpc_binding(self, service_name, vpc_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_vpc_binding_with_options(service_name, vpc_id, headers, runtime)

    def delete_vpc_binding_with_options(self, service_name, vpc_id, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        vpc_id = OpenApiUtilClient.get_encode_param(vpc_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeleteVpcBindingResponse(),
            self.do_roarequest('DeleteVpcBinding', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/bindings/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(vpc_id)), 'none', req, runtime)
        )

    def deregister_event_source(self, service_name, function_name, source_arn, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deregister_event_source_with_options(service_name, function_name, source_arn, request, headers, runtime)

    def deregister_event_source_with_options(self, service_name, function_name, source_arn, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        source_arn = OpenApiUtilClient.get_encode_param(source_arn)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.DeregisterEventSourceResponse(),
            self.do_roarequest('DeregisterEventSource', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/services/%s/functions/%s/event-sources/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(source_arn)), 'none', req, runtime)
        )

    def get_account_settings(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_account_settings_with_options(headers, runtime)

    def get_account_settings_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetAccountSettingsResponse(),
            self.do_roarequest('GetAccountSettings', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/account-settings', 'json', req, runtime)
        )

    def get_alias(self, service_name, alias_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alias_with_options(service_name, alias_name, headers, runtime)

    def get_alias_with_options(self, service_name, alias_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        alias_name = OpenApiUtilClient.get_encode_param(alias_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetAliasResponse(),
            self.do_roarequest('GetAlias', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/aliases/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(alias_name)), 'json', req, runtime)
        )

    def get_custom_domain(self, domain_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_domain_with_options(domain_name, headers, runtime)

    def get_custom_domain_with_options(self, domain_name, headers, runtime):
        domain_name = OpenApiUtilClient.get_encode_param(domain_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetCustomDomainResponse(),
            self.do_roarequest('GetCustomDomain', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/custom-domains/%s' % TeaConverter.to_unicode(domain_name), 'json', req, runtime)
        )

    def get_function(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_with_options(service_name, function_name, request, headers, runtime)

    def get_function_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionResponse(),
            self.do_roarequest('GetFunction', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def get_function_async_invoke_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_async_invoke_config_with_options(service_name, function_name, request, headers, runtime)

    def get_function_async_invoke_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionAsyncInvokeConfigResponse(),
            self.do_roarequest('GetFunctionAsyncInvokeConfig', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/async-invoke-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def get_function_code(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_code_with_options(service_name, function_name, request, headers, runtime)

    def get_function_code_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionCodeResponse(),
            self.do_roarequest('GetFunctionCode', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/code' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def get_function_on_demand_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_on_demand_config_with_options(service_name, function_name, request, headers, runtime)

    def get_function_on_demand_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetFunctionOnDemandConfigResponse(),
            self.do_roarequest('GetFunctionOnDemandConfig', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/on-demand-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def get_layer_version(self, layer_name, version):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_with_options(layer_name, version, headers, runtime)

    def get_layer_version_with_options(self, layer_name, version, headers, runtime):
        layer_name = OpenApiUtilClient.get_encode_param(layer_name)
        version = OpenApiUtilClient.get_encode_param(version)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetLayerVersionResponse(),
            self.do_roarequest('GetLayerVersion', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/layers/%s/versions/%s' % (TeaConverter.to_unicode(layer_name), TeaConverter.to_unicode(version)), 'json', req, runtime)
        )

    def get_layer_version_by_arn(self, arn):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_by_arn_with_options(arn, headers, runtime)

    def get_layer_version_by_arn_with_options(self, arn, headers, runtime):
        arn = OpenApiUtilClient.get_encode_param(arn)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetLayerVersionByArnResponse(),
            self.do_roarequest('GetLayerVersionByArn', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/layerarn/%s' % TeaConverter.to_unicode(arn), 'json', req, runtime)
        )

    def get_provision_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_provision_config_with_options(service_name, function_name, request, headers, runtime)

    def get_provision_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetProvisionConfigResponse(),
            self.do_roarequest('GetProvisionConfig', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/provision-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def get_resource_tags(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_tags_with_options(request, headers, runtime)

    def get_resource_tags_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_arn):
            query['resourceArn'] = request.resource_arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetResourceTagsResponse(),
            self.do_roarequest('GetResourceTags', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/tag', 'json', req, runtime)
        )

    def get_service(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_name, request, headers, runtime)

    def get_service_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetServiceResponse(),
            self.do_roarequest('GetService', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def get_stateful_async_invocation(self, service_name, function_name, invocation_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_stateful_async_invocation_with_options(service_name, function_name, invocation_id, request, headers, runtime)

    def get_stateful_async_invocation_with_options(self, service_name, function_name, invocation_id, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        invocation_id = OpenApiUtilClient.get_encode_param(invocation_id)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetStatefulAsyncInvocationResponse(),
            self.do_roarequest('GetStatefulAsyncInvocation', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/stateful-async-invocations/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(invocation_id)), 'json', req, runtime)
        )

    def get_trigger(self, service_name, function_name, trigger_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trigger_with_options(service_name, function_name, trigger_name, headers, runtime)

    def get_trigger_with_options(self, service_name, function_name, trigger_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        trigger_name = OpenApiUtilClient.get_encode_param(trigger_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.GetTriggerResponse(),
            self.do_roarequest('GetTrigger', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/triggers/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(trigger_name)), 'json', req, runtime)
        )

    def invoke_function(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.InvokeFunctionHeaders()
        return self.invoke_function_with_options(service_name, function_name, request, headers, runtime)

    def invoke_function_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = headers.x_fc_account_id
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = headers.x_fc_invocation_type
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = headers.x_fc_log_type
        if not UtilClient.is_unset(headers.x_fc_stateful_async_invocation_id):
            real_headers['x-fc-stateful-async-invocation-id'] = headers.x_fc_stateful_async_invocation_id
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            fc__open_20210406_models.InvokeFunctionResponse(),
            self.do_roarequest('InvokeFunction', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/functions/%s/invocations' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'byte', req, runtime)
        )

    def list_aliases(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aliases_with_options(service_name, request, headers, runtime)

    def list_aliases_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListAliasesResponse(),
            self.do_roarequest('ListAliases', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/aliases' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def list_custom_domains(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_custom_domains_with_options(request, headers, runtime)

    def list_custom_domains_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListCustomDomainsResponse(),
            self.do_roarequest('ListCustomDomains', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/custom-domains', 'json', req, runtime)
        )

    def list_event_sources(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_event_sources_with_options(service_name, function_name, request, headers, runtime)

    def list_event_sources_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListEventSourcesResponse(),
            self.do_roarequest('ListEventSources', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/event-sources' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def list_function_async_invoke_configs(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_async_invoke_configs_with_options(service_name, function_name, request, headers, runtime)

    def list_function_async_invoke_configs_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListFunctionAsyncInvokeConfigsResponse(),
            self.do_roarequest('ListFunctionAsyncInvokeConfigs', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/async-invoke-configs' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def list_functions(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(service_name, request, headers, runtime)

    def list_functions_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListFunctionsResponse(),
            self.do_roarequest('ListFunctions', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def list_layer_versions(self, layer_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layer_versions_with_options(layer_name, request, headers, runtime)

    def list_layer_versions_with_options(self, layer_name, request, headers, runtime):
        UtilClient.validate_model(request)
        layer_name = OpenApiUtilClient.get_encode_param(layer_name)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.start_version):
            query['startVersion'] = request.start_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListLayerVersionsResponse(),
            self.do_roarequest('ListLayerVersions', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/layers/%s/versions' % TeaConverter.to_unicode(layer_name), 'json', req, runtime)
        )

    def list_layers(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    def list_layers_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListLayersResponse(),
            self.do_roarequest('ListLayers', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/layers', 'json', req, runtime)
        )

    def list_on_demand_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_on_demand_configs_with_options(request, headers, runtime)

    def list_on_demand_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListOnDemandConfigsResponse(),
            self.do_roarequest('ListOnDemandConfigs', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/on-demand-configs', 'json', req, runtime)
        )

    def list_provision_configs(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_provision_configs_with_options(request, headers, runtime)

    def list_provision_configs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListProvisionConfigsResponse(),
            self.do_roarequest('ListProvisionConfigs', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/provision-configs', 'json', req, runtime)
        )

    def list_reserved_capacities(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_reserved_capacities_with_options(request, headers, runtime)

    def list_reserved_capacities_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListReservedCapacitiesResponse(),
            self.do_roarequest('ListReservedCapacities', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/reserved-capacities', 'json', req, runtime)
        )

    def list_service_versions(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_versions_with_options(service_name, request, headers, runtime)

    def list_service_versions_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListServiceVersionsResponse(),
            self.do_roarequest('ListServiceVersions', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/versions' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    def list_services_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListServicesResponse(),
            self.do_roarequest('ListServices', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services', 'json', req, runtime)
        )

    def list_stateful_async_invocations(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_stateful_async_invocations_with_options(service_name, function_name, request, headers, runtime)

    def list_stateful_async_invocations_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.include_payload):
            query['includePayload'] = request.include_payload
        if not UtilClient.is_unset(request.invocation_id_prefix):
            query['invocationIdPrefix'] = request.invocation_id_prefix
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.sort_order_by_time):
            query['sortOrderByTime'] = request.sort_order_by_time
        if not UtilClient.is_unset(request.started_time_begin):
            query['startedTimeBegin'] = request.started_time_begin
        if not UtilClient.is_unset(request.started_time_end):
            query['startedTimeEnd'] = request.started_time_end
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListStatefulAsyncInvocationsResponse(),
            self.do_roarequest('ListStatefulAsyncInvocations', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/stateful-async-invocations' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def list_tagged_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tagged_resources_with_options(request, headers, runtime)

    def list_tagged_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListTaggedResourcesResponse(),
            self.do_roarequest('ListTaggedResources', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/tags', 'json', req, runtime)
        )

    def list_triggers(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_triggers_with_options(service_name, function_name, request, headers, runtime)

    def list_triggers_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListTriggersResponse(),
            self.do_roarequest('ListTriggers', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/functions/%s/triggers' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def list_vpc_bindings(self, service_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_bindings_with_options(service_name, headers, runtime)

    def list_vpc_bindings_with_options(self, service_name, headers, runtime):
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.ListVpcBindingsResponse(),
            self.do_roarequest('ListVpcBindings', '2021-04-06', 'HTTPS', 'GET', 'AK', '/2021-04-06/services/%s/bindings' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def permanent_delete_layer_version(self, user_id, layer_name, version):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.permanent_delete_layer_version_with_options(user_id, layer_name, version, headers, runtime)

    def permanent_delete_layer_version_with_options(self, user_id, layer_name, version, headers, runtime):
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        layer_name = OpenApiUtilClient.get_encode_param(layer_name)
        version = OpenApiUtilClient.get_encode_param(version)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PermanentDeleteLayerVersionResponse(),
            self.do_roarequest('PermanentDeleteLayerVersion', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/adminlayers/%s/%s/versions/%s' % (TeaConverter.to_unicode(user_id), TeaConverter.to_unicode(layer_name), TeaConverter.to_unicode(version)), 'none', req, runtime)
        )

    def publish_layer_as_public(self, layer_name, version):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_layer_as_public_with_options(layer_name, version, headers, runtime)

    def publish_layer_as_public_with_options(self, layer_name, version, headers, runtime):
        layer_name = OpenApiUtilClient.get_encode_param(layer_name)
        version = OpenApiUtilClient.get_encode_param(version)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PublishLayerAsPublicResponse(),
            self.do_roarequest('PublishLayerAsPublic', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/layers/%s/versions/%s' % (TeaConverter.to_unicode(layer_name), TeaConverter.to_unicode(version)), 'none', req, runtime)
        )

    def publish_service_version(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PublishServiceVersionHeaders()
        return self.publish_service_version_with_options(service_name, request, headers, runtime)

    def publish_service_version_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PublishServiceVersionResponse(),
            self.do_roarequest('PublishServiceVersion', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/versions' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def put_function_async_invoke_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_function_async_invoke_config_with_options(service_name, function_name, request, headers, runtime)

    def put_function_async_invoke_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.destination_config):
            body['destinationConfig'] = request.destination_config
        if not UtilClient.is_unset(request.max_async_event_age_in_seconds):
            body['maxAsyncEventAgeInSeconds'] = request.max_async_event_age_in_seconds
        if not UtilClient.is_unset(request.max_async_retry_attempts):
            body['maxAsyncRetryAttempts'] = request.max_async_retry_attempts
        if not UtilClient.is_unset(request.stateful_invocation):
            body['statefulInvocation'] = request.stateful_invocation
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutFunctionAsyncInvokeConfigResponse(),
            self.do_roarequest('PutFunctionAsyncInvokeConfig', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/functions/%s/async-invoke-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def put_function_on_demand_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.PutFunctionOnDemandConfigHeaders()
        return self.put_function_on_demand_config_with_options(service_name, function_name, request, headers, runtime)

    def put_function_on_demand_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.maximum_instance_count):
            body['maximumInstanceCount'] = request.maximum_instance_count
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutFunctionOnDemandConfigResponse(),
            self.do_roarequest('PutFunctionOnDemandConfig', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/functions/%s/on-demand-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def put_provision_config(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_provision_config_with_options(service_name, function_name, request, headers, runtime)

    def put_provision_config_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.scheduled_actions):
            body['scheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.target):
            body['target'] = request.target
        if not UtilClient.is_unset(request.target_tracking_policies):
            body['targetTrackingPolicies'] = request.target_tracking_policies
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.PutProvisionConfigResponse(),
            self.do_roarequest('PutProvisionConfig', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/functions/%s/provision-config' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def register_event_source(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.register_event_source_with_options(service_name, function_name, request, headers, runtime)

    def register_event_source_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        body = {}
        if not UtilClient.is_unset(request.source_arn):
            body['sourceArn'] = request.source_arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.RegisterEventSourceResponse(),
            self.do_roarequest('RegisterEventSource', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/services/%s/functions/%s/event-sources' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def stop_stateful_async_invocation(self, service_name, function_name, invocation_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_stateful_async_invocation_with_options(service_name, function_name, invocation_id, request, headers, runtime)

    def stop_stateful_async_invocation_with_options(self, service_name, function_name, invocation_id, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        invocation_id = OpenApiUtilClient.get_encode_param(invocation_id)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.StopStatefulAsyncInvocationResponse(),
            self.do_roarequest('StopStatefulAsyncInvocation', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/functions/%s/stateful-async-invocations/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(invocation_id)), 'none', req, runtime)
        )

    def tag_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resource_with_options(request, headers, runtime)

    def tag_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['resourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.TagResourceResponse(),
            self.do_roarequest('TagResource', '2021-04-06', 'HTTPS', 'POST', 'AK', '/2021-04-06/tag', 'none', req, runtime)
        )

    def untag_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resource_with_options(request, headers, runtime)

    def untag_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_arn):
            body['resourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.tag_keys):
            body['tagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UntagResourceResponse(),
            self.do_roarequest('UntagResource', '2021-04-06', 'HTTPS', 'DELETE', 'AK', '/2021-04-06/tag', 'none', req, runtime)
        )

    def update_alias(self, service_name, alias_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateAliasHeaders()
        return self.update_alias_with_options(service_name, alias_name, request, headers, runtime)

    def update_alias_with_options(self, service_name, alias_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        alias_name = OpenApiUtilClient.get_encode_param(alias_name)
        body = {}
        if not UtilClient.is_unset(request.additional_version_weight):
            body['additionalVersionWeight'] = request.additional_version_weight
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.version_id):
            body['versionId'] = request.version_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateAliasResponse(),
            self.do_roarequest('UpdateAlias', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/aliases/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(alias_name)), 'json', req, runtime)
        )

    def update_custom_domain(self, domain_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_custom_domain_with_options(domain_name, request, headers, runtime)

    def update_custom_domain_with_options(self, domain_name, request, headers, runtime):
        UtilClient.validate_model(request)
        domain_name = OpenApiUtilClient.get_encode_param(domain_name)
        body = {}
        if not UtilClient.is_unset(request.cert_config):
            body['certConfig'] = request.cert_config
        if not UtilClient.is_unset(request.protocol):
            body['protocol'] = request.protocol
        if not UtilClient.is_unset(request.route_config):
            body['routeConfig'] = request.route_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateCustomDomainResponse(),
            self.do_roarequest('UpdateCustomDomain', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/custom-domains/%s' % TeaConverter.to_unicode(domain_name), 'json', req, runtime)
        )

    def update_function(self, service_name, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateFunctionHeaders()
        return self.update_function_with_options(service_name, function_name, request, headers, runtime)

    def update_function_with_options(self, service_name, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        body = {}
        if not UtilClient.is_unset(request.instance_concurrency):
            body['InstanceConcurrency'] = request.instance_concurrency
        if not UtilClient.is_unset(request.ca_port):
            body['caPort'] = request.ca_port
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.custom_container_config):
            body['customContainerConfig'] = request.custom_container_config
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.environment_variables):
            body['environmentVariables'] = request.environment_variables
        if not UtilClient.is_unset(request.handler):
            body['handler'] = request.handler
        if not UtilClient.is_unset(request.initialization_timeout):
            body['initializationTimeout'] = request.initialization_timeout
        if not UtilClient.is_unset(request.initializer):
            body['initializer'] = request.initializer
        if not UtilClient.is_unset(request.instance_lifecycle_config):
            body['instanceLifecycleConfig'] = request.instance_lifecycle_config
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.layers):
            body['layers'] = request.layers
        if not UtilClient.is_unset(request.memory_size):
            body['memorySize'] = request.memory_size
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = headers.x_fc_account_id
        if not UtilClient.is_unset(headers.x_fc_code_checksum):
            real_headers['x-fc-code-checksum'] = headers.x_fc_code_checksum
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateFunctionResponse(),
            self.do_roarequest('UpdateFunction', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/functions/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name)), 'json', req, runtime)
        )

    def update_service(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateServiceHeaders()
        return self.update_service_with_options(service_name, request, headers, runtime)

    def update_service_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.internet_access):
            body['internetAccess'] = request.internet_access
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.nas_config):
            body['nasConfig'] = request.nas_config
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.tracing_config):
            body['tracingConfig'] = request.tracing_config
        if not UtilClient.is_unset(request.vpc_config):
            body['vpcConfig'] = request.vpc_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = headers.x_fc_account_id
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateServiceResponse(),
            self.do_roarequest('UpdateService', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s' % TeaConverter.to_unicode(service_name), 'json', req, runtime)
        )

    def update_trigger(self, service_name, function_name, trigger_name, request):
        runtime = util_models.RuntimeOptions()
        headers = fc__open_20210406_models.UpdateTriggerHeaders()
        return self.update_trigger_with_options(service_name, function_name, trigger_name, request, headers, runtime)

    def update_trigger_with_options(self, service_name, function_name, trigger_name, request, headers, runtime):
        UtilClient.validate_model(request)
        service_name = OpenApiUtilClient.get_encode_param(service_name)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        trigger_name = OpenApiUtilClient.get_encode_param(trigger_name)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.invocation_role):
            body['invocationRole'] = request.invocation_role
        if not UtilClient.is_unset(request.qualifier):
            body['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.if_match):
            real_headers['If-Match'] = headers.if_match
        if not UtilClient.is_unset(headers.x_fc_account_id):
            real_headers['X-Fc-Account-Id'] = headers.x_fc_account_id
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            fc__open_20210406_models.UpdateTriggerResponse(),
            self.do_roarequest('UpdateTrigger', '2021-04-06', 'HTTPS', 'PUT', 'AK', '/2021-04-06/services/%s/functions/%s/triggers/%s' % (TeaConverter.to_unicode(service_name), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(trigger_name)), 'json', req, runtime)
        )
