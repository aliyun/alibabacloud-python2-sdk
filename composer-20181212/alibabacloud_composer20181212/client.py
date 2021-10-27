# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_composer20181212 import models as composer_20181212_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('composer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def clone_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.CloneFlowResponse(),
            self.do_rpcrequest('CloneFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    def create_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.CreateFlowResponse(),
            self.do_rpcrequest('CreateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    def delete_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.DeleteFlowResponse(),
            self.do_rpcrequest('DeleteFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    def disable_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.DisableFlowResponse(),
            self.do_rpcrequest('DisableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_flow_with_options(request, runtime)

    def enable_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.EnableFlowResponse(),
            self.do_rpcrequest('EnableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_flow_with_options(request, runtime)

    def get_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetFlowResponse(),
            self.do_rpcrequest('GetFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_flow_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def get_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GetVersionResponse(),
            self.do_rpcrequest('GetVersion', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_version_with_options(request, runtime)

    def group_invoke_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.GroupInvokeFlowResponse(),
            self.do_rpcrequest('GroupInvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def group_invoke_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.group_invoke_flow_with_options(request, runtime)

    def invoke_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.InvokeFlowResponse(),
            self.do_rpcrequest('InvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_flow_with_options(request, runtime)

    def list_flows_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListFlowsResponse(),
            self.do_rpcrequest('ListFlows', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flows(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListTemplatesResponse(),
            self.do_rpcrequest('ListTemplates', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def list_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.ListVersionsResponse(),
            self.do_rpcrequest('ListVersions', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            composer_20181212_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            composer_20181212_models.UpdateFlowResponse(),
            self.do_rpcrequest('UpdateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_flow_with_options(request, runtime)
