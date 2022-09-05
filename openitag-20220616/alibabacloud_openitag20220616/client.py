# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openitag20220616 import models as open_itag_20220616_models
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
        self._endpoint = self.get_endpoint('openitag', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_work_node_workforce(self, tenant_id, task_id, work_node_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_work_node_workforce_with_options(tenant_id, task_id, work_node_id, request, headers, runtime)

    def add_work_node_workforce_with_options(self, tenant_id, task_id, work_node_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        work_node_id = OpenApiUtilClient.get_encode_param(work_node_id)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWorkNodeWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/worknodes/%s/workforce' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id), TeaConverter.to_unicode(work_node_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.AddWorkNodeWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(tenant_id, request, headers, runtime)

    def create_task_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks' % TeaConverter.to_unicode(tenant_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(tenant_id, request, headers, runtime)

    def create_template_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates' % TeaConverter.to_unicode(tenant_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(tenant_id, request, headers, runtime)

    def create_user_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        body = {}
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/users' % TeaConverter.to_unicode(tenant_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_task(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(tenant_id, task_id, headers, runtime)

    def delete_task_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, tenant_id, template_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(tenant_id, template_id, headers, runtime)

    def delete_template_with_options(self, tenant_id, template_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(template_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, tenant_id, user_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(tenant_id, user_id, headers, runtime)

    def delete_user_with_options(self, tenant_id, user_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/users/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(user_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def export_annotations(self, tenant_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_annotations_with_options(tenant_id, task_id, request, headers, runtime)

    def export_annotations_with_options(self, tenant_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.register_dataset):
            query['RegisterDataset'] = request.register_dataset
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportAnnotations',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/annotations/export' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ExportAnnotationsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_job(self, tenant_id, job_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(tenant_id, job_id, request, headers, runtime)

    def get_job_with_options(self, tenant_id, job_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/jobs/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(job_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subtask(self, tenant_id, task_id, subtask_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subtask_with_options(tenant_id, task_id, subtask_id, headers, runtime)

    def get_subtask_with_options(self, tenant_id, task_id, subtask_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSubtask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/subtasks/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id), TeaConverter.to_unicode(subtask_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetSubtaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_subtask_item(self, tenant_id, task_id, subtask_id, item_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subtask_item_with_options(tenant_id, task_id, subtask_id, item_id, headers, runtime)

    def get_subtask_item_with_options(self, tenant_id, task_id, subtask_id, item_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        item_id = OpenApiUtilClient.get_encode_param(item_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSubtaskItem',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/subtasks/%s/items/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id), TeaConverter.to_unicode(subtask_id), TeaConverter.to_unicode(item_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetSubtaskItemResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(tenant_id, task_id, headers, runtime)

    def get_task_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_statistics(self, tenant_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_statistics_with_options(tenant_id, task_id, request, headers, runtime)

    def get_task_statistics_with_options(self, tenant_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatistics',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/statistics' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_status(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(tenant_id, task_id, headers, runtime)

    def get_task_status_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/status' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_template(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_with_options(tenant_id, task_id, headers, runtime)

    def get_task_template_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/template' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_template_questions(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_questions_with_options(tenant_id, task_id, headers, runtime)

    def get_task_template_questions_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplateQuestions',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/template/questions' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_template_views(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_template_views_with_options(tenant_id, task_id, headers, runtime)

    def get_task_template_views_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskTemplateViews',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/template/views' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskTemplateViewsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_workforce(self, tenant_id, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_workforce_with_options(tenant_id, task_id, headers, runtime)

    def get_task_workforce_with_options(self, tenant_id, task_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/workforce' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_workforce_statistic(self, tenant_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_workforce_statistic_with_options(tenant_id, task_id, request, headers, runtime)

    def get_task_workforce_statistic_with_options(self, tenant_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stat_type):
            query['StatType'] = request.stat_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskWorkforceStatistic',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/workforce/statistic' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTaskWorkforceStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, tenant_id, template_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(tenant_id, template_id, headers, runtime)

    def get_template_with_options(self, tenant_id, template_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(template_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_questions(self, tenant_id, template_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_questions_with_options(tenant_id, template_id, headers, runtime)

    def get_template_questions_with_options(self, tenant_id, template_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplateQuestions',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates/%s/questions' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(template_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template_view(self, tenant_id, template_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_view_with_options(tenant_id, template_id, headers, runtime)

    def get_template_view_with_options(self, tenant_id, template_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplateView',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates/%s/views' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(template_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTemplateViewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tenant(self, tenant_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_with_options(tenant_id, headers, runtime)

    def get_tenant_with_options(self, tenant_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTenant',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s' % TeaConverter.to_unicode(tenant_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetTenantResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, tenant_id, user_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(tenant_id, user_id, headers, runtime)

    def get_user_with_options(self, tenant_id, user_id, headers, runtime):
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/users/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(user_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_jobs(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(tenant_id, request, headers, runtime)

    def list_jobs_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/jobs' % TeaConverter.to_unicode(tenant_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subtask_items(self, tenant_id, task_id, subtask_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subtask_items_with_options(tenant_id, task_id, subtask_id, request, headers, runtime)

    def list_subtask_items_with_options(self, tenant_id, task_id, subtask_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        subtask_id = OpenApiUtilClient.get_encode_param(subtask_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubtaskItems',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/subtasks/%s/items' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id), TeaConverter.to_unicode(subtask_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListSubtaskItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_subtasks(self, tenant_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subtasks_with_options(tenant_id, task_id, request, headers, runtime)

    def list_subtasks_with_options(self, tenant_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubtasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/subtasks' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListSubtasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(tenant_id, request, headers, runtime)

    def list_tasks_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks' % TeaConverter.to_unicode(tenant_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_templates(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(tenant_id, request, headers, runtime)

    def list_templates_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates' % TeaConverter.to_unicode(tenant_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tenants(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tenants_with_options(request, headers, runtime)

    def list_tenants_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTenants',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(tenant_id, request, headers, runtime)

    def list_users_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/users' % TeaConverter.to_unicode(tenant_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_work_node_workforce(self, tenant_id, task_id, work_node_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_work_node_workforce_with_options(tenant_id, task_id, work_node_id, request, headers, runtime)

    def remove_work_node_workforce_with_options(self, tenant_id, task_id, work_node_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        work_node_id = OpenApiUtilClient.get_encode_param(work_node_id)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveWorkNodeWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/worknodes/%s/workforce' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id), TeaConverter.to_unicode(work_node_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.RemoveWorkNodeWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_task(self, tenant_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_with_options(tenant_id, task_id, request, headers, runtime)

    def update_task_with_options(self, tenant_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateTask',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_task_workforce(self, tenant_id, task_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_workforce_with_options(tenant_id, task_id, request, headers, runtime)

    def update_task_workforce_with_options(self, tenant_id, task_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        body = {}
        if not UtilClient.is_unset(request.workforce):
            body['Workforce'] = request.workforce
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskWorkforce',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/tasks/%s/workforce' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTaskWorkforceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template(self, tenant_id, template_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(tenant_id, template_id, request, headers, runtime)

    def update_template_with_options(self, tenant_id, template_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(TeaCore.to_map(request.body))
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/templates/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(template_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_tenant(self, tenant_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tenant_with_options(tenant_id, request, headers, runtime)

    def update_tenant_with_options(self, tenant_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenant',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s' % TeaConverter.to_unicode(tenant_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateTenantResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, tenant_id, user_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(tenant_id, user_id, request, headers, runtime)

    def update_user_with_options(self, tenant_id, user_id, request, headers, runtime):
        UtilClient.validate_model(request)
        tenant_id = OpenApiUtilClient.get_encode_param(tenant_id)
        user_id = OpenApiUtilClient.get_encode_param(user_id)
        body = {}
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-06-16',
            protocol='HTTPS',
            pathname='/openapi/api/v1/tenants/%s/users/%s' % (TeaConverter.to_unicode(tenant_id), TeaConverter.to_unicode(user_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_itag_20220616_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )
