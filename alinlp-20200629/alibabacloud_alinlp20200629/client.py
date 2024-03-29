# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alinlp20200629 import models as alinlp_20200629_models
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
        self._endpoint = self.get_endpoint('alinlp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def a_dclock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADClock',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADClockResponse(),
            self.call_api(params, req, runtime)
        )

    def a_dclock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.a_dclock_with_options(request, runtime)

    def a_dmmuwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMMU',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMMUResponse(),
            self.call_api(params, req, runtime)
        )

    def a_dmmu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.a_dmmuwith_options(request, runtime)

    def a_dmini_cog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMiniCog',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMiniCogResponse(),
            self.call_api(params, req, runtime)
        )

    def a_dmini_cog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.a_dmini_cog_with_options(request, runtime)

    def a_dmini_cog_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ADMiniCogResult',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ADMiniCogResultResponse(),
            self.call_api(params, req, runtime)
        )

    def a_dmini_cog_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.a_dmini_cog_result_with_options(request, runtime)

    def delete_service_data_by_conditions_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.DeleteServiceDataByConditionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceDataByConditions',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.DeleteServiceDataByConditionsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_data_by_conditions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_data_by_conditions_with_options(request, runtime)

    def delete_service_data_by_ids_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.DeleteServiceDataByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        body = {}
        if not UtilClient.is_unset(request.ids_shrink):
            body['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceDataByIds',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.DeleteServiceDataByIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_data_by_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_data_by_ids_with_options(request, runtime)

    def get_brand_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBrandChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetBrandChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_brand_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_brand_ch_ecom_with_options(request, runtime)

    def get_cate_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCateChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCateChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cate_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cate_ch_ecom_with_options(request, runtime)

    def get_check_duplication_ch_medical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCheckDuplicationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetCheckDuplicationChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_check_duplication_ch_medical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_check_duplication_ch_medical_with_options(request, runtime)

    def get_diagnosis_ch_medical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDiagnosisChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDiagnosisChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_diagnosis_ch_medical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_ch_medical_with_options(request, runtime)

    def get_dp_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dp_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_ecom_with_options(request, runtime)

    def get_dp_ch_general_ctbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralCTB',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralCTBResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dp_ch_general_ctb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_ctbwith_options(request, runtime)

    def get_dp_ch_general_stanford_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDpChGeneralStanford',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetDpChGeneralStanfordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dp_ch_general_stanford(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dp_ch_general_stanford_with_options(request, runtime)

    def get_ec_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ec_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ec_ch_general_with_options(request, runtime)

    def get_ec_en_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEcEnGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEcEnGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ec_en_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ec_en_general_with_options(request, runtime)

    def get_embedding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.text_type):
            body['TextType'] = request.text_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmbedding',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetEmbeddingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_embedding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_embedding_with_options(request, runtime)

    def get_item_pub_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetItemPubChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetItemPubChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_item_pub_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_item_pub_ch_ecom_with_options(request, runtime)

    def get_keyword_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_version):
            body['ApiVersion'] = request.api_version
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_keyword_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_ch_ecom_with_options(request, runtime)

    def get_keyword_en_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordEnEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetKeywordEnEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_keyword_en_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_en_ecom_with_options(request, runtime)

    def get_medicine_ch_medical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory):
            body['Factory'] = request.factory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.specification):
            body['Specification'] = request.specification
        if not UtilClient.is_unset(request.unit):
            body['Unit'] = request.unit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMedicineChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetMedicineChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_medicine_ch_medical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_medicine_ch_medical_with_options(request, runtime)

    def get_ner_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lexer_id):
            body['LexerId'] = request.lexer_id
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ner_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_ecom_with_options(request, runtime)

    def get_ner_ch_medical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ner_ch_medical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ner_ch_medical_with_options(request, runtime)

    def get_ner_customized_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lexer_id):
            body['LexerId'] = request.lexer_id
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ner_customized_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_ch_ecom_with_options(request, runtime)

    def get_ner_customized_sea_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNerCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetNerCustomizedSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ner_customized_sea_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ner_customized_sea_ecom_with_options(request, runtime)

    def get_open_nluwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.examples):
            body['Examples'] = request.examples
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.sentence):
            body['Sentence'] = request.sentence
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenNLU',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOpenNLUResponse(),
            self.call_api(params, req, runtime)
        )

    def get_open_nlu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_open_nluwith_options(request, runtime)

    def get_open_nluhigh_recall_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.examples):
            body['Examples'] = request.examples
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.sentence):
            body['Sentence'] = request.sentence
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpenNLUHighRecall',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOpenNLUHighRecallResponse(),
            self.call_api(params, req, runtime)
        )

    def get_open_nluhigh_recall(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_open_nluhigh_recall_with_options(request, runtime)

    def get_operation_ch_medical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOperationChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetOperationChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_operation_ch_medical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_operation_ch_medical_with_options(request, runtime)

    def get_pos_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPosChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pos_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_ecom_with_options(request, runtime)

    def get_pos_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPosChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPosChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pos_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pos_ch_general_with_options(request, runtime)

    def get_price_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPriceChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetPriceChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_price_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_price_ch_ecom_with_options(request, runtime)

    def get_ssetest_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSSETest',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSSETestResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ssetest(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ssetest_with_options(request, runtime)

    def get_sa_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sa_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sa_ch_general_with_options(request, runtime)

    def get_sa_sea_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSaSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSaSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sa_sea_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sa_sea_ecom_with_options(request, runtime)

    def get_service_data_import_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.GetServiceDataImportStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_import_ids):
            request.data_import_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_import_ids, 'DataImportIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_import_ids_shrink):
            body['DataImportIds'] = request.data_import_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceDataImportStatus',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetServiceDataImportStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_data_import_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_data_import_status_with_options(request, runtime)

    def get_similarity_ch_medical_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSimilarityChMedical',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSimilarityChMedicalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_similarity_ch_medical(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_similarity_ch_medical_with_options(request, runtime)

    def get_summary_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSummaryChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetSummaryChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_summary_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_summary_ch_ecom_with_options(request, runtime)

    def get_table_qaservice_info_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTableQAServiceInfoById',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTableQAServiceInfoByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_qaservice_info_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_table_qaservice_info_by_id_with_options(request, runtime)

    def get_tc_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTcChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tc_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_ecom_with_options(request, runtime)

    def get_tc_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTcChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTcChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_tc_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_tc_ch_general_with_options(request, runtime)

    def get_ts_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.origin_q):
            body['OriginQ'] = request.origin_q
        if not UtilClient.is_unset(request.origin_t):
            body['OriginT'] = request.origin_t
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTsChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetTsChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ts_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ts_ch_ecom_with_options(request, runtime)

    def get_user_upload_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserUploadSign',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetUserUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_upload_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_upload_sign_with_options(request, runtime)

    def get_we_ch_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_we_ch_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_comment_with_options(request, runtime)

    def get_we_ch_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_we_ch_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_ecom_with_options(request, runtime)

    def get_we_ch_entertainment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChEntertainmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_we_ch_entertainment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_entertainment_with_options(request, runtime)

    def get_we_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_we_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_general_with_options(request, runtime)

    def get_we_ch_search_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWeChSearch',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWeChSearchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_we_ch_search(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_we_ch_search_with_options(request, runtime)

    def get_ws_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_ch_general_with_options(request, runtime)

    def get_ws_customized_ch_ecom_comment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomComment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomCommentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_comment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_comment_with_options(request, runtime)

    def get_ws_customized_ch_ecom_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomContent',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomContentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_content_with_options(request, runtime)

    def get_ws_customized_ch_ecom_title_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEcomTitle',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEcomTitleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_ch_ecom_title(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_ecom_title_with_options(request, runtime)

    def get_ws_customized_ch_entertainment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChEntertainment',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChEntertainmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_ch_entertainment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_entertainment_with_options(request, runtime)

    def get_ws_customized_ch_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_ch_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_general_with_options(request, runtime)

    def get_ws_customized_ch_o2owith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.out_type):
            body['OutType'] = request.out_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.tokenizer_id):
            body['TokenizerId'] = request.tokenizer_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedChO2O',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedChO2OResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_ch_o2o(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_ch_o2owith_options(request, runtime)

    def get_ws_customized_sea_ecom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaEcom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaEcomResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_sea_ecom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_ecom_with_options(request, runtime)

    def get_ws_customized_sea_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWsCustomizedSeaGeneral',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.GetWsCustomizedSeaGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ws_customized_sea_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ws_customized_sea_general_with_options(request, runtime)

    def import_service_data_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.ImportServiceDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition):
            request.partition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition, 'Partition', 'json')
        body = {}
        if not UtilClient.is_unset(request.partition_shrink):
            body['Partition'] = request.partition_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.sub_path):
            body['SubPath'] = request.sub_path
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportServiceData',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ImportServiceDataResponse(),
            self.call_api(params, req, runtime)
        )

    def import_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_service_data_with_options(request, runtime)

    def import_service_data_v2with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.ImportServiceDataV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportServiceDataV2',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.ImportServiceDataV2Response(),
            self.call_api(params, req, runtime)
        )

    def import_service_data_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_service_data_v2with_options(request, runtime)

    def insert_custom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_id):
            body['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.custom_file_name):
            body['CustomFileName'] = request.custom_file_name
        if not UtilClient.is_unset(request.custom_url):
            body['CustomUrl'] = request.custom_url
        if not UtilClient.is_unset(request.reg_file_name):
            body['RegFileName'] = request.reg_file_name
        if not UtilClient.is_unset(request.reg_url):
            body['RegUrl'] = request.reg_url
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertCustom',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.InsertCustomResponse(),
            self.call_api(params, req, runtime)
        )

    def insert_custom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_custom_with_options(request, runtime)

    def open_alinlp_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenAlinlpService',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.OpenAlinlpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_alinlp_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_alinlp_service_with_options(runtime)

    def post_isconv_rewriter_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostISConvRewriterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.debug):
            body['Debug'] = request.debug
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostISConvRewriter',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostISConvRewriterResponse(),
            self.call_api(params, req, runtime)
        )

    def post_isconv_rewriter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_isconv_rewriter_with_options(request, runtime)

    def post_isretrieve_router_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostISRetrieveRouterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        body = {}
        if not UtilClient.is_unset(request.algorithm):
            body['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostISRetrieveRouter',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostISRetrieveRouterResponse(),
            self.call_api(params, req, runtime)
        )

    def post_isretrieve_router(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_isretrieve_router_with_options(request, runtime)

    def post_msconv_search_token_generated_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PostMSConvSearchTokenGenerated',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSConvSearchTokenGeneratedResponse(),
            self.call_api(params, req, runtime)
        )

    def post_msconv_search_token_generated(self):
        runtime = util_models.RuntimeOptions()
        return self.post_msconv_search_token_generated_with_options(runtime)

    def post_msdata_processing_count_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSDataProcessingCountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_ids):
            request.data_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_ids, 'DataIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_ids_shrink):
            body['DataIds'] = request.data_ids_shrink
        if not UtilClient.is_unset(request.data_import_id):
            body['DataImportId'] = request.data_import_id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSDataProcessingCount',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSDataProcessingCountResponse(),
            self.call_api(params, req, runtime)
        )

    def post_msdata_processing_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_msdata_processing_count_with_options(request, runtime)

    def post_mssearch_enhance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSSearchEnhanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_config_info):
            request.custom_config_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_config_info, 'CustomConfigInfo', 'json')
        if not UtilClient.is_unset(tmp_req.fields):
            request.fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fields, 'Fields', 'json')
        if not UtilClient.is_unset(tmp_req.rank_model_info):
            request.rank_model_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rank_model_info, 'RankModelInfo', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.custom_config_info_shrink):
            body['CustomConfigInfo'] = request.custom_config_info_shrink
        if not UtilClient.is_unset(request.debug):
            body['Debug'] = request.debug
        if not UtilClient.is_unset(request.fields_shrink):
            body['Fields'] = request.fields_shrink
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.queries):
            body['Queries'] = request.queries
        if not UtilClient.is_unset(request.rank_model_info_shrink):
            body['RankModelInfo'] = request.rank_model_info_shrink
        if not UtilClient.is_unset(request.rows):
            body['Rows'] = request.rows
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uq):
            body['Uq'] = request.uq
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSSearchEnhance',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSSearchEnhanceResponse(),
            self.call_api(params, req, runtime)
        )

    def post_mssearch_enhance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_mssearch_enhance_with_options(request, runtime)

    def post_msservice_data_import_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.PostMSServiceDataImportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.documents):
            request.documents_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.documents, 'Documents', 'json')
        body = {}
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.documents_shrink):
            body['Documents'] = request.documents_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PostMSServiceDataImport',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.PostMSServiceDataImportResponse(),
            self.call_api(params, req, runtime)
        )

    def post_msservice_data_import(self, request):
        runtime = util_models.RuntimeOptions()
        return self.post_msservice_data_import_with_options(request, runtime)

    def request_table_qawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestTableQA',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.RequestTableQAResponse(),
            self.call_api(params, req, runtime)
        )

    def request_table_qa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_table_qawith_options(request, runtime)

    def request_table_qaonline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bot_id):
            body['BotId'] = request.bot_id
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.question):
            body['Question'] = request.question
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestTableQAOnline',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.RequestTableQAOnlineResponse(),
            self.call_api(params, req, runtime)
        )

    def request_table_qaonline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.request_table_qaonline_with_options(request, runtime)

    def update_service_data_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alinlp_20200629_models.UpdateServiceDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        body = {}
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceData',
            version='2020-06-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alinlp_20200629_models.UpdateServiceDataResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_service_data_with_options(request, runtime)
