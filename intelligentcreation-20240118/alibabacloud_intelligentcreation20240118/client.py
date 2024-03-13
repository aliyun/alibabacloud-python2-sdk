# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_intelligentcreation20240118 import models as intelligent_creation_20240118_models
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
        self._endpoint = self.get_endpoint('intelligentcreation', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def actual_deduct_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ActualDeductResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/digital-human/commands/actual-deduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.ActualDeductResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def actual_deduct_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.actual_deduct_resource_with_options(request, headers, runtime)

    def actual_deduct_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ActualDeductResources',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/actualDeductResources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.ActualDeductResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def actual_deduct_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.actual_deduct_resources_with_options(request, headers, runtime)

    def copywriting_qawith_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240118_models.CopywritingQAShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.histories):
            request.histories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.histories, 'histories', 'json')
        if not UtilClient.is_unset(tmp_req.history):
            request.history_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.history, 'history', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.histories_shrink):
            query['histories'] = request.histories_shrink
        if not UtilClient.is_unset(request.history_shrink):
            query['history'] = request.history_shrink
        if not UtilClient.is_unset(request.question):
            query['question'] = request.question
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream):
            query['stream'] = request.stream
        if not UtilClient.is_unset(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopywritingQA',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/copywritingQA',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.CopywritingQAResponse(),
            self.call_api(params, req, runtime)
        )

    def copywriting_qa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copywriting_qawith_options(request, headers, runtime)

    def copywriting_qav1with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CopywritingQAV1',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/copywritingQAV1',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.CopywritingQAV1Response(),
            self.call_api(params, req, runtime)
        )

    def copywriting_qav1(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copywriting_qav1with_options(request, headers, runtime)

    def delete_digital_video_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['accountId'] = request.account_id
        if not UtilClient.is_unset(request.video_id):
            body['videoId'] = request.video_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDigitalVideo',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/videos',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.DeleteDigitalVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_digital_video(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_digital_video_with_options(request, headers, runtime)

    def direct_deduct_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DirectDeductResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/digital-human/commands/direct-deduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.DirectDeductResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def direct_deduct_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.direct_deduct_resource_with_options(request, headers, runtime)

    def direct_deduct_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='DirectDeductResources',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/directDeductResources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.DirectDeductResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def direct_deduct_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.direct_deduct_resources_with_options(request, headers, runtime)

    def expect_deduct_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ExpectDeductResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/digital-human/commands/expect-deduct',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.ExpectDeductResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def expect_deduct_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.expect_deduct_resource_with_options(request, headers, runtime)

    def expect_deduct_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ExpectDeductResources',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/expectDeductResources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.ExpectDeductResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def expect_deduct_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.expect_deduct_resources_with_options(request, headers, runtime)

    def get_remain_resource_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRemainResource',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/getRemainResource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.GetRemainResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_remain_resource(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_remain_resource_with_options(request, headers, runtime)

    def submit_bullet_questions_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = intelligent_creation_20240118_models.SubmitBulletQuestionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.questions):
            request.questions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.questions, 'questions', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['accountId'] = request.account_id
        if not UtilClient.is_unset(request.questions_shrink):
            query['questions'] = request.questions_shrink
        if not UtilClient.is_unset(request.room_id):
            query['roomId'] = request.room_id
        if not UtilClient.is_unset(request.sub_account_id):
            query['subAccountId'] = request.sub_account_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitBulletQuestions',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/submitBulletQuestions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.SubmitBulletQuestionsResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_bullet_questions(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_bullet_questions_with_options(request, headers, runtime)

    def submit_bullet_questions_v1with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='SubmitBulletQuestionsV1',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/openService/v1/digitalHuman/commands/submitBulletQuestionsV1',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            intelligent_creation_20240118_models.SubmitBulletQuestionsV1Response(),
            self.call_api(params, req, runtime)
        )

    def submit_bullet_questions_v1(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_bullet_questions_v1with_options(request, headers, runtime)
