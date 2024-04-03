# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetFxCustomerTypeRequest(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFxCustomerTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetFxCustomerTypeResponseBodyData(TeaModel):
    def __init__(self, customer_type=None, is_sub=None, parent_id=None):
        self.customer_type = customer_type  # type: int
        self.is_sub = is_sub  # type: int
        self.parent_id = parent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFxCustomerTypeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_type is not None:
            result['CustomerType'] = self.customer_type
        if self.is_sub is not None:
            result['IsSub'] = self.is_sub
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerType') is not None:
            self.customer_type = m.get('CustomerType')
        if m.get('IsSub') is not None:
            self.is_sub = m.get('IsSub')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class GetFxCustomerTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetFxCustomerTypeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetFxCustomerTypeResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFxCustomerTypeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFxCustomerTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFxCustomerTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFxCustomerTypeResponse, self).to_map()
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
            temp_model = GetFxCustomerTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


