# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeApplicationInfoRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, app_name=None, app_type_list=None, apping_list=None,
                 item_code=None):
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type_list = app_type_list  # type: str
        self.apping_list = apping_list  # type: str
        self.item_code = item_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplicationInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        if self.apping_list is not None:
            result['AppingList'] = self.apping_list
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        if m.get('AppingList') is not None:
            self.apping_list = m.get('AppingList')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class ChangeApplicationInfoResponseBody(TeaModel):
    def __init__(self, app_id=None, code=None, message=None, request_id=None, success=None):
        self.app_id = app_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeApplicationInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeApplicationInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeApplicationInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeApplicationInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeApplicationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationInfoRequestAppingList(TeaModel):
    def __init__(self, ext_id=None, flow_ip=None, flow_url=None, original_ip_list=None, original_url_list=None):
        self.ext_id = ext_id  # type: long
        self.flow_ip = flow_ip  # type: list[str]
        self.flow_url = flow_url  # type: list[str]
        self.original_ip_list = original_ip_list  # type: list[str]
        self.original_url_list = original_url_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationInfoRequestAppingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class CreateApplicationInfoRequest(TeaModel):
    def __init__(self, ali_uid=None, app_name=None, app_type_list=None, apping_list=None, item_code=None):
        self.ali_uid = ali_uid  # type: long
        self.app_name = app_name  # type: str
        self.app_type_list = app_type_list  # type: list[str]
        self.apping_list = apping_list  # type: list[CreateApplicationInfoRequestAppingList]
        self.item_code = item_code  # type: str

    def validate(self):
        if self.apping_list:
            for k in self.apping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateApplicationInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        result['AppingList'] = []
        if self.apping_list is not None:
            for k in self.apping_list:
                result['AppingList'].append(k.to_map() if k else None)
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        self.apping_list = []
        if m.get('AppingList') is not None:
            for k in m.get('AppingList'):
                temp_model = CreateApplicationInfoRequestAppingList()
                self.apping_list.append(temp_model.from_map(k))
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class CreateApplicationInfoResponseBody(TeaModel):
    def __init__(self, app_id=None, code=None, message=None, request_id=None, success=None):
        self.app_id = app_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateApplicationInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApplicationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAliyunXgipTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAliyunXgipTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAliyunXgipTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAliyunXgipTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAliyunXgipTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAliyunXgipTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(self, ali_uid=None, app_code=None, item_code=None):
        self.ali_uid = ali_uid  # type: long
        self.app_code = app_code  # type: str
        self.item_code = item_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[dict[str, any]]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowInstanceRequest(TeaModel):
    def __init__(self, aliuid=None, app_id=None, instance_id=None, item_code=None):
        self.aliuid = aliuid  # type: long
        self.app_id = app_id  # type: str
        self.instance_id = instance_id  # type: str
        self.item_code = item_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class GetFreeFlowInstanceResponseBodyData(TeaModel):
    def __init__(self, app_code=None, app_name=None, end_time=None, instance_memo=None, instance_status=None,
                 open_time=None, spec_type=None, start_time=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.end_time = end_time  # type: str
        self.instance_memo = instance_memo  # type: str
        self.instance_status = instance_status  # type: str
        self.open_time = open_time  # type: str
        self.spec_type = spec_type  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_memo is not None:
            result['InstanceMemo'] = self.instance_memo
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceMemo') is not None:
            self.instance_memo = m.get('InstanceMemo')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetFreeFlowInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetFreeFlowInstanceResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFreeFlowInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetFreeFlowInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFreeFlowInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFreeFlowInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFreeFlowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowProductListRequest(TeaModel):
    def __init__(self, ali_uid=None, instance_id=None):
        self.ali_uid = ali_uid  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowProductListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetFreeFlowProductListResponseBodyData(TeaModel):
    def __init__(self, configured=None, flow_product_amount=None, flow_product_id=None, flow_product_name=None,
                 flow_product_period=None, flow_type=None, operator=None, spec_type=None, spid=None, unit_price=None):
        self.configured = configured  # type: bool
        self.flow_product_amount = flow_product_amount  # type: str
        self.flow_product_id = flow_product_id  # type: str
        self.flow_product_name = flow_product_name  # type: str
        self.flow_product_period = flow_product_period  # type: str
        self.flow_type = flow_type  # type: str
        self.operator = operator  # type: str
        self.spec_type = spec_type  # type: str
        self.spid = spid  # type: str
        self.unit_price = unit_price  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowProductListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configured is not None:
            result['Configured'] = self.configured
        if self.flow_product_amount is not None:
            result['FlowProductAmount'] = self.flow_product_amount
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.flow_product_name is not None:
            result['FlowProductName'] = self.flow_product_name
        if self.flow_product_period is not None:
            result['FlowProductPeriod'] = self.flow_product_period
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.spid is not None:
            result['Spid'] = self.spid
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configured') is not None:
            self.configured = m.get('Configured')
        if m.get('FlowProductAmount') is not None:
            self.flow_product_amount = m.get('FlowProductAmount')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('FlowProductName') is not None:
            self.flow_product_name = m.get('FlowProductName')
        if m.get('FlowProductPeriod') is not None:
            self.flow_product_period = m.get('FlowProductPeriod')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('Spid') is not None:
            self.spid = m.get('Spid')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetFreeFlowProductListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetFreeFlowProductListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFreeFlowProductListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetFreeFlowProductListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowProductListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFreeFlowProductListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFreeFlowProductListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFreeFlowProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowUsageRequest(TeaModel):
    def __init__(self, ali_uid=None, cur_page_num=None, instance_id=None, month=None, num_per_page=None):
        self.ali_uid = ali_uid  # type: long
        self.cur_page_num = cur_page_num  # type: int
        self.instance_id = instance_id  # type: str
        self.month = month  # type: str
        self.num_per_page = num_per_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        return self


class GetFreeFlowUsageResponseBodyDataCustomerList(TeaModel):
    def __init__(self, channel_id=None, customer_end_time=None, customer_flow_order_id=None,
                 customer_flow_status=None, customer_open_time=None, customer_start_time=None, flow_product_id=None,
                 flow_product_name=None, is_lasting=None, mobile_number=None, unit_num=None, unit_price=None):
        self.channel_id = channel_id  # type: str
        self.customer_end_time = customer_end_time  # type: str
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_status = customer_flow_status  # type: str
        self.customer_open_time = customer_open_time  # type: str
        self.customer_start_time = customer_start_time  # type: str
        self.flow_product_id = flow_product_id  # type: str
        self.flow_product_name = flow_product_name  # type: str
        self.is_lasting = is_lasting  # type: bool
        self.mobile_number = mobile_number  # type: str
        self.unit_num = unit_num  # type: int
        self.unit_price = unit_price  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowUsageResponseBodyDataCustomerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.customer_end_time is not None:
            result['CustomerEndTime'] = self.customer_end_time
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_status is not None:
            result['CustomerFlowStatus'] = self.customer_flow_status
        if self.customer_open_time is not None:
            result['CustomerOpenTime'] = self.customer_open_time
        if self.customer_start_time is not None:
            result['CustomerStartTime'] = self.customer_start_time
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.flow_product_name is not None:
            result['FlowProductName'] = self.flow_product_name
        if self.is_lasting is not None:
            result['IsLasting'] = self.is_lasting
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CustomerEndTime') is not None:
            self.customer_end_time = m.get('CustomerEndTime')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowStatus') is not None:
            self.customer_flow_status = m.get('CustomerFlowStatus')
        if m.get('CustomerOpenTime') is not None:
            self.customer_open_time = m.get('CustomerOpenTime')
        if m.get('CustomerStartTime') is not None:
            self.customer_start_time = m.get('CustomerStartTime')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('FlowProductName') is not None:
            self.flow_product_name = m.get('FlowProductName')
        if m.get('IsLasting') is not None:
            self.is_lasting = m.get('IsLasting')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetFreeFlowUsageResponseBodyData(TeaModel):
    def __init__(self, cur_page_num=None, customer_list=None, has_next=None, has_prev=None, instance_id=None,
                 num_per_page=None, total_num=None, total_page_num=None):
        self.cur_page_num = cur_page_num  # type: int
        self.customer_list = customer_list  # type: list[GetFreeFlowUsageResponseBodyDataCustomerList]
        self.has_next = has_next  # type: bool
        self.has_prev = has_prev  # type: bool
        self.instance_id = instance_id  # type: str
        self.num_per_page = num_per_page  # type: int
        self.total_num = total_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.customer_list:
            for k in self.customer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFreeFlowUsageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        result['CustomerList'] = []
        if self.customer_list is not None:
            for k in self.customer_list:
                result['CustomerList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.has_prev is not None:
            result['HasPrev'] = self.has_prev
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        self.customer_list = []
        if m.get('CustomerList') is not None:
            for k in m.get('CustomerList'):
                temp_model = GetFreeFlowUsageResponseBodyDataCustomerList()
                self.customer_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('HasPrev') is not None:
            self.has_prev = m.get('HasPrev')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class GetFreeFlowUsageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetFreeFlowUsageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFreeFlowUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFreeFlowUsageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFreeFlowUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFreeFlowUsageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFreeFlowUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowUsageStatisticRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, app_name=None, instance_id=None, month=None):
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.instance_id = instance_id  # type: str
        self.month = month  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowUsageStatisticRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetFreeFlowUsageStatisticResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, spec_type=None, total_money=None, total_order_number=None,
                 total_unit_number=None, yun_out_product=None):
        self.instance_id = instance_id  # type: str
        self.spec_type = spec_type  # type: str
        self.total_money = total_money  # type: str
        self.total_order_number = total_order_number  # type: long
        self.total_unit_number = total_unit_number  # type: long
        self.yun_out_product = yun_out_product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowUsageStatisticResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.total_money is not None:
            result['TotalMoney'] = self.total_money
        if self.total_order_number is not None:
            result['TotalOrderNumber'] = self.total_order_number
        if self.total_unit_number is not None:
            result['TotalUnitNumber'] = self.total_unit_number
        if self.yun_out_product is not None:
            result['YunOutProduct'] = self.yun_out_product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('TotalMoney') is not None:
            self.total_money = m.get('TotalMoney')
        if m.get('TotalOrderNumber') is not None:
            self.total_order_number = m.get('TotalOrderNumber')
        if m.get('TotalUnitNumber') is not None:
            self.total_unit_number = m.get('TotalUnitNumber')
        if m.get('YunOutProduct') is not None:
            self.yun_out_product = m.get('YunOutProduct')
        return self


class GetFreeFlowUsageStatisticResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetFreeFlowUsageStatisticResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFreeFlowUsageStatisticResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetFreeFlowUsageStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFreeFlowUsageStatisticResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFreeFlowUsageStatisticResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFreeFlowUsageStatisticResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFreeFlowUsageStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderFreeFlowProductStatusRequest(TeaModel):
    def __init__(self, ali_uid=None, customer_flow_order_id=None):
        self.ali_uid = ali_uid  # type: long
        self.customer_flow_order_id = customer_flow_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrderFreeFlowProductStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        return self


class GetOrderFreeFlowProductStatusResponseBodyData(TeaModel):
    def __init__(self, customer_flow_order_id=None, customer_flow_request_id=None, error=None, status=None):
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        self.error = error  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrderFreeFlowProductStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.error is not None:
            result['Error'] = self.error
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetOrderFreeFlowProductStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetOrderFreeFlowProductStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOrderFreeFlowProductStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOrderFreeFlowProductStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderFreeFlowProductStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrderFreeFlowProductStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrderFreeFlowProductStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOrderFreeFlowProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQosFlowUsageRequest(TeaModel):
    def __init__(self, ali_uid=None, cur_page_num=None, end_time=None, instance_id=None, month=None,
                 num_per_page=None, start_time=None, type=None):
        self.ali_uid = ali_uid  # type: long
        self.cur_page_num = cur_page_num  # type: int
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.month = month  # type: long
        self.num_per_page = num_per_page  # type: int
        self.start_time = start_time  # type: str
        self.type = type  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQosFlowUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQosFlowUsageResponseBodyDataCustomerList(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, ds_day=None, ds_month=None, end_time=None, instance_id=None,
                 item_code=None, message=None, name=None, operator=None, order_num=None, product_id=None, product_name=None,
                 provice=None, qos_request_id=None, remark=None, spec_type=None, start_time=None, status=None,
                 total_price=None, totol_time=None):
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        self.ds_day = ds_day  # type: long
        self.ds_month = ds_month  # type: long
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.item_code = item_code  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.operator = operator  # type: str
        self.order_num = order_num  # type: int
        self.product_id = product_id  # type: str
        self.product_name = product_name  # type: str
        self.provice = provice  # type: str
        self.qos_request_id = qos_request_id  # type: str
        self.remark = remark  # type: str
        self.spec_type = spec_type  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.total_price = total_price  # type: int
        self.totol_time = totol_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQosFlowUsageResponseBodyDataCustomerList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ds_day is not None:
            result['DsDay'] = self.ds_day
        if self.ds_month is not None:
            result['DsMonth'] = self.ds_month
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.qos_request_id is not None:
            result['QosRequestId'] = self.qos_request_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.totol_time is not None:
            result['TotolTime'] = self.totol_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DsDay') is not None:
            self.ds_day = m.get('DsDay')
        if m.get('DsMonth') is not None:
            self.ds_month = m.get('DsMonth')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('QosRequestId') is not None:
            self.qos_request_id = m.get('QosRequestId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('TotolTime') is not None:
            self.totol_time = m.get('TotolTime')
        return self


class GetQosFlowUsageResponseBodyData(TeaModel):
    def __init__(self, cur_page_num=None, customer_list=None, has_next=None, has_prev=None, instance_id=None,
                 num_per_page=None, total_num=None, total_page_num=None):
        self.cur_page_num = cur_page_num  # type: int
        self.customer_list = customer_list  # type: list[GetQosFlowUsageResponseBodyDataCustomerList]
        self.has_next = has_next  # type: bool
        self.has_prev = has_prev  # type: bool
        self.instance_id = instance_id  # type: str
        self.num_per_page = num_per_page  # type: int
        self.total_num = total_num  # type: int
        self.total_page_num = total_page_num  # type: int

    def validate(self):
        if self.customer_list:
            for k in self.customer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQosFlowUsageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        result['CustomerList'] = []
        if self.customer_list is not None:
            for k in self.customer_list:
                result['CustomerList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.has_prev is not None:
            result['HasPrev'] = self.has_prev
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        self.customer_list = []
        if m.get('CustomerList') is not None:
            for k in m.get('CustomerList'):
                temp_model = GetQosFlowUsageResponseBodyDataCustomerList()
                self.customer_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('HasPrev') is not None:
            self.has_prev = m.get('HasPrev')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class GetQosFlowUsageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQosFlowUsageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQosFlowUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQosFlowUsageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQosFlowUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQosFlowUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQosFlowUsageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQosFlowUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQosUsageStatisticRequest(TeaModel):
    def __init__(self, ali_uid=None, cur_page_num=None, end_time=None, instance_id=None, month=None,
                 num_per_page=None, request_id=None, start_time=None):
        self.ali_uid = ali_uid  # type: long
        self.cur_page_num = cur_page_num  # type: int
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.month = month  # type: long
        self.num_per_page = num_per_page  # type: int
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQosUsageStatisticRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList(TeaModel):
    def __init__(self, bill_count=None, ds_day=None, fail_count=None, instance_id=None, month=None, operator=None,
                 product_name=None, provice=None, spec_type=None, sucess_count=None, total_count=None, yun_out_product=None):
        self.bill_count = bill_count  # type: long
        self.ds_day = ds_day  # type: long
        self.fail_count = fail_count  # type: long
        self.instance_id = instance_id  # type: str
        self.month = month  # type: long
        self.operator = operator  # type: str
        self.product_name = product_name  # type: str
        self.provice = provice  # type: str
        self.spec_type = spec_type  # type: str
        self.sucess_count = sucess_count  # type: long
        self.total_count = total_count  # type: long
        self.yun_out_product = yun_out_product  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_count is not None:
            result['BillCount'] = self.bill_count
        if self.ds_day is not None:
            result['DsDay'] = self.ds_day
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.sucess_count is not None:
            result['SucessCount'] = self.sucess_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.yun_out_product is not None:
            result['YunOutProduct'] = self.yun_out_product
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillCount') is not None:
            self.bill_count = m.get('BillCount')
        if m.get('DsDay') is not None:
            self.ds_day = m.get('DsDay')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('SucessCount') is not None:
            self.sucess_count = m.get('SucessCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('YunOutProduct') is not None:
            self.yun_out_product = m.get('YunOutProduct')
        return self


class GetQosUsageStatisticResponseBodyData(TeaModel):
    def __init__(self, cur_page_num=None, get_qos_usage_statistic_res_list=None, num_per_page=None, total_num=None):
        self.cur_page_num = cur_page_num  # type: int
        self.get_qos_usage_statistic_res_list = get_qos_usage_statistic_res_list  # type: list[GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList]
        self.num_per_page = num_per_page  # type: int
        self.total_num = total_num  # type: int

    def validate(self):
        if self.get_qos_usage_statistic_res_list:
            for k in self.get_qos_usage_statistic_res_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQosUsageStatisticResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_page_num is not None:
            result['CurPageNum'] = self.cur_page_num
        result['GetQosUsageStatisticResList'] = []
        if self.get_qos_usage_statistic_res_list is not None:
            for k in self.get_qos_usage_statistic_res_list:
                result['GetQosUsageStatisticResList'].append(k.to_map() if k else None)
        if self.num_per_page is not None:
            result['NumPerPage'] = self.num_per_page
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurPageNum') is not None:
            self.cur_page_num = m.get('CurPageNum')
        self.get_qos_usage_statistic_res_list = []
        if m.get('GetQosUsageStatisticResList') is not None:
            for k in m.get('GetQosUsageStatisticResList'):
                temp_model = GetQosUsageStatisticResponseBodyDataGetQosUsageStatisticResList()
                self.get_qos_usage_statistic_res_list.append(temp_model.from_map(k))
        if m.get('NumPerPage') is not None:
            self.num_per_page = m.get('NumPerPage')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetQosUsageStatisticResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQosUsageStatisticResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQosUsageStatisticResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQosUsageStatisticResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQosUsageStatisticResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetQosUsageStatisticResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQosUsageStatisticResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQosUsageStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUatDataListRequest(TeaModel):
    def __init__(self, ali_uid=None, ds_month=None, item_id=None):
        self.ali_uid = ali_uid  # type: long
        self.ds_month = ds_month  # type: long
        self.item_id = item_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUatDataListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.ds_month is not None:
            result['DsMonth'] = self.ds_month
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DsMonth') is not None:
            self.ds_month = m.get('DsMonth')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetUatDataListResponseBodyDataDsList(TeaModel):
    def __init__(self, ds_data=None, ds_day=None):
        self.ds_data = ds_data  # type: long
        self.ds_day = ds_day  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUatDataListResponseBodyDataDsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_data is not None:
            result['DsData'] = self.ds_data
        if self.ds_day is not None:
            result['DsDay'] = self.ds_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DsData') is not None:
            self.ds_data = m.get('DsData')
        if m.get('DsDay') is not None:
            self.ds_day = m.get('DsDay')
        return self


class GetUatDataListResponseBodyData(TeaModel):
    def __init__(self, ds_list=None, spec_type=None):
        self.ds_list = ds_list  # type: list[GetUatDataListResponseBodyDataDsList]
        self.spec_type = spec_type  # type: str

    def validate(self):
        if self.ds_list:
            for k in self.ds_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUatDataListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DsList'] = []
        if self.ds_list is not None:
            for k in self.ds_list:
                result['DsList'].append(k.to_map() if k else None)
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ds_list = []
        if m.get('DsList') is not None:
            for k in m.get('DsList'):
                temp_model = GetUatDataListResponseBodyDataDsList()
                self.ds_list.append(temp_model.from_map(k))
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        return self


class GetUatDataListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetUatDataListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUatDataListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetUatDataListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUatDataListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUatDataListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUatDataListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUatDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUatSpecCtDataRequest(TeaModel):
    def __init__(self, ali_uid=None, ds_month=None, item_id=None):
        self.ali_uid = ali_uid  # type: long
        self.ds_month = ds_month  # type: long
        self.item_id = item_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUatSpecCtDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.ds_month is not None:
            result['DsMonth'] = self.ds_month
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DsMonth') is not None:
            self.ds_month = m.get('DsMonth')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetUatSpecCtDataResponseBodyData(TeaModel):
    def __init__(self, month_count=None, spec_type=None):
        self.month_count = month_count  # type: long
        self.spec_type = spec_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUatSpecCtDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.month_count is not None:
            result['MonthCount'] = self.month_count
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MonthCount') is not None:
            self.month_count = m.get('MonthCount')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        return self


class GetUatSpecCtDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetUatSpecCtDataResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUatSpecCtDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetUatSpecCtDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUatSpecCtDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUatSpecCtDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUatSpecCtDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUatSpecCtDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MockGetOrderFreeFlowProductStatusRequest(TeaModel):
    def __init__(self, ali_uid=None, customer_flow_order_id=None):
        self.ali_uid = ali_uid  # type: long
        self.customer_flow_order_id = customer_flow_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MockGetOrderFreeFlowProductStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        return self


class MockGetOrderFreeFlowProductStatusResponseBodyData(TeaModel):
    def __init__(self, customer_flow_order_id=None, customer_flow_request_id=None, error=None, status=None):
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        self.error = error  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MockGetOrderFreeFlowProductStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.error is not None:
            result['Error'] = self.error
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MockGetOrderFreeFlowProductStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: MockGetOrderFreeFlowProductStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MockGetOrderFreeFlowProductStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MockGetOrderFreeFlowProductStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MockGetOrderFreeFlowProductStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MockGetOrderFreeFlowProductStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MockGetOrderFreeFlowProductStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MockGetOrderFreeFlowProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MockOrderFreeFlowProductRequest(TeaModel):
    def __init__(self, ali_uid=None, channel_id=None, customer_flow_request_id=None, flow_product_id=None,
                 instance_id=None, lasting=None, mobile_number=None, notify_url=None, operator=None, purchase_order_id=None):
        self.ali_uid = ali_uid  # type: long
        self.channel_id = channel_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        self.flow_product_id = flow_product_id  # type: str
        self.instance_id = instance_id  # type: str
        self.lasting = lasting  # type: str
        self.mobile_number = mobile_number  # type: str
        self.notify_url = notify_url  # type: str
        self.operator = operator  # type: str
        self.purchase_order_id = purchase_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MockOrderFreeFlowProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lasting is not None:
            result['Lasting'] = self.lasting
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.purchase_order_id is not None:
            result['PurchaseOrderId'] = self.purchase_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lasting') is not None:
            self.lasting = m.get('Lasting')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PurchaseOrderId') is not None:
            self.purchase_order_id = m.get('PurchaseOrderId')
        return self


class MockOrderFreeFlowProductResponseBodyData(TeaModel):
    def __init__(self, biz_code=None, customer_flow_order_id=None, customer_flow_request_id=None, status=None):
        self.biz_code = biz_code  # type: str
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MockOrderFreeFlowProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MockOrderFreeFlowProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: MockOrderFreeFlowProductResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MockOrderFreeFlowProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MockOrderFreeFlowProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MockOrderFreeFlowProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MockOrderFreeFlowProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MockOrderFreeFlowProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MockOrderFreeFlowProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApplicationRequestAppingList(TeaModel):
    def __init__(self, ext_id=None, flow_ip=None, flow_url=None, original_ip_list=None, original_url_list=None):
        self.ext_id = ext_id  # type: long
        self.flow_ip = flow_ip  # type: list[str]
        self.flow_url = flow_url  # type: list[str]
        self.original_ip_list = original_ip_list  # type: list[str]
        self.original_url_list = original_url_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyApplicationRequestAppingList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class ModifyApplicationRequest(TeaModel):
    def __init__(self, ali_uid=None, app_code=None, app_name=None, app_type_list=None, apping_list=None):
        self.ali_uid = ali_uid  # type: long
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.app_type_list = app_type_list  # type: list[str]
        self.apping_list = apping_list  # type: list[ModifyApplicationRequestAppingList]

    def validate(self):
        if self.apping_list:
            for k in self.apping_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        result['AppingList'] = []
        if self.apping_list is not None:
            for k in self.apping_list:
                result['AppingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        self.apping_list = []
        if m.get('AppingList') is not None:
            for k in m.get('AppingList'):
                temp_model = ModifyApplicationRequestAppingList()
                self.apping_list.append(temp_model.from_map(k))
        return self


class ModifyApplicationResponseBody(TeaModel):
    def __init__(self, app_id=None, code=None, message=None, request_id=None, success=None):
        self.app_id = app_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderFreeFlowProductRequest(TeaModel):
    def __init__(self, ali_uid=None, channel_id=None, customer_flow_request_id=None, flow_product_id=None,
                 instance_id=None, lasting=None, mobile_number=None, notify_url=None, operator=None, purchase_order_id=None):
        self.ali_uid = ali_uid  # type: long
        self.channel_id = channel_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        self.flow_product_id = flow_product_id  # type: str
        self.instance_id = instance_id  # type: str
        self.lasting = lasting  # type: str
        self.mobile_number = mobile_number  # type: str
        self.notify_url = notify_url  # type: str
        self.operator = operator  # type: str
        self.purchase_order_id = purchase_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderFreeFlowProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lasting is not None:
            result['Lasting'] = self.lasting
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.purchase_order_id is not None:
            result['PurchaseOrderId'] = self.purchase_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lasting') is not None:
            self.lasting = m.get('Lasting')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PurchaseOrderId') is not None:
            self.purchase_order_id = m.get('PurchaseOrderId')
        return self


class OrderFreeFlowProductResponseBodyData(TeaModel):
    def __init__(self, biz_code=None, customer_flow_order_id=None, customer_flow_request_id=None, status=None):
        self.biz_code = biz_code  # type: str
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderFreeFlowProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.customer_flow_order_id is not None:
            result['CustomerFlowOrderId'] = self.customer_flow_order_id
        if self.customer_flow_request_id is not None:
            result['CustomerFlowRequestId'] = self.customer_flow_request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('CustomerFlowOrderId') is not None:
            self.customer_flow_order_id = m.get('CustomerFlowOrderId')
        if m.get('CustomerFlowRequestId') is not None:
            self.customer_flow_request_id = m.get('CustomerFlowRequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class OrderFreeFlowProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: OrderFreeFlowProductResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(OrderFreeFlowProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = OrderFreeFlowProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OrderFreeFlowProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderFreeFlowProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OrderFreeFlowProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OrderFreeFlowProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderQosProductRequest(TeaModel):
    def __init__(self, ali_uid=None, channel_id=None, ipv_6=None, instance_id=None, ip_type=None, mobile_number=None,
                 operator=None, private_ipv_4=None, product_id=None, provice=None, public_ipv_4=None, qos_request_id=None,
                 target_ip_list=None, token=None, unit_num=None):
        self.ali_uid = ali_uid  # type: long
        self.channel_id = channel_id  # type: str
        self.ipv_6 = ipv_6  # type: str
        self.instance_id = instance_id  # type: str
        self.ip_type = ip_type  # type: str
        self.mobile_number = mobile_number  # type: str
        self.operator = operator  # type: str
        self.private_ipv_4 = private_ipv_4  # type: str
        self.product_id = product_id  # type: str
        self.provice = provice  # type: str
        self.public_ipv_4 = public_ipv_4  # type: str
        self.qos_request_id = qos_request_id  # type: str
        self.target_ip_list = target_ip_list  # type: list[str]
        self.token = token  # type: str
        self.unit_num = unit_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderQosProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.private_ipv_4 is not None:
            result['PrivateIpv4'] = self.private_ipv_4
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.provice is not None:
            result['Provice'] = self.provice
        if self.public_ipv_4 is not None:
            result['PublicIpv4'] = self.public_ipv_4
        if self.qos_request_id is not None:
            result['QosRequestId'] = self.qos_request_id
        if self.target_ip_list is not None:
            result['TargetIpList'] = self.target_ip_list
        if self.token is not None:
            result['Token'] = self.token
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PrivateIpv4') is not None:
            self.private_ipv_4 = m.get('PrivateIpv4')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Provice') is not None:
            self.provice = m.get('Provice')
        if m.get('PublicIpv4') is not None:
            self.public_ipv_4 = m.get('PublicIpv4')
        if m.get('QosRequestId') is not None:
            self.qos_request_id = m.get('QosRequestId')
        if m.get('TargetIpList') is not None:
            self.target_ip_list = m.get('TargetIpList')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class OrderQosProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderQosProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OrderQosProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderQosProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OrderQosProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OrderQosProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApplicationInfoRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, app_name=None, app_type_list=None, apping_list=None,
                 item_code=None):
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type_list = app_type_list  # type: str
        self.apping_list = apping_list  # type: str
        self.item_code = item_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApplicationInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type_list is not None:
            result['AppTypeList'] = self.app_type_list
        if self.apping_list is not None:
            result['AppingList'] = self.apping_list
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTypeList') is not None:
            self.app_type_list = m.get('AppTypeList')
        if m.get('AppingList') is not None:
            self.apping_list = m.get('AppingList')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class SaveApplicationInfoResponseBody(TeaModel):
    def __init__(self, app_id=None, code=None, message=None, request_id=None, success=None):
        self.app_id = app_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApplicationInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveApplicationInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApplicationInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApplicationInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveApplicationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkValidateStatusRequest(TeaModel):
    def __init__(self, app_id=None, credential_type=None, credential_value=None, operator=None, token=None):
        self.app_id = app_id  # type: str
        self.credential_type = credential_type  # type: str
        self.credential_value = credential_value  # type: str
        self.operator = operator  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkValidateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.credential_value is not None:
            result['CredentialValue'] = self.credential_value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('CredentialValue') is not None:
            self.credential_value = m.get('CredentialValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class SdkValidateStatusResponseBodyDataAppExtPopList(TeaModel):
    def __init__(self, ext_id=None, flow_ip=None, flow_url=None, original_ip_list=None, original_url_list=None):
        self.ext_id = ext_id  # type: long
        self.flow_ip = flow_ip  # type: list[str]
        self.flow_url = flow_url  # type: list[str]
        self.original_ip_list = original_ip_list  # type: list[str]
        self.original_url_list = original_url_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SdkValidateStatusResponseBodyDataAppExtPopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class SdkValidateStatusResponseBodyData(TeaModel):
    def __init__(self, app_ext_pop_list=None, free_flow=None, pseudo_code=None):
        self.app_ext_pop_list = app_ext_pop_list  # type: list[SdkValidateStatusResponseBodyDataAppExtPopList]
        self.free_flow = free_flow  # type: bool
        self.pseudo_code = pseudo_code  # type: str

    def validate(self):
        if self.app_ext_pop_list:
            for k in self.app_ext_pop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SdkValidateStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppExtPopList'] = []
        if self.app_ext_pop_list is not None:
            for k in self.app_ext_pop_list:
                result['AppExtPopList'].append(k.to_map() if k else None)
        if self.free_flow is not None:
            result['FreeFlow'] = self.free_flow
        if self.pseudo_code is not None:
            result['PseudoCode'] = self.pseudo_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_ext_pop_list = []
        if m.get('AppExtPopList') is not None:
            for k in m.get('AppExtPopList'):
                temp_model = SdkValidateStatusResponseBodyDataAppExtPopList()
                self.app_ext_pop_list.append(temp_model.from_map(k))
        if m.get('FreeFlow') is not None:
            self.free_flow = m.get('FreeFlow')
        if m.get('PseudoCode') is not None:
            self.pseudo_code = m.get('PseudoCode')
        return self


class SdkValidateStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SdkValidateStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SdkValidateStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SdkValidateStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SdkValidateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SdkValidateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SdkValidateStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SdkValidateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidControllerAuthorRequest(TeaModel):
    def __init__(self, ali_uid=None, item_code=None):
        self.ali_uid = ali_uid  # type: long
        self.item_code = item_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidControllerAuthorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        return self


class ValidControllerAuthorResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidControllerAuthorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidControllerAuthorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValidControllerAuthorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidControllerAuthorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidControllerAuthorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateStatusRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, credential_type=None, credential_value=None, operator=None):
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        self.credential_type = credential_type  # type: str
        self.credential_value = credential_value  # type: str
        self.operator = operator  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.credential_value is not None:
            result['CredentialValue'] = self.credential_value
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('CredentialValue') is not None:
            self.credential_value = m.get('CredentialValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class ValidateStatusResponseBodyDataAppExtPopList(TeaModel):
    def __init__(self, ext_id=None, flow_ip=None, flow_url=None, original_ip_list=None, original_url_list=None):
        self.ext_id = ext_id  # type: long
        self.flow_ip = flow_ip  # type: list[str]
        self.flow_url = flow_url  # type: list[str]
        self.original_ip_list = original_ip_list  # type: list[str]
        self.original_url_list = original_url_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateStatusResponseBodyDataAppExtPopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.flow_ip is not None:
            result['FlowIp'] = self.flow_ip
        if self.flow_url is not None:
            result['FlowUrl'] = self.flow_url
        if self.original_ip_list is not None:
            result['OriginalIpList'] = self.original_ip_list
        if self.original_url_list is not None:
            result['OriginalUrlList'] = self.original_url_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('FlowIp') is not None:
            self.flow_ip = m.get('FlowIp')
        if m.get('FlowUrl') is not None:
            self.flow_url = m.get('FlowUrl')
        if m.get('OriginalIpList') is not None:
            self.original_ip_list = m.get('OriginalIpList')
        if m.get('OriginalUrlList') is not None:
            self.original_url_list = m.get('OriginalUrlList')
        return self


class ValidateStatusResponseBodyData(TeaModel):
    def __init__(self, app_ext_pop_list=None, free_flow=None, pseudo_code=None):
        self.app_ext_pop_list = app_ext_pop_list  # type: list[ValidateStatusResponseBodyDataAppExtPopList]
        self.free_flow = free_flow  # type: bool
        self.pseudo_code = pseudo_code  # type: str

    def validate(self):
        if self.app_ext_pop_list:
            for k in self.app_ext_pop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ValidateStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppExtPopList'] = []
        if self.app_ext_pop_list is not None:
            for k in self.app_ext_pop_list:
                result['AppExtPopList'].append(k.to_map() if k else None)
        if self.free_flow is not None:
            result['FreeFlow'] = self.free_flow
        if self.pseudo_code is not None:
            result['PseudoCode'] = self.pseudo_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_ext_pop_list = []
        if m.get('AppExtPopList') is not None:
            for k in m.get('AppExtPopList'):
                temp_model = ValidateStatusResponseBodyDataAppExtPopList()
                self.app_ext_pop_list.append(temp_model.from_map(k))
        if m.get('FreeFlow') is not None:
            self.free_flow = m.get('FreeFlow')
        if m.get('PseudoCode') is not None:
            self.pseudo_code = m.get('PseudoCode')
        return self


class ValidateStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ValidateStatusResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.rt = rt  # type: long
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ValidateStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ValidateStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValidateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


