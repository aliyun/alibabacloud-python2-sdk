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

    def recognize_driving_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDrivingLicenseResponse(),
            self.do_rpcrequest('RecognizeDrivingLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_driving_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_driving_license_with_options(request, runtime)

    def recognize_korean_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeKoreanResponse(),
            self.do_rpcrequest('RecognizeKorean', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_korean(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_korean_with_options(request, runtime)

    def recognize_car_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarInvoiceResponse(),
            self.do_rpcrequest('RecognizeCarInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_car_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_invoice_with_options(request, runtime)

    def recognize_mixed_invoices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedInvoicesResponse(),
            self.do_rpcrequest('RecognizeMixedInvoices', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_mixed_invoices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_mixed_invoices_with_options(request, runtime)

    def recognize_estate_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEstateCertificationResponse(),
            self.do_rpcrequest('RecognizeEstateCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_estate_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_estate_certification_with_options(request, runtime)

    def recognize_car_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarNumberResponse(),
            self.do_rpcrequest('RecognizeCarNumber', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_car_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_number_with_options(request, runtime)

    def recognize_edu_paper_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperOcrResponse(),
            self.do_rpcrequest('RecognizeEduPaperOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_paper_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_ocr_with_options(request, runtime)

    def recognize_trade_mark_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTradeMarkCertificationResponse(),
            self.do_rpcrequest('RecognizeTradeMarkCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_trade_mark_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_trade_mark_certification_with_options(request, runtime)

    def recognize_birth_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBirthCertificationResponse(),
            self.do_rpcrequest('RecognizeBirthCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_birth_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_birth_certification_with_options(request, runtime)

    def recognize_doctype_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeDoctypeResponse(),
            self.do_rpcrequest('RecognizeDoctype', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_doctype(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_doctype_with_options(request, runtime)

    def recognize_bank_account_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankAccountLicenseResponse(),
            self.do_rpcrequest('RecognizeBankAccountLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_bank_account_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_account_license_with_options(request, runtime)

    def recognize_food_manage_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodManageLicenseResponse(),
            self.do_rpcrequest('RecognizeFoodManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_food_manage_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_manage_license_with_options(request, runtime)

    def recognize_roll_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRollTicketResponse(),
            self.do_rpcrequest('RecognizeRollTicket', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_roll_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_roll_ticket_with_options(request, runtime)

    def recognize_edu_formula_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduFormulaResponse(),
            self.do_rpcrequest('RecognizeEduFormula', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_formula(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_formula_with_options(request, runtime)

    def recognize_passport_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizePassportResponse(),
            self.do_rpcrequest('RecognizePassport', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_passport(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_passport_with_options(request, runtime)

    def recognize_taxi_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTaxiInvoiceResponse(),
            self.do_rpcrequest('RecognizeTaxiInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_taxi_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_taxi_invoice_with_options(request, runtime)

    def recognize_food_produce_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeFoodProduceLicenseResponse(),
            self.do_rpcrequest('RecognizeFoodProduceLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_food_produce_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_food_produce_license_with_options(request, runtime)

    def recognize_medical_device_produce_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceProduceLicenseResponse(),
            self.do_rpcrequest('RecognizeMedicalDeviceProduceLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_medical_device_produce_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_produce_license_with_options(request, runtime)

    def recognize_handwriting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHandwritingResponse(),
            self.do_rpcrequest('RecognizeHandwriting', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_handwriting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_handwriting_with_options(request, runtime)

    def recognize_air_itinerary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAirItineraryResponse(),
            self.do_rpcrequest('RecognizeAirItinerary', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_air_itinerary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_air_itinerary_with_options(request, runtime)

    def recognize_janpanese_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeJanpaneseResponse(),
            self.do_rpcrequest('RecognizeJanpanese', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_janpanese(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_janpanese_with_options(request, runtime)

    def recognize_ctwo_medical_device_manage_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCtwoMedicalDeviceManageLicenseResponse(),
            self.do_rpcrequest('RecognizeCtwoMedicalDeviceManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_ctwo_medical_device_manage_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_ctwo_medical_device_manage_license_with_options(request, runtime)

    def recognize_thai_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeThaiResponse(),
            self.do_rpcrequest('RecognizeThai', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_thai(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_thai_with_options(request, runtime)

    def recognize_medical_device_manage_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMedicalDeviceManageLicenseResponse(),
            self.do_rpcrequest('RecognizeMedicalDeviceManageLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_medical_device_manage_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_medical_device_manage_license_with_options(request, runtime)

    def recognize_latin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeLatinResponse(),
            self.do_rpcrequest('RecognizeLatin', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_latin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_latin_with_options(request, runtime)

    def recognize_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeInvoiceResponse(),
            self.do_rpcrequest('RecognizeInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_invoice_with_options(request, runtime)

    def recognize_mixed_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMixedCardsResponse(),
            self.do_rpcrequest('RecognizeMixedCards', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_mixed_cards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_mixed_cards_with_options(request, runtime)

    def recognize_waybill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeWaybillResponse(),
            self.do_rpcrequest('RecognizeWaybill', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_waybill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_waybill_with_options(request, runtime)

    def recognize_car_vin_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeCarVinCodeResponse(),
            self.do_rpcrequest('RecognizeCarVinCode', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_car_vin_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_vin_code_with_options(request, runtime)

    def recognize_advanced_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeAdvancedResponse(),
            self.do_rpcrequest('RecognizeAdvanced', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_advanced(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_advanced_with_options(request, runtime)

    def recognize_vehicle_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeVehicleLicenseResponse(),
            self.do_rpcrequest('RecognizeVehicleLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_vehicle_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_license_with_options(request, runtime)

    def recognize_russian_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeRussianResponse(),
            self.do_rpcrequest('RecognizeRussian', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_russian(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_russian_with_options(request, runtime)

    def recognize_house_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseCertificationResponse(),
            self.do_rpcrequest('RecognizeHouseCertification', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_house_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_house_certification_with_options(request, runtime)

    def recognize_basic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBasicResponse(),
            self.do_rpcrequest('RecognizeBasic', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_basic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_basic_with_options(request, runtime)

    def recognize_business_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBusinessLicenseResponse(),
            self.do_rpcrequest('RecognizeBusinessLicense', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_business_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_business_license_with_options(request, runtime)

    def recognize_bank_card_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeBankCardResponse(),
            self.do_rpcrequest('RecognizeBankCard', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_bank_card(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_bank_card_with_options(request, runtime)

    def recognize_edu_paper_cut_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperCutResponse(),
            self.do_rpcrequest('RecognizeEduPaperCut', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_paper_cut(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_cut_with_options(request, runtime)

    def recognize_household_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeHouseholdResponse(),
            self.do_rpcrequest('RecognizeHousehold', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_household(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_household_with_options(request, runtime)

    def recognize_edu_question_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduQuestionOcrResponse(),
            self.do_rpcrequest('RecognizeEduQuestionOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_question_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_question_ocr_with_options(request, runtime)

    def recognize_train_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTrainInvoiceResponse(),
            self.do_rpcrequest('RecognizeTrainInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_train_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_train_invoice_with_options(request, runtime)

    def recognize_table_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeTableOcrResponse(),
            self.do_rpcrequest('RecognizeTableOcr', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_table_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_table_ocr_with_options(request, runtime)

    def recognize_english_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEnglishResponse(),
            self.do_rpcrequest('RecognizeEnglish', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_english(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_english_with_options(request, runtime)

    def recognize_multi_language_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocr_api_20210707_models.RecognizeMultiLanguageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.languages):
            request.languages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.languages, 'Languages', 'simple')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeMultiLanguageResponse(),
            self.do_rpcrequest('RecognizeMultiLanguage', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_multi_language(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_multi_language_with_options(request, runtime)

    def recognize_edu_oral_calculation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduOralCalculationResponse(),
            self.do_rpcrequest('RecognizeEduOralCalculation', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_oral_calculation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_oral_calculation_with_options(request, runtime)

    def recognize_quota_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeQuotaInvoiceResponse(),
            self.do_rpcrequest('RecognizeQuotaInvoice', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_quota_invoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_quota_invoice_with_options(request, runtime)

    def recognize_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeGeneralResponse(),
            self.do_rpcrequest('RecognizeGeneral', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_general_with_options(request, runtime)

    def recognize_edu_paper_structed_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeEduPaperStructedResponse(),
            self.do_rpcrequest('RecognizeEduPaperStructed', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_edu_paper_structed(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_edu_paper_structed_with_options(request, runtime)

    def recognize_idcard_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ocr_api_20210707_models.RecognizeIdcardResponse(),
            self.do_rpcrequest('RecognizeIdcard', '2021-07-07', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def recognize_idcard(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_idcard_with_options(request, runtime)
