# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dt_oc_info20220829 import models as dt_oc_info_20220829_models
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
        self._endpoint = self.get_endpoint('dt-oc-info', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_oc_competitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcCompetitors',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcCompetitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_competitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_competitors_with_options(request, runtime)

    def get_oc_core_teams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcCoreTeams',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcCoreTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_core_teams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_core_teams_with_options(request, runtime)

    def get_oc_financing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcFinancing',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcFinancingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_financing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_financing_with_options(request, runtime)

    def get_oc_fuzz_search_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcFuzzSearch',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcFuzzSearchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_fuzz_search(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_fuzz_search_with_options(request, runtime)

    def get_oc_ic_abnormal_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcAbnormalOperation',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcAbnormalOperationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_abnormal_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_abnormal_operation_with_options(request, runtime)

    def get_oc_ic_admin_license_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcAdminLicense',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcAdminLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_admin_license(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_admin_license_with_options(request, runtime)

    def get_oc_ic_basic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcBasic',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcBasicResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_basic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_basic_with_options(request, runtime)

    def get_oc_ic_branch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcBranch',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcBranchResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_branch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_branch_with_options(request, runtime)

    def get_oc_ic_change_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcChangeRecord',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcChangeRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_change_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_change_record_with_options(request, runtime)

    def get_oc_ic_checkup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcCheckup',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcCheckupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_checkup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_checkup_with_options(request, runtime)

    def get_oc_ic_clear_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcClearAccount',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcClearAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_clear_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_clear_account_with_options(request, runtime)

    def get_oc_ic_double_checkup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcDoubleCheckup',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcDoubleCheckupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_double_checkup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_double_checkup_with_options(request, runtime)

    def get_oc_ic_employee_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEmployee',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEmployeeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_employee(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_employee_with_options(request, runtime)

    def get_oc_ic_equity_frozen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEquityFrozen',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEquityFrozenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_equity_frozen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_equity_frozen_with_options(request, runtime)

    def get_oc_ic_equity_pledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcEquityPledge',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcEquityPledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_equity_pledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_equity_pledge_with_options(request, runtime)

    def get_oc_ic_investment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcInvestment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcInvestmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_investment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_investment_with_options(request, runtime)

    def get_oc_ic_knowledge_property_pledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcKnowledgePropertyPledge',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcKnowledgePropertyPledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_knowledge_property_pledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_knowledge_property_pledge_with_options(request, runtime)

    def get_oc_ic_mortgage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcMortgage',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcMortgageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_mortgage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_mortgage_with_options(request, runtime)

    def get_oc_ic_serious_offense_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcSeriousOffense',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcSeriousOffenseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_serious_offense(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_serious_offense_with_options(request, runtime)

    def get_oc_ic_shareholder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcShareholder',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcShareholderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_shareholder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_shareholder_with_options(request, runtime)

    def get_oc_ic_simple_cancel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIcSimpleCancel',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIcSimpleCancelResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ic_simple_cancel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ic_simple_cancel_with_options(request, runtime)

    def get_oc_ip_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpCertificate',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ip_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_certificate_with_options(request, runtime)

    def get_oc_ip_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpDomain',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ip_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_domain_with_options(request, runtime)

    def get_oc_ip_patent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpPatent',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpPatentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ip_patent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_patent_with_options(request, runtime)

    def get_oc_ip_software_copyright_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpSoftwareCopyright',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpSoftwareCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ip_software_copyright(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_software_copyright_with_options(request, runtime)

    def get_oc_ip_trademark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpTrademark',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpTrademarkResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ip_trademark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_trademark_with_options(request, runtime)

    def get_oc_ip_works_copyright_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcIpWorksCopyright',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcIpWorksCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_ip_works_copyright(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_ip_works_copyright_with_options(request, runtime)

    def get_oc_justice_auction_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeAuction',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeAuctionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_auction(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_auction_with_options(request, runtime)

    def get_oc_justice_case_filing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCaseFiling',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCaseFilingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_case_filing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_case_filing_with_options(request, runtime)

    def get_oc_justice_court_announcement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCourtAnnouncement',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCourtAnnouncementResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_court_announcement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_court_announcement_with_options(request, runtime)

    def get_oc_justice_court_notice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeCourtNotice',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeCourtNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_court_notice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_court_notice_with_options(request, runtime)

    def get_oc_justice_dishonesty_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeDishonesty',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeDishonestyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_dishonesty(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_dishonesty_with_options(request, runtime)

    def get_oc_justice_executed_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeExecuted',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeExecutedResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_executed(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_executed_with_options(request, runtime)

    def get_oc_justice_judgement_doc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeJudgementDoc',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeJudgementDocResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_judgement_doc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_judgement_doc_with_options(request, runtime)

    def get_oc_justice_limit_high_consume_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeLimitHighConsume',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeLimitHighConsumeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_limit_high_consume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_limit_high_consume_with_options(request, runtime)

    def get_oc_justice_terminal_case_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcJusticeTerminalCase',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcJusticeTerminalCaseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_justice_terminal_case(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_justice_terminal_case_with_options(request, runtime)

    def get_oc_listed_company_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcListedCompany',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcListedCompanyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_listed_company(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_listed_company_with_options(request, runtime)

    def get_oc_negative_admin_punishment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeAdminPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeAdminPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_negative_admin_punishment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_admin_punishment_with_options(request, runtime)

    def get_oc_negative_customs_punishment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeCustomsPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeCustomsPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_negative_customs_punishment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_customs_punishment_with_options(request, runtime)

    def get_oc_negative_environment_punishment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeEnvironmentPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeEnvironmentPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_negative_environment_punishment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_environment_punishment_with_options(request, runtime)

    def get_oc_negative_food_drug_punishment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeFoodDrugPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeFoodDrugPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_negative_food_drug_punishment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_food_drug_punishment_with_options(request, runtime)

    def get_oc_negative_quality_punishment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcNegativeQualityPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcNegativeQualityPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_negative_quality_punishment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_negative_quality_punishment_with_options(request, runtime)

    def get_oc_operation_bidding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationBidding',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationBiddingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_operation_bidding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_bidding_with_options(request, runtime)

    def get_oc_operation_customs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationCustoms',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationCustomsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_operation_customs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_customs_with_options(request, runtime)

    def get_oc_operation_purchase_land_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationPurchaseLand',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationPurchaseLandResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_operation_purchase_land(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_purchase_land_with_options(request, runtime)

    def get_oc_operation_recruitment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcOperationRecruitment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcOperationRecruitmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_operation_recruitment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_operation_recruitment_with_options(request, runtime)

    def get_oc_product_band_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcProductBand',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcProductBandResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_product_band(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_product_band_with_options(request, runtime)

    def get_oc_tax_abnormal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxAbnormal',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxAbnormalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_tax_abnormal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_abnormal_with_options(request, runtime)

    def get_oc_tax_class_awith_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxClassA',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxClassAResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_tax_class_a(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_class_awith_options(request, runtime)

    def get_oc_tax_general_taxpayer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxGeneralTaxpayer',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxGeneralTaxpayerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_tax_general_taxpayer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_general_taxpayer_with_options(request, runtime)

    def get_oc_tax_illegal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxIllegal',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxIllegalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_tax_illegal(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_illegal_with_options(request, runtime)

    def get_oc_tax_overdue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxOverdue',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxOverdueResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_tax_overdue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_overdue_with_options(request, runtime)

    def get_oc_tax_punishment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOcTaxPunishment',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetOcTaxPunishmentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oc_tax_punishment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oc_tax_punishment_with_options(request, runtime)

    def get_qcc_certification_detail_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQccCertificationDetailById',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetQccCertificationDetailByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_qcc_certification_detail_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_qcc_certification_detail_by_id_with_options(request, runtime)

    def get_qcc_search_certification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_category):
            body['CertCategory'] = request.cert_category
        if not UtilClient.is_unset(request.ent_name):
            body['EntName'] = request.ent_name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetQccSearchCertification',
            version='2022-08-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dt_oc_info_20220829_models.GetQccSearchCertificationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_qcc_search_certification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_qcc_search_certification_with_options(request, runtime)
