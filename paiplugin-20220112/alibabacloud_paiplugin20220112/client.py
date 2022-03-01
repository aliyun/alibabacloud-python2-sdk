# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiplugin20220112 import models as pai_plugin_20220112_models
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
        self._endpoint = self.get_endpoint('paiplugin', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_group(self, request):
        """
        注册人群
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    def create_group_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        if not UtilClient.is_unset(request.inference_job_id):
            body['InferenceJobId'] = request.inference_job_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.table):
            body['Table'] = request.table
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_inference_job(self, request):
        """
        注册推理任务
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_inference_job_with_options(request, headers, runtime)

    def create_inference_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.training_job_id):
            body['TrainingJobId'] = request.training_job_id
        if not UtilClient.is_unset(request.user_config):
            body['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/inference/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_schedule(self, request):
        """
        注册触达计划
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_schedule_with_options(request, headers, runtime)

    def create_schedule_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_time):
            body['ExecuteTime'] = request.execute_time
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.repeat_cycle):
            body['RepeatCycle'] = request.repeat_cycle
        if not UtilClient.is_unset(request.repeat_cycle_unit):
            body['RepeatCycleUnit'] = request.repeat_cycle_unit
        if not UtilClient.is_unset(request.repeat_times):
            body['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/schedules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_signature(self, request):
        """
        注册签名。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_signature_with_options(request, headers, runtime)

    def create_signature_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/signatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        """
        注册模板
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    def create_template_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_training_job(self, request):
        """
        注册训练任务
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_training_job_with_options(request, headers, runtime)

    def create_training_job_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_config):
            body['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/training/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.CreateTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, id):
        """
        删除人群
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(id, headers, runtime)

    def delete_group_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/groups/%s' % TeaConverter.to_unicode(id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_inference_job(self, id):
        """
        删除推理任务
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_inference_job_with_options(id, headers, runtime)

    def delete_inference_job_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/inference/jobs/%s' % TeaConverter.to_unicode(id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_schedule(self, id):
        """
        删除触达计划
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_schedule_with_options(id, headers, runtime)

    def delete_schedule_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/schedules/%s' % TeaConverter.to_unicode(id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_signature(self, id):
        """
        删除签名。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_signature_with_options(id, headers, runtime)

    def delete_signature_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/signatures/%s' % TeaConverter.to_unicode(id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, id):
        """
        删除模板
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(id, headers, runtime)

    def delete_template_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/templates/%s' % TeaConverter.to_unicode(id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_training_job(self, id):
        """
        删除训练任务
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_training_job_with_options(id, headers, runtime)

    def delete_training_job_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/training/jobs/%s' % TeaConverter.to_unicode(id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.DeleteTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_algorithm(self, id):
        """
        获取算法详情
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_with_options(id, headers, runtime)

    def get_algorithm_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlgorithm',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/algorithms/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    def get_group(self, id):
        """
        获取人群
        默认返回所有人群信息
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(id, headers, runtime)

    def get_group_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/groups/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_inference_job(self, id):
        """
        获取推理任务
        默认返回所有推理任务信息
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_inference_job_with_options(id, headers, runtime)

    def get_inference_job_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInferenceJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/inference/jobs/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_schedule(self, id):
        """
        获取触达计划详情。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_schedule_with_options(id, headers, runtime)

    def get_schedule_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSchedule',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/schedules/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_signature(self, id):
        """
        获取签名详情
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_signature_with_options(id, headers, runtime)

    def get_signature_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSignature',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/signatures/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    def get_template(self, id):
        """
        获取模板
        默认返回所有模板信息
        ![模板列表](https://intranetproxy.alipay.com/skylark/lark/0/2021/png/302991/1615264998427-d2943cfb-106a-421d-b4a4-f06307b4d9be.png)
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(id, headers, runtime)

    def get_template_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/templates/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_training_job(self, id):
        """
        获取训练任务
        默认返回所有训练任务信息
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_training_job_with_options(id, headers, runtime)

    def get_training_job_with_options(self, id, headers, runtime):
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrainingJob',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/training/jobs/%s' % TeaConverter.to_unicode(id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.GetTrainingJobResponse(),
            self.call_api(params, req, runtime)
        )

    def list_algorithms(self, request):
        """
        获取算法列表
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_algorithms_with_options(request, headers, runtime)

    def list_algorithms_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithms',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/algorithms',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListAlgorithmsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_groups(self, request):
        """
        获取人群列表
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_groups_with_options(request, headers, runtime)

    def list_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_inference_jobs(self, request):
        """
        获取推理任务列表
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_inference_jobs_with_options(request, headers, runtime)

    def list_inference_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInferenceJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/inference/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListInferenceJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_message_metrics(self, request):
        """
        获取用户短信发送统计
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_message_metrics_with_options(request, headers, runtime)

    def list_message_metrics_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageMetrics',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/messages/metrics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessageMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_messages(self, request):
        """
        查询短信发送详情
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(request, headers, runtime)

    def list_messages_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.datetime):
            query['Datetime'] = request.datetime
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessages',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/messages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_schedules(self, request):
        """
        获取触达计划列表。
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_schedules_with_options(request, headers, runtime)

    def list_schedules_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchedules',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/schedules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_signatures(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_signatures_with_options(request, headers, runtime)

    def list_signatures_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSignatures',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/signatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListSignaturesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_templates(self, request):
        """
        获取模板列表
        默认返回所有模板信息
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    def list_templates_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_training_jobs(self, request):
        """
        获取训练任务列表
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_training_jobs_with_options(request, headers, runtime)

    def list_training_jobs_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrainingJobs',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/training/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.ListTrainingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def send_message(self, request):
        """
        发送短信
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_message_with_options(request, headers, runtime)

    def send_message_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.out_ids):
            body['OutIds'] = request.out_ids
        if not UtilClient.is_unset(request.phone_numbers):
            body['PhoneNumbers'] = request.phone_numbers
        if not UtilClient.is_unset(request.schedule_id):
            body['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.signature_id):
            body['SignatureId'] = request.signature_id
        if not UtilClient.is_unset(request.sms_up_extend_codes):
            body['SmsUpExtendCodes'] = request.sms_up_extend_codes
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_params):
            body['TemplateParams'] = request.template_params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/api/v2/messages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_plugin_20220112_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )
