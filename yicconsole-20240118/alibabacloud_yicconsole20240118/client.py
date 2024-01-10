# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yicconsole20240118 import models as yic_console_20240118_models
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
        self._endpoint = self.get_endpoint('yicconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def billing_process_message_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BillingProcessMessage',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/billing/commands/lifecycle',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yic_console_20240118_models.BillingProcessMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def billing_process_message(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.billing_process_message_with_options(request, headers, runtime)

    def check_pay_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CheckPayOrder',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/billing/commands/verify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yic_console_20240118_models.CheckPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def check_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_pay_order_with_options(request, headers, runtime)

    def check_refund_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CheckRefund',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/billing/commands/check-refund',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yic_console_20240118_models.CheckRefundResponse(),
            self.call_api(params, req, runtime)
        )

    def check_refund(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_refund_with_options(request, headers, runtime)

    def pay_order_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PayOrder',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/billing/commands/pay',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yic_console_20240118_models.PayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pay_order_with_options(request, headers, runtime)

    def prepaid_cease_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='PrepaidCease',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/billing/commands/prepaid-cease',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yic_console_20240118_models.PrepaidCeaseResponse(),
            self.call_api(params, req, runtime)
        )

    def prepaid_cease(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.prepaid_cease_with_options(request, headers, runtime)

    def refund_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='Refund',
            version='2024-01-18',
            protocol='HTTPS',
            pathname='/yic/yic-console/v1/billing/commands/refund',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yic_console_20240118_models.RefundResponse(),
            self.call_api(params, req, runtime)
        )

    def refund(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refund_with_options(request, headers, runtime)
