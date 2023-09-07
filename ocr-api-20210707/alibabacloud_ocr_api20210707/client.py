# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
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
        self._endpoint = self.get_endpoint('ocr-api', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def recognize_advanced_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.no_stamp):
            query['NoStamp'] = request.no_stamp
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
        if not UtilClient.is_unset(request.row):
            query['Row'] = request.row
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeAdvanced',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAdvancedResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_advanced(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_advanced_with_options(request, runtime)

    def recognize_air_itinerary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeAirItinerary',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAirItineraryResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_air_itinerary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_air_itinerary_with_options(request, runtime)

    def recognize_all_text_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeAllTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_config):
            request.advanced_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_config, 'AdvancedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.id_card_config):
            request.id_card_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.id_card_config, 'IdCardConfig', 'json')
        if not UtilClient.is_unset(tmp_req.international_id_card_config):
            request.international_id_card_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.international_id_card_config, 'InternationalIdCardConfig', 'json')
        if not UtilClient.is_unset(tmp_req.multi_lan_config):
            request.multi_lan_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_lan_config, 'MultiLanConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.advanced_config_shrink):
            query['AdvancedConfig'] = request.advanced_config_shrink
        if not UtilClient.is_unset(request.id_card_config_shrink):
            query['IdCardConfig'] = request.id_card_config_shrink
        if not UtilClient.is_unset(request.international_id_card_config_shrink):
            query['InternationalIdCardConfig'] = request.international_id_card_config_shrink
        if not UtilClient.is_unset(request.multi_lan_config_shrink):
            query['MultiLanConfig'] = request.multi_lan_config_shrink
        if not UtilClient.is_unset(request.output_bar_code):
            query['OutputBarCode'] = request.output_bar_code
        if not UtilClient.is_unset(request.output_coordinate):
            query['OutputCoordinate'] = request.output_coordinate
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_kvexcel):
            query['OutputKVExcel'] = request.output_kvexcel
        if not UtilClient.is_unset(request.output_oricoord):
            query['OutputOricoord'] = request.output_oricoord
        if not UtilClient.is_unset(request.output_qrcode):
            query['OutputQrcode'] = request.output_qrcode
        if not UtilClient.is_unset(request.output_stamp):
            query['OutputStamp'] = request.output_stamp
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=tmp_req.body
        )
        params = open_api_models.Params(
            action='RecognizeAllText',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAllTextResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_all_text(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_all_text_with_options(request, runtime)

    def recognize_bank_acceptance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankAcceptance',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAcceptanceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_bank_acceptance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_acceptance_with_options(request, runtime)

    def recognize_bank_account_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankAccountLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAccountLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_bank_account_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_account_license_with_options(request, runtime)

    def recognize_bank_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBankCard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankCardResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_bank_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_card_with_options(request, runtime)

    def recognize_basic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBasic',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBasicResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_basic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_basic_with_options(request, runtime)

    def recognize_birth_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBirthCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBirthCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_birth_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_birth_certification_with_options(request, runtime)

    def recognize_bus_ship_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBusShipTicket',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusShipTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_bus_ship_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_bus_ship_ticket_with_options(request, runtime)

    def recognize_business_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeBusinessLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_business_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_business_license_with_options(request, runtime)

    def recognize_car_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_car_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_invoice_with_options(request, runtime)

    def recognize_car_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarNumber',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_car_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_number_with_options(request, runtime)

    def recognize_car_vin_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCarVinCode',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarVinCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_car_vin_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_vin_code_with_options(request, runtime)

    def recognize_chinese_passport_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeChinesePassport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeChinesePassportResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_chinese_passport(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_chinese_passport_with_options(request, runtime)

    def recognize_common_printed_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCommonPrintedInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCommonPrintedInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_common_printed_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_common_printed_invoice_with_options(request, runtime)

    def recognize_cosmetic_produce_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCosmeticProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCosmeticProduceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_cosmetic_produce_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_cosmetic_produce_license_with_options(request, runtime)

    def recognize_covid_test_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.multiple_result):
            query['MultipleResult'] = request.multiple_result
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCovidTestReport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCovidTestReportResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_covid_test_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_covid_test_report_with_options(request, runtime)

    def recognize_ctwo_medical_device_manage_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeCtwoMedicalDeviceManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_ctwo_medical_device_manage_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_ctwo_medical_device_manage_license_with_options(request, runtime)

    def recognize_document_structure_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.no_stamp):
            query['NoStamp'] = request.no_stamp
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.paragraph):
            query['Paragraph'] = request.paragraph
        if not UtilClient.is_unset(request.row):
            query['Row'] = request.row
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.use_new_style_output):
            query['UseNewStyleOutput'] = request.use_new_style_output
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeDocumentStructure',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDocumentStructureResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_document_structure(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_document_structure_with_options(request, runtime)

    def recognize_driving_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeDrivingLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDrivingLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_driving_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_driving_license_with_options(request, runtime)

    def recognize_edu_formula_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduFormula',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduFormulaResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_edu_formula(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_formula_with_options(request, runtime)

    def recognize_edu_oral_calculation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduOralCalculation',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduOralCalculationResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_edu_oral_calculation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_oral_calculation_with_options(request, runtime)

    def recognize_edu_paper_cut_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cut_type):
            query['CutType'] = request.cut_type
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperCut',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperCutResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_edu_paper_cut(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_cut_with_options(request, runtime)

    def recognize_edu_paper_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.output_oricoord):
            query['OutputOricoord'] = request.output_oricoord
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperOcrResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_edu_paper_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_ocr_with_options(request, runtime)

    def recognize_edu_paper_structed_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduPaperStructed',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperStructedResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_edu_paper_structed(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_structed_with_options(request, runtime)

    def recognize_edu_question_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEduQuestionOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduQuestionOcrResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_edu_question_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_question_ocr_with_options(request, runtime)

    def recognize_english_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEnglish',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEnglishResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_english(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_english_with_options(request, runtime)

    def recognize_estate_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeEstateCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEstateCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_estate_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_estate_certification_with_options(request, runtime)

    def recognize_exit_entry_permit_to_hkwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeExitEntryPermitToHK',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExitEntryPermitToHKResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_exit_entry_permit_to_hk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_exit_entry_permit_to_hkwith_options(request, runtime)

    def recognize_exit_entry_permit_to_mainland_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeExitEntryPermitToMainland',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeExitEntryPermitToMainlandResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_exit_entry_permit_to_mainland(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_exit_entry_permit_to_mainland_with_options(request, runtime)

    def recognize_food_manage_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeFoodManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodManageLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_food_manage_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_manage_license_with_options(request, runtime)

    def recognize_food_produce_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeFoodProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_food_produce_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_produce_license_with_options(request, runtime)

    def recognize_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeGeneral',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_general_with_options(request, runtime)

    def recognize_hkidcard_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHKIdcard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHKIdcardResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_hkidcard(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_hkidcard_with_options(request, runtime)

    def recognize_handwriting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHandwriting',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHandwritingResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_handwriting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_handwriting_with_options(request, runtime)

    def recognize_health_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHealthCode',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHealthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_health_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_health_code_with_options(request, runtime)

    def recognize_hotel_consume_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHotelConsume',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHotelConsumeResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_hotel_consume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_hotel_consume_with_options(request, runtime)

    def recognize_household_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_resident_page):
            query['IsResidentPage'] = request.is_resident_page
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeHousehold',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseholdResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_household(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_household_with_options(request, runtime)

    def recognize_idcard_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_figure):
            query['OutputFigure'] = request.output_figure
        if not UtilClient.is_unset(request.output_quality_info):
            query['OutputQualityInfo'] = request.output_quality_info
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeIdcard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeIdcardResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_idcard(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_idcard_with_options(request, runtime)

    def recognize_international_business_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInternationalBusinessLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInternationalBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_international_business_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_international_business_license_with_options(request, runtime)

    def recognize_international_idcard_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInternationalIdcard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInternationalIdcardResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_international_idcard(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_international_idcard_with_options(request, runtime)

    def recognize_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_invoice_with_options(request, runtime)

    def recognize_janpanese_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeJanpanese',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeJanpaneseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_janpanese(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_janpanese_with_options(request, runtime)

    def recognize_korean_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeKorean',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeKoreanResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_korean(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_korean_with_options(request, runtime)

    def recognize_latin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeLatin',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeLatinResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_latin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_latin_with_options(request, runtime)

    def recognize_medical_device_manage_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMedicalDeviceManageLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_medical_device_manage_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_manage_license_with_options(request, runtime)

    def recognize_medical_device_produce_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMedicalDeviceProduceLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_medical_device_produce_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_produce_license_with_options(request, runtime)

    def recognize_mixed_invoices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeMixedInvoices',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedInvoicesResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_mixed_invoices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_mixed_invoices_with_options(request, runtime)

    def recognize_multi_language_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeMultiLanguageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.languages):
            request.languages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.languages, 'Languages', 'simple')
        query = {}
        if not UtilClient.is_unset(request.languages_shrink):
            query['Languages'] = request.languages_shrink
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.need_sort_page):
            query['NeedSortPage'] = request.need_sort_page
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=tmp_req.body
        )
        params = open_api_models.Params(
            action='RecognizeMultiLanguage',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMultiLanguageResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_multi_language(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_multi_language_with_options(request, runtime)

    def recognize_non_tax_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeNonTaxInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeNonTaxInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_non_tax_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_non_tax_invoice_with_options(request, runtime)

    def recognize_passport_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePassport',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePassportResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_passport(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_passport_with_options(request, runtime)

    def recognize_payment_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePaymentRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePaymentRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_payment_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_payment_record_with_options(request, runtime)

    def recognize_purchase_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_multi_orders):
            query['OutputMultiOrders'] = request.output_multi_orders
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizePurchaseRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePurchaseRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_purchase_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_purchase_record_with_options(request, runtime)

    def recognize_quota_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeQuotaInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeQuotaInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_quota_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_quota_invoice_with_options(request, runtime)

    def recognize_ride_hailing_itinerary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRideHailingItinerary',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRideHailingItineraryResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_ride_hailing_itinerary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_ride_hailing_itinerary_with_options(request, runtime)

    def recognize_roll_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRollTicket',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRollTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_roll_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_roll_ticket_with_options(request, runtime)

    def recognize_russian_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeRussian',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRussianResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_russian(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_russian_with_options(request, runtime)

    def recognize_shopping_receipt_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeShoppingReceipt',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeShoppingReceiptResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_shopping_receipt(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_shopping_receipt_with_options(request, runtime)

    def recognize_social_security_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeSocialSecurityCard',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeSocialSecurityCardResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_social_security_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_social_security_card_with_options(request, runtime)

    def recognize_social_security_card_version_iiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeSocialSecurityCardVersionII',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeSocialSecurityCardVersionIIResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_social_security_card_version_ii(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_social_security_card_version_iiwith_options(request, runtime)

    def recognize_table_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_hand_writing):
            query['IsHandWriting'] = request.is_hand_writing
        if not UtilClient.is_unset(request.line_less):
            query['LineLess'] = request.line_less
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.skip_detection):
            query['SkipDetection'] = request.skip_detection
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTableOcr',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTableOcrResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_table_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_table_ocr_with_options(request, runtime)

    def recognize_tax_clearance_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTaxClearanceCertificate',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxClearanceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_tax_clearance_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_tax_clearance_certificate_with_options(request, runtime)

    def recognize_taxi_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTaxiInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxiInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_taxi_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_taxi_invoice_with_options(request, runtime)

    def recognize_thai_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.need_rotate):
            query['NeedRotate'] = request.need_rotate
        if not UtilClient.is_unset(request.output_char_info):
            query['OutputCharInfo'] = request.output_char_info
        if not UtilClient.is_unset(request.output_table):
            query['OutputTable'] = request.output_table
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeThai',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeThaiResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_thai(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_thai_with_options(request, runtime)

    def recognize_toll_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTollInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTollInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_toll_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_toll_invoice_with_options(request, runtime)

    def recognize_trade_mark_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTradeMarkCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_trade_mark_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_trade_mark_certification_with_options(request, runtime)

    def recognize_train_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeTrainInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTrainInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_train_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_train_invoice_with_options(request, runtime)

    def recognize_used_car_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeUsedCarInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeUsedCarInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_used_car_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_used_car_invoice_with_options(request, runtime)

    def recognize_vehicle_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleCertification',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_vehicle_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_certification_with_options(request, runtime)

    def recognize_vehicle_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_vehicle_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_license_with_options(request, runtime)

    def recognize_vehicle_registration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeVehicleRegistration',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_vehicle_registration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_registration_with_options(request, runtime)

    def recognize_waybill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=request.body,
            stream=request.body
        )
        params = open_api_models.Params(
            action='RecognizeWaybill',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeWaybillResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_waybill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_waybill_with_options(request, runtime)

    def verify_business_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.credit_code):
            query['CreditCode'] = request.credit_code
        if not UtilClient.is_unset(request.legal_person):
            query['LegalPerson'] = request.legal_person
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyBusinessLicense',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.VerifyBusinessLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_business_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_business_license_with_options(request, runtime)

    def verify_vatinvoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invoice_code):
            query['InvoiceCode'] = request.invoice_code
        if not UtilClient.is_unset(request.invoice_date):
            query['InvoiceDate'] = request.invoice_date
        if not UtilClient.is_unset(request.invoice_no):
            query['InvoiceNo'] = request.invoice_no
        if not UtilClient.is_unset(request.invoice_sum):
            query['InvoiceSum'] = request.invoice_sum
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyVATInvoice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.VerifyVATInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_vatinvoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_vatinvoice_with_options(request, runtime)
