# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dm20170622 import models as dm_20170622_models
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
        self._endpoint = self.get_endpoint('dm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_ipfilter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_address):
            query['IpAddress'] = request.ip_address
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpfilter',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.AddIpfilterResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ipfilter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ipfilter_with_options(request, runtime)

    def batch_send_mail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSendMail',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.BatchSendMailResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_send_mail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_send_mail_with_options(request, runtime)

    def check_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomain',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def check_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    def check_domain_dns_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDomainDns',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CheckDomainDnsResponse(),
            self.call_api(params, req, runtime)
        )

    def check_domain_dns(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_domain_dns_with_options(request, runtime)

    def create_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_mail_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMailAddress',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CreateMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mail_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mail_address_with_options(request, runtime)

    def create_receiver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receivers_alias):
            query['ReceiversAlias'] = request.receivers_alias
        if not UtilClient.is_unset(request.receivers_name):
            query['ReceiversName'] = request.receivers_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReceiver',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CreateReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    def create_receiver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_receiver_with_options(request, runtime)

    def create_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.sms_type):
            query['SmsType'] = request.sms_type
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_nick_name):
            query['TemplateNickName'] = request.template_nick_name
        if not UtilClient.is_unset(request.template_subject):
            query['TemplateSubject'] = request.template_subject
        if not UtilClient.is_unset(request.template_text):
            query['TemplateText'] = request.template_text
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def delete_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    def delete_mail_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMailAddress',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DeleteMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mail_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mail_address_with_options(request, runtime)

    def delete_receiver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReceiver',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DeleteReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_receiver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_receiver_with_options(request, runtime)

    def delete_receiver_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReceiverDetail',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DeleteReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_receiver_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_receiver_detail_with_options(request, runtime)

    def delete_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def desc_account_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescAccountSummary',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DescAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def desc_account_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.desc_account_summary_with_options(request, runtime)

    def desc_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.require_real_time_dns_records):
            query['RequireRealTimeDnsRecords'] = request.require_real_time_dns_records
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescDomain',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DescDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def desc_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.desc_domain_with_options(request, runtime)

    def desc_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescTemplate',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.DescTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def desc_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.desc_template_with_options(request, runtime)

    def get_account_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not UtilClient.is_unset(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountList',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.GetAccountListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_list_with_options(request, runtime)

    def get_mail_address_msg_call_back_url_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetMailAddressMsgCallBackUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMailAddressMsgCallBackUrlResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_from):
            query['MailFrom'] = request.mail_from
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMailAddressMsgCallBackUrl',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.GetMailAddressMsgCallBackUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mail_address_msg_call_back_url(self, request):
        """
        @deprecated
        

        @param request: GetMailAddressMsgCallBackUrlRequest

        @return: GetMailAddressMsgCallBackUrlResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mail_address_msg_call_back_url_with_options(request, runtime)

    def get_track_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.offset_create_time):
            query['OffsetCreateTime'] = request.offset_create_time
        if not UtilClient.is_unset(request.offset_create_time_desc):
            query['OffsetCreateTimeDesc'] = request.offset_create_time_desc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total):
            query['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrackList',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.GetTrackListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_track_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_track_list_with_options(request, runtime)

    def modify_mail_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mail_address_id):
            query['MailAddressId'] = request.mail_address_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMailAddress',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.ModifyMailAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_mail_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_mail_address_with_options(request, runtime)

    def modify_pwby_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPWByDomain',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.ModifyPWByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_pwby_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_pwby_domain_with_options(request, runtime)

    def modify_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTag',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.ModifyTagResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_with_options(request, runtime)

    def modify_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sms_content):
            query['SmsContent'] = request.sms_content
        if not UtilClient.is_unset(request.sms_type):
            query['SmsType'] = request.sms_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_nick_name):
            query['TemplateNickName'] = request.template_nick_name
        if not UtilClient.is_unset(request.template_subject):
            query['TemplateSubject'] = request.template_subject
        if not UtilClient.is_unset(request.template_text):
            query['TemplateText'] = request.template_text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplate',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.ModifyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    def query_domain_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDomainByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryDomainByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def query_domain_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_domain_by_param_with_options(request, runtime)

    def query_invalid_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInvalidAddress',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryInvalidAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def query_invalid_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_invalid_address_with_options(request, runtime)

    def query_mail_address_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sendtype):
            query['Sendtype'] = request.sendtype
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMailAddressByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryMailAddressByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mail_address_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mail_address_by_param_with_options(request, runtime)

    def query_receiver_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReceiverByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryReceiverByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def query_receiver_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_receiver_by_param_with_options(request, runtime)

    def query_receiver_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReceiverDetail',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_receiver_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_receiver_detail_with_options(request, runtime)

    def query_tag_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryTagByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tag_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tag_by_param_with_options(request, runtime)

    def query_task_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryTaskByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_by_param_with_options(request, runtime)

    def query_template_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_type):
            query['FromType'] = request.from_type
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.QueryTemplateByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def query_template_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_template_by_param_with_options(request, runtime)

    def save_receiver_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['Detail'] = request.detail
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.receiver_id):
            query['ReceiverId'] = request.receiver_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveReceiverDetail',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.SaveReceiverDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def save_receiver_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_receiver_detail_with_options(request, runtime)

    def sender_statistics_by_tag_name_and_batch_idwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SenderStatisticsByTagNameAndBatchID',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.SenderStatisticsByTagNameAndBatchIDResponse(),
            self.call_api(params, req, runtime)
        )

    def sender_statistics_by_tag_name_and_batch_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sender_statistics_by_tag_name_and_batch_idwith_options(request, runtime)

    def sender_statistics_detail_by_param_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.next_start):
            query['NextStart'] = request.next_start
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SenderStatisticsDetailByParam',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.SenderStatisticsDetailByParamResponse(),
            self.call_api(params, req, runtime)
        )

    def sender_statistics_detail_by_param(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sender_statistics_detail_by_param_with_options(request, runtime)

    def single_send_mail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.from_alias):
            query['FromAlias'] = request.from_alias
        if not UtilClient.is_unset(request.html_body):
            query['HtmlBody'] = request.html_body
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.reply_to_address):
            query['ReplyToAddress'] = request.reply_to_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.text_body):
            query['TextBody'] = request.text_body
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleSendMail',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.SingleSendMailResponse(),
            self.call_api(params, req, runtime)
        )

    def single_send_mail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.single_send_mail_with_options(request, runtime)

    def single_send_mail_v2with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = dm_20170622_models.SingleSendMailV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.html_body_place_holders):
            request.html_body_place_holders_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.html_body_place_holders, 'HtmlBodyPlaceHolders', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.click_trace):
            query['ClickTrace'] = request.click_trace
        if not UtilClient.is_unset(request.from_alias):
            query['FromAlias'] = request.from_alias
        if not UtilClient.is_unset(request.html_body):
            query['HtmlBody'] = request.html_body
        if not UtilClient.is_unset(request.html_body_place_holders_shrink):
            query['HtmlBodyPlaceHolders'] = request.html_body_place_holders_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.reply_address):
            query['ReplyAddress'] = request.reply_address
        if not UtilClient.is_unset(request.reply_address_alias):
            query['ReplyAddressAlias'] = request.reply_address_alias
        if not UtilClient.is_unset(request.reply_to_address):
            query['ReplyToAddress'] = request.reply_to_address
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        if not UtilClient.is_unset(request.text_body):
            query['TextBody'] = request.text_body
        if not UtilClient.is_unset(request.to_address):
            query['ToAddress'] = request.to_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleSendMailV2',
            version='2017-06-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dm_20170622_models.SingleSendMailV2Response(),
            self.call_api(params, req, runtime)
        )

    def single_send_mail_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.single_send_mail_v2with_options(request, runtime)
