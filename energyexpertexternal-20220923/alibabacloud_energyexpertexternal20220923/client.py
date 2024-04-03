# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_energyexpertexternal20220923 import models as energy_expert_external_20220923_models
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
        self._endpoint = self.get_endpoint('energyexpertexternal', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def generate_result_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/generate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GenerateResultResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_result(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_result_with_options(request, headers, runtime)

    def get_area_elec_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAreaElecConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/elec/area',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetAreaElecConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_area_elec_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_area_elec_constitute_with_options(request, headers, runtime)

    def get_carbon_emission_trend_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.trend_type):
            body['trendType'] = request.trend_type
        if not UtilClient.is_unset(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCarbonEmissionTrend',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/trend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def get_carbon_emission_trend(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_carbon_emission_trend_with_options(request, headers, runtime)

    def get_data_item_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataItemList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/data/item/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDataItemListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_item_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_item_list_with_options(request, headers, runtime)

    def get_data_quality_analysis_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataQualityAnalysis',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/data/quality/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDataQualityAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_quality_analysis(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_quality_analysis_with_options(request, headers, runtime)

    def get_device_info_with_options(self, request, headers, runtime):
        """
        You can call this operation to query the parameters of a data collection device based on the device ID. If the verification is passed, the device parameters are returned. If the verification fails, a null value is returned.
        *   You can query the parameters of a single device by day. If data of the device does not exist, a null value is returned.
        

        @param request: GetDeviceInfoRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ds):
            query['ds'] = request.ds
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/external/getDeviceInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_info(self, request):
        """
        You can call this operation to query the parameters of a data collection device based on the device ID. If the verification is passed, the device parameters are returned. If the verification fails, a null value is returned.
        *   You can query the parameters of a single device by day. If data of the device does not exist, a null value is returned.
        

        @param request: GetDeviceInfoRequest

        @return: GetDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_device_info_with_options(request, headers, runtime)

    def get_device_list_with_options(self, request, headers, runtime):
        """
        You can query the information about data collection devices of a site based on the ID of the site. If the verification is passed, the information about the devices of the site is returned. If the verification fails, a null value is returned.
        *   Virtual meters at the site are not returned.
        

        @param request: GetDeviceListRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDeviceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/external/getDeviceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_list(self, request):
        """
        You can query the information about data collection devices of a site based on the ID of the site. If the verification is passed, the information about the devices of the site is returned. If the verification fails, a null value is returned.
        *   Virtual meters at the site are not returned.
        

        @param request: GetDeviceListRequest

        @return: GetDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_device_list_with_options(request, headers, runtime)

    def get_elec_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElecConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/elec/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetElecConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_elec_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elec_constitute_with_options(request, headers, runtime)

    def get_elec_trend_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElecTrend',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/elec/trend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetElecTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def get_elec_trend(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elec_trend_with_options(request, headers, runtime)

    def get_emission_source_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmissionSourceConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_emission_source_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emission_source_constitute_with_options(request, headers, runtime)

    def get_emission_summary_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmissionSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEmissionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_emission_summary(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emission_summary_with_options(request, headers, runtime)

    def get_epd_inventory_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpdInventoryConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/epd/inventory/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_epd_inventory_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_epd_inventory_constitute_with_options(request, headers, runtime)

    def get_epd_summary_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpdSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/epd/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEpdSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_epd_summary(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_epd_summary_with_options(request, headers, runtime)

    def get_footprint_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFootprintList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/product/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetFootprintListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_footprint_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_footprint_list_with_options(request, headers, runtime)

    def get_gas_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGasConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/gas/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGasConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gas_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gas_constitute_with_options(request, headers, runtime)

    def get_gwp_benchmark_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpBenchmarkList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/gwp/benchmark/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpBenchmarkListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gwp_benchmark_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_benchmark_list_with_options(request, headers, runtime)

    def get_gwp_benchmark_summary_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpBenchmarkSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/gwp/benchmark/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gwp_benchmark_summary(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_benchmark_summary_with_options(request, headers, runtime)

    def get_gwp_inventory_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpInventoryConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/gwp/inventory/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gwp_inventory_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_inventory_constitute_with_options(request, headers, runtime)

    def get_gwp_inventory_summary_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpInventorySummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/gwp/inventory/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpInventorySummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gwp_inventory_summary(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_inventory_summary_with_options(request, headers, runtime)

    def get_inventory_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.emission_type):
            body['emissionType'] = request.emission_type
        if not UtilClient.is_unset(request.group):
            body['group'] = request.group
        if not UtilClient.is_unset(request.method_type):
            body['methodType'] = request.method_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInventoryList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/inventory/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetInventoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_inventory_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_inventory_list_with_options(request, headers, runtime)

    def get_org_and_factory_with_options(self, headers, runtime):
        """
        You can set multiple request parameters to filter query results. Specified parameters have logical AND relations. Parameters without assigned values are not used as filtering conditions.
        *   The x-acs-caller-uid header is used to check whether the activated service plan is the required service plan. If the verification is passed, the information about the organizations and sites that are activated by using the Alibaba Cloud account is returned. If the verification fails, a null value is returned.
        *   If activated organizations and sites exist, the data of the organizations and sites is returned. If no organization or site data exists, a null value is returned.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOrgAndFactoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrgAndFactory',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/external/getOrgAndFactory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgAndFactoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_org_and_factory(self):
        """
        You can set multiple request parameters to filter query results. Specified parameters have logical AND relations. Parameters without assigned values are not used as filtering conditions.
        *   The x-acs-caller-uid header is used to check whether the activated service plan is the required service plan. If the verification is passed, the information about the organizations and sites that are activated by using the Alibaba Cloud account is returned. If the verification fails, a null value is returned.
        *   If activated organizations and sites exist, the data of the organizations and sites is returned. If no organization or site data exists, a null value is returned.
        

        @return: GetOrgAndFactoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_org_and_factory_with_options(headers, runtime)

    def get_org_constitute_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOrgConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/analysis/org',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_org_constitute(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_org_constitute_with_options(request, headers, runtime)

    def get_pcr_info_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPcrInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/pcr/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetPcrInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pcr_info(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pcr_info_with_options(request, headers, runtime)

    def get_reduction_proposal_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReductionProposal',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/reduction/proposal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetReductionProposalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_reduction_proposal(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_reduction_proposal_with_options(request, headers, runtime)

    def is_completed_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsCompleted',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/footprint/result/completed',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.IsCompletedResponse(),
            self.call_api(params, req, runtime)
        )

    def is_completed(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.is_completed_with_options(request, headers, runtime)

    def push_device_data_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['deviceType'] = request.device_type
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushDeviceData',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/data/increment/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.PushDeviceDataResponse(),
            self.call_api(params, req, runtime)
        )

    def push_device_data(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_device_data_with_options(request, headers, runtime)

    def push_item_data_with_options(self, request, headers, runtime):
        """
        N/A.
        

        @param request: PushItemDataRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PushItemDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.items):
            body['items'] = request.items
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushItemData',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/data/item/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.PushItemDataResponse(),
            self.call_api(params, req, runtime)
        )

    def push_item_data(self, request):
        """
        N/A.
        

        @param request: PushItemDataRequest

        @return: PushItemDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_item_data_with_options(request, headers, runtime)

    def recalculate_carbon_emission_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecalculateCarbonEmission',
            version='2022-09-23',
            protocol='HTTPS',
            pathname='/api/v1/carbon/emission/data/item/recalculate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse(),
            self.call_api(params, req, runtime)
        )

    def recalculate_carbon_emission(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recalculate_carbon_emission_with_options(request, headers, runtime)
