# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tingwu20230930 import models as tingwu_20230930_models
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
        self._endpoint = self.get_endpoint('tingwu', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_task_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation):
            query['operation'] = request.operation
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/tasks',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    def create_transcription_phrases_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/resources/phrases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.CreateTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_transcription_phrases(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_transcription_phrases_with_options(request, headers, runtime)

    def delete_transcription_phrases_with_options(self, phrase_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/resources/phrases/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(phrase_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.DeleteTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_transcription_phrases(self, phrase_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_transcription_phrases_with_options(phrase_id, headers, runtime)

    def get_task_info_with_options(self, task_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTaskInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/tasks/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.GetTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task_info(self, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_info_with_options(task_id, headers, runtime)

    def get_transcription_phrases_with_options(self, phrase_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/resources/phrases/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(phrase_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.GetTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_transcription_phrases(self, phrase_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_transcription_phrases_with_options(phrase_id, headers, runtime)

    def list_transcription_phrases_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/resources/phrases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.ListTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_transcription_phrases(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_transcription_phrases_with_options(headers, runtime)

    def update_transcription_phrases_with_options(self, phrase_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.word_weights):
            body['WordWeights'] = request.word_weights
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTranscriptionPhrases',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/openapi/tingwu/v2/resources/phrases/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(phrase_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tingwu_20230930_models.UpdateTranscriptionPhrasesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_transcription_phrases(self, phrase_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_transcription_phrases_with_options(phrase_id, request, headers, runtime)
