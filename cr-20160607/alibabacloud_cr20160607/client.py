# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cr20160607 import models as cr_20160607_models
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
        self._endpoint = self.get_endpoint('cr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_repo_build(self, repo_namespace, repo_name, build_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_repo_build_with_options(repo_namespace, repo_name, build_id, headers, runtime)

    def cancel_repo_build_with_options(self, repo_namespace, repo_name, build_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_id = OpenApiUtilClient.get_encode_param(build_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRepoBuild',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/build/%s/cancel' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(build_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CancelRepoBuildResponse(),
            self.call_api(params, req, runtime)
        )

    def create_namespace(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(headers, runtime)

    def create_namespace_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repo_with_options(headers, runtime)

    def create_repo_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_build_rule(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repo_build_rule_with_options(repo_namespace, repo_name, headers, runtime)

    def create_repo_build_rule_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/rules' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_repo_webhook(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_repo_webhook_with_options(repo_namespace, repo_name, headers, runtime)

    def create_repo_webhook_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/webhooks' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_info_with_options(headers, runtime)

    def create_user_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateUserInfo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.CreateUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image(self, repo_namespace, repo_name, tag):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_image_with_options(repo_namespace, repo_name, tag, headers, runtime)

    def delete_image_with_options(self, repo_namespace, repo_name, tag, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_namespace(self, namespace):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(namespace, headers, runtime)

    def delete_namespace_with_options(self, namespace, headers, runtime):
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/namespace/%s' % TeaConverter.to_unicode(namespace),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repo_with_options(repo_namespace, repo_name, headers, runtime)

    def delete_repo_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo_build_rule(self, repo_namespace, repo_name, build_rule_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repo_build_rule_with_options(repo_namespace, repo_name, build_rule_id, headers, runtime)

    def delete_repo_build_rule_with_options(self, repo_namespace, repo_name, build_rule_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/rules/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(build_rule_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_repo_webhook(self, repo_namespace, repo_name, webhook_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_repo_webhook_with_options(repo_namespace, repo_name, webhook_id, headers, runtime)

    def delete_repo_webhook_with_options(self, repo_namespace, repo_name, webhook_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        webhook_id = OpenApiUtilClient.get_encode_param(webhook_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/webhooks/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(webhook_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.DeleteRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def get_authorization_token(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_authorization_token_with_options(headers, runtime)

    def get_authorization_token_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAuthorizationToken',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/tokens',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetAuthorizationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_layer(self, repo_namespace, repo_name, tag):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_layer_with_options(repo_namespace, repo_name, tag, headers, runtime)

    def get_image_layer_with_options(self, repo_namespace, repo_name, tag, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetImageLayer',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s/layers' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetImageLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_image_manifest(self, repo_namespace, repo_name, tag, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_manifest_with_options(repo_namespace, repo_name, tag, request, headers, runtime)

    def get_image_manifest_with_options(self, repo_namespace, repo_name, tag, request, headers, runtime):
        UtilClient.validate_model(request)
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        query = {}
        if not UtilClient.is_unset(request.schema_version):
            query['SchemaVersion'] = request.schema_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageManifest',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s/manifest' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetImageManifestResponse(),
            self.call_api(params, req, runtime)
        )

    def get_namespace(self, namespace):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_namespace_with_options(namespace, headers, runtime)

    def get_namespace_with_options(self, namespace, headers, runtime):
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/namespace/%s' % TeaConverter.to_unicode(namespace),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_namespace_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_namespace_list_with_options(request, headers, runtime)

    def get_namespace_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNamespaceList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_region(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_with_options(request, headers, runtime)

    def get_region_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegion',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_region_list(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_list_with_options(headers, runtime)

    def get_region_list_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegionList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_with_options(repo_namespace, repo_name, headers, runtime)

    def get_repo_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_build_list(self, repo_namespace, repo_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_build_list_with_options(repo_namespace, repo_name, request, headers, runtime)

    def get_repo_build_list_with_options(self, repo_namespace, repo_name, request, headers, runtime):
        UtilClient.validate_model(request)
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoBuildList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/build' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_build_rule_list(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_build_rule_list_with_options(repo_namespace, repo_name, headers, runtime)

    def get_repo_build_rule_list_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoBuildRuleList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/rules' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_build_status(self, repo_namespace, repo_name, build_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_build_status_with_options(repo_namespace, repo_name, build_id, headers, runtime)

    def get_repo_build_status_with_options(self, repo_namespace, repo_name, build_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_id = OpenApiUtilClient.get_encode_param(build_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoBuildStatus',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/build/%s/status' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(build_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoBuildStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_list_with_options(request, headers, runtime)

    def get_repo_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_list_by_namespace(self, repo_namespace, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_list_by_namespace_with_options(repo_namespace, request, headers, runtime)

    def get_repo_list_by_namespace_with_options(self, repo_namespace, request, headers, runtime):
        UtilClient.validate_model(request)
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoListByNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s' % TeaConverter.to_unicode(repo_namespace),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoListByNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag(self, repo_namespace, repo_name, tag):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_with_options(repo_namespace, repo_name, tag, headers, runtime)

    def get_repo_tag_with_options(self, repo_namespace, repo_name, tag, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTag',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_scan_list(self, repo_namespace, repo_name, tag, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_scan_list_with_options(repo_namespace, repo_name, tag, request, headers, runtime)

    def get_repo_tag_scan_list_with_options(self, repo_namespace, repo_name, tag, request, headers, runtime):
        UtilClient.validate_model(request)
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTagScanList',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s/scanResult' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_scan_status(self, repo_namespace, repo_name, tag):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_scan_status_with_options(repo_namespace, repo_name, tag, headers, runtime)

    def get_repo_tag_scan_status_with_options(self, repo_namespace, repo_name, tag, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTagScanStatus',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s/scanStatus' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tag_scan_summary(self, repo_namespace, repo_name, tag):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tag_scan_summary_with_options(repo_namespace, repo_name, tag, headers, runtime)

    def get_repo_tag_scan_summary_with_options(self, repo_namespace, repo_name, tag, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoTagScanSummary',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s/scanCount' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagScanSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_tags(self, repo_namespace, repo_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_tags_with_options(repo_namespace, repo_name, request, headers, runtime)

    def get_repo_tags_with_options(self, repo_namespace, repo_name, request, headers, runtime):
        UtilClient.validate_model(request)
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRepoTags',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_repo_webhook(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_repo_webhook_with_options(repo_namespace, repo_name, headers, runtime)

    def get_repo_webhook_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/webhooks' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_quota(self, resource_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_quota_with_options(resource_name, headers, runtime)

    def get_resource_quota_with_options(self, resource_name, headers, runtime):
        resource_name = OpenApiUtilClient.get_encode_param(resource_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResourceQuota',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/resource/%s' % TeaConverter.to_unicode(resource_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.GetResourceQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def start_image_scan(self, repo_namespace, repo_name, tag):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_image_scan_with_options(repo_namespace, repo_name, tag, headers, runtime)

    def start_image_scan_with_options(self, repo_namespace, repo_name, tag, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        tag = OpenApiUtilClient.get_encode_param(tag)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartImageScan',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/tags/%s/scan' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(tag)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.StartImageScanResponse(),
            self.call_api(params, req, runtime)
        )

    def start_repo_build_by_rule(self, repo_namespace, repo_name, build_rule_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_repo_build_by_rule_with_options(repo_namespace, repo_name, build_rule_id, headers, runtime)

    def start_repo_build_by_rule_with_options(self, repo_namespace, repo_name, build_rule_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartRepoBuildByRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/rules/%s/build' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(build_rule_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.StartRepoBuildByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_namespace(self, namespace):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(namespace, headers, runtime)

    def update_namespace_with_options(self, namespace, headers, runtime):
        namespace = OpenApiUtilClient.get_encode_param(namespace)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/namespace/%s' % TeaConverter.to_unicode(namespace),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repo(self, repo_namespace, repo_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repo_with_options(repo_namespace, repo_name, headers, runtime)

    def update_repo_with_options(self, repo_namespace, repo_name, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repo_build_rule(self, repo_namespace, repo_name, build_rule_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repo_build_rule_with_options(repo_namespace, repo_name, build_rule_id, headers, runtime)

    def update_repo_build_rule_with_options(self, repo_namespace, repo_name, build_rule_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        build_rule_id = OpenApiUtilClient.get_encode_param(build_rule_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepoBuildRule',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/rules/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(build_rule_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_repo_webhook(self, repo_namespace, repo_name, webhook_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_repo_webhook_with_options(repo_namespace, repo_name, webhook_id, headers, runtime)

    def update_repo_webhook_with_options(self, repo_namespace, repo_name, webhook_id, headers, runtime):
        repo_namespace = OpenApiUtilClient.get_encode_param(repo_namespace)
        repo_name = OpenApiUtilClient.get_encode_param(repo_name)
        webhook_id = OpenApiUtilClient.get_encode_param(webhook_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateRepoWebhook',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/repos/%s/%s/webhooks/%s' % (TeaConverter.to_unicode(repo_namespace), TeaConverter.to_unicode(repo_name), TeaConverter.to_unicode(webhook_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateRepoWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_info(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_info_with_options(headers, runtime)

    def update_user_info_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateUserInfo',
            version='2016-06-07',
            protocol='HTTPS',
            pathname='/users',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cr_20160607_models.UpdateUserInfoResponse(),
            self.call_api(params, req, runtime)
        )
