# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qualitycheck20190115 import models as qualitycheck_20190115_models
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
        self._endpoint = self.get_endpoint('qualitycheck', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_business_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBusinessCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddBusinessCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_business_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_business_category_with_options(request, runtime)

    def add_rule_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_rule_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_rule_category_with_options(request, runtime)

    def add_thesaurus_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddThesaurusForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddThesaurusForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def add_thesaurus_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_thesaurus_for_api_with_options(request, runtime)

    def assign_reviewer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignReviewer',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AssignReviewerResponse(),
            self.call_api(params, req, runtime)
        )

    def assign_reviewer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_reviewer_with_options(request, runtime)

    def create_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    def create_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_asr_vocab_with_options(request, runtime)

    def create_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_config_with_options(request, runtime)

    def create_task_assign_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task_assign_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_task_assign_rule_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_warning_config_with_options(request, runtime)

    def del_rule_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DelRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def del_rule_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_rule_category_with_options(request, runtime)

    def del_thesaurus_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelThesaurusForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DelThesaurusForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def del_thesaurus_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_thesaurus_for_api_with_options(request, runtime)

    def delete_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_asr_vocab_with_options(request, runtime)

    def delete_business_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteBusinessCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_business_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_category_with_options(request, runtime)

    def delete_customization_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomizationConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteCustomizationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_customization_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_customization_config_with_options(request, runtime)

    def delete_data_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    def delete_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeletePrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_precision_task_with_options(request, runtime)

    def delete_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScoreForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_score_for_api_with_options(request, runtime)

    def delete_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_config_with_options(request, runtime)

    def delete_sub_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubScoreForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteSubScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sub_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_score_for_api_with_options(request, runtime)

    def delete_task_assign_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_task_assign_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_task_assign_rule_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_warning_config_with_options(request, runtime)

    def edit_thesaurus_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditThesaurusForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.EditThesaurusForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_thesaurus_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_thesaurus_for_api_with_options(request, runtime)

    def get_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    def get_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_asr_vocab_with_options(request, runtime)

    def get_business_category_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessCategoryList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetBusinessCategoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_business_category_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_category_list_with_options(request, runtime)

    def get_customization_config_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizationConfigList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetCustomizationConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_customization_config_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customization_config_list_with_options(request, runtime)

    def get_hit_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHitResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetHitResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hit_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hit_result_with_options(request, runtime)

    def get_next_result_to_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNextResultToVerify',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetNextResultToVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_next_result_to_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_next_result_to_verify_with_options(request, runtime)

    def get_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_precision_task_with_options(request, runtime)

    def get_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_result_with_options(request, runtime)

    def get_result_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResultCallback',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def get_result_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_result_callback_with_options(request, runtime)

    def get_result_to_review_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResultToReview',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultToReviewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_result_to_review(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_result_to_review_with_options(request, runtime)

    def get_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    def get_rule_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rule_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_category_with_options(request, runtime)

    def get_rule_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleDetail',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rule_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    def get_score_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScoreInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetScoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_score_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_score_info_with_options(request, runtime)

    def get_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_config_with_options(request, runtime)

    def get_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyncResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sync_result_with_options(request, runtime)

    def get_thesaurus_by_synonym_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThesaurusBySynonymForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def get_thesaurus_by_synonym_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thesaurus_by_synonym_for_api_with_options(request, runtime)

    def handle_complaint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleComplaint',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.HandleComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    def handle_complaint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_complaint_with_options(request, runtime)

    def insert_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertScoreForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.InsertScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_score_for_api_with_options(request, runtime)

    def insert_sub_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSubScoreForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.InsertSubScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_sub_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_sub_score_for_api_with_options(request, runtime)

    def invalid_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvalidRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.InvalidRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def invalid_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invalid_rule_with_options(request, runtime)

    def list_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    def list_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_asr_vocab_with_options(request, runtime)

    def list_hot_words_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotWordsTasks',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListHotWordsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hot_words_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hot_words_tasks_with_options(request, runtime)

    def list_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_precision_task_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def list_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    def list_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_config_with_options(request, runtime)

    def list_task_assign_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskAssignRules',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListTaskAssignRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_task_assign_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_assign_rules_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_warning_config_with_options(request, runtime)

    def restart_asr_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartAsrTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.RestartAsrTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_asr_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_asr_task_with_options(request, runtime)

    def save_config_data_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveConfigDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SaveConfigDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    def save_config_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_config_data_set_with_options(request, runtime)

    def submit_complaint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitComplaint',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_complaint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_complaint_with_options(request, runtime)

    def submit_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_precision_task_with_options(request, runtime)

    def submit_quality_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitQualityCheckTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitQualityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_quality_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_quality_check_task_with_options(request, runtime)

    def submit_review_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitReviewInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitReviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_review_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_review_info_with_options(request, runtime)

    def sync_quality_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncQualityCheck',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SyncQualityCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_quality_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_quality_check_with_options(request, runtime)

    def update_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    def update_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_asr_vocab_with_options(request, runtime)

    def update_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    def update_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScoreForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def update_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_score_for_api_with_options(request, runtime)

    def update_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_config_with_options(request, runtime)

    def update_sub_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubScoreForApi',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSubScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sub_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sub_score_for_api_with_options(request, runtime)

    def update_sync_quality_check_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSyncQualityCheckData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sync_quality_check_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sync_quality_check_data_with_options(request, runtime)

    def update_task_assign_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_task_assign_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_task_assign_rule_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_user_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_config_with_options(request, runtime)

    def update_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_warning_config_with_options(request, runtime)

    def upload_audio_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadAudioData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadAudioDataResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_audio_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_audio_data_with_options(request, runtime)

    def upload_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_data_with_options(request, runtime)

    def upload_data_sync_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadDataSync',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataSyncResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_data_sync(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_data_sync_with_options(request, runtime)

    def upload_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_rule_with_options(request, runtime)

    def verify_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyFile',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.VerifyFileResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_file_with_options(request, runtime)

    def verify_sentence_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySentence',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.VerifySentenceResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_sentence(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_sentence_with_options(request, runtime)
