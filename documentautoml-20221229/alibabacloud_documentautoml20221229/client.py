# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_documentautoml20221229 import models as document_automl_20221229_models
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
        self._endpoint = self.get_endpoint('documentautoml', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_model_async_predict_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelAsyncPredict',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.CreateModelAsyncPredictResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model_async_predict(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_model_async_predict_with_options(request, runtime)

    def get_model_async_predict_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_predict_id):
            query['AsyncPredictId'] = request.async_predict_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModelAsyncPredict',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.GetModelAsyncPredictResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model_async_predict(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_model_async_predict_with_options(request, runtime)

    def predict_classifier_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_prediction):
            query['AutoPrediction'] = request.auto_prediction
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.classifier_id):
            query['ClassifierId'] = request.classifier_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictClassifierModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictClassifierModelResponse(),
            self.call_api(params, req, runtime)
        )

    def predict_classifier_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_classifier_model_with_options(request, runtime)

    def predict_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictModelResponse(),
            self.call_api(params, req, runtime)
        )

    def predict_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_model_with_options(request, runtime)

    def predict_pre_train_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictPreTrainModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictPreTrainModelResponse(),
            self.call_api(params, req, runtime)
        )

    def predict_pre_train_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_pre_train_model_with_options(request, runtime)

    def predict_template_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictTemplateModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictTemplateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def predict_template_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_template_model_with_options(request, runtime)
