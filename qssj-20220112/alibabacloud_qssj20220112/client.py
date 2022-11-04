# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qssj20220112 import models as qssj_20220112_models
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
        self._endpoint = self.get_endpoint('qssj', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_age_distribution_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_ids):
            query['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgeDistribution',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetAgeDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_age_distribution(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_age_distribution_with_options(request, runtime)

    def get_all_trend_category_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAllTrendCategory',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetAllTrendCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_trend_category(self):
        runtime = util_models.RuntimeOptions()
        return self.get_all_trend_category_with_options(runtime)

    def get_crowd_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCrowdLabel',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetCrowdLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def get_crowd_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_crowd_label_with_options(request, runtime)

    def get_crowd_regin_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_ids):
            query['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCrowdRegin',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetCrowdReginResponse(),
            self.call_api(params, req, runtime)
        )

    def get_crowd_regin(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_crowd_regin_with_options(request, runtime)

    def get_opportunity_market_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        if not UtilClient.is_unset(request.time_display):
            body['TimeDisplay'] = request.time_display
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOpportunityMarket',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetOpportunityMarketResponse(),
            self.call_api(params, req, runtime)
        )

    def get_opportunity_market(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_opportunity_market_with_options(request, runtime)

    def get_price_range_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPriceRange',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetPriceRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_price_range(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_price_range_with_options(request, runtime)

    def get_sex_ratio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_ids):
            query['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSexRatio',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetSexRatioResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sex_ratio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sex_ratio_with_options(request, runtime)

    def get_store_sales_volume_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStoreSalesVolumeTop',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetStoreSalesVolumeTopResponse(),
            self.call_api(params, req, runtime)
        )

    def get_store_sales_volume_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_store_sales_volume_top_with_options(request, runtime)

    def get_store_search_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStoreSearchTop',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetStoreSearchTopResponse(),
            self.call_api(params, req, runtime)
        )

    def get_store_search_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_store_search_top_with_options(request, runtime)

    def get_style_top_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.time_display):
            body['TimeDisplay'] = request.time_display
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStyleTop',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetStyleTopResponse(),
            self.call_api(params, req, runtime)
        )

    def get_style_top(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_style_top_with_options(request, runtime)

    def get_trend_image_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ai_img_id):
            query['AiImgId'] = request.ai_img_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrendImageDetail',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetTrendImageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trend_image_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trend_image_detail_with_options(request, runtime)

    def get_trend_image_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrendImageList',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetTrendImageListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trend_image_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trend_image_list_with_options(request, runtime)

    def get_trend_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        if not UtilClient.is_unset(request.month_num):
            body['MonthNum'] = request.month_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrendIndex',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetTrendIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trend_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trend_index_with_options(request, runtime)

    def get_trend_search_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrendSearchRecord',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetTrendSearchRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trend_search_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trend_search_record_with_options(request, runtime)

    def get_trend_statistic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cate_ids):
            body['CateIds'] = request.cate_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrendStatistic',
            version='2022-01-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qssj_20220112_models.GetTrendStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trend_statistic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trend_statistic_with_options(request, runtime)
