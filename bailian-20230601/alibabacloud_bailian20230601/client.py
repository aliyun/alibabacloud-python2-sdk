# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bailian20230601 import models as bailian_20230601_models
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
        self._endpoint = self.get_endpoint('bailian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_enterprise_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEnterpriseTag',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.AddEnterpriseTagResponse(),
            self.call_api(params, req, runtime)
        )

    def add_enterprise_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_enterprise_tag_with_options(request, runtime)

    def cancel_fine_tune_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CancelFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_fine_tune_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_fine_tune_job_with_options(request, runtime)

    def create_fine_tune_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.CreateFineTuneJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.hyper_parameters):
            request.hyper_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.hyper_parameters, 'HyperParameters', 'json')
        if not UtilClient.is_unset(tmp_req.training_files):
            request.training_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.training_files, 'TrainingFiles', 'json')
        if not UtilClient.is_unset(tmp_req.validation_files):
            request.validation_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.validation_files, 'ValidationFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.base_model):
            body['BaseModel'] = request.base_model
        if not UtilClient.is_unset(request.hyper_parameters_shrink):
            body['HyperParameters'] = request.hyper_parameters_shrink
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.training_files_shrink):
            body['TrainingFiles'] = request.training_files_shrink
        if not UtilClient.is_unset(request.training_type):
            body['TrainingType'] = request.training_type
        if not UtilClient.is_unset(request.validation_files_shrink):
            body['ValidationFiles'] = request.validation_files_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_fine_tune_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_fine_tune_job_with_options(request, runtime)

    def create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    def create_text_embeddings_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.CreateTextEmbeddingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.text_type):
            query['TextType'] = request.text_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTextEmbeddings',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateTextEmbeddingsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_text_embeddings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_text_embeddings_with_options(request, runtime)

    def create_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateToken',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.CreateTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_token_with_options(request, runtime)

    def del_enterprise_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelEnterpriseTag',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DelEnterpriseTagResponse(),
            self.call_api(params, req, runtime)
        )

    def del_enterprise_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_enterprise_tag_with_options(request, runtime)

    def delete_enterprise_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseData',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteEnterpriseDataResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_enterprise_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_data_with_options(request, runtime)

    def delete_fine_tune_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_fine_tune_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_fine_tune_job_with_options(request, runtime)

    def delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    def describe_fine_tune_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeFineTuneJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DescribeFineTuneJobResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fine_tune_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fine_tune_job_with_options(request, runtime)

    def describe_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeService',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.DescribeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_with_options(request, runtime)

    def get_enterprise_data_by_data_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataByDataId',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetEnterpriseDataByDataIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_data_by_data_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_by_data_id_with_options(request, runtime)

    def get_enterprise_data_chunk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataChunk',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetEnterpriseDataChunkResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_data_chunk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_chunk_with_options(request, runtime)

    def get_enterprise_data_page_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataPageImage',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetEnterpriseDataPageImageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_data_page_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_page_image_with_options(request, runtime)

    def get_enterprise_data_parse_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDataParseResult',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetEnterpriseDataParseResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_data_parse_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_data_parse_result_with_options(request, runtime)

    def get_file_store_upload_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_store_id):
            query['FileStoreId'] = request.file_store_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileStoreUploadPolicy',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetFileStoreUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_store_upload_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_store_upload_policy_with_options(request, runtime)

    def get_import_task_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImportTaskResult',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetImportTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_import_task_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_import_task_result_with_options(request, runtime)

    def get_prompt_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.prompt_id):
            query['PromptId'] = request.prompt_id
        if not UtilClient.is_unset(request.vars):
            query['Vars'] = request.vars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrompt',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetPromptResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prompt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prompt_with_options(request, runtime)

    def get_text_2image_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetText2ImageJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.GetText2ImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_text_2image_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_text_2image_job_with_options(request, runtime)

    def import_enterprise_document_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.ImportEnterpriseDocumentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.document_list):
            request.document_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_list, 'DocumentList', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.document_list_shrink):
            query['DocumentList'] = request.document_list_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportEnterpriseDocument',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ImportEnterpriseDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    def import_enterprise_document(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_enterprise_document_with_options(request, runtime)

    def import_user_document_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_store_id):
            query['FileStoreId'] = request.file_store_id
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportUserDocument',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ImportUserDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    def import_user_document(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_user_document_with_options(request, runtime)

    def list_fine_tune_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFineTuneJobs',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ListFineTuneJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_fine_tune_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_fine_tune_jobs_with_options(request, runtime)

    def list_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_key):
            body['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    def query_enterprise_data_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.QueryEnterpriseDataListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_type):
            query['StoreType'] = request.store_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseDataList',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.QueryEnterpriseDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_enterprise_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_enterprise_data_list_with_options(request, runtime)

    def query_enterprise_data_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseDataTag',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.QueryEnterpriseDataTagResponse(),
            self.call_api(params, req, runtime)
        )

    def query_enterprise_data_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_enterprise_data_tag_with_options(request, runtime)

    def query_enterprise_tag_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnterpriseTagList',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.QueryEnterpriseTagListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_enterprise_tag_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_enterprise_tag_list_with_options(request, runtime)

    def query_user_document_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserDocument',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.QueryUserDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    def query_user_document(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_user_document_with_options(request, runtime)

    def search_enterprise_data_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.SearchEnterpriseDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_id_list):
            request.data_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_id_list, 'DataIdList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_id_list):
            request.tag_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_id_list, 'TagIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id_list_shrink):
            query['DataIdList'] = request.data_id_list_shrink
        if not UtilClient.is_unset(request.enable_rank):
            query['EnableRank'] = request.enable_rank
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.store_id):
            query['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.tag_id_list_shrink):
            query['TagIdList'] = request.tag_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEnterpriseData',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.SearchEnterpriseDataResponse(),
            self.call_api(params, req, runtime)
        )

    def search_enterprise_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_enterprise_data_with_options(request, runtime)

    def submit_text_2image_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.n):
            query['N'] = request.n
        if not UtilClient.is_unset(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.style):
            query['Style'] = request.style
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitText2ImageJob',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.SubmitText2ImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_text_2image_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_text_2image_job_with_options(request, runtime)

    def update_enterprise_data_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.file_preview_link):
            query['FilePreviewLink'] = request.file_preview_link
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseDataInfo',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.UpdateEnterpriseDataInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_enterprise_data_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_data_info_with_options(request, runtime)

    def update_enterprise_data_tag_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = bailian_20230601_models.UpdateEnterpriseDataTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseDataTag',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.UpdateEnterpriseDataTagResponse(),
            self.call_api(params, req, runtime)
        )

    def update_enterprise_data_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_data_tag_with_options(request, runtime)

    def update_enterprise_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseTag',
            version='2023-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bailian_20230601_models.UpdateEnterpriseTagResponse(),
            self.call_api(params, req, runtime)
        )

    def update_enterprise_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_tag_with_options(request, runtime)
