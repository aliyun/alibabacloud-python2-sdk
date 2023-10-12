# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cmn20200825 import models as cmn_20200825_models
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
        self._endpoint = self.get_endpoint('cmn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_ipwith_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ApplyIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_type_id):
            query['BusinessTypeId'] = request.business_type_id
        if not UtilClient.is_unset(request.business_type_params):
            query['BusinessTypeParams'] = request.business_type_params
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            query['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.loopback_port):
            query['LoopbackPort'] = request.loopback_port
        if not UtilClient.is_unset(request.net_location):
            query['NetLocation'] = request.net_location
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyIP',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ApplyIPResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_ipwith_options(request, runtime)

    def auto_duty_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duty_batch):
            body['DutyBatch'] = request.duty_batch
        if not UtilClient.is_unset(request.duty_name):
            body['DutyName'] = request.duty_name
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AutoDuty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.AutoDutyResponse(),
            self.call_api(params, req, runtime)
        )

    def auto_duty(self, request):
        runtime = util_models.RuntimeOptions()
        return self.auto_duty_with_options(request, runtime)

    def close_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_object_id):
            body['EventObjectId'] = request.event_object_id
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseEvent',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CloseEventResponse(),
            self.call_api(params, req, runtime)
        )

    def close_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_event_with_options(request, runtime)

    def create_configuration_specification_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: CreateConfigurationSpecificationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.related_variate_shrink):
            body['RelatedVariate'] = request.related_variate_shrink
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.specification_content):
            body['SpecificationContent'] = request.specification_content
        if not UtilClient.is_unset(request.specification_name):
            body['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_configuration_specification(self, request):
        """
        @deprecated
        

        @param request: CreateConfigurationSpecificationRequest

        @return: CreateConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_configuration_specification_with_options(request, runtime)

    def create_configuration_variate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.format_function):
            body['FormatFunction'] = request.format_function
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.variate_name):
            body['VariateName'] = request.variate_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_configuration_variate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_configuration_variate_with_options(request, runtime)

    def create_dedicated_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.contact):
            body['Contact'] = request.contact
        if not UtilClient.is_unset(request.dedicated_line_gateway):
            body['DedicatedLineGateway'] = request.dedicated_line_gateway
        if not UtilClient.is_unset(request.dedicated_line_ip):
            body['DedicatedLineIp'] = request.dedicated_line_ip
        if not UtilClient.is_unset(request.dedicated_line_role):
            body['DedicatedLineRole'] = request.dedicated_line_role
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_port):
            body['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.expiration_date):
            body['ExpirationDate'] = request.expiration_date
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.isp):
            body['Isp'] = request.isp
        if not UtilClient.is_unset(request.isp_form_id):
            body['IspFormId'] = request.isp_form_id
        if not UtilClient.is_unset(request.isp_id):
            body['IspId'] = request.isp_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.online_date):
            body['OnlineDate'] = request.online_date
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dedicated_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_line_with_options(request, runtime)

    def create_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name):
            body['HostName'] = request.host_name
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    def create_device_form_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.account_config):
            body['AccountConfig'] = request.account_config
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_compare):
            body['ConfigCompare'] = request.config_compare
        if not UtilClient.is_unset(request.detail_display):
            body['DetailDisplay'] = request.detail_display
        if not UtilClient.is_unset(request.device_form_name):
            body['DeviceFormName'] = request.device_form_name
        if not UtilClient.is_unset(request.related_device_form_id):
            body['RelatedDeviceFormId'] = request.related_device_form_id
        if not UtilClient.is_unset(request.resource_use):
            body['ResourceUse'] = request.resource_use
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.unique_key):
            body['UniqueKey'] = request.unique_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_form(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_form_with_options(request, runtime)

    def create_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.property_content):
            body['PropertyContent'] = request.property_content
        if not UtilClient.is_unset(request.property_format):
            body['PropertyFormat'] = request.property_format
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_property_with_options(request, runtime)

    def create_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_param_model_list):
            request.device_param_model_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_param_model_list, 'DeviceParamModelList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.device_param_model_list_shrink):
            body['DeviceParamModelList'] = request.device_param_model_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_devices_with_options(request, runtime)

    def create_event_definition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateEventDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_event_definition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_event_definition_with_options(request, runtime)

    def create_link_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.auto_confirm):
            body['AutoConfirm'] = request.auto_confirm
        if not UtilClient.is_unset(request.double_convert_strategy):
            body['DoubleConvertStrategy'] = request.double_convert_strategy
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.single_strategy):
            body['SingleStrategy'] = request.single_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLinkJob',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateLinkJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_link_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_link_job_with_options(request, runtime)

    def create_monitor_item_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateMonitorItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_rule_list):
            request.alarm_rule_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_rule_list, 'AlarmRuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_rule_list_shrink):
            body['AlarmRuleList'] = request.alarm_rule_list_shrink
        if not UtilClient.is_unset(request.analysis_code):
            body['AnalysisCode'] = request.analysis_code
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.collection_type):
            body['CollectionType'] = request.collection_type
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.data_item):
            body['DataItem'] = request.data_item
        if not UtilClient.is_unset(request.device_form):
            body['DeviceForm'] = request.device_form
        if not UtilClient.is_unset(request.effective):
            body['Effective'] = request.effective
        if not UtilClient.is_unset(request.exec_interval):
            body['ExecInterval'] = request.exec_interval
        if not UtilClient.is_unset(request.monitor_item_description):
            body['MonitorItemDescription'] = request.monitor_item_description
        if not UtilClient.is_unset(request.monitor_item_name):
            body['MonitorItemName'] = request.monitor_item_name
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMonitorItem',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateMonitorItemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_item_with_options(request, runtime)

    def create_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.boot_patch):
            body['BootPatch'] = request.boot_patch
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.feature_patch):
            body['FeaturePatch'] = request.feature_patch
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.system_patch):
            body['SystemPatch'] = request.system_patch
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_os_version_with_options(request, runtime)

    def create_physical_space_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreatePhysicalSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.security_domain_list):
            request.security_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain_list, 'SecurityDomainList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.parent_uid):
            body['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_domain_list_shrink):
            body['SecurityDomainList'] = request.security_domain_list_shrink
        if not UtilClient.is_unset(request.space_abbreviation):
            body['SpaceAbbreviation'] = request.space_abbreviation
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreatePhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_physical_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_physical_space_with_options(request, runtime)

    def create_realtime_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.check_duplicate_policy):
            body['CheckDuplicatePolicy'] = request.check_duplicate_policy
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.item_name):
            body['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRealtimeTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateRealtimeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_realtime_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_realtime_task_with_options(request, runtime)

    def create_resource_information_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: CreateResourceInformationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateResourceInformationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.architecture_id):
            body['ArchitectureId'] = request.architecture_id
        body_flat = {}
        if not UtilClient.is_unset(request.information):
            body_flat['Information'] = request.information
        if not UtilClient.is_unset(request.resource_attribute):
            body['ResourceAttribute'] = request.resource_attribute
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateResourceInformationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_information(self, request):
        """
        @deprecated
        

        @param request: CreateResourceInformationRequest

        @return: CreateResourceInformationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_information_with_options(request, runtime)

    def create_setup_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_time):
            body['DeliveryTime'] = request.delivery_time
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_setup_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_setup_project_with_options(request, runtime)

    def create_space_model_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_space_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_space_model_with_options(request, runtime)

    def create_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    def create_time_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.time_period_description):
            body['TimePeriodDescription'] = request.time_period_description
        if not UtilClient.is_unset(request.time_period_name):
            body['TimePeriodName'] = request.time_period_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTimePeriod',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTimePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def create_time_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_time_period_with_options(request, runtime)

    def delete_configuration_specification_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: DeleteConfigurationSpecificationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_specification_id):
            body['ConfigurationSpecificationId'] = request.configuration_specification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_configuration_specification(self, request):
        """
        @deprecated
        

        @param request: DeleteConfigurationSpecificationRequest

        @return: DeleteConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_configuration_specification_with_options(request, runtime)

    def delete_configuration_variate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configuration_variate_id):
            body['ConfigurationVariateId'] = request.configuration_variate_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_configuration_variate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_configuration_variate_with_options(request, runtime)

    def delete_dedicated_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.dedicated_line_id):
            body['DedicatedLineId'] = request.dedicated_line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dedicated_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_line_with_options(request, runtime)

    def delete_delivery_arch_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_arch_version_id):
            body['DeliveryArchVersionId'] = request.delivery_arch_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryArchVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeliveryArchVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_delivery_arch_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_arch_version_with_options(request, runtime)

    def delete_delivery_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_project_id):
            body['DeliveryProjectId'] = request.delivery_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeliveryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_delivery_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_project_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def delete_device_form_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_form(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_form_with_options(request, runtime)

    def delete_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_property_id):
            body['DevicePropertyId'] = request.device_property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_property_with_options(request, runtime)

    def delete_device_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_resource_with_options(request, runtime)

    def delete_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DeleteDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_ids_shrink):
            body['DeviceIds'] = request.device_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devices_with_options(request, runtime)

    def delete_event_definition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteEventDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_definition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_definition_with_options(request, runtime)

    def delete_inspection_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInspectionTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_inspection_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_inspection_task_with_options(request, runtime)

    def delete_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.os_version_id):
            body['OsVersionId'] = request.os_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_os_version_with_options(request, runtime)

    def delete_physical_space_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeletePhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_physical_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_space_with_options(request, runtime)

    def delete_resource_information_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.resource_information_id):
            body['ResourceInformationId'] = request.resource_information_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteResourceInformationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_information_with_options(request, runtime)

    def delete_setup_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_setup_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_setup_project_with_options(request, runtime)

    def delete_space_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.space_model_id):
            query['SpaceModelId'] = request.space_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_space_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_space_model_with_options(request, runtime)

    def disable_notification_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DisableNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.expiry_time):
            body['ExpiryTime'] = request.expiry_time
        if not UtilClient.is_unset(request.list_shrink):
            body['List'] = request.list_shrink
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableNotification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DisableNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_notification_with_options(request, runtime)

    def download_device_resource_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DownloadDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DownloadDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def download_device_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.download_device_resource_with_options(request, runtime)

    def enable_notification_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.EnableNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.list_shrink):
            body['List'] = request.list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableNotification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.EnableNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_notification_with_options(request, runtime)

    def get_alarm_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlarmStatus',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetAlarmStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alarm_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alarm_status_with_options(request, runtime)

    def get_configuration_specification_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: GetConfigurationSpecificationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_configuration_specification(self, request):
        """
        @deprecated
        

        @param request: GetConfigurationSpecificationRequest

        @return: GetConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_specification_with_options(request, runtime)

    def get_configuration_variate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_configuration_variate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_variate_with_options(request, runtime)

    def get_dedicated_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    def get_dedicated_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dedicated_line_with_options(request, runtime)

    def get_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_with_options(request, runtime)

    def get_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfig',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_with_options(request, runtime)

    def get_device_config_date_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigDate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_config_date(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_date_with_options(request, runtime)

    def get_device_config_diff_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigDiff',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDiffResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_config_diff(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_diff_with_options(request, runtime)

    def get_device_form_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_form(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_form_with_options(request, runtime)

    def get_device_op_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceOpLog',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceOpLogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_op_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_op_log_with_options(request, runtime)

    def get_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_property_with_options(request, runtime)

    def get_device_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_resource_with_options(request, runtime)

    def get_inspection_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInspectionTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_inspection_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_inspection_task_with_options(request, runtime)

    def get_monitor_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonitorItem',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetMonitorItemResponse(),
            self.call_api(params, req, runtime)
        )

    def get_monitor_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_item_with_options(request, runtime)

    def get_os_download_path_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOsDownloadPath',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsDownloadPathResponse(),
            self.call_api(params, req, runtime)
        )

    def get_os_download_path(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_os_download_path_with_options(request, runtime)

    def get_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_os_version_with_options(request, runtime)

    def get_oss_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssPolicy',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_oss_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    def get_physical_space_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_physical_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_physical_space_with_options(request, runtime)

    def get_physical_space_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.physical_space_id):
            query['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.topo_type):
            query['TopoType'] = request.topo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalSpaceTopo',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceTopoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_physical_space_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_physical_space_topo_with_options(request, runtime)

    def get_realtime_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetRealtimeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_realtime_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_task_with_options(request, runtime)

    def get_schedule_worker_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScheduleWorker',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_schedule_worker(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_schedule_worker_with_options(request, runtime)

    def get_setup_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_setup_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_setup_project_with_options(request, runtime)

    def get_space_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    def get_space_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_with_options(request, runtime)

    def get_space_model_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModelInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_space_model_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_instance_with_options(request, runtime)

    def get_space_model_sort_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModelSort',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelSortResponse(),
            self.call_api(params, req, runtime)
        )

    def get_space_model_sort(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_sort_with_options(request, runtime)

    def get_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    def list_alarm_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatus',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alarm_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_with_options(request, runtime)

    def list_alarm_status_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatusHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alarm_status_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_histories_with_options(request, runtime)

    def list_alarm_status_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatusStatistics',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alarm_status_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_statistics_with_options(request, runtime)

    def list_architecture_attribute_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListArchitectureAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListArchitectureAttributeResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArchitectureAttribute',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListArchitectureAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_architecture_attribute(self, request):
        """
        @deprecated
        

        @param request: ListArchitectureAttributeRequest

        @return: ListArchitectureAttributeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_architecture_attribute_with_options(request, runtime)

    def list_configuration_specifications_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListConfigurationSpecificationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConfigurationSpecificationsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigurationSpecifications',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_configuration_specifications(self, request):
        """
        @deprecated
        

        @param request: ListConfigurationSpecificationsRequest

        @return: ListConfigurationSpecificationsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_configuration_specifications_with_options(request, runtime)

    def list_configuration_variate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_configuration_variate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_configuration_variate_with_options(request, runtime)

    def list_connection_policies_with_options(self, request, runtime):
        """
        @deprecated
        

        @param request: ListConnectionPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConnectionPoliciesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.architecture_iteration_id):
            body['ArchitectureIterationId'] = request.architecture_iteration_id
        if not UtilClient.is_unset(request.connection_policy_id):
            body['ConnectionPolicyId'] = request.connection_policy_id
        if not UtilClient.is_unset(request.downlink_architecture_device_id):
            body['DownlinkArchitectureDeviceId'] = request.downlink_architecture_device_id
        if not UtilClient.is_unset(request.downlink_architecture_module_id):
            body['DownlinkArchitectureModuleId'] = request.downlink_architecture_module_id
        if not UtilClient.is_unset(request.uplink_architecture_device_id):
            body['UplinkArchitectureDeviceId'] = request.uplink_architecture_device_id
        if not UtilClient.is_unset(request.uplink_architecture_module_id):
            body['UplinkArchitectureModuleId'] = request.uplink_architecture_module_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnectionPolicies',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConnectionPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connection_policies(self, request):
        """
        @deprecated
        

        @param request: ListConnectionPoliciesRequest

        @return: ListConnectionPoliciesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_connection_policies_with_options(request, runtime)

    def list_dedicated_lines_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDedicatedLines',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDedicatedLinesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dedicated_lines(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dedicated_lines_with_options(request, runtime)

    def list_device_forms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceForms',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceFormsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_forms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_forms_with_options(request, runtime)

    def list_device_properties_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceProperties',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_properties(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_properties_with_options(request, runtime)

    def list_device_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceResources',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_resources_with_options(request, runtime)

    def list_device_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceValues',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_values_with_options(request, runtime)

    def list_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        if not UtilClient.is_unset(tmp_req.host_name):
            request.host_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name, 'HostName', 'json')
        if not UtilClient.is_unset(tmp_req.ip):
            request.ip_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip, 'Ip', 'json')
        if not UtilClient.is_unset(tmp_req.mac):
            request.mac_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mac, 'Mac', 'json')
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        if not UtilClient.is_unset(tmp_req.security_domain):
            request.security_domain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain, 'SecurityDomain', 'json')
        if not UtilClient.is_unset(tmp_req.service_status):
            request.service_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_status, 'ServiceStatus', 'json')
        if not UtilClient.is_unset(tmp_req.sn):
            request.sn_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sn, 'Sn', 'json')
        if not UtilClient.is_unset(tmp_req.vendor):
            request.vendor_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor, 'Vendor', 'json')
        query = {}
        if not UtilClient.is_unset(request.calculate_amount):
            query['CalculateAmount'] = request.calculate_amount
        if not UtilClient.is_unset(request.device_form_id):
            query['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.device_form_name):
            query['DeviceFormName'] = request.device_form_name
        if not UtilClient.is_unset(request.device_ids_shrink):
            query['DeviceIds'] = request.device_ids_shrink
        if not UtilClient.is_unset(request.ext_attributes):
            query['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name_shrink):
            query['HostName'] = request.host_name_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_shrink):
            query['Ip'] = request.ip_shrink
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.mac_shrink):
            query['Mac'] = request.mac_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.model_shrink):
            query['Model'] = request.model_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.physical_space_id):
            query['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_ids_shrink):
            query['PhysicalSpaceIds'] = request.physical_space_ids_shrink
        if not UtilClient.is_unset(request.security_domain_shrink):
            query['SecurityDomain'] = request.security_domain_shrink
        if not UtilClient.is_unset(request.service_status_shrink):
            query['ServiceStatus'] = request.service_status_shrink
        if not UtilClient.is_unset(request.sn_shrink):
            query['Sn'] = request.sn_shrink
        if not UtilClient.is_unset(request.vendor_shrink):
            query['Vendor'] = request.vendor_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    def list_event_definitions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventDefinitions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListEventDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event_definitions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_definitions_with_options(request, runtime)

    def list_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvents',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_events_with_options(request, runtime)

    def list_inspection_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_inspection_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_devices_with_options(request, runtime)

    def list_inspection_task_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionTaskReports',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTaskReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_inspection_task_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_task_reports_with_options(request, runtime)

    def list_inspection_tasks_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_status):
            request.alarm_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_status, 'AlarmStatus', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionTasks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_inspection_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_tasks_with_options(request, runtime)

    def list_instances_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(runtime)

    def list_ip_blocks_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListIpBlocksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_attributes):
            request.ext_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_attributes, 'ExtAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.ip_list):
            request.ip_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_list, 'IpList', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpBlocks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ip_blocks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ip_blocks_with_options(request, runtime)

    def list_links_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLinks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListLinksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_links(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_links_with_options(request, runtime)

    def list_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_logs_with_options(request, runtime)

    def list_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMonitorData',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def list_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_monitor_data_with_options(request, runtime)

    def list_notification_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_notification_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notification_histories_with_options(request, runtime)

    def list_notification_histories_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationHistoriesStatistics',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_notification_histories_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notification_histories_statistics_with_options(request, runtime)

    def list_os_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOsVersions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListOsVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_os_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_os_versions_with_options(request, runtime)

    def list_physical_spaces_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListPhysicalSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhysicalSpaces',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListPhysicalSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_physical_spaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_physical_spaces_with_options(request, runtime)

    def list_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    def list_resource_informations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInformations',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInformationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_informations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_informations_with_options(request, runtime)

    def list_resource_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_instances_with_options(request, runtime)

    def list_resource_types_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_types(self):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(runtime)

    def list_setup_projects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSetupProjects',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSetupProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_setup_projects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_setup_projects_with_options(request, runtime)

    def list_space_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpaceModels',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSpaceModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_space_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_space_models_with_options(request, runtime)

    def list_tasks_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasksHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTasksHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tasks_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_histories_with_options(request, runtime)

    def list_tree_physical_spaces_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListTreePhysicalSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTreePhysicalSpaces',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTreePhysicalSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tree_physical_spaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tree_physical_spaces_with_options(request, runtime)

    def lock_space_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.space_model_id):
            query['SpaceModelId'] = request.space_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.LockSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_space_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_space_model_with_options(request, runtime)

    def release_ipwith_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ReleaseIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            query['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseIP',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ReleaseIPResponse(),
            self.call_api(params, req, runtime)
        )

    def release_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_ipwith_options(request, runtime)

    def retry_tasks_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.RetryTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_tasks):
            request.retry_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_tasks, 'RetryTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.retry_tasks_shrink):
            query['RetryTasks'] = request.retry_tasks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryTasks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.RetryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_tasks_with_options(request, runtime)

    def update_configuration_specification_with_options(self, tmp_req, runtime):
        """
        @deprecated
        

        @param tmp_req: UpdateConfigurationSpecificationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.configuration_specification_id):
            body['ConfigurationSpecificationId'] = request.configuration_specification_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.related_variate_shrink):
            body['RelatedVariate'] = request.related_variate_shrink
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.specification_content):
            body['SpecificationContent'] = request.specification_content
        if not UtilClient.is_unset(request.specification_name):
            body['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_configuration_specification(self, request):
        """
        @deprecated
        

        @param request: UpdateConfigurationSpecificationRequest

        @return: UpdateConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_specification_with_options(request, runtime)

    def update_configuration_variate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.configuration_variate_id):
            body['ConfigurationVariateId'] = request.configuration_variate_id
        if not UtilClient.is_unset(request.format_function):
            body['FormatFunction'] = request.format_function
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.variate_name):
            body['VariateName'] = request.variate_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_configuration_variate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_variate_with_options(request, runtime)

    def update_dedicated_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.contact):
            body['Contact'] = request.contact
        if not UtilClient.is_unset(request.dedicated_line_gateway):
            body['DedicatedLineGateway'] = request.dedicated_line_gateway
        if not UtilClient.is_unset(request.dedicated_line_id):
            body['DedicatedLineId'] = request.dedicated_line_id
        if not UtilClient.is_unset(request.dedicated_line_ip):
            body['DedicatedLineIp'] = request.dedicated_line_ip
        if not UtilClient.is_unset(request.dedicated_line_role):
            body['DedicatedLineRole'] = request.dedicated_line_role
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_port):
            body['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.expiration_date):
            body['ExpirationDate'] = request.expiration_date
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.isp):
            body['Isp'] = request.isp
        if not UtilClient.is_unset(request.isp_id):
            body['IspId'] = request.isp_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.online_date):
            body['OnlineDate'] = request.online_date
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dedicated_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dedicated_line_with_options(request, runtime)

    def update_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name):
            body['HostName'] = request.host_name
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_with_options(request, runtime)

    def update_device_form_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceFormShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_list):
            request.attribute_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_list, 'AttributeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.account_config):
            body['AccountConfig'] = request.account_config
        if not UtilClient.is_unset(request.attribute_list_shrink):
            body['AttributeList'] = request.attribute_list_shrink
        if not UtilClient.is_unset(request.config_compare):
            body['ConfigCompare'] = request.config_compare
        if not UtilClient.is_unset(request.detail_display):
            body['DetailDisplay'] = request.detail_display
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.related_device_form_id):
            body['RelatedDeviceFormId'] = request.related_device_form_id
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device_form(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_form_with_options(request, runtime)

    def update_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_property_id):
            body['DevicePropertyId'] = request.device_property_id
        if not UtilClient.is_unset(request.property_content):
            body['PropertyContent'] = request.property_content
        if not UtilClient.is_unset(request.property_format):
            body['PropertyFormat'] = request.property_format
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_property_with_options(request, runtime)

    def update_device_resource_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.device_resource_id):
            body['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            body['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_resource_with_options(request, runtime)

    def update_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_ids_shrink):
            body['DeviceIds'] = request.device_ids_shrink
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_devices_with_options(request, runtime)

    def update_event_definition_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateEventDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_event_definition(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_event_definition_with_options(request, runtime)

    def update_information_key_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.key_action):
            query['KeyAction'] = request.key_action
        if not UtilClient.is_unset(request.resource_information_id):
            query['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInformationKeyAction',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInformationKeyActionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_information_key_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_information_key_action_with_options(request, runtime)

    def update_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    def update_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.boot_patch):
            body['BootPatch'] = request.boot_patch
        if not UtilClient.is_unset(request.feature_patch):
            body['FeaturePatch'] = request.feature_patch
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.os_version_id):
            body['OsVersionId'] = request.os_version_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.system_patch):
            body['SystemPatch'] = request.system_patch
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_with_options(request, runtime)

    def update_physical_space_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdatePhysicalSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.security_domain_list):
            request.security_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain_list, 'SecurityDomainList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.move_action):
            body['MoveAction'] = request.move_action
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.parent_uid):
            body['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_domain_list_shrink):
            body['SecurityDomainList'] = request.security_domain_list_shrink
        if not UtilClient.is_unset(request.space_abbreviation):
            body['SpaceAbbreviation'] = request.space_abbreviation
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        if not UtilClient.is_unset(request.target_uid):
            body['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdatePhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_physical_space(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_physical_space_with_options(request, runtime)

    def update_project_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.progress):
            body['Progress'] = request.progress
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectProgress',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateProjectProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_progress_with_options(request, runtime)

    def update_resource_information_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.information):
            request.information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.information, 'Information', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.information_shrink):
            body['Information'] = request.information_shrink
        if not UtilClient.is_unset(request.resource_attribute):
            body['ResourceAttribute'] = request.resource_attribute
        if not UtilClient.is_unset(request.resource_information_id):
            body['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInformationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_information(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_information_with_options(request, runtime)

    def update_resource_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_information):
            request.resource_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_information, 'ResourceInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_information_shrink):
            query['ResourceInformation'] = request.resource_information_shrink
        if not UtilClient.is_unset(request.resource_information_id):
            query['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_instance_with_options(request, runtime)

    def update_setup_project_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSetupProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.packages):
            request.packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.packages, 'Packages', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.architecture_id):
            body['ArchitectureId'] = request.architecture_id
        if not UtilClient.is_unset(request.delivery_time):
            body['DeliveryTime'] = request.delivery_time
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.packages_shrink):
            body['Packages'] = request.packages_shrink
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_setup_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_setup_project_with_options(request, runtime)

    def update_space_model_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.space_model_id):
            body['SpaceModelId'] = request.space_model_id
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_space_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_space_model_with_options(request, runtime)

    def update_space_model_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSpaceModelInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_space_model_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_space_model_instance_with_options(request, runtime)
