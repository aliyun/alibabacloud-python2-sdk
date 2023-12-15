# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_baasdis20200509 import models as baas_dis_20200509_models
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
        self._endpoint = self.get_endpoint('baasdis', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_eenterprise_didwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_unique_id):
            body['OwnerUniqueID'] = request.owner_unique_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEenterpriseDID',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.CreateEenterpriseDIDResponse(),
            self.call_api(params, req, runtime)
        )

    def create_eenterprise_did(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_eenterprise_didwith_options(request, runtime)

    def create_personal_didwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_unique_id):
            body['OwnerUniqueID'] = request.owner_unique_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePersonalDID',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.CreatePersonalDIDResponse(),
            self.call_api(params, req, runtime)
        )

    def create_personal_did(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_personal_didwith_options(request, runtime)

    def create_tenant_didwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantDID',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.CreateTenantDIDResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tenant_did(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_didwith_options(request, runtime)

    def get_didwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.did):
            body['DID'] = request.did
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDID',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.GetDIDResponse(),
            self.call_api(params, req, runtime)
        )

    def get_did(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_didwith_options(request, runtime)

    def issue_normal_verifiable_vcwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bare_claim_struct_body):
            body['BareClaimStructBody'] = request.bare_claim_struct_body
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expiration):
            body['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.issuer):
            body['Issuer'] = request.issuer
        if not UtilClient.is_unset(request.subject):
            body['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IssueNormalVerifiableVC',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.IssueNormalVerifiableVCResponse(),
            self.call_api(params, req, runtime)
        )

    def issue_normal_verifiable_vc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.issue_normal_verifiable_vcwith_options(request, runtime)

    def update_vcwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.issuer_did):
            body['IssuerDid'] = request.issuer_did
        if not UtilClient.is_unset(request.vcid):
            body['VCId'] = request.vcid
        if not UtilClient.is_unset(request.vcstatus):
            body['VCStatus'] = request.vcstatus
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVC',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.UpdateVCResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vcwith_options(request, runtime)

    def verify_verifiable_claim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vccontent):
            body['VCContent'] = request.vccontent
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyVerifiableClaim',
            version='2020-05-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            baas_dis_20200509_models.VerifyVerifiableClaimResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_verifiable_claim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_verifiable_claim_with_options(request, runtime)
