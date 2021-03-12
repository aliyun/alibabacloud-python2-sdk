# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mseap20210118 import models as mseap_20210118_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('mseap', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mseap_20210118_models.ActivateLicenseResponse().from_map(
            self.do_rpcrequest('ActivateLicense', '2021-01-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    def business_license_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mseap_20210118_models.BusinessLicenseOcrResponse().from_map(
            self.do_rpcrequest('BusinessLicenseOcr', '2021-01-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def business_license_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.business_license_ocr_with_options(request, runtime)

    def certificate_quality_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mseap_20210118_models.CertificateQualityResponse().from_map(
            self.do_rpcrequest('CertificateQuality', '2021-01-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def certificate_quality(self, request):
        runtime = util_models.RuntimeOptions()
        return self.certificate_quality_with_options(request, runtime)

    def describe_agreement_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mseap_20210118_models.DescribeAgreementStatusResponse().from_map(
            self.do_rpcrequest('DescribeAgreementStatus', '2021-01-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_agreement_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_agreement_status_with_options(request, runtime)

    def identity_card_ocr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mseap_20210118_models.IdentityCardOcrResponse().from_map(
            self.do_rpcrequest('IdentityCardOcr', '2021-01-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def identity_card_ocr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.identity_card_ocr_with_options(request, runtime)

    def update_agreement_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mseap_20210118_models.UpdateAgreementStatusResponse().from_map(
            self.do_rpcrequest('UpdateAgreementStatus', '2021-01-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_agreement_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_agreement_status_with_options(request, runtime)
