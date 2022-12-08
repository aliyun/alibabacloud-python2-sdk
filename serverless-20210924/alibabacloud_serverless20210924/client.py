# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_serverless20210924 import models as serverless_20210924_models
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
        self._endpoint = self.get_endpoint('serverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_task(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(name, headers, runtime)

    def cancel_task_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks/%s/cancel' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    def create_application_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_deploy):
            body['autoDeploy'] = request.auto_deploy
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.env_vars):
            body['envVars'] = request.env_vars
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.repo_source):
            body['repoSource'] = request.repo_source
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.trigger):
            body['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/applications',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pipeline(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_with_options(request, headers, runtime)

    def create_pipeline_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreatePipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pipeline_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipeline_template_with_options(request, headers, runtime)

    def create_pipeline_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreatePipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelinetemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreatePipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_release(self, app_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_release_with_options(app_name, request, headers, runtime)

    def create_release_with_options(self, app_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRelease',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/applications/%s/releases' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    def create_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task_template(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_template_with_options(request, headers, runtime)

    def create_task_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasktemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.CreateTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(name, headers, runtime)

    def delete_application_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/applications/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_environment(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(name, headers, runtime)

    def delete_environment_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/environments/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipeline_template(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipeline_template_with_options(name, headers, runtime)

    def delete_pipeline_template_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelinetemplates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeletePipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_task_template(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_template_with_options(name, headers, runtime)

    def delete_task_template_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasktemplates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(name, request, headers, runtime)

    def delete_template_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/templates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_application(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_application_with_options(name, headers, runtime)

    def get_application_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/applications/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_environment(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(name, headers, runtime)

    def get_environment_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/environments/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_with_options(name, headers, runtime)

    def get_pipeline_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelines/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pipeline_template(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pipeline_template_with_options(name, headers, runtime)

    def get_pipeline_template_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelinetemplates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetPipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_release(self, app_name, version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_release_with_options(app_name, version_id, headers, runtime)

    def get_release_with_options(self, app_name, version_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRelease',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/applications/%s/releases/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(app_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(name, headers, runtime)

    def get_service_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/services/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(name, headers, runtime)

    def get_task_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_template(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_with_options(name, headers, runtime)

    def get_task_template_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasktemplates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(name, request, headers, runtime)

    def get_template_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/templates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environment_revisions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environment_revisions_with_options(request, headers, runtime)

    def list_environment_revisions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_name):
            query['environmentName'] = request.environment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/environmentrevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_environments(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(headers, runtime)

    def list_environments_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/environments/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_templates_with_options(request, headers, runtime)

    def list_pipeline_templates_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListPipelineTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelineTemplates',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelinetemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListPipelineTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipelines(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipelines_with_options(request, headers, runtime)

    def list_pipelines_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListPipelinesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_service_revisions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_revisions_with_options(request, headers, runtime)

    def list_service_revisions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/servicerevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServiceRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_services(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(headers, runtime)

    def list_services_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/services/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_task_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_templates_with_options(request, headers, runtime)

    def list_task_templates_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListTaskTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskTemplates',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasktemplates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTaskTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    def list_tasks_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = serverless_20210924_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'labelSelector', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_selector_shrink):
            query['labelSelector'] = request.label_selector_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_template_revisions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_template_revisions_with_options(request, headers, runtime)

    def list_template_revisions_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_version):
            query['templateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateRevisions',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/templaterevisions/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTemplateRevisionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    def list_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/templates/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def put_environment(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_environment_with_options(name, request, headers, runtime)

    def put_environment_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutEnvironment',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/environments/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def put_pipeline_status(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_status_with_options(name, request, headers, runtime)

    def put_pipeline_status_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutPipelineStatus',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelines/%s/status' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutPipelineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def put_pipeline_template(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_pipeline_template_with_options(name, request, headers, runtime)

    def put_pipeline_template_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutPipelineTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelinetemplates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutPipelineTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def put_service(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_service_with_options(name, request, headers, runtime)

    def put_service_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutService',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/services/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def put_task_status(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_task_status_with_options(name, request, headers, runtime)

    def put_task_status_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutTaskStatus',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks/%s/status' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def put_task_template(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_task_template_with_options(name, request, headers, runtime)

    def put_task_template_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutTaskTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasktemplates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def put_template(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_template_with_options(name, request, headers, runtime)

    def put_template_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='PutTemplate',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/templates/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.PutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_task(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(name, headers, runtime)

    def resume_task_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks/%s/resume' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.ResumeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_pipeline(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_pipeline_with_options(name, headers, runtime)

    def start_pipeline_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartPipeline',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/pipelines/%s/start' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.StartPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def start_task(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_task_with_options(name, headers, runtime)

    def start_task_with_options(self, name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartTask',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/tasks/%s/start' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.StartTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_with_options(name, request, headers, runtime)

    def update_application_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateApplication',
            version='2021-09-24',
            protocol='HTTPS',
            pathname='/apis/serverlessdeployment/v1/applications/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            serverless_20210924_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )
