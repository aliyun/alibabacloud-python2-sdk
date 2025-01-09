# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_fc20230330 import models as fc20230330_models
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
        self._endpoint = self.get_endpoint('fc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_alias_with_options(self, function_name, request, headers, runtime):
        """
        @summary 创建函数别名。
        

        @param request: CreateAliasRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/aliases' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alias(self, function_name, request):
        """
        @summary 创建函数别名。
        

        @param request: CreateAliasRequest

        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_alias_with_options(function_name, request, headers, runtime)

    def create_custom_domain_with_options(self, request, headers, runtime):
        """
        @summary Creates a custom domain name.
        
        @description If you want to use a fixed domain name to access an application or function in a production environment of Function Compute, or to resolve the issue of forced downloads when accessing an HTTP trigger, you can bind a custom domain name to the application or function.
        

        @param request: CreateCustomDomainRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/custom-domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_domain(self, request):
        """
        @summary Creates a custom domain name.
        
        @description If you want to use a fixed domain name to access an application or function in a production environment of Function Compute, or to resolve the issue of forced downloads when accessing an HTTP trigger, you can bind a custom domain name to the application or function.
        

        @param request: CreateCustomDomainRequest

        @return: CreateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_custom_domain_with_options(request, headers, runtime)

    def create_function_with_options(self, request, headers, runtime):
        """
        @summary Creates a function.
        
        @description Resources of Function Compute are scheduled and run based on functions. A function usually refers to a code snippet that is written by a user and can be independently executed to respond to events and requests.
        

        @param request: CreateFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_function(self, request):
        """
        @summary Creates a function.
        
        @description Resources of Function Compute are scheduled and run based on functions. A function usually refers to a code snippet that is written by a user and can be independently executed to respond to events and requests.
        

        @param request: CreateFunctionRequest

        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_with_options(request, headers, runtime)

    def create_layer_version_with_options(self, layer_name, request, headers, runtime):
        """
        @summary 创建层版本。
        

        @param request: CreateLayerVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLayerVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layers/%s/versions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_layer_version(self, layer_name, request):
        """
        @summary 创建层版本。
        

        @param request: CreateLayerVersionRequest

        @return: CreateLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_version_with_options(layer_name, request, headers, runtime)

    def create_trigger_with_options(self, function_name, request, headers, runtime):
        """
        @summary 创建函数触发器。
        

        @param request: CreateTriggerRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/triggers' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_trigger(self, function_name, request):
        """
        @summary 创建函数触发器。
        

        @param request: CreateTriggerRequest

        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(function_name, request, headers, runtime)

    def create_vpc_binding_with_options(self, function_name, request, headers, runtime):
        """
        @summary Creates a VPC connection.
        

        @param request: CreateVpcBindingRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateVpcBindingResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateVpcBinding',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/vpc-bindings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.CreateVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vpc_binding(self, function_name, request):
        """
        @summary Creates a VPC connection.
        

        @param request: CreateVpcBindingRequest

        @return: CreateVpcBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_vpc_binding_with_options(function_name, request, headers, runtime)

    def delete_alias_with_options(self, function_name, alias_name, headers, runtime):
        """
        @summary Deletes an alias.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/aliases/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(alias_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alias(self, function_name, alias_name):
        """
        @summary Deletes an alias.
        

        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alias_with_options(function_name, alias_name, headers, runtime)

    def delete_async_invoke_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Deletes an asynchronous invocation configuration.
        

        @param request: DeleteAsyncInvokeConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/async-invoke-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_async_invoke_config(self, function_name, request):
        """
        @summary Deletes an asynchronous invocation configuration.
        

        @param request: DeleteAsyncInvokeConfigRequest

        @return: DeleteAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_async_invoke_config_with_options(function_name, request, headers, runtime)

    def delete_concurrency_config_with_options(self, function_name, headers, runtime):
        """
        @summary Deletes a concurrency configuration.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConcurrencyConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/concurrency' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_concurrency_config(self, function_name):
        """
        @summary Deletes a concurrency configuration.
        

        @return: DeleteConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_concurrency_config_with_options(function_name, headers, runtime)

    def delete_custom_domain_with_options(self, domain_name, headers, runtime):
        """
        @summary Deletes a custom domain name.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCustomDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/custom-domains/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(domain_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_domain(self, domain_name):
        """
        @summary Deletes a custom domain name.
        

        @return: DeleteCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_custom_domain_with_options(domain_name, headers, runtime)

    def delete_function_with_options(self, function_name, headers, runtime):
        """
        @summary Deletes a function.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFunctionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_function(self, function_name):
        """
        @summary Deletes a function.
        

        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_with_options(function_name, headers, runtime)

    def delete_function_version_with_options(self, function_name, version_id, headers, runtime):
        """
        @summary Deletes a function version.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFunctionVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/versions/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_function_version(self, function_name, version_id):
        """
        @summary Deletes a function version.
        

        @return: DeleteFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_version_with_options(function_name, version_id, headers, runtime)

    def delete_layer_version_with_options(self, layer_name, version, headers, runtime):
        """
        @summary Deletes a layer version.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLayerVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layers/%s/versions/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_layer_version(self, layer_name, version):
        """
        @summary Deletes a layer version.
        

        @return: DeleteLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_version_with_options(layer_name, version, headers, runtime)

    def delete_provision_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Deletes a provisioned configuration.
        

        @param request: DeleteProvisionConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/provision-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_provision_config(self, function_name, request):
        """
        @summary Deletes a provisioned configuration.
        

        @param request: DeleteProvisionConfigRequest

        @return: DeleteProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_provision_config_with_options(function_name, request, headers, runtime)

    def delete_trigger_with_options(self, function_name, trigger_name, headers, runtime):
        """
        @summary Deletes a trigger.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/triggers/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(trigger_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_trigger(self, function_name, trigger_name):
        """
        @summary Deletes a trigger.
        

        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(function_name, trigger_name, headers, runtime)

    def delete_vpc_binding_with_options(self, function_name, vpc_id, headers, runtime):
        """
        @summary Deletes an access control policy from a specified policy group for a VPC firewall.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVpcBindingResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteVpcBinding',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/vpc-bindings/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(vpc_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.DeleteVpcBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vpc_binding(self, function_name, vpc_id):
        """
        @summary Deletes an access control policy from a specified policy group for a VPC firewall.
        

        @return: DeleteVpcBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_vpc_binding_with_options(function_name, vpc_id, headers, runtime)

    def get_alias_with_options(self, function_name, alias_name, headers, runtime):
        """
        @summary Queries information about an alias.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/aliases/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(alias_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alias(self, function_name, alias_name):
        """
        @summary Queries information about an alias.
        

        @return: GetAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alias_with_options(function_name, alias_name, headers, runtime)

    def get_async_invoke_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Gets asynchronous invocation configurations of a function.
        

        @param request: GetAsyncInvokeConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/async-invoke-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_invoke_config(self, function_name, request):
        """
        @summary Gets asynchronous invocation configurations of a function.
        

        @param request: GetAsyncInvokeConfigRequest

        @return: GetAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_invoke_config_with_options(function_name, request, headers, runtime)

    def get_async_task_with_options(self, function_name, task_id, request, headers, runtime):
        """
        @summary Queries the information about an asynchronous task.
        

        @param request: GetAsyncTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncTask',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/async-tasks/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_task(self, function_name, task_id, request):
        """
        @summary Queries the information about an asynchronous task.
        

        @param request: GetAsyncTaskRequest

        @return: GetAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(function_name, task_id, request, headers, runtime)

    def get_concurrency_config_with_options(self, function_name, headers, runtime):
        """
        @summary Obtains a concurrency configuration.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetConcurrencyConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/concurrency' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_concurrency_config(self, function_name):
        """
        @summary Obtains a concurrency configuration.
        

        @return: GetConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_concurrency_config_with_options(function_name, headers, runtime)

    def get_custom_domain_with_options(self, domain_name, headers, runtime):
        """
        @summary Queries information about a custom domain name.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetCustomDomainResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/custom-domains/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(domain_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def get_custom_domain(self, domain_name):
        """
        @summary Queries information about a custom domain name.
        

        @return: GetCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_domain_with_options(domain_name, headers, runtime)

    def get_function_with_options(self, function_name, request, headers, runtime):
        """
        @summary http://pre.hhht/#vpc
        

        @param request: GetFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function(self, function_name, request):
        """
        @summary http://pre.hhht/#vpc
        

        @param request: GetFunctionRequest

        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_with_options(function_name, request, headers, runtime)

    def get_function_code_with_options(self, function_name, request, headers, runtime):
        """
        @summary Queries a code package of a function.
        

        @param request: GetFunctionCodeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFunctionCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCode',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/code' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetFunctionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function_code(self, function_name, request):
        """
        @summary Queries a code package of a function.
        

        @param request: GetFunctionCodeRequest

        @return: GetFunctionCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_code_with_options(function_name, request, headers, runtime)

    def get_layer_version_with_options(self, layer_name, version, headers, runtime):
        """
        @summary Queries versions of a layer.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLayerVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayerVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layers/%s/versions/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetLayerVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_layer_version(self, layer_name, version):
        """
        @summary Queries versions of a layer.
        

        @return: GetLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_with_options(layer_name, version, headers, runtime)

    def get_layer_version_by_arn_with_options(self, arn, headers, runtime):
        """
        @summary Obtain version information of a layer by using ARNs.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetLayerVersionByArnResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLayerVersionByArn',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layerarn/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(arn)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetLayerVersionByArnResponse(),
            self.call_api(params, req, runtime)
        )

    def get_layer_version_by_arn(self, arn):
        """
        @summary Obtain version information of a layer by using ARNs.
        

        @return: GetLayerVersionByArnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_by_arn_with_options(arn, headers, runtime)

    def get_provision_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Queries provisioned configurations.
        

        @param request: GetProvisionConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/provision-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_provision_config(self, function_name, request):
        """
        @summary Queries provisioned configurations.
        

        @param request: GetProvisionConfigRequest

        @return: GetProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_provision_config_with_options(function_name, request, headers, runtime)

    def get_trigger_with_options(self, function_name, trigger_name, headers, runtime):
        """
        @summary Queries information about a trigger.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTriggerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/triggers/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(trigger_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trigger(self, function_name, trigger_name):
        """
        @summary Queries information about a trigger.
        

        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trigger_with_options(function_name, trigger_name, headers, runtime)

    def invoke_function_with_options(self, function_name, request, headers, runtime):
        """
        @summary Invokes a function.
        

        @param request: InvokeFunctionRequest

        @param headers: InvokeFunctionHeaders

        @param runtime: runtime options for this request RuntimeOptions

        @return: InvokeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_fc_async_task_id):
            real_headers['x-fc-async-task-id'] = UtilClient.to_jsonstring(headers.x_fc_async_task_id)
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='InvokeFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/invocations' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='binary'
        )
        res = fc20230330_models.InvokeFunctionResponse()
        tmp = UtilClient.assert_as_map(self.call_api(params, req, runtime))
        if not UtilClient.is_unset(tmp.get('body')):
            resp_body = UtilClient.assert_as_readable(tmp.get('body'))
            res.body = resp_body
        if not UtilClient.is_unset(tmp.get('headers')):
            resp_headers = UtilClient.assert_as_map(tmp.get('headers'))
            res.headers = UtilClient.stringify_map_value(resp_headers)
        if not UtilClient.is_unset(tmp.get('statusCode')):
            status_code = UtilClient.assert_as_integer(tmp.get('statusCode'))
            res.status_code = status_code
        return res

    def invoke_function(self, function_name, request):
        """
        @summary Invokes a function.
        

        @param request: InvokeFunctionRequest

        @return: InvokeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc20230330_models.InvokeFunctionHeaders()
        return self.invoke_function_with_options(function_name, request, headers, runtime)

    def list_aliases_with_options(self, function_name, request, headers, runtime):
        """
        @summary Queries aliases.
        

        @param request: ListAliasesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAliasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/aliases' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_aliases(self, function_name, request):
        """
        @summary Queries aliases.
        

        @param request: ListAliasesRequest

        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aliases_with_options(function_name, request, headers, runtime)

    def list_async_invoke_configs_with_options(self, request, headers, runtime):
        """
        @summary Queries all asynchronous configurations of a function.
        

        @param request: ListAsyncInvokeConfigsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAsyncInvokeConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsyncInvokeConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/async-invoke-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAsyncInvokeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_async_invoke_configs(self, request):
        """
        @summary Queries all asynchronous configurations of a function.
        

        @param request: ListAsyncInvokeConfigsRequest

        @return: ListAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_async_invoke_configs_with_options(request, headers, runtime)

    def list_async_tasks_with_options(self, function_name, request, headers, runtime):
        """
        @summary Lists asynchronous tasks.
        

        @param request: ListAsyncTasksRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAsyncTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_payload):
            query['includePayload'] = request.include_payload
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
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
        params = open_api_models.Params(
            action='ListAsyncTasks',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/async-tasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListAsyncTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_async_tasks(self, function_name, request):
        """
        @summary Lists asynchronous tasks.
        

        @param request: ListAsyncTasksRequest

        @return: ListAsyncTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_async_tasks_with_options(function_name, request, headers, runtime)

    def list_concurrency_configs_with_options(self, request, headers, runtime):
        """
        @summary 列出函数并发度配置。
        

        @param request: ListConcurrencyConfigsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConcurrencyConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConcurrencyConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/concurrency-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListConcurrencyConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_concurrency_configs(self, request):
        """
        @summary 列出函数并发度配置。
        

        @param request: ListConcurrencyConfigsRequest

        @return: ListConcurrencyConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_concurrency_configs_with_options(request, headers, runtime)

    def list_custom_domains_with_options(self, request, headers, runtime):
        """
        @summary Queries custom domain names.
        

        @param request: ListCustomDomainsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCustomDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomDomains',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/custom-domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListCustomDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_domains(self, request):
        """
        @summary Queries custom domain names.
        

        @param request: ListCustomDomainsRequest

        @return: ListCustomDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_custom_domains_with_options(request, headers, runtime)

    def list_function_versions_with_options(self, function_name, request, headers, runtime):
        """
        @summary Queries versions of a function.
        

        @param request: ListFunctionVersionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFunctionVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionVersions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/versions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListFunctionVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function_versions(self, function_name, request):
        """
        @summary Queries versions of a function.
        

        @param request: ListFunctionVersionsRequest

        @return: ListFunctionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_versions_with_options(function_name, request, headers, runtime)

    def list_functions_with_options(self, request, headers, runtime):
        """
        @summary 列出函数。
        

        @param request: ListFunctionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fc_version):
            query['fcVersion'] = request.fc_version
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_functions(self, request):
        """
        @summary 列出函数。
        

        @param request: ListFunctionsRequest

        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(request, headers, runtime)

    def list_instances_with_options(self, function_name, tmp_req, headers, runtime):
        """
        @summary Queries a list of function instances.
        

        @param tmp_req: ListInstancesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'instanceIds', 'json')
        if not UtilClient.is_unset(tmp_req.instance_status):
            request.instance_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_status, 'instanceStatus', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time_ms):
            query['endTimeMs'] = request.end_time_ms
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['instanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.instance_status_shrink):
            query['instanceStatus'] = request.instance_status_shrink
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        if not UtilClient.is_unset(request.start_key):
            query['startKey'] = request.start_key
        if not UtilClient.is_unset(request.start_time_ms):
            query['startTimeMs'] = request.start_time_ms
        if not UtilClient.is_unset(request.with_all_active):
            query['withAllActive'] = request.with_all_active
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/instances' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, function_name, request):
        """
        @summary Queries a list of function instances.
        

        @param request: ListInstancesRequest

        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(function_name, request, headers, runtime)

    def list_layer_versions_with_options(self, layer_name, request, headers, runtime):
        """
        @summary Gets a list of layer versions.
        

        @param request: ListLayerVersionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLayerVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.start_version):
            query['startVersion'] = request.start_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayerVersions',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layers/%s/versions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListLayerVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_layer_versions(self, layer_name, request):
        """
        @summary Gets a list of layer versions.
        

        @param request: ListLayerVersionsRequest

        @return: ListLayerVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layer_versions_with_options(layer_name, request, headers, runtime)

    def list_layers_with_options(self, request, headers, runtime):
        """
        @summary Gets a list of layers.
        

        @param request: ListLayersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLayersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.official):
            query['official'] = request.official
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLayers',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListLayersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_layers(self, request):
        """
        @summary Gets a list of layers.
        

        @param request: ListLayersRequest

        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    def list_provision_configs_with_options(self, request, headers, runtime):
        """
        @summary Queries a list of provisioned configurations.
        

        @param request: ListProvisionConfigsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProvisionConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['functionName'] = request.function_name
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProvisionConfigs',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/provision-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListProvisionConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_provision_configs(self, request):
        """
        @summary Queries a list of provisioned configurations.
        

        @param request: ListProvisionConfigsRequest

        @return: ListProvisionConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_provision_configs_with_options(request, headers, runtime)

    def list_tag_resources_with_options(self, tmp_req, headers, runtime):
        """
        @summary Lists all tagged resources.
        

        @param tmp_req: ListTagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tags-v2',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        @summary Lists all tagged resources.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def list_triggers_with_options(self, function_name, request, headers, runtime):
        """
        @summary Queries the triggers of a function.
        

        @param request: ListTriggersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/triggers' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_triggers(self, function_name, request):
        """
        @summary Queries the triggers of a function.
        

        @param request: ListTriggersRequest

        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_triggers_with_options(function_name, request, headers, runtime)

    def list_vpc_bindings_with_options(self, function_name, headers, runtime):
        """
        @summary Queries a list of existing VPC connections.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListVpcBindingsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListVpcBindings',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/vpc-bindings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListVpcBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpc_bindings(self, function_name):
        """
        @summary Queries a list of existing VPC connections.
        

        @return: ListVpcBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_bindings_with_options(function_name, headers, runtime)

    def publish_function_version_with_options(self, function_name, request, headers, runtime):
        """
        @summary Publishes a function version.
        

        @param request: PublishFunctionVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublishFunctionVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PublishFunctionVersion',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/versions' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PublishFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_function_version(self, function_name, request):
        """
        @summary Publishes a function version.
        

        @param request: PublishFunctionVersionRequest

        @return: PublishFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_function_version_with_options(function_name, request, headers, runtime)

    def put_async_invoke_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Creates or modifies an asynchronous invocation configuration for a function.
        

        @param request: PutAsyncInvokeConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutAsyncInvokeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutAsyncInvokeConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/async-invoke-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutAsyncInvokeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def put_async_invoke_config(self, function_name, request):
        """
        @summary Creates or modifies an asynchronous invocation configuration for a function.
        

        @param request: PutAsyncInvokeConfigRequest

        @return: PutAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_async_invoke_config_with_options(function_name, request, headers, runtime)

    def put_concurrency_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Configures concurrency of a function.
        

        @param request: PutConcurrencyConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutConcurrencyConfigResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutConcurrencyConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/concurrency' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutConcurrencyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def put_concurrency_config(self, function_name, request):
        """
        @summary Configures concurrency of a function.
        

        @param request: PutConcurrencyConfigRequest

        @return: PutConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_concurrency_config_with_options(function_name, request, headers, runtime)

    def put_layer_aclwith_options(self, layer_name, request, headers, runtime):
        """
        @summary Modifies permissions of a layer.
        

        @param request: PutLayerACLRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutLayerACLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl):
            query['acl'] = request.acl
        if not UtilClient.is_unset(request.public):
            query['public'] = request.public
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutLayerACL',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/layers/%s/acl' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(layer_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.PutLayerACLResponse(),
            self.call_api(params, req, runtime)
        )

    def put_layer_acl(self, layer_name, request):
        """
        @summary Modifies permissions of a layer.
        

        @param request: PutLayerACLRequest

        @return: PutLayerACLResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_layer_aclwith_options(layer_name, request, headers, runtime)

    def put_provision_config_with_options(self, function_name, request, headers, runtime):
        """
        @summary Creates provisioned configurations.
        

        @param request: PutProvisionConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutProvisionConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PutProvisionConfig',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/provision-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.PutProvisionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def put_provision_config(self, function_name, request):
        """
        @summary Creates provisioned configurations.
        

        @param request: PutProvisionConfigRequest

        @return: PutProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_provision_config_with_options(function_name, request, headers, runtime)

    def stop_async_task_with_options(self, function_name, task_id, request, headers, runtime):
        """
        @summary Stops an asynchronous task.
        

        @param request: StopAsyncTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAsyncTask',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/async-tasks/%s/stop' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.StopAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_async_task(self, function_name, task_id, request):
        """
        @summary Stops an asynchronous task.
        

        @param request: StopAsyncTaskRequest

        @return: StopAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_async_task_with_options(function_name, task_id, request, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
        """
        @summary Adds tags to a resource.
        
        @description Tags are used to identify resources. Tags allow you to categorize, search for, and aggregate resources that have the same characteristics from different dimensions. This facilitates resource management. For more information, see [Tag overview](https://help.aliyun.com/document_detail/156983.html).
        

        @param request: TagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tags-v2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        @summary Adds tags to a resource.
        
        @description Tags are used to identify resources. Tags allow you to categorize, search for, and aggregate resources that have the same characteristics from different dimensions. This facilitates resource management. For more information, see [Tag overview](https://help.aliyun.com/document_detail/156983.html).
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def untag_resources_with_options(self, tmp_req, headers, runtime):
        """
        @summary Removes tags from a resource.
        

        @param tmp_req: UntagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fc20230330_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tags-v2',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        @summary Removes tags from a resource.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def update_alias_with_options(self, function_name, alias_name, request, headers, runtime):
        """
        @summary Updates an alias.
        

        @param request: UpdateAliasRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAlias',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/aliases/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(alias_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alias(self, function_name, alias_name, request):
        """
        @summary Updates an alias.
        

        @param request: UpdateAliasRequest

        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_alias_with_options(function_name, alias_name, request, headers, runtime)

    def update_custom_domain_with_options(self, domain_name, request, headers, runtime):
        """
        @summary Update a custom domain name.
        

        @param request: UpdateCustomDomainRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateCustomDomain',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/custom-domains/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(domain_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateCustomDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_domain(self, domain_name, request):
        """
        @summary Update a custom domain name.
        

        @param request: UpdateCustomDomainRequest

        @return: UpdateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_custom_domain_with_options(domain_name, request, headers, runtime)

    def update_function_with_options(self, function_name, request, headers, runtime):
        """
        @summary Updates the information about a function.
        

        @param request: UpdateFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateFunction',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_function(self, function_name, request):
        """
        @summary Updates the information about a function.
        

        @param request: UpdateFunctionRequest

        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_with_options(function_name, request, headers, runtime)

    def update_trigger_with_options(self, function_name, trigger_name, request, headers, runtime):
        """
        @summary Modifies a trigger.
        

        @param request: UpdateTriggerRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/functions/%s/triggers/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(function_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(trigger_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_trigger(self, function_name, trigger_name, request):
        """
        @summary Modifies a trigger.
        

        @param request: UpdateTriggerRequest

        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_trigger_with_options(function_name, trigger_name, request, headers, runtime)
