# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_easygene20210315 import models as easy_gene_20210315_models
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
        self._endpoint = self.get_endpoint('easygene', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_run_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortRunResponse(),
            self.call_api(params, req, runtime)
        )

    def abort_run(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abort_run_with_options(request, runtime)

    def abort_submission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.AbortSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def abort_submission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.abort_submission_with_options(request, runtime)

    def copy_public_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset):
            query['Dataset'] = request.dataset
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyPublicEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CopyPublicEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_public_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_public_entity_with_options(request, runtime)

    def create_app_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.dependencies):
            request.dependencies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependencies, 'Dependencies', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_version):
            query['LanguageVersion'] = request.language_version
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.revision_comment):
            query['RevisionComment'] = request.revision_comment
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.definition):
            body['Definition'] = request.definition
        if not UtilClient.is_unset(request.dependencies_shrink):
            body['Dependencies'] = request.dependencies_shrink
        if not UtilClient.is_unset(request.documentation):
            body['Documentation'] = request.documentation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_entity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_entity_with_options(request, runtime)

    def create_run_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateRunShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_options):
            request.execute_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_options, 'ExecuteOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_runtime):
            query['DefaultRuntime'] = request.default_runtime
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execute_directory):
            query['ExecuteDirectory'] = request.execute_directory
        if not UtilClient.is_unset(request.execute_options_shrink):
            query['ExecuteOptions'] = request.execute_options_shrink
        if not UtilClient.is_unset(request.inputs):
            query['Inputs'] = request.inputs
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.output_folder):
            query['OutputFolder'] = request.output_folder
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.run_name):
            query['RunName'] = request.run_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateRunResponse(),
            self.call_api(params, req, runtime)
        )

    def create_run(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_run_with_options(request, runtime)

    def create_submission_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateSubmissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_runtime):
            query['DefaultRuntime'] = request.default_runtime
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.execute_directory):
            query['ExecuteDirectory'] = request.execute_directory
        if not UtilClient.is_unset(request.execute_options):
            query['ExecuteOptions'] = request.execute_options
        if not UtilClient.is_unset(request.inputs):
            query['Inputs'] = request.inputs
        if not UtilClient.is_unset(request.output_folder):
            query['OutputFolder'] = request.output_folder
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_submission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_submission_with_options(request, runtime)

    def create_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs_expression):
            request.inputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs_expression, 'InputsExpression', 'json')
        if not UtilClient.is_unset(tmp_req.outputs_expression):
            request.outputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs_expression, 'OutputsExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.root_entity):
            query['RootEntity'] = request.root_entity
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.inputs_expression_shrink):
            body['InputsExpression'] = request.inputs_expression_shrink
        if not UtilClient.is_unset(request.outputs_expression_shrink):
            body['OutputsExpression'] = request.outputs_expression_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def create_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.job_lifecycle):
            query['JobLifecycle'] = request.job_lifecycle
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.storage):
            query['Storage'] = request.storage
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_workspace_with_options(request, runtime)

    def delete_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    def delete_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_with_options(request, runtime)

    def delete_entity_items_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DeleteEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_entity_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_items_with_options(request, runtime)

    def delete_run_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['RunId'] = request.run_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteRunResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_run(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_run_with_options(request, runtime)

    def delete_submission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_submission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_submission_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def delete_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_workspace_with_options(request, runtime)

    def download_entity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.DownloadEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_names):
            request.entity_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_names, 'EntityNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_names_shrink):
            query['EntityNames'] = request.entity_names_shrink
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.DownloadEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def download_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_entity_with_options(request, runtime)

    def get_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.revision):
            query['Revision'] = request.revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    def get_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_entity_with_options(request, runtime)

    def get_global_app_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetGlobalAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGlobalApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetGlobalAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_global_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_global_app_with_options(request, runtime)

    def get_public_dataset_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.GetPublicDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicDataset',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_public_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_public_dataset_with_options(request, runtime)

    def get_public_dataset_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicDatasetEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetPublicDatasetEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_public_dataset_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_public_dataset_entity_with_options(request, runtime)

    def get_run_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRun',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetRunResponse(),
            self.call_api(params, req, runtime)
        )

    def get_run(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_run_with_options(request, runtime)

    def get_submission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_submission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_submission_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def get_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_workspace_with_options(request, runtime)

    def import_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ImportAppResponse(),
            self.call_api(params, req, runtime)
        )

    def import_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_app_with_options(request, runtime)

    def install_global_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.installed_app_name):
            query['InstalledAppName'] = request.installed_app_name
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallGlobalApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.InstallGlobalAppResponse(),
            self.call_api(params, req, runtime)
        )

    def install_global_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_global_app_with_options(request, runtime)

    def list_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.label_selector):
            query['LabelSelector'] = request.label_selector
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    def list_authorized_software_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthorizedSoftware',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListAuthorizedSoftwareResponse(),
            self.call_api(params, req, runtime)
        )

    def list_authorized_software(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_authorized_software_with_options(request, runtime)

    def list_container_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContainerImages',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListContainerImagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_container_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_container_images_with_options(request, runtime)

    def list_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntities',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_entities_with_options(request, runtime)

    def list_entity_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_entity_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_entity_items_with_options(request, runtime)

    def list_global_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGlobalApps',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListGlobalAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_global_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_global_apps_with_options(request, runtime)

    def list_public_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDataset',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def list_public_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_with_options(request, runtime)

    def list_public_dataset_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetEntities',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_public_dataset_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_entities_with_options(request, runtime)

    def list_public_dataset_entity_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_public_dataset_entity_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_entity_items_with_options(request, runtime)

    def list_public_dataset_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicDatasetTags',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListPublicDatasetTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_public_dataset_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_public_dataset_tags_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def list_runs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuns',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListRunsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_runs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_runs_with_options(request, runtime)

    def list_submissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubmissions',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListSubmissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_submissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_submissions_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_reversed):
            query['IsReversed'] = request.is_reversed
        if not UtilClient.is_unset(request.label_selector):
            query['LabelSelector'] = request.label_selector
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def list_user_active_runs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserActiveRuns',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListUserActiveRunsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_active_runs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_active_runs_with_options(request, runtime)

    def list_workspaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_workspaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_workspaces_with_options(request, runtime)

    def resume_submission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.submission_id):
            query['SubmissionId'] = request.submission_id
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSubmission',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.ResumeSubmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_submission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_submission_with_options(request, runtime)

    def tag_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_revision):
            query['AppRevision'] = request.app_revision
        if not UtilClient.is_unset(request.revision_tag):
            query['RevisionTag'] = request.revision_tag
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagApp',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.TagAppResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_app_with_options(request, runtime)

    def update_entity_with_options(self, tmp_req, runtime):
        """
        @deprecated : UpdateEntity is deprecated, please use EasyGene::2021-03-15::UpdateEntityItems instead.
        

        @param tmp_req: UpdateEntityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateEntityResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def update_entity(self, request):
        """
        @deprecated : UpdateEntity is deprecated, please use EasyGene::2021-03-15::UpdateEntityItems instead.
        

        @param request: UpdateEntityRequest

        @return: UpdateEntityResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_entity_with_options(request, runtime)

    def update_entity_items_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateEntityItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.entity_items):
            request.entity_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.entity_items, 'EntityItems', 'json')
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.entity_items_shrink):
            body['EntityItems'] = request.entity_items_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntityItems',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateEntityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_entity_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_entity_items_with_options(request, runtime)

    def update_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = easy_gene_20210315_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs_expression):
            request.inputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs_expression, 'InputsExpression', 'json')
        if not UtilClient.is_unset(tmp_req.outputs_expression):
            request.outputs_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.outputs_expression, 'OutputsExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.root_entity):
            query['RootEntity'] = request.root_entity
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        body = {}
        if not UtilClient.is_unset(request.inputs_expression_shrink):
            body['InputsExpression'] = request.inputs_expression_shrink
        if not UtilClient.is_unset(request.outputs_expression_shrink):
            body['OutputsExpression'] = request.outputs_expression_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    def update_workspace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.job_lifecycle):
            query['JobLifecycle'] = request.job_lifecycle
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_workspace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_with_options(request, runtime)

    def upload_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_csvfile):
            query['EntityCSVFile'] = request.entity_csvfile
        if not UtilClient.is_unset(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadEntity',
            version='2021-03-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            easy_gene_20210315_models.UploadEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_entity_with_options(request, runtime)
