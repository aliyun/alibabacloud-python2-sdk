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
        create function version
        

        @param request: CreateAliasRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        create function version
        

        @param request: CreateAliasRequest

        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_alias_with_options(function_name, request, headers, runtime)

    def create_custom_domain_with_options(self, request, headers, runtime):
        """
        Create custom domain.
        

        @param request: CreateCustomDomainRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Create custom domain.
        

        @param request: CreateCustomDomainRequest

        @return: CreateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_custom_domain_with_options(request, headers, runtime)

    def create_function_with_options(self, request, headers, runtime):
        """
        Create function
        

        @param request: CreateFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Create function
        

        @param request: CreateFunctionRequest

        @return: CreateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_with_options(request, headers, runtime)

    def create_layer_version_with_options(self, layer_name, request, headers, runtime):
        """
        Create layer version
        

        @param request: CreateLayerVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLayerVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Create layer version
        

        @param request: CreateLayerVersionRequest

        @return: CreateLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_layer_version_with_options(layer_name, request, headers, runtime)

    def create_trigger_with_options(self, function_name, request, headers, runtime):
        """
        Create trigger.
        

        @param request: CreateTriggerRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Create trigger.
        

        @param request: CreateTriggerRequest

        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(function_name, request, headers, runtime)

    def delete_alias_with_options(self, function_name, alias_name, headers, runtime):
        """
        Delete function alias
        

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
        Delete function alias
        

        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alias_with_options(function_name, alias_name, headers, runtime)

    def delete_async_invoke_config_with_options(self, function_name, request, headers, runtime):
        """
        Delete function async invoke config
        

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
        Delete function async invoke config
        

        @param request: DeleteAsyncInvokeConfigRequest

        @return: DeleteAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_async_invoke_config_with_options(function_name, request, headers, runtime)

    def delete_concurrency_config_with_options(self, function_name, headers, runtime):
        """
        deletes the concurrency config for a function
        

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
        deletes the concurrency config for a function
        

        @return: DeleteConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_concurrency_config_with_options(function_name, headers, runtime)

    def delete_custom_domain_with_options(self, domain_name, headers, runtime):
        """
        Delete custom domain.
        

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
        Delete custom domain.
        

        @return: DeleteCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_custom_domain_with_options(domain_name, headers, runtime)

    def delete_function_with_options(self, function_name, headers, runtime):
        """
        Delete function
        

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
        Delete function
        

        @return: DeleteFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_with_options(function_name, headers, runtime)

    def delete_function_version_with_options(self, function_name, version_id, headers, runtime):
        """
        Delete function version
        

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
        Delete function version
        

        @return: DeleteFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_version_with_options(function_name, version_id, headers, runtime)

    def delete_layer_version_with_options(self, layer_name, version, headers, runtime):
        """
        Delete layer version
        

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
        Delete layer version
        

        @return: DeleteLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_layer_version_with_options(layer_name, version, headers, runtime)

    def delete_provision_config_with_options(self, function_name, request, headers, runtime):
        """
        Delete provision config.
        

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
        Delete provision config.
        

        @param request: DeleteProvisionConfigRequest

        @return: DeleteProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_provision_config_with_options(function_name, request, headers, runtime)

    def delete_trigger_with_options(self, function_name, trigger_name, headers, runtime):
        """
        Delete trigger.
        

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
        Delete trigger.
        

        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(function_name, trigger_name, headers, runtime)

    def get_alias_with_options(self, function_name, alias_name, headers, runtime):
        """
        Get function alias
        

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
        Get function alias
        

        @return: GetAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alias_with_options(function_name, alias_name, headers, runtime)

    def get_async_invoke_config_with_options(self, function_name, request, headers, runtime):
        """
        Get function async invoke config
        

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
        Get function async invoke config
        

        @param request: GetAsyncInvokeConfigRequest

        @return: GetAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_invoke_config_with_options(function_name, request, headers, runtime)

    def get_concurrency_config_with_options(self, function_name, headers, runtime):
        """
        gets the concurrency config for a function
        

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
        gets the concurrency config for a function
        

        @return: GetConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_concurrency_config_with_options(function_name, headers, runtime)

    def get_custom_domain_with_options(self, domain_name, headers, runtime):
        """
        Get custom domain.
        

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
        Get custom domain.
        

        @return: GetCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_custom_domain_with_options(domain_name, headers, runtime)

    def get_function_with_options(self, function_name, request, headers, runtime):
        """
        Get function info by function name
        

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
        Get function info by function name
        

        @param request: GetFunctionRequest

        @return: GetFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_with_options(function_name, request, headers, runtime)

    def get_function_code_with_options(self, function_name, request, headers, runtime):
        """
        Get function code by function name
        

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
        Get function code by function name
        

        @param request: GetFunctionCodeRequest

        @return: GetFunctionCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_code_with_options(function_name, request, headers, runtime)

    def get_layer_version_with_options(self, layer_name, version, headers, runtime):
        """
        Get layer version.
        

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
        Get layer version.
        

        @return: GetLayerVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_with_options(layer_name, version, headers, runtime)

    def get_layer_version_by_arn_with_options(self, arn, headers, runtime):
        """
        Get layer version by arn.
        

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
        Get layer version by arn.
        

        @return: GetLayerVersionByArnResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_layer_version_by_arn_with_options(arn, headers, runtime)

    def get_provision_config_with_options(self, function_name, request, headers, runtime):
        """
        Get provision config.
        

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
        Get provision config.
        

        @param request: GetProvisionConfigRequest

        @return: GetProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_provision_config_with_options(function_name, request, headers, runtime)

    def get_resource_tags_with_options(self, request, headers, runtime):
        """
        Get resource tag
        

        @param request: GetResourceTagsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetResourceTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arn):
            query['arn'] = request.arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTags',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tag',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.GetResourceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_tags(self, request):
        """
        Get resource tag
        

        @param request: GetResourceTagsRequest

        @return: GetResourceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_tags_with_options(request, headers, runtime)

    def get_trigger_with_options(self, function_name, trigger_name, headers, runtime):
        """
        Get trigger.
        

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
        Get trigger.
        

        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trigger_with_options(function_name, trigger_name, headers, runtime)

    def invoke_function_with_options(self, function_name, request, headers, runtime):
        """
        Invoke function
        

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
        if not UtilClient.is_unset(headers.x_fc_invocation_type):
            real_headers['x-fc-invocation-type'] = UtilClient.to_jsonstring(headers.x_fc_invocation_type)
        if not UtilClient.is_unset(headers.x_fc_log_type):
            real_headers['x-fc-log-type'] = UtilClient.to_jsonstring(headers.x_fc_log_type)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query),
            body=request.request,
            stream=request.request
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
        Invoke function
        

        @param request: InvokeFunctionRequest

        @return: InvokeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = fc20230330_models.InvokeFunctionHeaders()
        return self.invoke_function_with_options(function_name, request, headers, runtime)

    def list_aliases_with_options(self, function_name, request, headers, runtime):
        """
        List function aliases
        

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
        List function aliases
        

        @param request: ListAliasesRequest

        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aliases_with_options(function_name, request, headers, runtime)

    def list_async_invoke_configs_with_options(self, request, headers, runtime):
        """
        List all functions async invoke config
        

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
        List all functions async invoke config
        

        @param request: ListAsyncInvokeConfigsRequest

        @return: ListAsyncInvokeConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_async_invoke_configs_with_options(request, headers, runtime)

    def list_concurrency_configs_with_options(self, request, headers, runtime):
        """
        List all functions concurrency configs
        

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
        List all functions concurrency configs
        

        @param request: ListConcurrencyConfigsRequest

        @return: ListConcurrencyConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_concurrency_configs_with_options(request, headers, runtime)

    def list_custom_domains_with_options(self, request, headers, runtime):
        """
        List custom domains.
        

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
        List custom domains.
        

        @param request: ListCustomDomainsRequest

        @return: ListCustomDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_custom_domains_with_options(request, headers, runtime)

    def list_function_versions_with_options(self, function_name, request, headers, runtime):
        """
        List function versions
        

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
        List function versions
        

        @param request: ListFunctionVersionsRequest

        @return: ListFunctionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_versions_with_options(function_name, request, headers, runtime)

    def list_functions_with_options(self, request, headers, runtime):
        """
        Lists existing functions.
        

        @param request: ListFunctionsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFunctionsResponse
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
        Lists existing functions.
        

        @param request: ListFunctionsRequest

        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(request, headers, runtime)

    def list_instances_with_options(self, function_name, request, headers, runtime):
        """
        List instances for function.
        

        @param request: ListInstancesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.qualifier):
            query['qualifier'] = request.qualifier
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
        List instances for function.
        

        @param request: ListInstancesRequest

        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(function_name, request, headers, runtime)

    def list_layer_versions_with_options(self, layer_name, request, headers, runtime):
        """
        List layer versions.
        

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
        List layer versions.
        

        @param request: ListLayerVersionsRequest

        @return: ListLayerVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layer_versions_with_options(layer_name, request, headers, runtime)

    def list_layers_with_options(self, request, headers, runtime):
        """
        List layers .
        

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
        List layers .
        

        @param request: ListLayersRequest

        @return: ListLayersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_layers_with_options(request, headers, runtime)

    def list_provision_configs_with_options(self, request, headers, runtime):
        """
        List provision configs.
        

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
        List provision configs.
        

        @param request: ListProvisionConfigsRequest

        @return: ListProvisionConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_provision_configs_with_options(request, headers, runtime)

    def list_tagged_resources_with_options(self, request, headers, runtime):
        """
        List tagged resources
        

        @param request: ListTaggedResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTaggedResourcesResponse
        """
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
        params = open_api_models.Params(
            action='ListTaggedResources',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.ListTaggedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tagged_resources(self, request):
        """
        List tagged resources
        

        @param request: ListTaggedResourcesRequest

        @return: ListTaggedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tagged_resources_with_options(request, headers, runtime)

    def list_triggers_with_options(self, function_name, request, headers, runtime):
        """
        List triggers.
        

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
        List triggers.
        

        @param request: ListTriggersRequest

        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_triggers_with_options(function_name, request, headers, runtime)

    def publish_function_version_with_options(self, function_name, request, headers, runtime):
        """
        publish new function version
        

        @param request: PublishFunctionVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublishFunctionVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        publish new function version
        

        @param request: PublishFunctionVersionRequest

        @return: PublishFunctionVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_function_version_with_options(function_name, request, headers, runtime)

    def put_async_invoke_config_with_options(self, function_name, request, headers, runtime):
        """
        Put function async invoke config.
        

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
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Put function async invoke config.
        

        @param request: PutAsyncInvokeConfigRequest

        @return: PutAsyncInvokeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_async_invoke_config_with_options(function_name, request, headers, runtime)

    def put_concurrency_config_with_options(self, function_name, request, headers, runtime):
        """
        sets the concurrency config for a function
        

        @param request: PutConcurrencyConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutConcurrencyConfigResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        sets the concurrency config for a function
        

        @param request: PutConcurrencyConfigRequest

        @return: PutConcurrencyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_concurrency_config_with_options(function_name, request, headers, runtime)

    def put_layer_aclwith_options(self, layer_name, request, headers, runtime):
        """
        Update layer ACL.
        

        @param request: PutLayerACLRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutLayerACLResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        Update layer ACL.
        

        @param request: PutLayerACLRequest

        @return: PutLayerACLResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_layer_aclwith_options(layer_name, request, headers, runtime)

    def put_provision_config_with_options(self, function_name, request, headers, runtime):
        """
        Put provision config.
        

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
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Put provision config.
        

        @param request: PutProvisionConfigRequest

        @return: PutProvisionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_provision_config_with_options(function_name, request, headers, runtime)

    def tag_resource_with_options(self, request, headers, runtime):
        """
        Tag resource
        

        @param request: TagResourceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourceResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
        )
        params = open_api_models.Params(
            action='TagResource',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            fc20230330_models.TagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resource(self, request):
        """
        Tag resource
        

        @param request: TagResourceRequest

        @return: TagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resource_with_options(request, headers, runtime)

    def untag_resource_with_options(self, request, headers, runtime):
        """
        Untag resource tag, support resource type: function, service
        

        @param request: UntagResourceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.arn):
            query['arn'] = request.arn
        if not UtilClient.is_unset(request.tag_keys):
            query['tagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResource',
            version='2023-03-30',
            protocol='HTTPS',
            pathname='/2023-03-30/tag',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            fc20230330_models.UntagResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resource(self, request):
        """
        Untag resource tag, support resource type: function, service
        

        @param request: UntagResourceRequest

        @return: UntagResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resource_with_options(request, headers, runtime)

    def update_alias_with_options(self, function_name, alias_name, request, headers, runtime):
        """
        Update function alias
        

        @param request: UpdateAliasRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAliasResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Update function alias
        

        @param request: UpdateAliasRequest

        @return: UpdateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_alias_with_options(function_name, alias_name, request, headers, runtime)

    def update_custom_domain_with_options(self, domain_name, request, headers, runtime):
        """
        Update custom domain.
        

        @param request: UpdateCustomDomainRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCustomDomainResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Update custom domain.
        

        @param request: UpdateCustomDomainRequest

        @return: UpdateCustomDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_custom_domain_with_options(domain_name, request, headers, runtime)

    def update_function_with_options(self, function_name, request, headers, runtime):
        """
        Update function
        

        @param request: UpdateFunctionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateFunctionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Update function
        

        @param request: UpdateFunctionRequest

        @return: UpdateFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_with_options(function_name, request, headers, runtime)

    def update_trigger_with_options(self, function_name, trigger_name, request, headers, runtime):
        """
        Update trigger.
        

        @param request: UpdateTriggerRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.request)
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
        Update trigger.
        

        @param request: UpdateTriggerRequest

        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_trigger_with_options(function_name, trigger_name, request, headers, runtime)
