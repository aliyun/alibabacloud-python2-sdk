# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_address_purification20191118 import models as address_purification_20191118_models
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
        self._endpoint = self.get_endpoint('address-purification', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_address_division_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressDivisionCodeResponse(),
            self.do_rpcrequest('GetAddressDivisionCode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_division_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_division_code_with_options(request, runtime)

    def structure_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.StructureAddressResponse(),
            self.do_rpcrequest('StructureAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def structure_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.structure_address_with_options(request, runtime)

    def extract_express_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractExpressResponse(),
            self.do_rpcrequest('ExtractExpress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_express(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_express_with_options(request, runtime)

    def extract_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractNameResponse(),
            self.do_rpcrequest('ExtractName', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_name_with_options(request, runtime)

    def get_address_block_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressBlockMappingResponse(),
            self.do_rpcrequest('GetAddressBlockMapping', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_block_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_block_mapping_with_options(request, runtime)

    def get_address_search_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSearchResponse(),
            self.do_rpcrequest('GetAddressSearch', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_search(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_search_with_options(request, runtime)

    def predict_poiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.PredictPOIResponse(),
            self.do_rpcrequest('PredictPOI', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def predict_poi(self, request):
        runtime = util_models.RuntimeOptions()
        return self.predict_poiwith_options(request, runtime)

    def classify_poiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ClassifyPOIResponse(),
            self.do_rpcrequest('ClassifyPOI', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def classify_poi(self, request):
        runtime = util_models.RuntimeOptions()
        return self.classify_poiwith_options(request, runtime)

    def correct_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CorrectAddressResponse(),
            self.do_rpcrequest('CorrectAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def correct_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.correct_address_with_options(request, runtime)

    def get_zipcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetZipcodeResponse(),
            self.do_rpcrequest('GetZipcode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_zipcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_zipcode_with_options(request, runtime)

    def complete_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.CompleteAddressResponse(),
            self.do_rpcrequest('CompleteAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_address_with_options(request, runtime)

    def get_address_similarity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressSimilarityResponse(),
            self.do_rpcrequest('GetAddressSimilarity', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_similarity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_similarity_with_options(request, runtime)

    def get_address_geocode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressGeocodeResponse(),
            self.do_rpcrequest('GetAddressGeocode', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_geocode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_geocode_with_options(request, runtime)

    def transfer_coord_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.TransferCoordResponse(),
            self.do_rpcrequest('TransferCoord', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transfer_coord(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_coord_with_options(request, runtime)

    def update_project_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = address_purification_20191118_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def extract_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractPhoneResponse(),
            self.do_rpcrequest('ExtractPhone', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_phone_with_options(request, runtime)

    def get_input_search_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetInputSearchResponse(),
            self.do_rpcrequest('GetInputSearch', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_input_search(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_input_search_with_options(request, runtime)

    def get_address_evaluate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.GetAddressEvaluateResponse(),
            self.do_rpcrequest('GetAddressEvaluate', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_address_evaluate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_address_evaluate_with_options(request, runtime)

    def extract_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            address_purification_20191118_models.ExtractAddressResponse(),
            self.do_rpcrequest('ExtractAddress', '2019-11-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extract_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.extract_address_with_options(request, runtime)
