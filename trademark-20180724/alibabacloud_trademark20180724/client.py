# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_trademark20180724 import models as trademark_20180724_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('trademark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def query_trade_produce_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceListResponse(),
            self.do_rpcrequest('QueryTradeProduceList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_produce_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_produce_list_with_options(request, runtime)

    def query_trademark_monitor_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorResultsResponse(),
            self.do_rpcrequest('QueryTrademarkMonitorResults', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trademark_monitor_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_monitor_results_with_options(request, runtime)

    def cancel_trade_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CancelTradeOrderResponse(),
            self.do_rpcrequest('CancelTradeOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_trade_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_trade_order_with_options(request, runtime)

    def delete_tm_monitor_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTmMonitorRuleResponse(),
            self.do_rpcrequest('DeleteTmMonitorRule', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tm_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tm_monitor_rule_with_options(request, runtime)

    def upload_notary_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadNotaryDataResponse(),
            self.do_rpcrequest('UploadNotaryData', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_notary_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_notary_data_with_options(request, runtime)

    def copy_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CopyApplicantResponse(),
            self.do_rpcrequest('CopyApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_applicant_with_options(request, runtime)

    def partner_update_trademark_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.PartnerUpdateTrademarkNameResponse(),
            self.do_rpcrequest('PartnerUpdateTrademarkName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def partner_update_trademark_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.partner_update_trademark_name_with_options(request, runtime)

    def query_intention_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionDetailResponse(),
            self.do_rpcrequest('QueryIntentionDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intention_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_detail_with_options(request, runtime)

    def query_intention_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionPriceResponse(),
            self.do_rpcrequest('QueryIntentionPrice', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intention_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_price_with_options(request, runtime)

    def query_official_file_custom_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOfficialFileCustomListResponse(),
            self.do_rpcrequest('QueryOfficialFileCustomList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_official_file_custom_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_official_file_custom_list_with_options(request, runtime)

    def check_trademark_icon_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkIconResponse(),
            self.do_rpcrequest('CheckTrademarkIcon', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_trademark_icon(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_icon_with_options(request, runtime)

    def query_supplement_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QuerySupplementDetailResponse(),
            self.do_rpcrequest('QuerySupplementDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_supplement_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_supplement_detail_with_options(request, runtime)

    def upload_trademark_on_sale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UploadTrademarkOnSaleResponse(),
            self.do_rpcrequest('UploadTrademarkOnSale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_trademark_on_sale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_trademark_on_sale_with_options(request, runtime)

    def apply_notary_post_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ApplyNotaryPostResponse(),
            self.do_rpcrequest('ApplyNotaryPost', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_notary_post(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_notary_post_with_options(request, runtime)

    def query_trade_mark_applications_by_intention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsByIntentionResponse(),
            self.do_rpcrequest('QueryTradeMarkApplicationsByIntention', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_applications_by_intention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_applications_by_intention_with_options(request, runtime)

    def save_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveExtensionAttributeResponse(),
            self.do_rpcrequest('SaveExtensionAttribute', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_extension_attribute_with_options(request, runtime)

    def accept_partner_notification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.AcceptPartnerNotificationResponse(),
            self.do_rpcrequest('AcceptPartnerNotification', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_partner_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_partner_notification_with_options(request, runtime)

    def submit_supplement_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_oss_key_list):
            request.upload_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.upload_oss_key_list, 'UploadOssKeyList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitSupplementResponse(),
            self.do_rpcrequest('SubmitSupplement', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_supplement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_supplement_with_options(request, runtime)

    def force_upload_trademark_onsale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ForceUploadTrademarkOnsaleResponse(),
            self.do_rpcrequest('ForceUploadTrademarkOnsale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def force_upload_trademark_onsale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.force_upload_trademark_onsale_with_options(request, runtime)

    def bind_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.BindMaterialResponse(),
            self.do_rpcrequest('BindMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_material_with_options(request, runtime)

    def get_default_principal_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalResponse(),
            self.do_rpcrequest('GetDefaultPrincipal', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_principal(self):
        runtime = util_models.RuntimeOptions()
        return self.get_default_principal_with_options(runtime)

    def query_communication_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCommunicationLogsResponse(),
            self.do_rpcrequest('QueryCommunicationLogs', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_communication_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_communication_logs_with_options(request, runtime)

    def generate_qr_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateQrCodeResponse(),
            self.do_rpcrequest('GenerateQrCode', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_qr_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_qr_code_with_options(request, runtime)

    def confirm_dissent_original_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmDissentOriginalResponse(),
            self.do_rpcrequest('ConfirmDissentOriginal', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_dissent_original(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_dissent_original_with_options(request, runtime)

    def convert_image_to_gray_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConvertImageToGrayResponse(),
            self.do_rpcrequest('ConvertImageToGray', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_image_to_gray(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_image_to_gray_with_options(request, runtime)

    def query_intention_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryIntentionListResponse(),
            self.do_rpcrequest('QueryIntentionList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intention_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intention_list_with_options(request, runtime)

    def get_authorization_letter_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetAuthorizationLetterVersionResponse(),
            self.do_rpcrequest('GetAuthorizationLetterVersion', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authorization_letter_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_authorization_letter_version_with_options(request, runtime)

    def query_trademark_price_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.QueryTrademarkPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_data):
            request.order_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_data, 'OrderData', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkPriceResponse(),
            self.do_rpcrequest('QueryTrademarkPrice', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trademark_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_price_with_options(request, runtime)

    def insert_tm_monitor_rule_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.InsertTmMonitorRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.classification):
            request.classification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.classification, 'Classification', 'json')
        if not UtilClient.is_unset(tmp_req.notify_status):
            request.notify_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notify_status, 'NotifyStatus', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTmMonitorRuleResponse(),
            self.do_rpcrequest('InsertTmMonitorRule', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_tm_monitor_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_tm_monitor_rule_with_options(request, runtime)

    def query_trademark_monitor_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTrademarkMonitorRulesResponse(),
            self.do_rpcrequest('QueryTrademarkMonitorRules', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trademark_monitor_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trademark_monitor_rules_with_options(request, runtime)

    def deny_supplement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DenySupplementResponse(),
            self.do_rpcrequest('DenySupplement', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deny_supplement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deny_supplement_with_options(request, runtime)

    def query_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialResponse(),
            self.do_rpcrequest('QueryMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_material_with_options(request, runtime)

    def create_trademark_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateTrademarkOrderResponse(),
            self.do_rpcrequest('CreateTrademarkOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_trademark_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_trademark_order_with_options(request, runtime)

    def query_material_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMaterialListResponse(),
            self.do_rpcrequest('QueryMaterialList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_material_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_material_list_with_options(request, runtime)

    def check_trademark_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckTrademarkOrderResponse(),
            self.do_rpcrequest('CheckTrademarkOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_trademark_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_trademark_order_with_options(request, runtime)

    def query_trade_mark_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationsResponse(),
            self.do_rpcrequest('QueryTradeMarkApplications', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_applications_with_options(request, runtime)

    def update_applicant_contacter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateApplicantContacterResponse(),
            self.do_rpcrequest('UpdateApplicantContacter', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_applicant_contacter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_applicant_contacter_with_options(request, runtime)

    def save_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskResponse(),
            self.do_rpcrequest('SaveTask', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_with_options(request, runtime)

    def submit_trademark_application_complaint_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SubmitTrademarkApplicationComplaintShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SubmitTrademarkApplicationComplaintResponse(),
            self.do_rpcrequest('SubmitTrademarkApplicationComplaint', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_trademark_application_complaint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_trademark_application_complaint_with_options(request, runtime)

    def write_intention_communication_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteIntentionCommunicationLogResponse(),
            self.do_rpcrequest('WriteIntentionCommunicationLog', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def write_intention_communication_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.write_intention_communication_log_with_options(request, runtime)

    def save_task_for_official_file_custom_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTaskForOfficialFileCustomResponse(),
            self.do_rpcrequest('SaveTaskForOfficialFileCustom', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_task_for_official_file_custom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_official_file_custom_with_options(request, runtime)

    def descirbe_combine_trademark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DescirbeCombineTrademarkResponse(),
            self.do_rpcrequest('DescirbeCombineTrademark', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def descirbe_combine_trademark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.descirbe_combine_trademark_with_options(request, runtime)

    def get_notary_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetNotaryOrderResponse(),
            self.do_rpcrequest('GetNotaryOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_notary_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_notary_order_with_options(request, runtime)

    def confirm_additional_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmAdditionalMaterialResponse(),
            self.do_rpcrequest('ConfirmAdditionalMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_additional_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_additional_material_with_options(request, runtime)

    def insert_renew_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertRenewInfoResponse(),
            self.do_rpcrequest('InsertRenewInfo', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_renew_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_renew_info_with_options(request, runtime)

    def query_credentials_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryCredentialsInfoResponse(),
            self.do_rpcrequest('QueryCredentialsInfo', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_credentials_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_credentials_info_with_options(request, runtime)

    def search_tm_onsales_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SearchTmOnsalesResponse(),
            self.do_rpcrequest('SearchTmOnsales', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_tm_onsales(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_tm_onsales_with_options(request, runtime)

    def generate_upload_file_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GenerateUploadFilePolicyResponse(),
            self.do_rpcrequest('GenerateUploadFilePolicy', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_upload_file_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_file_policy_with_options(request, runtime)

    def delete_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteMaterialResponse(),
            self.do_rpcrequest('DeleteMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_material_with_options(request, runtime)

    def write_communication_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.WriteCommunicationLogResponse(),
            self.do_rpcrequest('WriteCommunicationLog', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def write_communication_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.write_communication_log_with_options(request, runtime)

    def insert_trade_intention_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertTradeIntentionUserResponse(),
            self.do_rpcrequest('InsertTradeIntentionUser', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_trade_intention_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_trade_intention_user_with_options(request, runtime)

    def query_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryExtensionAttributeResponse(),
            self.do_rpcrequest('QueryExtensionAttribute', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_extension_attribute_with_options(request, runtime)

    def update_trademark_onsale_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkOnsaleResponse(),
            self.do_rpcrequest('UpdateTrademarkOnsale', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trademark_onsale(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_trademark_onsale_with_options(request, runtime)

    def query_trade_produce_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeProduceDetailResponse(),
            self.do_rpcrequest('QueryTradeProduceDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_produce_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_produce_detail_with_options(request, runtime)

    def query_qr_code_upload_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryQrCodeUploadStatusResponse(),
            self.do_rpcrequest('QueryQrCodeUploadStatus', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_qr_code_upload_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_qr_code_upload_status_with_options(request, runtime)

    def reject_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RejectApplicantResponse(),
            self.do_rpcrequest('RejectApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reject_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reject_applicant_with_options(request, runtime)

    def query_trade_intention_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeIntentionUserListResponse(),
            self.do_rpcrequest('QueryTradeIntentionUserList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_intention_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_intention_user_list_with_options(request, runtime)

    def store_material_temporarily_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.StoreMaterialTemporarilyResponse(),
            self.do_rpcrequest('StoreMaterialTemporarily', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def store_material_temporarily(self, request):
        runtime = util_models.RuntimeOptions()
        return self.store_material_temporarily_with_options(request, runtime)

    def refuse_additional_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseAdditionalMaterialResponse(),
            self.do_rpcrequest('RefuseAdditionalMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refuse_additional_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refuse_additional_material_with_options(request, runtime)

    def list_notary_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryInfosResponse(),
            self.do_rpcrequest('ListNotaryInfos', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_notary_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notary_infos_with_options(request, runtime)

    def get_default_principal_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.GetDefaultPrincipalNameResponse(),
            self.do_rpcrequest('GetDefaultPrincipalName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_principal_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_default_principal_name_with_options(request, runtime)

    def query_trade_mark_application_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationDetailResponse(),
            self.do_rpcrequest('QueryTradeMarkApplicationDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_application_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_application_detail_with_options(request, runtime)

    def save_classification_conditions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveClassificationConditionsResponse(),
            self.do_rpcrequest('SaveClassificationConditions', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_classification_conditions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_classification_conditions_with_options(request, runtime)

    def fill_logistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.FillLogisticsResponse(),
            self.do_rpcrequest('FillLogistics', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fill_logistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fill_logistics_with_options(request, runtime)

    def update_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateMaterialResponse(),
            self.do_rpcrequest('UpdateMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_material_with_options(request, runtime)

    def query_trade_mark_application_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTradeMarkApplicationLogsResponse(),
            self.do_rpcrequest('QueryTradeMarkApplicationLogs', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trade_mark_application_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_trade_mark_application_logs_with_options(request, runtime)

    def refund_produce_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefundProduceResponse(),
            self.do_rpcrequest('RefundProduce', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_produce(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_produce_with_options(request, runtime)

    def sync_trademark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SyncTrademarkResponse(),
            self.do_rpcrequest('SyncTrademark', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_trademark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_trademark_with_options(request, runtime)

    def combine_loa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CombineLoaResponse(),
            self.do_rpcrequest('CombineLoa', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def combine_loa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.combine_loa_with_options(request, runtime)

    def filter_unavailable_codes_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.FilterUnavailableCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.codes):
            request.codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.codes, 'Codes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.FilterUnavailableCodesResponse(),
            self.do_rpcrequest('FilterUnavailableCodes', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def filter_unavailable_codes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.filter_unavailable_codes_with_options(request, runtime)

    def insert_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.InsertMaterialResponse(),
            self.do_rpcrequest('InsertMaterial', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def insert_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.insert_material_with_options(request, runtime)

    def save_trade_mark_review_material_detail_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = trademark_20180724_models.SaveTradeMarkReviewMaterialDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_oss_key_list):
            request.additional_oss_key_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_oss_key_list, 'AdditionalOssKeyList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.SaveTradeMarkReviewMaterialDetailResponse(),
            self.do_rpcrequest('SaveTradeMarkReviewMaterialDetail', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_trade_mark_review_material_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_trade_mark_review_material_detail_with_options(request, runtime)

    def query_monitor_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryMonitorKeywordsResponse(),
            self.do_rpcrequest('QueryMonitorKeywords', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_monitor_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monitor_keywords_with_options(request, runtime)

    def query_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryTaskListResponse(),
            self.do_rpcrequest('QueryTaskList', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    def update_trademark_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateTrademarkNameResponse(),
            self.do_rpcrequest('UpdateTrademarkName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trademark_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_trademark_name_with_options(request, runtime)

    def check_loa_fill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CheckLoaFillResponse(),
            self.do_rpcrequest('CheckLoaFill', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_loa_fill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_loa_fill_with_options(request, runtime)

    def confirm_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ConfirmApplicantResponse(),
            self.do_rpcrequest('ConfirmApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_applicant_with_options(request, runtime)

    def create_intention_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderResponse(),
            self.do_rpcrequest('CreateIntentionOrder', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intention_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intention_order_with_options(request, runtime)

    def query_oss_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.QueryOssResourcesResponse(),
            self.do_rpcrequest('QueryOssResources', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_oss_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_oss_resources_with_options(request, runtime)

    def refuse_applicant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.RefuseApplicantResponse(),
            self.do_rpcrequest('RefuseApplicant', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refuse_applicant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refuse_applicant_with_options(request, runtime)

    def create_intention_order_generating_pay_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.CreateIntentionOrderGeneratingPayResponse(),
            self.do_rpcrequest('CreateIntentionOrderGeneratingPay', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intention_order_generating_pay(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intention_order_generating_pay_with_options(request, runtime)

    def list_notary_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.ListNotaryOrdersResponse(),
            self.do_rpcrequest('ListNotaryOrders', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_notary_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notary_orders_with_options(request, runtime)

    def get_support_principal_name_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            trademark_20180724_models.GetSupportPrincipalNameResponse(),
            self.do_rpcrequest('GetSupportPrincipalName', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_support_principal_name(self):
        runtime = util_models.RuntimeOptions()
        return self.get_support_principal_name_with_options(runtime)

    def start_notary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.StartNotaryResponse(),
            self.do_rpcrequest('StartNotary', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_notary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_notary_with_options(request, runtime)

    def update_send_material_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.UpdateSendMaterialNumResponse(),
            self.do_rpcrequest('UpdateSendMaterialNum', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_send_material_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_send_material_num_with_options(request, runtime)

    def delete_trademark_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            trademark_20180724_models.DeleteTrademarkApplicationResponse(),
            self.do_rpcrequest('DeleteTrademarkApplication', '2018-07-24', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trademark_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_trademark_application_with_options(request, runtime)
