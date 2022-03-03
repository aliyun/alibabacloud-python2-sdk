# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetCardDetailRequest(TeaModel):
    def __init__(self, destroy_card=None, iccid=None, instance_id=None, show_psim=None):
        self.destroy_card = destroy_card  # type: bool
        self.iccid = iccid  # type: str
        self.instance_id = instance_id  # type: str
        self.show_psim = show_psim  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destroy_card is not None:
            result['DestroyCard'] = self.destroy_card
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.show_psim is not None:
            result['ShowPsim'] = self.show_psim
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestroyCard') is not None:
            self.destroy_card = m.get('DestroyCard')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ShowPsim') is not None:
            self.show_psim = m.get('ShowPsim')
        return self


class GetCardDetailResponseBodyDataListPsimCards(TeaModel):
    def __init__(self, apn_name=None, certify_status=None, iccid=None, imsi=None, msisdn=None, os_status=None,
                 period_add_flow=None, period_sms_use=None, private_network_segment=None, status=None, vendor=None):
        self.apn_name = apn_name  # type: str
        self.certify_status = certify_status  # type: str
        self.iccid = iccid  # type: str
        self.imsi = imsi  # type: list[str]
        self.msisdn = msisdn  # type: list[str]
        self.os_status = os_status  # type: str
        self.period_add_flow = period_add_flow  # type: str
        self.period_sms_use = period_sms_use  # type: str
        self.private_network_segment = private_network_segment  # type: str
        self.status = status  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardDetailResponseBodyDataListPsimCards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.status is not None:
            result['Status'] = self.status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetCardDetailResponseBodyDataVsimCardInfoTagList(TeaModel):
    def __init__(self, id=None, tag_name=None):
        self.id = id  # type: long
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardDetailResponseBodyDataVsimCardInfoTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class GetCardDetailResponseBodyDataVsimCardInfo(TeaModel):
    def __init__(self, active_time=None, active_type=None, ali_fee=None, aliyun_order_id=None, apn_name=None,
                 auto_limit_resume=None, auto_rebind_reuse=None, card_limit_speed_threshold=None, card_limit_stop_threshold=None,
                 certify_status=None, certify_type=None, credential_instance_id=None, credential_limit_speed_threshold=None,
                 credential_limit_stop_threshold=None, credential_no=None, credential_type=None, data_level=None, data_type=None, device_imei=None,
                 directional_group_id=None, directional_group_name=None, expire_time=None, flow_threshold_unit=None, iccid=None,
                 imsi=None, is_auto_recharge=None, msisdn=None, notify_id=None, open_account_time=None, os_status=None,
                 period=None, period_add_flow=None, period_rest_flow=None, period_sms_use=None,
                 private_network_segment=None, sim_type=None, status=None, tag_list=None, vendor=None, vsim_instance_id=None):
        self.active_time = active_time  # type: str
        self.active_type = active_type  # type: str
        self.ali_fee = ali_fee  # type: str
        self.aliyun_order_id = aliyun_order_id  # type: str
        self.apn_name = apn_name  # type: str
        self.auto_limit_resume = auto_limit_resume  # type: bool
        self.auto_rebind_reuse = auto_rebind_reuse  # type: bool
        self.card_limit_speed_threshold = card_limit_speed_threshold  # type: int
        self.card_limit_stop_threshold = card_limit_stop_threshold  # type: int
        self.certify_status = certify_status  # type: str
        self.certify_type = certify_type  # type: str
        self.credential_instance_id = credential_instance_id  # type: str
        self.credential_limit_speed_threshold = credential_limit_speed_threshold  # type: int
        self.credential_limit_stop_threshold = credential_limit_stop_threshold  # type: int
        self.credential_no = credential_no  # type: str
        self.credential_type = credential_type  # type: str
        self.data_level = data_level  # type: str
        self.data_type = data_type  # type: str
        self.device_imei = device_imei  # type: str
        self.directional_group_id = directional_group_id  # type: str
        self.directional_group_name = directional_group_name  # type: str
        self.expire_time = expire_time  # type: str
        self.flow_threshold_unit = flow_threshold_unit  # type: str
        self.iccid = iccid  # type: str
        self.imsi = imsi  # type: list[str]
        self.is_auto_recharge = is_auto_recharge  # type: bool
        self.msisdn = msisdn  # type: list[str]
        self.notify_id = notify_id  # type: str
        self.open_account_time = open_account_time  # type: str
        self.os_status = os_status  # type: str
        self.period = period  # type: str
        self.period_add_flow = period_add_flow  # type: str
        self.period_rest_flow = period_rest_flow  # type: str
        self.period_sms_use = period_sms_use  # type: str
        self.private_network_segment = private_network_segment  # type: str
        self.sim_type = sim_type  # type: str
        self.status = status  # type: str
        self.tag_list = tag_list  # type: list[GetCardDetailResponseBodyDataVsimCardInfoTagList]
        self.vendor = vendor  # type: str
        self.vsim_instance_id = vsim_instance_id  # type: int

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCardDetailResponseBodyDataVsimCardInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time
        if self.active_type is not None:
            result['ActiveType'] = self.active_type
        if self.ali_fee is not None:
            result['AliFee'] = self.ali_fee
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apn_name is not None:
            result['ApnName'] = self.apn_name
        if self.auto_limit_resume is not None:
            result['AutoLimitResume'] = self.auto_limit_resume
        if self.auto_rebind_reuse is not None:
            result['AutoRebindReuse'] = self.auto_rebind_reuse
        if self.card_limit_speed_threshold is not None:
            result['CardLimitSpeedThreshold'] = self.card_limit_speed_threshold
        if self.card_limit_stop_threshold is not None:
            result['CardLimitStopThreshold'] = self.card_limit_stop_threshold
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_limit_speed_threshold is not None:
            result['CredentialLimitSpeedThreshold'] = self.credential_limit_speed_threshold
        if self.credential_limit_stop_threshold is not None:
            result['CredentialLimitStopThreshold'] = self.credential_limit_stop_threshold
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.data_level is not None:
            result['DataLevel'] = self.data_level
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.device_imei is not None:
            result['DeviceImei'] = self.device_imei
        if self.directional_group_id is not None:
            result['DirectionalGroupId'] = self.directional_group_id
        if self.directional_group_name is not None:
            result['DirectionalGroupName'] = self.directional_group_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.flow_threshold_unit is not None:
            result['FlowThresholdUnit'] = self.flow_threshold_unit
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.is_auto_recharge is not None:
            result['IsAutoRecharge'] = self.is_auto_recharge
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.notify_id is not None:
            result['NotifyId'] = self.notify_id
        if self.open_account_time is not None:
            result['OpenAccountTime'] = self.open_account_time
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.period is not None:
            result['Period'] = self.period
        if self.period_add_flow is not None:
            result['PeriodAddFlow'] = self.period_add_flow
        if self.period_rest_flow is not None:
            result['PeriodRestFlow'] = self.period_rest_flow
        if self.period_sms_use is not None:
            result['PeriodSmsUse'] = self.period_sms_use
        if self.private_network_segment is not None:
            result['PrivateNetworkSegment'] = self.private_network_segment
        if self.sim_type is not None:
            result['SimType'] = self.sim_type
        if self.status is not None:
            result['Status'] = self.status
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.vsim_instance_id is not None:
            result['VsimInstanceId'] = self.vsim_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')
        if m.get('ActiveType') is not None:
            self.active_type = m.get('ActiveType')
        if m.get('AliFee') is not None:
            self.ali_fee = m.get('AliFee')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApnName') is not None:
            self.apn_name = m.get('ApnName')
        if m.get('AutoLimitResume') is not None:
            self.auto_limit_resume = m.get('AutoLimitResume')
        if m.get('AutoRebindReuse') is not None:
            self.auto_rebind_reuse = m.get('AutoRebindReuse')
        if m.get('CardLimitSpeedThreshold') is not None:
            self.card_limit_speed_threshold = m.get('CardLimitSpeedThreshold')
        if m.get('CardLimitStopThreshold') is not None:
            self.card_limit_stop_threshold = m.get('CardLimitStopThreshold')
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialLimitSpeedThreshold') is not None:
            self.credential_limit_speed_threshold = m.get('CredentialLimitSpeedThreshold')
        if m.get('CredentialLimitStopThreshold') is not None:
            self.credential_limit_stop_threshold = m.get('CredentialLimitStopThreshold')
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('DataLevel') is not None:
            self.data_level = m.get('DataLevel')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DeviceImei') is not None:
            self.device_imei = m.get('DeviceImei')
        if m.get('DirectionalGroupId') is not None:
            self.directional_group_id = m.get('DirectionalGroupId')
        if m.get('DirectionalGroupName') is not None:
            self.directional_group_name = m.get('DirectionalGroupName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FlowThresholdUnit') is not None:
            self.flow_threshold_unit = m.get('FlowThresholdUnit')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('IsAutoRecharge') is not None:
            self.is_auto_recharge = m.get('IsAutoRecharge')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('NotifyId') is not None:
            self.notify_id = m.get('NotifyId')
        if m.get('OpenAccountTime') is not None:
            self.open_account_time = m.get('OpenAccountTime')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodAddFlow') is not None:
            self.period_add_flow = m.get('PeriodAddFlow')
        if m.get('PeriodRestFlow') is not None:
            self.period_rest_flow = m.get('PeriodRestFlow')
        if m.get('PeriodSmsUse') is not None:
            self.period_sms_use = m.get('PeriodSmsUse')
        if m.get('PrivateNetworkSegment') is not None:
            self.private_network_segment = m.get('PrivateNetworkSegment')
        if m.get('SimType') is not None:
            self.sim_type = m.get('SimType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = GetCardDetailResponseBodyDataVsimCardInfoTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('VsimInstanceId') is not None:
            self.vsim_instance_id = m.get('VsimInstanceId')
        return self


class GetCardDetailResponseBodyData(TeaModel):
    def __init__(self, list_psim_cards=None, vsim_card_info=None):
        self.list_psim_cards = list_psim_cards  # type: list[GetCardDetailResponseBodyDataListPsimCards]
        self.vsim_card_info = vsim_card_info  # type: GetCardDetailResponseBodyDataVsimCardInfo

    def validate(self):
        if self.list_psim_cards:
            for k in self.list_psim_cards:
                if k:
                    k.validate()
        if self.vsim_card_info:
            self.vsim_card_info.validate()

    def to_map(self):
        _map = super(GetCardDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListPsimCards'] = []
        if self.list_psim_cards is not None:
            for k in self.list_psim_cards:
                result['ListPsimCards'].append(k.to_map() if k else None)
        if self.vsim_card_info is not None:
            result['VsimCardInfo'] = self.vsim_card_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_psim_cards = []
        if m.get('ListPsimCards') is not None:
            for k in m.get('ListPsimCards'):
                temp_model = GetCardDetailResponseBodyDataListPsimCards()
                self.list_psim_cards.append(temp_model.from_map(k))
        if m.get('VsimCardInfo') is not None:
            temp_model = GetCardDetailResponseBodyDataVsimCardInfo()
            self.vsim_card_info = temp_model.from_map(m['VsimCardInfo'])
        return self


class GetCardDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCardDetailResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCardDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCardDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCardDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCardDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCardFlowInfoRequest(TeaModel):
    def __init__(self, date_list=None, iccid=None):
        self.date_list = date_list  # type: list[str]
        self.iccid = iccid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_list is not None:
            result['DateList'] = self.date_list
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DateList') is not None:
            self.date_list = m.get('DateList')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow(TeaModel):
    def __init__(self, day=None, flow=None):
        self.day = day  # type: str
        self.flow = flow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class GetCardFlowInfoResponseBodyDataListCardMonthFlow(TeaModel):
    def __init__(self, flow_count=None, list_day_flow=None, month=None):
        self.flow_count = flow_count  # type: str
        self.list_day_flow = list_day_flow  # type: list[GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow]
        self.month = month  # type: str

    def validate(self):
        if self.list_day_flow:
            for k in self.list_day_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListCardMonthFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_count is not None:
            result['FlowCount'] = self.flow_count
        result['ListDayFlow'] = []
        if self.list_day_flow is not None:
            for k in self.list_day_flow:
                result['ListDayFlow'].append(k.to_map() if k else None)
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowCount') is not None:
            self.flow_count = m.get('FlowCount')
        self.list_day_flow = []
        if m.get('ListDayFlow') is not None:
            for k in m.get('ListDayFlow'):
                temp_model = GetCardFlowInfoResponseBodyDataListCardMonthFlowListDayFlow()
                self.list_day_flow.append(temp_model.from_map(k))
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetCardFlowInfoResponseBodyDataListPackageDTO(TeaModel):
    def __init__(self, effective_time=None, expire_time=None, package_name=None, remark=None):
        self.effective_time = effective_time  # type: str
        self.expire_time = expire_time  # type: str
        self.package_name = package_name  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListPackageDTO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class GetCardFlowInfoResponseBodyDataListVendorDetail(TeaModel):
    def __init__(self, net_work_delay=None, signal_strength=None, vendor=None):
        self.net_work_delay = net_work_delay  # type: str
        self.signal_strength = signal_strength  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyDataListVendorDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_work_delay is not None:
            result['NetWorkDelay'] = self.net_work_delay
        if self.signal_strength is not None:
            result['SignalStrength'] = self.signal_strength
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetWorkDelay') is not None:
            self.net_work_delay = m.get('NetWorkDelay')
        if m.get('SignalStrength') is not None:
            self.signal_strength = m.get('SignalStrength')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetCardFlowInfoResponseBodyData(TeaModel):
    def __init__(self, list_card_month_flow=None, list_package_dto=None, list_vendor_detail=None):
        self.list_card_month_flow = list_card_month_flow  # type: list[GetCardFlowInfoResponseBodyDataListCardMonthFlow]
        self.list_package_dto = list_package_dto  # type: list[GetCardFlowInfoResponseBodyDataListPackageDTO]
        self.list_vendor_detail = list_vendor_detail  # type: list[GetCardFlowInfoResponseBodyDataListVendorDetail]

    def validate(self):
        if self.list_card_month_flow:
            for k in self.list_card_month_flow:
                if k:
                    k.validate()
        if self.list_package_dto:
            for k in self.list_package_dto:
                if k:
                    k.validate()
        if self.list_vendor_detail:
            for k in self.list_vendor_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListCardMonthFlow'] = []
        if self.list_card_month_flow is not None:
            for k in self.list_card_month_flow:
                result['ListCardMonthFlow'].append(k.to_map() if k else None)
        result['ListPackageDTO'] = []
        if self.list_package_dto is not None:
            for k in self.list_package_dto:
                result['ListPackageDTO'].append(k.to_map() if k else None)
        result['ListVendorDetail'] = []
        if self.list_vendor_detail is not None:
            for k in self.list_vendor_detail:
                result['ListVendorDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list_card_month_flow = []
        if m.get('ListCardMonthFlow') is not None:
            for k in m.get('ListCardMonthFlow'):
                temp_model = GetCardFlowInfoResponseBodyDataListCardMonthFlow()
                self.list_card_month_flow.append(temp_model.from_map(k))
        self.list_package_dto = []
        if m.get('ListPackageDTO') is not None:
            for k in m.get('ListPackageDTO'):
                temp_model = GetCardFlowInfoResponseBodyDataListPackageDTO()
                self.list_package_dto.append(temp_model.from_map(k))
        self.list_vendor_detail = []
        if m.get('ListVendorDetail') is not None:
            for k in m.get('ListVendorDetail'):
                temp_model = GetCardFlowInfoResponseBodyDataListVendorDetail()
                self.list_vendor_detail.append(temp_model.from_map(k))
        return self


class GetCardFlowInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCardFlowInfoResponseBodyData
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCardFlowInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCardFlowInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCardFlowInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCardFlowInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCardFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCredentialPoolStatisticsRequest(TeaModel):
    def __init__(self, credential_no=None, date=None):
        self.credential_no = credential_no  # type: str
        self.date = date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetCredentialPoolStatisticsResponseBodyData(TeaModel):
    def __init__(self, card_active_num=None, card_total_num=None, credential_instance_id=None, credential_no=None,
                 credential_type=None, effective_available_flow=None, effective_total_flow=None, month_feature_fee=None,
                 pool_avaiable=None, pool_grand_total=None, pool_grand_total_used=None, pool_out_used=None, pool_used=None,
                 sms_used=None):
        self.card_active_num = card_active_num  # type: long
        self.card_total_num = card_total_num  # type: long
        self.credential_instance_id = credential_instance_id  # type: str
        self.credential_no = credential_no  # type: str
        self.credential_type = credential_type  # type: str
        self.effective_available_flow = effective_available_flow  # type: str
        self.effective_total_flow = effective_total_flow  # type: str
        self.month_feature_fee = month_feature_fee  # type: long
        self.pool_avaiable = pool_avaiable  # type: str
        self.pool_grand_total = pool_grand_total  # type: str
        self.pool_grand_total_used = pool_grand_total_used  # type: str
        self.pool_out_used = pool_out_used  # type: str
        self.pool_used = pool_used  # type: str
        self.sms_used = sms_used  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_active_num is not None:
            result['CardActiveNum'] = self.card_active_num
        if self.card_total_num is not None:
            result['CardTotalNum'] = self.card_total_num
        if self.credential_instance_id is not None:
            result['CredentialInstanceId'] = self.credential_instance_id
        if self.credential_no is not None:
            result['CredentialNO'] = self.credential_no
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.effective_available_flow is not None:
            result['EffectiveAvailableFlow'] = self.effective_available_flow
        if self.effective_total_flow is not None:
            result['EffectiveTotalFlow'] = self.effective_total_flow
        if self.month_feature_fee is not None:
            result['MonthFeatureFee'] = self.month_feature_fee
        if self.pool_avaiable is not None:
            result['PoolAvaiable'] = self.pool_avaiable
        if self.pool_grand_total is not None:
            result['PoolGrandTotal'] = self.pool_grand_total
        if self.pool_grand_total_used is not None:
            result['PoolGrandTotalUsed'] = self.pool_grand_total_used
        if self.pool_out_used is not None:
            result['PoolOutUsed'] = self.pool_out_used
        if self.pool_used is not None:
            result['PoolUsed'] = self.pool_used
        if self.sms_used is not None:
            result['SmsUsed'] = self.sms_used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CardActiveNum') is not None:
            self.card_active_num = m.get('CardActiveNum')
        if m.get('CardTotalNum') is not None:
            self.card_total_num = m.get('CardTotalNum')
        if m.get('CredentialInstanceId') is not None:
            self.credential_instance_id = m.get('CredentialInstanceId')
        if m.get('CredentialNO') is not None:
            self.credential_no = m.get('CredentialNO')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('EffectiveAvailableFlow') is not None:
            self.effective_available_flow = m.get('EffectiveAvailableFlow')
        if m.get('EffectiveTotalFlow') is not None:
            self.effective_total_flow = m.get('EffectiveTotalFlow')
        if m.get('MonthFeatureFee') is not None:
            self.month_feature_fee = m.get('MonthFeatureFee')
        if m.get('PoolAvaiable') is not None:
            self.pool_avaiable = m.get('PoolAvaiable')
        if m.get('PoolGrandTotal') is not None:
            self.pool_grand_total = m.get('PoolGrandTotal')
        if m.get('PoolGrandTotalUsed') is not None:
            self.pool_grand_total_used = m.get('PoolGrandTotalUsed')
        if m.get('PoolOutUsed') is not None:
            self.pool_out_used = m.get('PoolOutUsed')
        if m.get('PoolUsed') is not None:
            self.pool_used = m.get('PoolUsed')
        if m.get('SmsUsed') is not None:
            self.sms_used = m.get('SmsUsed')
        return self


class GetCredentialPoolStatisticsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCredentialPoolStatisticsResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCredentialPoolStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCredentialPoolStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCredentialPoolStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCredentialPoolStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCredentialPoolStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebindResumeSingleCardRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns = opt_msisdns  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebindResumeSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class RebindResumeSingleCardShrinkRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns_shrink=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns_shrink = opt_msisdns_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebindResumeSingleCardShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class RebindResumeSingleCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebindResumeSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RebindResumeSingleCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RebindResumeSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebindResumeSingleCardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebindResumeSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeSingleCardRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns = opt_msisdns  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class ResumeSingleCardShrinkRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns_shrink=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns_shrink = opt_msisdns_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSingleCardShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class ResumeSingleCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeSingleCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeSingleCardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSingleCardRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns = opt_msisdns  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSingleCardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns is not None:
            result['OptMsisdns'] = self.opt_msisdns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns = m.get('OptMsisdns')
        return self


class StopSingleCardShrinkRequest(TeaModel):
    def __init__(self, iccid=None, opt_msisdns_shrink=None):
        self.iccid = iccid  # type: str
        self.opt_msisdns_shrink = opt_msisdns_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSingleCardShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.opt_msisdns_shrink is not None:
            result['OptMsisdns'] = self.opt_msisdns_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptMsisdns') is not None:
            self.opt_msisdns_shrink = m.get('OptMsisdns')
        return self


class StopSingleCardResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, localized_message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_message = error_message  # type: str
        self.localized_message = localized_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSingleCardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.localized_message is not None:
            result['LocalizedMessage'] = self.localized_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LocalizedMessage') is not None:
            self.localized_message = m.get('LocalizedMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopSingleCardResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopSingleCardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopSingleCardResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopSingleCardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


