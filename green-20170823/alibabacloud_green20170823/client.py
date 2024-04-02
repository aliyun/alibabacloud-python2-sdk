# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20170823 import models as green_20170823_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def audit_item_submit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditItemSubmit',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.AuditItemSubmitResponse(),
            self.call_api(params, req, runtime)
        )

    def audit_item_submit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.audit_item_submit_with_options(request, runtime)

    def creat_custom_ocr_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.img_url):
            query['ImgUrl'] = request.img_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recognize_area):
            query['RecognizeArea'] = request.recognize_area
        if not UtilClient.is_unset(request.refer_area):
            query['ReferArea'] = request.refer_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreatCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def creat_custom_ocr_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.creat_custom_ocr_template_with_options(request, runtime)

    def create_audit_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_suggestions):
            query['CallbackSuggestions'] = request.callback_suggestions
        if not UtilClient.is_unset(request.callback_types):
            query['CallbackTypes'] = request.callback_types
        if not UtilClient.is_unset(request.crypt_type):
            query['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateAuditCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def create_audit_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_audit_callback_with_options(request, runtime)

    def create_biz_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_import):
            query['BizTypeImport'] = request.biz_type_import
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.cite_template):
            query['CiteTemplate'] = request.cite_template
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.industry_info):
            query['IndustryInfo'] = request.industry_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_biz_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_biz_type_with_options(request, runtime)

    def create_cdi_bag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdiBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cdi_bag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cdi_bag_with_options(request, runtime)

    def create_cdi_base_bag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBaseBagResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cdi_base_bag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cdi_base_bag_with_options(request, runtime)

    def create_image_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_lib_with_options(request, runtime)

    def create_keyword_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_keyword(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_keyword_with_options(request, runtime)

    def create_keyword_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    def create_keyword_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_keyword_lib_with_options(request, runtime)

    def create_web_site_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebSiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_web_site_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_web_site_instance_with_options(request, runtime)

    def create_website_index_page_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebsiteIndexPageBaseline',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebsiteIndexPageBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_website_index_page_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_website_index_page_baseline_with_options(request, runtime)

    def delete_biz_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_biz_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_type_with_options(request, runtime)

    def delete_custom_ocr_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_ocr_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_ocr_template_with_options(request, runtime)

    def delete_image_from_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageFromLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image_from_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_from_lib_with_options(request, runtime)

    def delete_image_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_lib_with_options(request, runtime)

    def delete_keyword_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_keyword(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_with_options(request, runtime)

    def delete_keyword_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_keyword_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_lib_with_options(request, runtime)

    def delete_notification_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_types):
            query['ContactTypes'] = request.contact_types
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationContacts',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteNotificationContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_notification_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_contacts_with_options(request, runtime)

    def describe_app_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info_with_options(request, runtime)

    def describe_audit_callback_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_callback(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_callback_with_options(runtime)

    def describe_audit_callback_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditCallbackList',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_callback_list(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_callback_list_with_options(runtime)

    def describe_audit_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keyword_id):
            query['KeywordId'] = request.keyword_id
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_content_with_options(request, runtime)

    def describe_audit_content_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditContentItem',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_content_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_content_item_with_options(request, runtime)

    def describe_audit_range_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAuditRange',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_range(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_range_with_options(runtime)

    def describe_audit_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_setting_with_options(request, runtime)

    def describe_biz_type_image_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_biz_type_image_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_image_lib_with_options(request, runtime)

    def describe_biz_type_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_biz_type_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_setting_with_options(request, runtime)

    def describe_biz_type_text_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypeTextLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeTextLibResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_biz_type_text_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_text_lib_with_options(request, runtime)

    def describe_biz_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.import_flag):
            query['ImportFlag'] = request.import_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizTypes',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_biz_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_types_with_options(request, runtime)

    def describe_cloud_monitor_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMonitorServices',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCloudMonitorServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cloud_monitor_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_monitor_services_with_options(request, runtime)

    def describe_custom_ocr_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_ocr_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_ocr_template_with_options(request, runtime)

    def describe_image_from_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image_lib_id):
            query['ImageLibId'] = request.image_lib_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageFromLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_from_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_from_lib_with_options(request, runtime)

    def describe_image_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_lib_with_options(request, runtime)

    def describe_image_upload_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageUploadInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_upload_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_upload_info_with_options(request, runtime)

    def describe_keyword_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyword',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_keyword(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_keyword_with_options(request, runtime)

    def describe_keyword_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.service_module):
            query['ServiceModule'] = request.service_module
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_keyword_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_keyword_lib_with_options(request, runtime)

    def describe_notification_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeNotificationSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_notification_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_setting_with_options(request, runtime)

    def describe_open_api_rcp_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiRcpStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiRcpStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_open_api_rcp_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_rcp_stats_with_options(request, runtime)

    def describe_open_api_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiUsage',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_open_api_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_usage_with_options(request, runtime)

    def describe_oss_callback_setting_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssCallbackSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssCallbackSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_callback_setting(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_callback_setting_with_options(runtime)

    def describe_oss_increment_check_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementCheckSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementCheckSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_increment_check_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_check_setting_with_options(request, runtime)

    def describe_oss_increment_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementOverview',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_increment_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_overview_with_options(request, runtime)

    def describe_oss_increment_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssIncrementStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_increment_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_stats_with_options(request, runtime)

    def describe_oss_result_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_score):
            query['MaxScore'] = request.max_score
        if not UtilClient.is_unset(request.min_score):
            query['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.object):
            query['Object'] = request.object
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssResultItems',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssResultItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_result_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_result_items_with_options(request, runtime)

    def describe_oss_stock_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssStockStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssStockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_stock_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_stock_status_with_options(request, runtime)

    def describe_sdk_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSdkUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeSdkUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sdk_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url_with_options(request, runtime)

    def describe_update_package_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpdatePackageResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUpdatePackageResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_update_package_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result_with_options(request, runtime)

    def describe_upload_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz):
            query['Biz'] = request.biz
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUploadInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_upload_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info_with_options(request, runtime)

    def describe_usage_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageBill',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUsageBillResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_bill(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_bill_with_options(request, runtime)

    def describe_user_biz_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customized):
            query['Customized'] = request.customized
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBizTypes',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserBizTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_biz_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_biz_types_with_options(request, runtime)

    def describe_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    def describe_view_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_id):
            query['DataId'] = request.data_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.keyword_id):
            query['KeywordId'] = request.keyword_id
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lib_type):
            query['LibType'] = request.lib_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeViewContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeViewContentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_view_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_view_content_with_options(request, runtime)

    def describe_website_index_page_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteIndexPageBaseline',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteIndexPageBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_index_page_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_index_page_baseline_with_options(request, runtime)

    def describe_website_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_with_options(request, runtime)

    def describe_website_instance_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstanceId',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_instance_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_id_with_options(request, runtime)

    def describe_website_instance_key_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteInstanceKeyUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_instance_key_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_key_url_with_options(request, runtime)

    def describe_website_scan_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.handle_status):
            query['HandleStatus'] = request.handle_status
        if not UtilClient.is_unset(request.label):
            query['Label'] = request.label
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_url):
            query['SiteUrl'] = request.site_url
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.sub_service_module):
            query['SubServiceModule'] = request.sub_service_module
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteScanResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_scan_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_scan_result_with_options(request, runtime)

    def describe_website_scan_result_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteScanResultDetail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_scan_result_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_scan_result_detail_with_options(request, runtime)

    def describe_website_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteStat',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteStatResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_stat_with_options(request, runtime)

    def describe_website_verify_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebsiteVerifyInfo',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteVerifyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_website_verify_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_website_verify_info_with_options(request, runtime)

    def export_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportKeywords',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    def export_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_keywords_with_options(request, runtime)

    def export_open_api_rcp_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportOpenApiRcpStats',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOpenApiRcpStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def export_open_api_rcp_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_open_api_rcp_stats_with_options(request, runtime)

    def export_oss_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_score):
            query['MaxScore'] = request.max_score
        if not UtilClient.is_unset(request.min_score):
            query['MinScore'] = request.min_score
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        if not UtilClient.is_unset(request.stock_task_id):
            query['StockTaskId'] = request.stock_task_id
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.total_count):
            query['TotalCount'] = request.total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportOssResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOssResultResponse(),
            self.call_api(params, req, runtime)
        )

    def export_oss_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_oss_result_with_options(request, runtime)

    def get_audit_item_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditItemDetail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_audit_item_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audit_item_detail_with_options(request, runtime)

    def get_audit_item_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuditItemList',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditItemListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_audit_item_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_audit_item_list_with_options(request, runtime)

    def get_audit_user_conf_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAuditUserConf',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.GetAuditUserConfResponse(),
            self.call_api(params, req, runtime)
        )

    def get_audit_user_conf(self):
        runtime = util_models.RuntimeOptions()
        return self.get_audit_user_conf_with_options(runtime)

    def import_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword_lib_id):
            query['KeywordLibId'] = request.keyword_lib_id
        if not UtilClient.is_unset(request.keywords_object):
            query['KeywordsObject'] = request.keywords_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeywords',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.ImportKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    def import_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_keywords_with_options(request, runtime)

    def mark_audit_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_illegal_reasons):
            query['AuditIllegalReasons'] = request.audit_illegal_reasons
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkAuditContent',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentResponse(),
            self.call_api(params, req, runtime)
        )

    def mark_audit_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mark_audit_content_with_options(request, runtime)

    def mark_audit_content_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_illegal_reasons):
            query['AuditIllegalReasons'] = request.audit_illegal_reasons
        if not UtilClient.is_unset(request.audit_result):
            query['AuditResult'] = request.audit_result
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkAuditContentItem',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentItemResponse(),
            self.call_api(params, req, runtime)
        )

    def mark_audit_content_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mark_audit_content_item_with_options(request, runtime)

    def mark_oss_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stock):
            query['Stock'] = request.stock
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkOssResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkOssResultResponse(),
            self.call_api(params, req, runtime)
        )

    def mark_oss_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mark_oss_result_with_options(request, runtime)

    def mark_website_scan_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MarkWebsiteScanResult',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.MarkWebsiteScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    def mark_website_scan_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mark_website_scan_result_with_options(request, runtime)

    def refund_cdi_bag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundCdiBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBagResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_cdi_bag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_cdi_bag_with_options(request, runtime)

    def refund_cdi_base_bag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBaseBagResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_cdi_base_bag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_cdi_base_bag_with_options(request, runtime)

    def refund_web_site_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RefundWebSiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def refund_web_site_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refund_web_site_instance_with_options(request, runtime)

    def renew_web_site_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_num):
            query['OrderNum'] = request.order_num
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewWebSiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.RenewWebSiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_web_site_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_web_site_instance_with_options(request, runtime)

    def send_verify_code_to_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCodeToEmail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verify_code_to_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_to_email_with_options(request, runtime)

    def send_verify_code_to_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCodeToPhone',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verify_code_to_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_to_phone_with_options(request, runtime)

    def send_website_feedback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendWebsiteFeedback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.SendWebsiteFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    def send_website_feedback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_website_feedback_with_options(request, runtime)

    def update_app_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug):
            query['Debug'] = request.debug
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppPackage',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAppPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_package_with_options(request, runtime)

    def update_audit_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.crypt_type):
            query['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditCallback',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def update_audit_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_audit_callback_with_options(request, runtime)

    def update_audit_range_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_range):
            query['AuditRange'] = request.audit_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditRange',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditRangeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_audit_range(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_audit_range_with_options(request, runtime)

    def update_audit_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_range):
            query['AuditRange'] = request.audit_range
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.seed):
            query['Seed'] = request.seed
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuditSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_audit_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_audit_setting_with_options(request, runtime)

    def update_biz_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizType',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_biz_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_with_options(request, runtime)

    def update_biz_type_image_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.black):
            query['Black'] = request.black
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.review):
            query['Review'] = request.review
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.white):
            query['White'] = request.white
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeImageLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    def update_biz_type_image_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_image_lib_with_options(request, runtime)

    def update_biz_type_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad):
            query['Ad'] = request.ad
        if not UtilClient.is_unset(request.antispam):
            query['Antispam'] = request.antispam
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.live):
            query['Live'] = request.live
        if not UtilClient.is_unset(request.porn):
            query['Porn'] = request.porn
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.terrorism):
            query['Terrorism'] = request.terrorism
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_biz_type_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_setting_with_options(request, runtime)

    def update_biz_type_text_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type_name):
            query['BizTypeName'] = request.biz_type_name
        if not UtilClient.is_unset(request.black):
            query['Black'] = request.black
        if not UtilClient.is_unset(request.ignore):
            query['Ignore'] = request.ignore
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.review):
            query['Review'] = request.review
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.white):
            query['White'] = request.white
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizTypeTextLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeTextLibResponse(),
            self.call_api(params, req, runtime)
        )

    def update_biz_type_text_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_text_lib_with_options(request, runtime)

    def update_custom_ocr_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recognize_area):
            query['RecognizeArea'] = request.recognize_area
        if not UtilClient.is_unset(request.refer_area):
            query['ReferArea'] = request.refer_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_ocr_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_custom_ocr_template_with_options(request, runtime)

    def update_keyword_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_types):
            query['BizTypes'] = request.biz_types
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.match_mode):
            query['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKeywordLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    def update_keyword_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_keyword_lib_with_options(request, runtime)

    def update_notification_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.realtime_message_list):
            query['RealtimeMessageList'] = request.realtime_message_list
        if not UtilClient.is_unset(request.reminder_mode_list):
            query['ReminderModeList'] = request.reminder_mode_list
        if not UtilClient.is_unset(request.schedule_message_time):
            query['ScheduleMessageTime'] = request.schedule_message_time
        if not UtilClient.is_unset(request.schedule_message_time_zone):
            query['ScheduleMessageTimeZone'] = request.schedule_message_time_zone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNotificationSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateNotificationSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_notification_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_notification_setting_with_options(request, runtime)

    def update_oss_callback_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_callback):
            query['AuditCallback'] = request.audit_callback
        if not UtilClient.is_unset(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.scan_callback):
            query['ScanCallback'] = request.scan_callback
        if not UtilClient.is_unset(request.scan_callback_suggestions):
            query['ScanCallbackSuggestions'] = request.scan_callback_suggestions
        if not UtilClient.is_unset(request.service_modules):
            query['ServiceModules'] = request.service_modules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssCallbackSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssCallbackSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_oss_callback_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_oss_callback_setting_with_options(request, runtime)

    def update_oss_increment_check_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_antispam_freeze_config):
            query['AudioAntispamFreezeConfig'] = request.audio_antispam_freeze_config
        if not UtilClient.is_unset(request.audio_auto_freeze_opened):
            query['AudioAutoFreezeOpened'] = request.audio_auto_freeze_opened
        if not UtilClient.is_unset(request.audio_max_size):
            query['AudioMaxSize'] = request.audio_max_size
        if not UtilClient.is_unset(request.audio_scan_limit):
            query['AudioScanLimit'] = request.audio_scan_limit
        if not UtilClient.is_unset(request.audio_scene_list):
            query['AudioSceneList'] = request.audio_scene_list
        if not UtilClient.is_unset(request.auto_freeze_type):
            query['AutoFreezeType'] = request.auto_freeze_type
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.bucket_config_list):
            query['BucketConfigList'] = request.bucket_config_list
        if not UtilClient.is_unset(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not UtilClient.is_unset(request.image_ad_freeze_config):
            query['ImageAdFreezeConfig'] = request.image_ad_freeze_config
        if not UtilClient.is_unset(request.image_auto_freeze):
            query['ImageAutoFreeze'] = request.image_auto_freeze
        if not UtilClient.is_unset(request.image_auto_freeze_opened):
            query['ImageAutoFreezeOpened'] = request.image_auto_freeze_opened
        if not UtilClient.is_unset(request.image_live_freeze_config):
            query['ImageLiveFreezeConfig'] = request.image_live_freeze_config
        if not UtilClient.is_unset(request.image_porn_freeze_config):
            query['ImagePornFreezeConfig'] = request.image_porn_freeze_config
        if not UtilClient.is_unset(request.image_scan_limit):
            query['ImageScanLimit'] = request.image_scan_limit
        if not UtilClient.is_unset(request.image_scene_list):
            query['ImageSceneList'] = request.image_scene_list
        if not UtilClient.is_unset(request.image_terrorism_freeze_config):
            query['ImageTerrorismFreezeConfig'] = request.image_terrorism_freeze_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scan_image_no_file_type):
            query['ScanImageNoFileType'] = request.scan_image_no_file_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.video_ad_freeze_config):
            query['VideoAdFreezeConfig'] = request.video_ad_freeze_config
        if not UtilClient.is_unset(request.video_auto_freeze_opened):
            query['VideoAutoFreezeOpened'] = request.video_auto_freeze_opened
        if not UtilClient.is_unset(request.video_auto_freeze_scene_list):
            query['VideoAutoFreezeSceneList'] = request.video_auto_freeze_scene_list
        if not UtilClient.is_unset(request.video_frame_interval):
            query['VideoFrameInterval'] = request.video_frame_interval
        if not UtilClient.is_unset(request.video_live_freeze_config):
            query['VideoLiveFreezeConfig'] = request.video_live_freeze_config
        if not UtilClient.is_unset(request.video_max_frames):
            query['VideoMaxFrames'] = request.video_max_frames
        if not UtilClient.is_unset(request.video_max_size):
            query['VideoMaxSize'] = request.video_max_size
        if not UtilClient.is_unset(request.video_porn_freeze_config):
            query['VideoPornFreezeConfig'] = request.video_porn_freeze_config
        if not UtilClient.is_unset(request.video_scan_limit):
            query['VideoScanLimit'] = request.video_scan_limit
        if not UtilClient.is_unset(request.video_scene_list):
            query['VideoSceneList'] = request.video_scene_list
        if not UtilClient.is_unset(request.video_terrorism_freeze_config):
            query['VideoTerrorismFreezeConfig'] = request.video_terrorism_freeze_config
        if not UtilClient.is_unset(request.video_voice_antispam_freeze_config):
            query['VideoVoiceAntispamFreezeConfig'] = request.video_voice_antispam_freeze_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssIncrementCheckSetting',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssIncrementCheckSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_oss_increment_check_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_oss_increment_check_setting_with_options(request, runtime)

    def update_oss_stock_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_auto_freeze_scene_list):
            query['AudioAutoFreezeSceneList'] = request.audio_auto_freeze_scene_list
        if not UtilClient.is_unset(request.audio_max_size):
            query['AudioMaxSize'] = request.audio_max_size
        if not UtilClient.is_unset(request.auto_freeze_type):
            query['AutoFreezeType'] = request.auto_freeze_type
        if not UtilClient.is_unset(request.bucket_config_list):
            query['BucketConfigList'] = request.bucket_config_list
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.image_auto_freeze):
            query['ImageAutoFreeze'] = request.image_auto_freeze
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.scene_list):
            query['SceneList'] = request.scene_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.video_auto_freeze_scene_list):
            query['VideoAutoFreezeSceneList'] = request.video_auto_freeze_scene_list
        if not UtilClient.is_unset(request.video_frame_interval):
            query['VideoFrameInterval'] = request.video_frame_interval
        if not UtilClient.is_unset(request.video_max_frames):
            query['VideoMaxFrames'] = request.video_max_frames
        if not UtilClient.is_unset(request.video_max_size):
            query['VideoMaxSize'] = request.video_max_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssStockStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssStockStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_oss_stock_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_oss_stock_status_with_options(request, runtime)

    def update_website_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.index_page):
            query['IndexPage'] = request.index_page
        if not UtilClient.is_unset(request.index_page_scan_interval):
            query['IndexPageScanInterval'] = request.index_page_scan_interval
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.site_protocol):
            query['SiteProtocol'] = request.site_protocol
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.website_scan_interval):
            query['WebsiteScanInterval'] = request.website_scan_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_website_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_with_options(request, runtime)

    def update_website_instance_key_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstanceKeyUrl',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def update_website_instance_key_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_key_url_with_options(request, runtime)

    def update_website_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebsiteInstanceStatus',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_website_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_status_with_options(request, runtime)

    def upgrade_cdi_base_bag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.flow_out_spec):
            query['FlowOutSpec'] = request.flow_out_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeCdiBaseBag',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UpgradeCdiBaseBagResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_cdi_base_bag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cdi_base_bag_with_options(request, runtime)

    def upload_image_to_lib_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_lib_id):
            query['ImageLibId'] = request.image_lib_id
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.urls):
            query['Urls'] = request.urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadImageToLib',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.UploadImageToLibResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_image_to_lib(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_image_to_lib_with_options(request, runtime)

    def verify_custom_ocr_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.test_img_url):
            query['TestImgUrl'] = request.test_img_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCustomOcrTemplate',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyCustomOcrTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_custom_ocr_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_custom_ocr_template_with_options(request, runtime)

    def verify_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyEmail',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    def verify_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyPhone',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_phone_with_options(request, runtime)

    def verify_website_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.verify_method):
            query['VerifyMethod'] = request.verify_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyWebsiteInstance',
            version='2017-08-23',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyWebsiteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_website_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_website_instance_with_options(request, runtime)
