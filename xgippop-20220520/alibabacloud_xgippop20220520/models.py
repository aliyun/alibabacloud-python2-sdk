# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeApplicationInfoRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, app_name=None, app_type_list=None, apping_list=None,
                 item_code=None):
        # 阿里UID
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # dynamic|static
        self.app_type_list = app_type_list  # type: str
        # [
        self.apping_list = apping_list  # type: str
        # 商品code
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
        # 应用id
        self.app_id = app_id  # type: str
        # 结果码
        self.code = code  # type: str
        # 结果描述
        self.message = message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 是否成功
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
        # cdn ip
        self.flow_ip = flow_ip  # type: list[str]
        # cdn 域名信息
        self.flow_url = flow_url  # type: list[str]
        # 业务方ip集合
        self.original_ip_list = original_ip_list  # type: list[str]
        # 业务方域名集合
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
        # 阿里UID
        self.ali_uid = ali_uid  # type: long
        # 应用名称
        self.app_name = app_name  # type: str
        # dynamic（动态业务）/static（静态业务
        self.app_type_list = app_type_list  # type: list[str]
        self.apping_list = apping_list  # type: list[CreateApplicationInfoRequestAppingList]
        # 商品code
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
        # 应用id
        self.app_id = app_id  # type: str
        # 结果码
        self.code = code  # type: str
        # 结果描述
        self.message = message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 是否成功
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


class GetApplicationRequest(TeaModel):
    def __init__(self, ali_uid=None, app_code=None):
        # 阿里UID
        self.ali_uid = ali_uid  # type: long
        # 应用ID
        self.app_code = app_code  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        # 结果码
        self.code = code  # type: str
        self.data = data  # type: list[dict[str, any]]
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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
        # 应用ID
        self.app_id = app_id  # type: str
        # 实例ID
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
        # APP编号
        self.app_code = app_code  # type: str
        # APP名称
        self.app_name = app_name  # type: str
        # 产品失效时间
        self.end_time = end_time  # type: str
        # 实例名称
        self.instance_memo = instance_memo  # type: str
        # 实例状态
        self.instance_status = instance_status  # type: str
        # 产品开通时间
        self.open_time = open_time  # type: str
        # 规格类型
        self.spec_type = spec_type  # type: str
        # 产品生效时间
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
        # 结果码
        self.code = code  # type: str
        # 结果
        self.data = data  # type: list[GetFreeFlowInstanceResponseBodyData]
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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
        # 用户编号
        self.ali_uid = ali_uid  # type: long
        # 实例ID
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
        # 产品当前状态，true为已配置，false为未配置
        self.configured = configured  # type: bool
        # 产品包含的流量大小
        self.flow_product_amount = flow_product_amount  # type: str
        # 免流产品ID
        self.flow_product_id = flow_product_id  # type: str
        # 流量包名称
        self.flow_product_name = flow_product_name  # type: str
        # 产品周期
        self.flow_product_period = flow_product_period  # type: str
        # 取值包括free（定向流量）/normal（通用流量）
        self.flow_type = flow_type  # type: str
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
        self.operator = operator  # type: str
        # 注意这里返回的全量套餐里，只能包含SpecType与该InstanceId的SpecType相同的规格
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
        # 结果码
        self.code = code  # type: str
        self.data = data  # type: list[GetFreeFlowProductListResponseBodyData]
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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


class GetFreeFlowStatusRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, flow_product_id=None, mobile_number=None, net_type=None,
                 operator=None, private_ip=None, pseudo_code=None, public_ip=None, token=None):
        self.ali_uid = ali_uid  # type: long
        # 应用ID
        self.app_id = app_id  # type: str
        # 免流产品ID
        self.flow_product_id = flow_product_id  # type: str
        # C端手机号
        self.mobile_number = mobile_number  # type: str
        # 网络类型，如3G、4G、5G
        self.net_type = net_type  # type: str
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
        self.operator = operator  # type: str
        # 手机端私网ip地址
        self.private_ip = private_ip  # type: str
        # C端手机在运营商侧端伪码，如："75D35971BD"
        self.pseudo_code = pseudo_code  # type: str
        # 手机端公网ip地址
        self.public_ip = public_ip  # type: str
        # 通过云通信获取的token
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.flow_product_id is not None:
            result['FlowProductId'] = self.flow_product_id
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip
        if self.pseudo_code is not None:
            result['PseudoCode'] = self.pseudo_code
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FlowProductId') is not None:
            self.flow_product_id = m.get('FlowProductId')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')
        if m.get('PseudoCode') is not None:
            self.pseudo_code = m.get('PseudoCode')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetFreeFlowStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        # 结果码
        self.code = code  # type: str
        # 结果
        self.data = data  # type: any
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFreeFlowStatusResponseBody, self).to_map()
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


class GetFreeFlowStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFreeFlowStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFreeFlowStatusResponse, self).to_map()
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
            temp_model = GetFreeFlowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFreeFlowUsageRequest(TeaModel):
    def __init__(self, ali_uid=None, cur_page_num=None, instance_id=None, month=None, num_per_page=None):
        self.ali_uid = ali_uid  # type: long
        # 当前页
        self.cur_page_num = cur_page_num  # type: int
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 查询月份
        self.month = month  # type: str
        # 每页的记录数量
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
        # 购买渠道
        self.channel_id = channel_id  # type: str
        # C端产品失效时间
        self.customer_end_time = customer_end_time  # type: str
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        # C端免流状态，取值包括create/working/expiration
        self.customer_flow_status = customer_flow_status  # type: str
        # C端产品开通时间
        self.customer_open_time = customer_open_time  # type: str
        # C端产品生效时间
        self.customer_start_time = customer_start_time  # type: str
        # 免流产品ID
        self.flow_product_id = flow_product_id  # type: str
        # 免流产品名
        self.flow_product_name = flow_product_name  # type: str
        # 是否包月，true或false
        self.is_lasting = is_lasting  # type: bool
        # C端手机号
        self.mobile_number = mobile_number  # type: str
        # 该流量包的计量单元数
        self.unit_num = unit_num  # type: int
        # 流量包价格
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
        # 当前页数
        self.cur_page_num = cur_page_num  # type: int
        # C端用户列表
        self.customer_list = customer_list  # type: list[GetFreeFlowUsageResponseBodyDataCustomerList]
        # 是否有下一页
        self.has_next = has_next  # type: bool
        # 是否有上一页
        self.has_prev = has_prev  # type: bool
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 每页的记录条数
        self.num_per_page = num_per_page  # type: int
        # 总记录条数
        self.total_num = total_num  # type: int
        # 总页数
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
        # 结果码
        self.code = code  # type: str
        # 结果
        self.data = data  # type: GetFreeFlowUsageResponseBodyData
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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
        # 该实例对应的包类型
        self.spec_type = spec_type  # type: str
        self.total_money = total_money  # type: str
        # 该实例的订单总数
        self.total_order_number = total_order_number  # type: long
        # 该实例的订单总计量单元数
        self.total_unit_number = total_unit_number  # type: long
        # 产品规格
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
        # 结果码
        self.code = code  # type: str
        # 结果
        self.data = data  # type: list[GetFreeFlowUsageStatisticResponseBodyData]
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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
        # 在订购接口2.1.9中引擎侧生成的id
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
        # C端免流订单ID
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        # status为fail时，描述fail的具体原因
        self.error = error  # type: str
        # 执行中ordering、成功success、失败fail
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
        # 结果码
        self.code = code  # type: str
        self.data = data  # type: GetOrderFreeFlowProductStatusResponseBodyData
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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


class ModifyApplicationRequestAppingList(TeaModel):
    def __init__(self, ext_id=None, flow_ip=None, flow_url=None, original_ip_list=None, original_url_list=None):
        self.ext_id = ext_id  # type: long
        # cdn ip
        self.flow_ip = flow_ip  # type: list[str]
        # cdn 域名信息
        self.flow_url = flow_url  # type: list[str]
        # 业务方ip集合
        self.original_ip_list = original_ip_list  # type: list[str]
        # 业务方域名集合
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
        # AliUid
        self.ali_uid = ali_uid  # type: long
        # AppId
        self.app_code = app_code  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # dynamic（动态业务）/static（静态业务
        self.app_type_list = app_type_list  # type: list[str]
        # 扩展属性 源域名和源ip信息保存
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
        # 应用id
        self.app_id = app_id  # type: str
        # 结果码
        self.code = code  # type: str
        # 结果描述
        self.message = message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 是否成功
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
        # 渠道ID
        self.channel_id = channel_id  # type: str
        # 客户侧生成的QoS请求ID，需要保证请求幂等性，确保不同请求间该参数值唯一
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        # 免流产品ID
        self.flow_product_id = flow_product_id  # type: str
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 是否包月，true为包月，false为不包月
        self.lasting = lasting  # type: str
        # C端手机号
        self.mobile_number = mobile_number  # type: str
        # 客户提供的回调通知接口url
        self.notify_url = notify_url  # type: str
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
        self.operator = operator  # type: str
        # 支付订单ID
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
        # C端免流订单ID
        self.customer_flow_order_id = customer_flow_order_id  # type: str
        self.customer_flow_request_id = customer_flow_request_id  # type: str
        # 执行中ordering、成功success、失败fail
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
        # 结果码
        self.code = code  # type: str
        # 结果
        self.data = data  # type: OrderFreeFlowProductResponseBodyData
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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


class SaveApplicationInfoRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, app_name=None, app_type_list=None, apping_list=None,
                 item_code=None):
        # 阿里UID
        self.ali_uid = ali_uid  # type: long
        self.app_id = app_id  # type: str
        # 应用名称
        self.app_name = app_name  # type: str
        # dynamic|static
        self.app_type_list = app_type_list  # type: str
        # [
        self.apping_list = apping_list  # type: str
        # 商品code
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
        # 应用id
        self.app_id = app_id  # type: str
        # 结果码
        self.code = code  # type: str
        # 结果描述
        self.message = message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 是否成功
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


class ValidateStatusRequest(TeaModel):
    def __init__(self, ali_uid=None, app_id=None, credential_type=None, credential_value=None, operator=None):
        # 阿里UID
        self.ali_uid = ali_uid  # type: long
        # 应用名称
        self.app_id = app_id  # type: str
        # 凭证类型
        self.credential_type = credential_type  # type: str
        # mobile=150xxxx4661
        self.credential_value = credential_value  # type: str
        # 取值包括cm（中国移动）/ct（中国电信）/cu（中国联通）
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
        # cdn ip
        self.flow_ip = flow_ip  # type: list[str]
        # cdn 域名信息
        self.flow_url = flow_url  # type: list[str]
        # 业务方ip集合
        self.original_ip_list = original_ip_list  # type: list[str]
        # 业务方域名集合
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
        # 是否处于免流状态，取值范围为true/false
        self.free_flow = free_flow  # type: bool
        # 伪码
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
        # 结果码
        self.code = code  # type: str
        # 结果
        self.data = data  # type: ValidateStatusResponseBodyData
        # 结果描述
        self.message = message  # type: str
        # 请求链路ID，如POP请求进来的requestId，返回时原样返回
        self.request_id = request_id  # type: str
        # 服务端处理耗时，ms
        self.rt = rt  # type: long
        # 是否成功
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


