# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudcontrol20220606 import models as cloudcontrol_20220606_models
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
        self._endpoint = self.get_endpoint('cloudcontrol', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    def cancel_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/tasks/%s/operation/cancel' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource(self, provider, product_code, resource_type_code, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    def create_resource_with_options(self, provider, product_code, resource_type_code, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s/resources' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource(self, provider, product_code, resource_type_code, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def delete_resource_with_options(self, provider, product_code, resource_type_code, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s/resources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource(self, provider, product_code, resource_type_code, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def get_resource_with_options(self, provider, product_code, resource_type_code, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s/resources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_type(self, provider, product_code, resource_type_code, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_type_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    def get_resource_type_with_options(self, provider, product_code, resource_type_code, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    def get_task_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_sources(self, provider, product_code, resource_type_code, attribute_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(provider, product_code, resource_type_code, attribute_name, request, headers, runtime)

    def list_data_sources_with_options(self, provider, product_code, resource_type_code, attribute_name, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220606_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s/dataSources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(attribute_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_products(self, provider, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(provider, request, headers, runtime)

    def list_products_with_options(self, provider, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_types(self, provider, product_code, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_types_with_options(provider, product_code, request, headers, runtime)

    def list_resource_types_with_options(self, provider, product_code, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220606_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_type_codes):
            request.resource_type_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_type_codes, 'resourceTypeCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type_codes_shrink):
            query['resourceTypeCodes'] = request.resource_type_codes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources(self, provider, product_code, resource_type_code, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    def list_resources_with_options(self, provider, product_code, resource_type_code, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220606_models.ListResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s/resources' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource(self, provider, product_code, resource_type_code, resource_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def update_resource_with_options(self, provider, product_code, resource_type_code, resource_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname='/api/v1/providers/%s/products/%s/resourceTypes/%s/resources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(provider)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(product_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_type_code)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(resource_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )
