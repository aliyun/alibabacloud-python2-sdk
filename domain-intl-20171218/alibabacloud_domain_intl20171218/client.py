# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_domain_intl20171218 import models as domain_intl_20171218_models
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
        self._endpoint = self.get_endpoint('domain-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def acknowledge_task_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_detail_no):
            query['TaskDetailNo'] = request.task_detail_no
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcknowledgeTaskResult',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.AcknowledgeTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    def acknowledge_task_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.acknowledge_task_result_with_options(request, runtime)

    def batch_fuzzy_match_domain_sensitive_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchFuzzyMatchDomainSensitiveWord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.BatchFuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_fuzzy_match_domain_sensitive_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    def cancel_domain_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDomainVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CancelDomainVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_domain_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_domain_verification_with_options(request, runtime)

    def cancel_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    def check_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fee_command):
            query['FeeCommand'] = request.fee_command
        if not UtilClient.is_unset(request.fee_currency):
            query['FeeCurrency'] = request.fee_currency
        if not UtilClient.is_unset(request.fee_period):
            query['FeePeriod'] = request.fee_period
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def check_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    def check_domain_sunrise_claim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomainSunriseClaim',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckDomainSunriseClaimResponse(),
            self.call_api(params, req, runtime)
        )

    def check_domain_sunrise_claim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_domain_sunrise_claim_with_options(request, runtime)

    def check_transfer_in_feasibility_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckTransferInFeasibility',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.CheckTransferInFeasibilityResponse(),
            self.call_api(params, req, runtime)
        )

    def check_transfer_in_feasibility(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_transfer_in_feasibility_with_options(request, runtime)

    def confirm_transfer_in_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmTransferInEmail',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ConfirmTransferInEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_transfer_in_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_transfer_in_email_with_options(request, runtime)

    def delete_email_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEmailVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.DeleteEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_email_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_email_verification_with_options(request, runtime)

    def delete_registrant_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRegistrantProfile',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.DeleteRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_registrant_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_registrant_profile_with_options(request, runtime)

    def email_verified_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EmailVerified',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.EmailVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    def email_verified(self, request):
        runtime = util_models.RuntimeOptions()
        return self.email_verified_with_options(request, runtime)

    def fuzzy_match_domain_sensitive_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyMatchDomainSensitiveWord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.FuzzyMatchDomainSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    def fuzzy_match_domain_sensitive_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_match_domain_sensitive_word_with_options(request, runtime)

    def list_email_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.verification_status):
            query['VerificationStatus'] = request.verification_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEmailVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ListEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_email_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_email_verification_with_options(request, runtime)

    def lookup_tmch_notice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.claim_key):
            query['ClaimKey'] = request.claim_key
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupTmchNotice',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.LookupTmchNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    def lookup_tmch_notice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lookup_tmch_notice_with_options(request, runtime)

    def poll_task_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_result_status):
            query['TaskResultStatus'] = request.task_result_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PollTaskResult',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.PollTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    def poll_task_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.poll_task_result_with_options(request, runtime)

    def query_art_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryArtExtension',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_art_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_art_extension_with_options(request, runtime)

    def query_change_log_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChangeLogList',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryChangeLogListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_change_log_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_change_log_list_with_options(request, runtime)

    def query_contact_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContactInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_contact_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_contact_info_with_options(request, runtime)

    def query_dsrecord_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDSRecord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dsrecord(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dsrecord_with_options(request, runtime)

    def query_dns_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dns_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dns_host_with_options(request, runtime)

    def query_domain_by_domain_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByDomainName',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainByDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    def query_domain_by_domain_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_domain_name_with_options(request, runtime)

    def query_domain_by_instance_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByInstanceId',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_domain_by_instance_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_instance_id_with_options(request, runtime)

    def query_domain_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_expiration_date):
            query['EndExpirationDate'] = request.end_expiration_date
        if not UtilClient.is_unset(request.end_registration_date):
            query['EndRegistrationDate'] = request.end_registration_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_expiration_date):
            query['StartExpirationDate'] = request.start_expiration_date
        if not UtilClient.is_unset(request.start_registration_date):
            query['StartRegistrationDate'] = request.start_registration_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainList',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_domain_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    def query_domain_real_name_verification_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainRealNameVerificationInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryDomainRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_domain_real_name_verification_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_domain_real_name_verification_info_with_options(request, runtime)

    def query_ens_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEnsAssociation',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_ens_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_ens_association_with_options(request, runtime)

    def query_fail_reason_for_domain_real_name_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.real_name_verification_action):
            query['RealNameVerificationAction'] = request.real_name_verification_action
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailReasonForDomainRealNameVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryFailReasonForDomainRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_fail_reason_for_domain_real_name_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_domain_real_name_verification_with_options(request, runtime)

    def query_fail_reason_for_registrant_profile_real_name_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFailReasonForRegistrantProfileRealNameVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryFailReasonForRegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_fail_reason_for_registrant_profile_real_name_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_fail_reason_for_registrant_profile_real_name_verification_with_options(request, runtime)

    def query_local_ens_association_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocalEnsAssociation',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryLocalEnsAssociationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_local_ens_association(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_local_ens_association_with_options(request, runtime)

    def query_registrant_profile_real_name_verification_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fetch_image):
            query['FetchImage'] = request.fetch_image
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfileRealNameVerificationInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryRegistrantProfileRealNameVerificationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_registrant_profile_real_name_verification_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profile_real_name_verification_info_with_options(request, runtime)

    def query_registrant_profiles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.real_name_status):
            query['RealNameStatus'] = request.real_name_status
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRegistrantProfiles',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryRegistrantProfilesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_registrant_profiles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_registrant_profiles_with_options(request, runtime)

    def query_task_detail_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_name_cursor):
            query['DomainNameCursor'] = request.domain_name_cursor
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_detail_no_cursor):
            query['TaskDetailNoCursor'] = request.task_detail_no_cursor
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetailHistory',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskDetailHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_detail_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_history_with_options(request, runtime)

    def query_task_detail_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no):
            query['TaskNo'] = request.task_no
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskDetailList',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_detail_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_detail_list_with_options(request, runtime)

    def query_task_info_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.create_time_cursor):
            query['CreateTimeCursor'] = request.create_time_cursor
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_no_cursor):
            query['TaskNoCursor'] = request.task_no_cursor
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskInfoHistory',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskInfoHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_info_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_info_history_with_options(request, runtime)

    def query_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not UtilClient.is_unset(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskList',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_list_with_options(request, runtime)

    def query_transfer_in_by_instance_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferInByInstanceId',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferInByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_transfer_in_by_instance_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_by_instance_id_with_options(request, runtime)

    def query_transfer_in_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.simple_transfer_in_status):
            query['SimpleTransferInStatus'] = request.simple_transfer_in_status
        if not UtilClient.is_unset(request.submission_end_date):
            query['SubmissionEndDate'] = request.submission_end_date
        if not UtilClient.is_unset(request.submission_start_date):
            query['SubmissionStartDate'] = request.submission_start_date
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferInList',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferInListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_transfer_in_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_in_list_with_options(request, runtime)

    def query_transfer_out_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTransferOutInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.QueryTransferOutInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_transfer_out_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_transfer_out_info_with_options(request, runtime)

    def registrant_profile_real_name_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileID'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegistrantProfileRealNameVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.RegistrantProfileRealNameVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def registrant_profile_real_name_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.registrant_profile_real_name_verification_with_options(request, runtime)

    def resend_email_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendEmailVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.ResendEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def resend_email_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resend_email_verification_with_options(request, runtime)

    def save_batch_task_for_creating_order_activate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_activate_param):
            query['OrderActivateParam'] = request.order_activate_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderActivate',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_creating_order_activate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_activate_with_options(request, runtime)

    def save_batch_task_for_creating_order_redeem_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_redeem_param):
            query['OrderRedeemParam'] = request.order_redeem_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderRedeem',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_creating_order_redeem(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_redeem_with_options(request, runtime)

    def save_batch_task_for_creating_order_renew_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_renew_param):
            query['OrderRenewParam'] = request.order_renew_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderRenew',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_creating_order_renew(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_renew_with_options(request, runtime)

    def save_batch_task_for_creating_order_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order_transfer_param):
            query['OrderTransferParam'] = request.order_transfer_param
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForCreatingOrderTransfer',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_creating_order_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_creating_order_transfer_with_options(request, runtime)

    def save_batch_task_for_domain_name_proxy_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForDomainNameProxyService',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_domain_name_proxy_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_domain_name_proxy_service_with_options(request, runtime)

    def save_batch_task_for_modifying_domain_dns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_name_server):
            query['DomainNameServer'] = request.domain_name_server
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForModifyingDomainDns',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForModifyingDomainDnsResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_modifying_domain_dns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_modifying_domain_dns_with_options(request, runtime)

    def save_batch_task_for_reserve_drop_list_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForReserveDropListDomain',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForReserveDropListDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_reserve_drop_list_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_reserve_drop_list_domain_with_options(request, runtime)

    def save_batch_task_for_transfer_prohibition_lock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForTransferProhibitionLock',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_transfer_prohibition_lock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_transfer_prohibition_lock_with_options(request, runtime)

    def save_batch_task_for_update_prohibition_lock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdateProhibitionLock',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_update_prohibition_lock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_update_prohibition_lock_with_options(request, runtime)

    def save_batch_task_for_updating_contact_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_with_options(request, runtime)

    def save_batch_task_for_updating_contact_info_by_new_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveBatchTaskForUpdatingContactInfoByNewContact',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveBatchTaskForUpdatingContactInfoByNewContactResponse(),
            self.call_api(params, req, runtime)
        )

    def save_batch_task_for_updating_contact_info_by_new_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_batch_task_for_updating_contact_info_by_new_contact_with_options(request, runtime)

    def save_registrant_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.default_registrant_profile):
            query['DefaultRegistrantProfile'] = request.default_registrant_profile
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_profile_type):
            query['RegistrantProfileType'] = request.registrant_profile_type
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRegistrantProfile',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveRegistrantProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def save_registrant_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_registrant_profile_with_options(request, runtime)

    def save_single_task_for_adding_dsrecord_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.digest_type):
            query['DigestType'] = request.digest_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForAddingDSRecord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForAddingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_adding_dsrecord(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_adding_dsrecord_with_options(request, runtime)

    def save_single_task_for_approving_transfer_out_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForApprovingTransferOut',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForApprovingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_approving_transfer_out(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_approving_transfer_out_with_options(request, runtime)

    def save_single_task_for_associating_ens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForAssociatingEns',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForAssociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_associating_ens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_associating_ens_with_options(request, runtime)

    def save_single_task_for_canceling_transfer_in_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCancelingTransferIn',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCancelingTransferInResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_in(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_in_with_options(request, runtime)

    def save_single_task_for_canceling_transfer_out_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCancelingTransferOut',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCancelingTransferOutResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_canceling_transfer_out(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_canceling_transfer_out_with_options(request, runtime)

    def save_single_task_for_creating_dns_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_creating_dns_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_dns_host_with_options(request, runtime)

    def save_single_task_for_creating_order_activate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.dns_1):
            query['Dns1'] = request.dns_1
        if not UtilClient.is_unset(request.dns_2):
            query['Dns2'] = request.dns_2
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.enable_domain_proxy):
            query['EnableDomainProxy'] = request.enable_domain_proxy
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permit_premium_activation):
            query['PermitPremiumActivation'] = request.permit_premium_activation
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.trademark_domain_activation):
            query['TrademarkDomainActivation'] = request.trademark_domain_activation
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderActivate',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderActivateResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_creating_order_activate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_activate_with_options(request, runtime)

    def save_single_task_for_creating_order_redeem_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderRedeem',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_creating_order_redeem(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_redeem_with_options(request, runtime)

    def save_single_task_for_creating_order_renew_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.current_expiration_date):
            query['CurrentExpirationDate'] = request.current_expiration_date
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.subscription_duration):
            query['SubscriptionDuration'] = request.subscription_duration
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderRenew',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderRenewResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_creating_order_renew(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_renew_with_options(request, runtime)

    def save_single_task_for_creating_order_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorization_code):
            query['AuthorizationCode'] = request.authorization_code
        if not UtilClient.is_unset(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permit_premium_transfer):
            query['PermitPremiumTransfer'] = request.permit_premium_transfer
        if not UtilClient.is_unset(request.promotion_no):
            query['PromotionNo'] = request.promotion_no
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.use_coupon):
            query['UseCoupon'] = request.use_coupon
        if not UtilClient.is_unset(request.use_promotion):
            query['UsePromotion'] = request.use_promotion
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForCreatingOrderTransfer',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForCreatingOrderTransferResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_creating_order_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_creating_order_transfer_with_options(request, runtime)

    def save_single_task_for_deleting_dsrecord_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDeletingDSRecord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDeletingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_deleting_dsrecord(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dsrecord_with_options(request, runtime)

    def save_single_task_for_deleting_dns_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDeletingDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDeletingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_deleting_dns_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_deleting_dns_host_with_options(request, runtime)

    def save_single_task_for_disassociating_ens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDisassociatingEns',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDisassociatingEnsResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_disassociating_ens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_disassociating_ens_with_options(request, runtime)

    def save_single_task_for_domain_name_proxy_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForDomainNameProxyService',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForDomainNameProxyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_domain_name_proxy_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_domain_name_proxy_service_with_options(request, runtime)

    def save_single_task_for_modifying_dsrecord_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.digest):
            query['Digest'] = request.digest
        if not UtilClient.is_unset(request.digest_type):
            query['DigestType'] = request.digest_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.key_tag):
            query['KeyTag'] = request.key_tag
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForModifyingDSRecord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForModifyingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_modifying_dsrecord(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dsrecord_with_options(request, runtime)

    def save_single_task_for_modifying_dns_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dns_name):
            query['DnsName'] = request.dns_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForModifyingDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForModifyingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_modifying_dns_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_modifying_dns_host_with_options(request, runtime)

    def save_single_task_for_querying_transfer_authorization_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForQueryingTransferAuthorizationCode',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForQueryingTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_querying_transfer_authorization_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_querying_transfer_authorization_code_with_options(request, runtime)

    def save_single_task_for_save_art_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_or_period):
            query['DateOrPeriod'] = request.date_or_period
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.features):
            query['Features'] = request.features
        if not UtilClient.is_unset(request.inscriptions_and_markings):
            query['InscriptionsAndMarkings'] = request.inscriptions_and_markings
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.maker):
            query['Maker'] = request.maker
        if not UtilClient.is_unset(request.materials_and_techniques):
            query['MaterialsAndTechniques'] = request.materials_and_techniques
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.reference):
            query['Reference'] = request.reference
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSaveArtExtension',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSaveArtExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_save_art_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_save_art_extension_with_options(request, runtime)

    def save_single_task_for_synchronizing_dsrecord_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSynchronizingDSRecord',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSynchronizingDSRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dsrecord(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dsrecord_with_options(request, runtime)

    def save_single_task_for_synchronizing_dns_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForSynchronizingDnsHost',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForSynchronizingDnsHostResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_synchronizing_dns_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_synchronizing_dns_host_with_options(request, runtime)

    def save_single_task_for_transfer_prohibition_lock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForTransferProhibitionLock',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForTransferProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_transfer_prohibition_lock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_transfer_prohibition_lock_with_options(request, runtime)

    def save_single_task_for_update_prohibition_lock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForUpdateProhibitionLock',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForUpdateProhibitionLockResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_update_prohibition_lock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_update_prohibition_lock_with_options(request, runtime)

    def save_single_task_for_updating_contact_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not UtilClient.is_unset(request.contact_type):
            query['ContactType'] = request.contact_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveSingleTaskForUpdatingContactInfo',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveSingleTaskForUpdatingContactInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def save_single_task_for_updating_contact_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_single_task_for_updating_contact_info_with_options(request, runtime)

    def save_task_for_submitting_domain_delete_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainDelete',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task_for_submitting_domain_delete(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_delete_with_options(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredential',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_identity_credential_with_options(request, runtime)

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileID',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForSubmittingDomainRealNameVerificationByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_idwith_options(request, runtime)

    def save_task_for_updating_registrant_info_by_identity_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.identity_credential_no):
            query['IdentityCredentialNo'] = request.identity_credential_no
        if not UtilClient.is_unset(request.identity_credential_type):
            query['IdentityCredentialType'] = request.identity_credential_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        body = {}
        if not UtilClient.is_unset(request.identity_credential):
            body['IdentityCredential'] = request.identity_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByIdentityCredential',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByIdentityCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_identity_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_identity_credential_with_options(request, runtime)

    def save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.registrant_profile_id):
            query['RegistrantProfileId'] = request.registrant_profile_id
        if not UtilClient.is_unset(request.transfer_out_prohibited):
            query['TransferOutProhibited'] = request.transfer_out_prohibited
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTaskForUpdatingRegistrantInfoByRegistrantProfileID',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SaveTaskForUpdatingRegistrantInfoByRegistrantProfileIDResponse(),
            self.call_api(params, req, runtime)
        )

    def save_task_for_updating_registrant_info_by_registrant_profile_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_task_for_updating_registrant_info_by_registrant_profile_idwith_options(request, runtime)

    def submit_email_verification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.send_if_exist):
            query['SendIfExist'] = request.send_if_exist
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitEmailVerification',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.SubmitEmailVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_email_verification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_email_verification_with_options(request, runtime)

    def transfer_in_check_mail_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInCheckMailToken',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInCheckMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_in_check_mail_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_check_mail_token_with_options(request, runtime)

    def transfer_in_reenter_transfer_authorization_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.transfer_authorization_code):
            query['TransferAuthorizationCode'] = request.transfer_authorization_code
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInReenterTransferAuthorizationCode',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInReenterTransferAuthorizationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_in_reenter_transfer_authorization_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_reenter_transfer_authorization_code_with_options(request, runtime)

    def transfer_in_refetch_whois_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInRefetchWhoisEmail',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInRefetchWhoisEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_in_refetch_whois_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_refetch_whois_email_with_options(request, runtime)

    def transfer_in_resend_mail_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInResendMailToken',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.TransferInResendMailTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_in_resend_mail_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_in_resend_mail_token_with_options(request, runtime)

    def verify_contact_field_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            query['City'] = request.city
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.registrant_name):
            query['RegistrantName'] = request.registrant_name
        if not UtilClient.is_unset(request.registrant_organization):
            query['RegistrantOrganization'] = request.registrant_organization
        if not UtilClient.is_unset(request.registrant_type):
            query['RegistrantType'] = request.registrant_type
        if not UtilClient.is_unset(request.tel_area):
            query['TelArea'] = request.tel_area
        if not UtilClient.is_unset(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyContactField',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.VerifyContactFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_contact_field(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_contact_field_with_options(request, runtime)

    def verify_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        if not UtilClient.is_unset(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyEmail',
            version='2017-12-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            domain_intl_20171218_models.VerifyEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)
