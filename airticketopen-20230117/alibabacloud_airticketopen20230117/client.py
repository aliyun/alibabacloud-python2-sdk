# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_airticketopen20230117 import models as airticket_open_20230117_models
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
        self._endpoint = self.get_endpoint('airticketopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def account_flow_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day_num):
            query['day_num'] = request.day_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.utc_begin_time):
            query['utc_begin_time'] = request.utc_begin_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccountFlowList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/account/flow-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.AccountFlowListResponse(),
            self.call_api(params, req, runtime)
        )

    def account_flow_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.AccountFlowListHeaders()
        return self.account_flow_list_with_options(request, headers, runtime)

    def ancillary_suggest_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AncillarySuggest',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/ancillary/action-suggest',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.AncillarySuggestResponse(),
            self.call_api(params, req, runtime)
        )

    def ancillary_suggest(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.AncillarySuggestHeaders()
        return self.ancillary_suggest_with_options(request, headers, runtime)

    def book_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.BookShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_ancillary_purchase_map_list):
            request.passenger_ancillary_purchase_map_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_ancillary_purchase_map_list, 'passenger_ancillary_purchase_map_list', 'json')
        if not UtilClient.is_unset(tmp_req.passenger_list):
            request.passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.passenger_list, 'passenger_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.out_order_num):
            body['out_order_num'] = request.out_order_num
        if not UtilClient.is_unset(request.passenger_ancillary_purchase_map_list_shrink):
            body['passenger_ancillary_purchase_map_list'] = request.passenger_ancillary_purchase_map_list_shrink
        if not UtilClient.is_unset(request.passenger_list_shrink):
            body['passenger_list'] = request.passenger_list_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Book',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-book',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.BookResponse(),
            self.call_api(params, req, runtime)
        )

    def book(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.BookHeaders()
        return self.book_with_options(request, headers, runtime)

    def cancel_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Cancel',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.CancelResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.CancelHeaders()
        return self.cancel_with_options(request, headers, runtime)

    def change_apply_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.ChangeApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.change_passenger_list):
            request.change_passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.change_passenger_list, 'change_passenger_list', 'json')
        if not UtilClient.is_unset(tmp_req.changed_journeys):
            request.changed_journeys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.changed_journeys, 'changed_journeys', 'json')
        if not UtilClient.is_unset(tmp_req.contact):
            request.contact_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact, 'contact', 'json')
        body = {}
        if not UtilClient.is_unset(request.change_passenger_list_shrink):
            body['change_passenger_list'] = request.change_passenger_list_shrink
        if not UtilClient.is_unset(request.changed_journeys_shrink):
            body['changed_journeys'] = request.changed_journeys_shrink
        if not UtilClient.is_unset(request.contact_shrink):
            body['contact'] = request.contact_shrink
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeApply',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/change/action-apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeApplyResponse(),
            self.call_api(params, req, runtime)
        )

    def change_apply(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeApplyHeaders()
        return self.change_apply_with_options(request, headers, runtime)

    def change_cancel_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeCancel',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/change/action-cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeCancelResponse(),
            self.call_api(params, req, runtime)
        )

    def change_cancel(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeCancelHeaders()
        return self.change_cancel_with_options(request, headers, runtime)

    def change_confirm_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_order_num):
            body['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeConfirm',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/change/action-confirm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    def change_confirm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeConfirmHeaders()
        return self.change_confirm_with_options(request, headers, runtime)

    def change_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_num):
            query['change_order_num'] = request.change_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/change/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def change_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailHeaders()
        return self.change_detail_with_options(request, headers, runtime)

    def change_detail_list_of_buyer_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.utc_create_begin):
            query['utc_create_begin'] = request.utc_create_begin
        if not UtilClient.is_unset(request.utc_create_end):
            query['utc_create_end'] = request.utc_create_end
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetailListOfBuyer',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/change/buyer/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailListOfBuyerResponse(),
            self.call_api(params, req, runtime)
        )

    def change_detail_list_of_buyer(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailListOfBuyerHeaders()
        return self.change_detail_list_of_buyer_with_options(request, headers, runtime)

    def change_detail_list_of_order_num_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDetailListOfOrderNum',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/change/order-num/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.ChangeDetailListOfOrderNumResponse(),
            self.call_api(params, req, runtime)
        )

    def change_detail_list_of_order_num(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.ChangeDetailListOfOrderNumHeaders()
        return self.change_detail_list_of_order_num_with_options(request, headers, runtime)

    def enrich_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.EnrichShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.journey_param_list):
            request.journey_param_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.journey_param_list, 'journey_param_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.adults):
            body['adults'] = request.adults
        if not UtilClient.is_unset(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.children):
            body['children'] = request.children
        if not UtilClient.is_unset(request.infants):
            body['infants'] = request.infants
        if not UtilClient.is_unset(request.journey_param_list_shrink):
            body['journey_param_list'] = request.journey_param_list_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Enrich',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-enrich',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.EnrichResponse(),
            self.call_api(params, req, runtime)
        )

    def enrich(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.EnrichHeaders()
        return self.enrich_with_options(request, headers, runtime)

    def file_upload_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_content):
            body['file_content'] = request.file_content
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileUpload',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/attachment/action-upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.FileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    def file_upload(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.FileUploadHeaders()
        return self.file_upload_with_options(request, headers, runtime)

    def flight_change_of_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FlightChangeOfOrder',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/flightchange/of-order',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.FlightChangeOfOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def flight_change_of_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.FlightChangeOfOrderHeaders()
        return self.flight_change_of_order_with_options(request, headers, runtime)

    def get_token_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['app_key'] = request.app_key
        if not UtilClient.is_unset(request.app_secret):
            query['app_secret'] = request.app_secret
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_token(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    def luggage_direct_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.LuggageDirectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.flight_segment_param_list):
            request.flight_segment_param_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.flight_segment_param_list, 'flight_segment_param_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.flight_segment_param_list_shrink):
            body['flight_segment_param_list'] = request.flight_segment_param_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LuggageDirect',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/flight-data/luggage-direct',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.LuggageDirectResponse(),
            self.call_api(params, req, runtime)
        )

    def luggage_direct(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.LuggageDirectHeaders()
        return self.luggage_direct_with_options(request, headers, runtime)

    def order_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.out_order_num):
            query['out_order_num'] = request.out_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/order-detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.OrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.OrderDetailHeaders()
        return self.order_detail_with_options(request, headers, runtime)

    def order_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.book_time_end):
            query['book_time_end'] = request.book_time_end
        if not UtilClient.is_unset(request.book_time_start):
            query['book_time_start'] = request.book_time_start
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/order-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.OrderListResponse(),
            self.call_api(params, req, runtime)
        )

    def order_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.OrderListHeaders()
        return self.order_list_with_options(request, headers, runtime)

    def pricing_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.solution_id):
            body['solution_id'] = request.solution_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Pricing',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-pricing',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.PricingResponse(),
            self.call_api(params, req, runtime)
        )

    def pricing(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.PricingHeaders()
        return self.pricing_with_options(request, headers, runtime)

    def refund_apply_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.RefundApplyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.refund_journeys):
            request.refund_journeys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_journeys, 'refund_journeys', 'json')
        if not UtilClient.is_unset(tmp_req.refund_passenger_list):
            request.refund_passenger_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_passenger_list, 'refund_passenger_list', 'json')
        if not UtilClient.is_unset(tmp_req.refund_type):
            request.refund_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.refund_type, 'refund_type', 'json')
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        if not UtilClient.is_unset(request.refund_journeys_shrink):
            body['refund_journeys'] = request.refund_journeys_shrink
        if not UtilClient.is_unset(request.refund_passenger_list_shrink):
            body['refund_passenger_list'] = request.refund_passenger_list_shrink
        if not UtilClient.is_unset(request.refund_type_shrink):
            body['refund_type'] = request.refund_type_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundApply',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/refund/action-apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundApplyResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_apply(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundApplyHeaders()
        return self.refund_apply_with_options(request, headers, runtime)

    def refund_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.refund_order_num):
            query['refund_order_num'] = request.refund_order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundDetail',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/refund/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundDetailHeaders()
        return self.refund_detail_with_options(request, headers, runtime)

    def refund_detail_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_num):
            query['order_num'] = request.order_num
        if not UtilClient.is_unset(request.page_index):
            query['page_index'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.refund_create_begin_time):
            query['refund_create_begin_time'] = request.refund_create_begin_time
        if not UtilClient.is_unset(request.refund_create_end_time):
            query['refund_create_end_time'] = request.refund_create_end_time
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundDetailList',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/refund/detail-list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.RefundDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.RefundDetailListHeaders()
        return self.refund_detail_list_with_options(request, headers, runtime)

    def search_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.SearchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.air_legs):
            request.air_legs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.air_legs, 'air_legs', 'json')
        body = {}
        if not UtilClient.is_unset(request.adults):
            body['adults'] = request.adults
        if not UtilClient.is_unset(request.air_legs_shrink):
            body['air_legs'] = request.air_legs_shrink
        if not UtilClient.is_unset(request.cabin_class):
            body['cabin_class'] = request.cabin_class
        if not UtilClient.is_unset(request.children):
            body['children'] = request.children
        if not UtilClient.is_unset(request.infants):
            body['infants'] = request.infants
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Search',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.SearchResponse(),
            self.call_api(params, req, runtime)
        )

    def search(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.SearchHeaders()
        return self.search_with_options(request, headers, runtime)

    def ticketing_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Ticketing',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-ticketing',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.TicketingResponse(),
            self.call_api(params, req, runtime)
        )

    def ticketing(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.TicketingHeaders()
        return self.ticketing_with_options(request, headers, runtime)

    def ticketing_check_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.order_num):
            body['order_num'] = request.order_num
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TicketingCheck',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/trade/action-ticketing-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.TicketingCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def ticketing_check(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.TicketingCheckHeaders()
        return self.ticketing_check_with_options(request, headers, runtime)

    def transit_visa_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = airticket_open_20230117_models.TransitVisaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.flight_segment_param_list):
            request.flight_segment_param_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.flight_segment_param_list, 'flight_segment_param_list', 'json')
        body = {}
        if not UtilClient.is_unset(request.flight_segment_param_list_shrink):
            body['flight_segment_param_list'] = request.flight_segment_param_list_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_airticket_access_token):
            real_headers['x-acs-airticket-access-token'] = UtilClient.to_jsonstring(headers.x_acs_airticket_access_token)
        if not UtilClient.is_unset(headers.x_acs_airticket_language):
            real_headers['x-acs-airticket-language'] = UtilClient.to_jsonstring(headers.x_acs_airticket_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransitVisa',
            version='2023-01-17',
            protocol='HTTPS',
            pathname='/airticket/v1/flight-data/transit-visa',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            airticket_open_20230117_models.TransitVisaResponse(),
            self.call_api(params, req, runtime)
        )

    def transit_visa(self, request):
        runtime = util_models.RuntimeOptions()
        headers = airticket_open_20230117_models.TransitVisaHeaders()
        return self.transit_visa_with_options(request, headers, runtime)
