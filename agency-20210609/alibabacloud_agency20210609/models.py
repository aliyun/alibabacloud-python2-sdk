# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetOwnerAgreementInstanceRequest(TeaModel):
    def __init__(self, aliyun_uid=None):
        self.aliyun_uid = aliyun_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOwnerAgreementInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        return self


class GetOwnerAgreementInstanceResponseBodyDataAgreementPropertyRoleDTOList(TeaModel):
    def __init__(self, agreement_code=None):
        self.agreement_code = agreement_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOwnerAgreementInstanceResponseBodyDataAgreementPropertyRoleDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class GetOwnerAgreementInstanceResponseBodyData(TeaModel):
    def __init__(self, agreement_property_role_dtolist=None, name=None, pid=None, uid=None):
        self.agreement_property_role_dtolist = agreement_property_role_dtolist  # type: list[GetOwnerAgreementInstanceResponseBodyDataAgreementPropertyRoleDTOList]
        self.name = name  # type: str
        self.pid = pid  # type: str
        self.uid = uid  # type: str

    def validate(self):
        if self.agreement_property_role_dtolist:
            for k in self.agreement_property_role_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOwnerAgreementInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AgreementPropertyRoleDTOList'] = []
        if self.agreement_property_role_dtolist is not None:
            for k in self.agreement_property_role_dtolist:
                result['AgreementPropertyRoleDTOList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.agreement_property_role_dtolist = []
        if m.get('AgreementPropertyRoleDTOList') is not None:
            for k in m.get('AgreementPropertyRoleDTOList'):
                temp_model = GetOwnerAgreementInstanceResponseBodyDataAgreementPropertyRoleDTOList()
                self.agreement_property_role_dtolist.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetOwnerAgreementInstanceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, request_id=None, success=None):
        self.data = data  # type: GetOwnerAgreementInstanceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOwnerAgreementInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetOwnerAgreementInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOwnerAgreementInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOwnerAgreementInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOwnerAgreementInstanceResponse, self).to_map()
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
            temp_model = GetOwnerAgreementInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPartnerByUidRequest(TeaModel):
    def __init__(self, aliyun_uid=None):
        self.aliyun_uid = aliyun_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPartnerByUidRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        return self


class GetPartnerByUidResponseBodyDataAgreementPropertyRoleDTOList(TeaModel):
    def __init__(self, agreement_code=None):
        self.agreement_code = agreement_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPartnerByUidResponseBodyDataAgreementPropertyRoleDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class GetPartnerByUidResponseBodyData(TeaModel):
    def __init__(self, agreement_property_role_dtolist=None, name=None, pid=None, uid=None):
        self.agreement_property_role_dtolist = agreement_property_role_dtolist  # type: list[GetPartnerByUidResponseBodyDataAgreementPropertyRoleDTOList]
        self.name = name  # type: str
        self.pid = pid  # type: str
        self.uid = uid  # type: str

    def validate(self):
        if self.agreement_property_role_dtolist:
            for k in self.agreement_property_role_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPartnerByUidResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AgreementPropertyRoleDTOList'] = []
        if self.agreement_property_role_dtolist is not None:
            for k in self.agreement_property_role_dtolist:
                result['AgreementPropertyRoleDTOList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.agreement_property_role_dtolist = []
        if m.get('AgreementPropertyRoleDTOList') is not None:
            for k in m.get('AgreementPropertyRoleDTOList'):
                temp_model = GetPartnerByUidResponseBodyDataAgreementPropertyRoleDTOList()
                self.agreement_property_role_dtolist.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetPartnerByUidResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, request_id=None, success=None):
        self.data = data  # type: GetPartnerByUidResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPartnerByUidResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetPartnerByUidResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPartnerByUidResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPartnerByUidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPartnerByUidResponse, self).to_map()
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
            temp_model = GetPartnerByUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFusionOrderListRequest(TeaModel):
    def __init__(self, end_time=None, end_user_id=None, order_id=None, page_no=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.end_user_id = end_user_id  # type: long
        self.order_id = order_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFusionOrderListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryFusionOrderListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, page_no=None, page_size=None, request_id=None, total=None):
        self.code = code  # type: str
        self.data = data  # type: list[str]
        self.msg = msg  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        # RequestId
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFusionOrderListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFusionOrderListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFusionOrderListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFusionOrderListResponse, self).to_map()
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
            temp_model = QueryFusionOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


