# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qualitycheck20190115 import models as qualitycheck_20190115_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddBusinessCategoryResponse().from_map(
            self.do_rpcrequest('AddBusinessCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_business_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_business_category_with_options(request, runtime)

    def add_rule_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddRuleCategoryResponse().from_map(
            self.do_rpcrequest('AddRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_rule_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_rule_category_with_options(request, runtime)

    def add_thesaurus_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddThesaurusForApiResponse().from_map(
            self.do_rpcrequest('AddThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_thesaurus_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_thesaurus_for_api_with_options(request, runtime)

    def add_upload_data_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddUploadDataSetResponse().from_map(
            self.do_rpcrequest('AddUploadDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_upload_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_upload_data_set_with_options(request, runtime)

    def assign_reviewer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AssignReviewerResponse().from_map(
            self.do_rpcrequest('AssignReviewer', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_reviewer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_reviewer_with_options(request, runtime)

    def config_data_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ConfigDataSetResponse().from_map(
            self.do_rpcrequest('ConfigDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_data_set_with_options(request, runtime)

    def create_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateAsrVocabResponse().from_map(
            self.do_rpcrequest('CreateAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_asr_vocab_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateRuleResponse().from_map(
            self.do_rpcrequest('CreateRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('CreateSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_config_with_options(request, runtime)

    def create_task_assign_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateTaskAssignRuleResponse().from_map(
            self.do_rpcrequest('CreateTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_task_assign_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_task_assign_rule_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateWarningConfigResponse().from_map(
            self.do_rpcrequest('CreateWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_warning_config_with_options(request, runtime)

    def delete_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteAsrVocabResponse().from_map(
            self.do_rpcrequest('DeleteAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_asr_vocab_with_options(request, runtime)

    def delete_business_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteBusinessCategoryResponse().from_map(
            self.do_rpcrequest('DeleteBusinessCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_business_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_business_category_with_options(request, runtime)

    def delete_customization_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteCustomizationConfigResponse().from_map(
            self.do_rpcrequest('DeleteCustomizationConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_customization_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_customization_config_with_options(request, runtime)

    def delete_data_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteDataSetResponse().from_map(
            self.do_rpcrequest('DeleteDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    def delete_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeletePrecisionTaskResponse().from_map(
            self.do_rpcrequest('DeletePrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_precision_task_with_options(request, runtime)

    def delete_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteScoreForApiResponse().from_map(
            self.do_rpcrequest('DeleteScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_score_for_api_with_options(request, runtime)

    def delete_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('DeleteSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_config_with_options(request, runtime)

    def delete_sub_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteSubScoreForApiResponse().from_map(
            self.do_rpcrequest('DeleteSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sub_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_score_for_api_with_options(request, runtime)

    def delete_task_assign_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteTaskAssignRuleResponse().from_map(
            self.do_rpcrequest('DeleteTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_task_assign_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_task_assign_rule_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteWarningConfigResponse().from_map(
            self.do_rpcrequest('DeleteWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_warning_config_with_options(request, runtime)

    def del_rule_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DelRuleCategoryResponse().from_map(
            self.do_rpcrequest('DelRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def del_rule_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_rule_category_with_options(request, runtime)

    def del_thesaurus_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DelThesaurusForApiResponse().from_map(
            self.do_rpcrequest('DelThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def del_thesaurus_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_thesaurus_for_api_with_options(request, runtime)

    def edit_thesaurus_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.EditThesaurusForApiResponse().from_map(
            self.do_rpcrequest('EditThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_thesaurus_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_thesaurus_for_api_with_options(request, runtime)

    def get_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetAsrVocabResponse().from_map(
            self.do_rpcrequest('GetAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_asr_vocab_with_options(request, runtime)

    def get_business_category_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetBusinessCategoryListResponse().from_map(
            self.do_rpcrequest('GetBusinessCategoryList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_business_category_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_business_category_list_with_options(request, runtime)

    def get_customization_config_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetCustomizationConfigListResponse().from_map(
            self.do_rpcrequest('GetCustomizationConfigList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_customization_config_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_customization_config_list_with_options(request, runtime)

    def get_hit_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetHitResultResponse().from_map(
            self.do_rpcrequest('GetHitResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hit_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_hit_result_with_options(request, runtime)

    def get_next_result_to_verify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetNextResultToVerifyResponse().from_map(
            self.do_rpcrequest('GetNextResultToVerify', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_next_result_to_verify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_next_result_to_verify_with_options(request, runtime)

    def get_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetPrecisionTaskResponse().from_map(
            self.do_rpcrequest('GetPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_precision_task_with_options(request, runtime)

    def get_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultResponse().from_map(
            self.do_rpcrequest('GetResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_result_with_options(request, runtime)

    def get_result_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultCallbackResponse().from_map(
            self.do_rpcrequest('GetResultCallback', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_result_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_result_callback_with_options(request, runtime)

    def get_result_to_review_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultToReviewResponse().from_map(
            self.do_rpcrequest('GetResultToReview', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_result_to_review(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_result_to_review_with_options(request, runtime)

    def get_review_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetReviewInfoResponse().from_map(
            self.do_rpcrequest('GetReviewInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_review_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_review_info_with_options(request, runtime)

    def get_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleResponse().from_map(
            self.do_rpcrequest('GetRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    def get_rule_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleCategoryResponse().from_map(
            self.do_rpcrequest('GetRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_category_with_options(request, runtime)

    def get_rule_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleDetailResponse().from_map(
            self.do_rpcrequest('GetRuleDetail', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    def get_rule_dimension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleDimensionResponse().from_map(
            self.do_rpcrequest('GetRuleDimension', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_dimension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_dimension_with_options(request, runtime)

    def get_score_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetScoreInfoResponse().from_map(
            self.do_rpcrequest('GetScoreInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_score_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_score_info_with_options(request, runtime)

    def get_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('GetSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_config_with_options(request, runtime)

    def get_sync_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetSyncResultResponse().from_map(
            self.do_rpcrequest('GetSyncResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sync_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sync_result_with_options(request, runtime)

    def get_task_file_result_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetTaskFileResultListResponse().from_map(
            self.do_rpcrequest('GetTaskFileResultList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_file_result_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_file_result_list_with_options(request, runtime)

    def get_task_rule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetTaskRuleListResponse().from_map(
            self.do_rpcrequest('GetTaskRuleList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_rule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_rule_list_with_options(request, runtime)

    def get_thesaurus_by_synonym_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse().from_map(
            self.do_rpcrequest('GetThesaurusBySynonymForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_thesaurus_by_synonym_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thesaurus_by_synonym_for_api_with_options(request, runtime)

    def handle_complaint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.HandleComplaintResponse().from_map(
            self.do_rpcrequest('HandleComplaint', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def handle_complaint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.handle_complaint_with_options(request, runtime)

    def insert_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InsertScoreForApiResponse().from_map(
            self.do_rpcrequest('InsertScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_score_for_api_with_options(request, runtime)

    def insert_sub_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InsertSubScoreForApiResponse().from_map(
            self.do_rpcrequest('InsertSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_sub_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_sub_score_for_api_with_options(request, runtime)

    def invalid_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InvalidRuleResponse().from_map(
            self.do_rpcrequest('InvalidRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invalid_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invalid_rule_with_options(request, runtime)

    def list_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListAsrVocabResponse().from_map(
            self.do_rpcrequest('ListAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_asr_vocab_with_options(request, runtime)

    def list_data_set_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListDataSetTaskResponse().from_map(
            self.do_rpcrequest('ListDataSetTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_set_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_set_task_with_options(request, runtime)

    def list_hot_words_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListHotWordsTasksResponse().from_map(
            self.do_rpcrequest('ListHotWordsTasks', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hot_words_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hot_words_tasks_with_options(request, runtime)

    def list_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListPrecisionTaskResponse().from_map(
            self.do_rpcrequest('ListPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_precision_task_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListRolesResponse().from_map(
            self.do_rpcrequest('ListRoles', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def list_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListRulesResponse().from_map(
            self.do_rpcrequest('ListRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    def list_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('ListSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_config_with_options(request, runtime)

    def list_task_assign_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListTaskAssignRulesResponse().from_map(
            self.do_rpcrequest('ListTaskAssignRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task_assign_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_assign_rules_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def list_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListWarningConfigResponse().from_map(
            self.do_rpcrequest('ListWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_warning_config_with_options(request, runtime)

    def remove_and_get_task_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse().from_map(
            self.do_rpcrequest('RemoveAndGetTaskRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_and_get_task_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_and_get_task_rules_with_options(request, runtime)

    def restart_asr_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.RestartAsrTaskResponse().from_map(
            self.do_rpcrequest('RestartAsrTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_asr_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_asr_task_with_options(request, runtime)

    def review_single_result_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ReviewSingleResultByIdResponse().from_map(
            self.do_rpcrequest('ReviewSingleResultById', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def review_single_result_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.review_single_result_by_id_with_options(request, runtime)

    def save_config_data_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SaveConfigDataSetResponse().from_map(
            self.do_rpcrequest('SaveConfigDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_config_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_config_data_set_with_options(request, runtime)

    def submit_complaint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitComplaintResponse().from_map(
            self.do_rpcrequest('SubmitComplaint', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_complaint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_complaint_with_options(request, runtime)

    def submit_customization_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitCustomizationConfigResponse().from_map(
            self.do_rpcrequest('SubmitCustomizationConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_customization_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_customization_config_with_options(request, runtime)

    def submit_precision_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitPrecisionTaskResponse().from_map(
            self.do_rpcrequest('SubmitPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_precision_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_precision_task_with_options(request, runtime)

    def submit_quality_check_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitQualityCheckTaskResponse().from_map(
            self.do_rpcrequest('SubmitQualityCheckTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_quality_check_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_quality_check_task_with_options(request, runtime)

    def submit_review_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitReviewInfoResponse().from_map(
            self.do_rpcrequest('SubmitReviewInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_review_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_review_info_with_options(request, runtime)

    def sync_quality_check_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SyncQualityCheckResponse().from_map(
            self.do_rpcrequest('SyncQualityCheck', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_quality_check(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_quality_check_with_options(request, runtime)

    def test_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.TestRuleResponse().from_map(
            self.do_rpcrequest('TestRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_rule_with_options(request, runtime)

    def update_asr_vocab_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateAsrVocabResponse().from_map(
            self.do_rpcrequest('UpdateAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_asr_vocab(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_asr_vocab_with_options(request, runtime)

    def update_on_purchase_success_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse().from_map(
            self.do_rpcrequest('UpdateOnPurchaseSuccess', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_on_purchase_success(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_on_purchase_success_with_options(request, runtime)

    def update_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateRuleResponse().from_map(
            self.do_rpcrequest('UpdateRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    def update_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateScoreForApiResponse().from_map(
            self.do_rpcrequest('UpdateScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_score_for_api_with_options(request, runtime)

    def update_skill_group_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('UpdateSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_skill_group_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_config_with_options(request, runtime)

    def update_sub_score_for_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSubScoreForApiResponse().from_map(
            self.do_rpcrequest('UpdateSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sub_score_for_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sub_score_for_api_with_options(request, runtime)

    def update_sync_quality_check_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse().from_map(
            self.do_rpcrequest('UpdateSyncQualityCheckData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sync_quality_check_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sync_quality_check_data_with_options(request, runtime)

    def update_task_assign_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateTaskAssignRuleResponse().from_map(
            self.do_rpcrequest('UpdateTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_task_assign_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_task_assign_rule_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_user_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateUserConfigResponse().from_map(
            self.do_rpcrequest('UpdateUserConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_config_with_options(request, runtime)

    def update_warning_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateWarningConfigResponse().from_map(
            self.do_rpcrequest('UpdateWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_warning_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_warning_config_with_options(request, runtime)

    def upload_audio_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadAudioDataResponse().from_map(
            self.do_rpcrequest('UploadAudioData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_audio_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_audio_data_with_options(request, runtime)

    def upload_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadDataResponse().from_map(
            self.do_rpcrequest('UploadData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_data_with_options(request, runtime)

    def upload_data_sync_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadDataSyncResponse().from_map(
            self.do_rpcrequest('UploadDataSync', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_data_sync(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_data_sync_with_options(request, runtime)

    def upload_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadRuleResponse().from_map(
            self.do_rpcrequest('UploadRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_rule_with_options(request, runtime)

    def verify_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.VerifyFileResponse().from_map(
            self.do_rpcrequest('VerifyFile', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_file_with_options(request, runtime)

    def verify_sentence_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.VerifySentenceResponse().from_map(
            self.do_rpcrequest('VerifySentence', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_sentence(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_sentence_with_options(request, runtime)
