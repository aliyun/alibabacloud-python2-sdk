# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataValue(TeaModel):
    def __init__(self, service_id=None, status=None, code=None, message=None):
        self.service_id = service_id  # type: long
        self.status = status  # type: str
        self.code = code  # type: int
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ADClockRequest(TeaModel):
    def __init__(self, params=None, service_code=None):
        self.params = params  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADClockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADClockResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADClockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADClockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ADClockResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ADClockResponse, self).to_map()
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
            temp_model = ADClockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ADMMURequest(TeaModel):
    def __init__(self, params=None, service_code=None):
        self.params = params  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADMMURequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADMMUResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADMMUResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADMMUResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ADMMUResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ADMMUResponse, self).to_map()
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
            temp_model = ADMMUResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ADMiniCogRequest(TeaModel):
    def __init__(self, params=None, service_code=None):
        self.params = params  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADMiniCogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADMiniCogResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADMiniCogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADMiniCogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ADMiniCogResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ADMiniCogResponse, self).to_map()
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
            temp_model = ADMiniCogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ADMiniCogResultRequest(TeaModel):
    def __init__(self, params=None, service_code=None):
        self.params = params  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADMiniCogResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADMiniCogResultResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ADMiniCogResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADMiniCogResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ADMiniCogResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ADMiniCogResultResponse, self).to_map()
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
            temp_model = ADMiniCogResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceDataByConditionsRequest(TeaModel):
    def __init__(self, conditions=None, service_id=None):
        self.conditions = conditions  # type: dict[str, any]
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceDataByConditionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceDataByConditionsShrinkRequest(TeaModel):
    def __init__(self, conditions_shrink=None, service_id=None):
        self.conditions_shrink = conditions_shrink  # type: str
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceDataByConditionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceDataByConditionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceDataByConditionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceDataByConditionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceDataByConditionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceDataByConditionsResponse, self).to_map()
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
            temp_model = DeleteServiceDataByConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceDataByIdsRequest(TeaModel):
    def __init__(self, ids=None, service_id=None):
        self.ids = ids  # type: list[str]
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceDataByIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceDataByIdsShrinkRequest(TeaModel):
    def __init__(self, ids_shrink=None, service_id=None):
        self.ids_shrink = ids_shrink  # type: str
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceDataByIdsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceDataByIdsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceDataByIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceDataByIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServiceDataByIdsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceDataByIdsResponse, self).to_map()
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
            temp_model = DeleteServiceDataByIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBrandChEcomRequest(TeaModel):
    def __init__(self, image_url=None, service_code=None, text=None):
        self.image_url = image_url  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBrandChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetBrandChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBrandChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBrandChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBrandChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBrandChEcomResponse, self).to_map()
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
            temp_model = GetBrandChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCateChEcomRequest(TeaModel):
    def __init__(self, image_url=None, service_code=None, text=None):
        self.image_url = image_url  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCateChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetCateChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCateChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCateChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCateChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCateChEcomResponse, self).to_map()
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
            temp_model = GetCateChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCheckDuplicationChMedicalRequest(TeaModel):
    def __init__(self, origin_q=None, origin_t=None, service_code=None):
        self.origin_q = origin_q  # type: str
        self.origin_t = origin_t  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCheckDuplicationChMedicalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_q is not None:
            result['OriginQ'] = self.origin_q
        if self.origin_t is not None:
            result['OriginT'] = self.origin_t
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginQ') is not None:
            self.origin_q = m.get('OriginQ')
        if m.get('OriginT') is not None:
            self.origin_t = m.get('OriginT')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetCheckDuplicationChMedicalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCheckDuplicationChMedicalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCheckDuplicationChMedicalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCheckDuplicationChMedicalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCheckDuplicationChMedicalResponse, self).to_map()
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
            temp_model = GetCheckDuplicationChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnosisChMedicalRequest(TeaModel):
    def __init__(self, name=None, service_code=None):
        self.name = name  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnosisChMedicalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetDiagnosisChMedicalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnosisChMedicalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiagnosisChMedicalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDiagnosisChMedicalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDiagnosisChMedicalResponse, self).to_map()
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
            temp_model = GetDiagnosisChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDpChEcomRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDpChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDpChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDpChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDpChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDpChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDpChEcomResponse, self).to_map()
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
            temp_model = GetDpChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDpChGeneralCTBRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDpChGeneralCTBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDpChGeneralCTBResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDpChGeneralCTBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDpChGeneralCTBResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDpChGeneralCTBResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDpChGeneralCTBResponse, self).to_map()
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
            temp_model = GetDpChGeneralCTBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDpChGeneralStanfordRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDpChGeneralStanfordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDpChGeneralStanfordResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDpChGeneralStanfordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDpChGeneralStanfordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDpChGeneralStanfordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDpChGeneralStanfordResponse, self).to_map()
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
            temp_model = GetDpChGeneralStanfordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEcChGeneralRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEcChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetEcChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEcChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEcChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEcChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEcChGeneralResponse, self).to_map()
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
            temp_model = GetEcChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEcEnGeneralRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEcEnGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetEcEnGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEcEnGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEcEnGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEcEnGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEcEnGeneralResponse, self).to_map()
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
            temp_model = GetEcEnGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmbeddingRequest(TeaModel):
    def __init__(self, service_code=None, text=None, text_type=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.text_type = text_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmbeddingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.text_type is not None:
            result['TextType'] = self.text_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')
        return self


class GetEmbeddingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEmbeddingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEmbeddingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEmbeddingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEmbeddingResponse, self).to_map()
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
            temp_model = GetEmbeddingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemPubChEcomRequest(TeaModel):
    def __init__(self, image_url=None, service_code=None, text=None):
        self.image_url = image_url  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetItemPubChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetItemPubChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetItemPubChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetItemPubChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetItemPubChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetItemPubChEcomResponse, self).to_map()
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
            temp_model = GetItemPubChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeywordChEcomRequest(TeaModel):
    def __init__(self, api_version=None, service_code=None, text=None):
        self.api_version = api_version  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKeywordChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetKeywordChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKeywordChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetKeywordChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetKeywordChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetKeywordChEcomResponse, self).to_map()
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
            temp_model = GetKeywordChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeywordEnEcomRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKeywordEnEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetKeywordEnEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKeywordEnEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetKeywordEnEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetKeywordEnEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetKeywordEnEcomResponse, self).to_map()
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
            temp_model = GetKeywordEnEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMedicineChMedicalRequest(TeaModel):
    def __init__(self, factory=None, name=None, service_code=None, specification=None, unit=None):
        self.factory = factory  # type: str
        self.name = name  # type: str
        self.service_code = service_code  # type: str
        self.specification = specification  # type: str
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMedicineChMedicalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory is not None:
            result['Factory'] = self.factory
        if self.name is not None:
            result['Name'] = self.name
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Factory') is not None:
            self.factory = m.get('Factory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetMedicineChMedicalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMedicineChMedicalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMedicineChMedicalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMedicineChMedicalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMedicineChMedicalResponse, self).to_map()
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
            temp_model = GetMedicineChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerChEcomRequest(TeaModel):
    def __init__(self, lexer_id=None, service_code=None, text=None):
        self.lexer_id = lexer_id  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lexer_id is not None:
            result['LexerId'] = self.lexer_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LexerId') is not None:
            self.lexer_id = m.get('LexerId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNerChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNerChEcomResponse, self).to_map()
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
            temp_model = GetNerChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerChMedicalRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerChMedicalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerChMedicalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerChMedicalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerChMedicalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNerChMedicalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNerChMedicalResponse, self).to_map()
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
            temp_model = GetNerChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerCustomizedChEcomRequest(TeaModel):
    def __init__(self, lexer_id=None, service_code=None, text=None):
        self.lexer_id = lexer_id  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerCustomizedChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lexer_id is not None:
            result['LexerId'] = self.lexer_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LexerId') is not None:
            self.lexer_id = m.get('LexerId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerCustomizedChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerCustomizedChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerCustomizedChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNerCustomizedChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNerCustomizedChEcomResponse, self).to_map()
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
            temp_model = GetNerCustomizedChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerCustomizedSeaEcomRequest(TeaModel):
    def __init__(self, language=None, service_code=None, text=None):
        self.language = language  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerCustomizedSeaEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerCustomizedSeaEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNerCustomizedSeaEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerCustomizedSeaEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNerCustomizedSeaEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNerCustomizedSeaEcomResponse, self).to_map()
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
            temp_model = GetNerCustomizedSeaEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenNLURequest(TeaModel):
    def __init__(self, examples=None, labels=None, sentence=None, service_code=None, task=None):
        self.examples = examples  # type: str
        self.labels = labels  # type: str
        self.sentence = sentence  # type: str
        self.service_code = service_code  # type: str
        self.task = task  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpenNLURequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.examples is not None:
            result['Examples'] = self.examples
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.sentence is not None:
            result['Sentence'] = self.sentence
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.task is not None:
            result['Task'] = self.task
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Examples') is not None:
            self.examples = m.get('Examples')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Sentence') is not None:
            self.sentence = m.get('Sentence')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        return self


class GetOpenNLUResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpenNLUResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOpenNLUResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOpenNLUResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOpenNLUResponse, self).to_map()
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
            temp_model = GetOpenNLUResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenNLUHighRecallRequest(TeaModel):
    def __init__(self, examples=None, labels=None, sentence=None, service_code=None, task=None):
        self.examples = examples  # type: str
        self.labels = labels  # type: str
        self.sentence = sentence  # type: str
        self.service_code = service_code  # type: str
        self.task = task  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpenNLUHighRecallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.examples is not None:
            result['Examples'] = self.examples
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.sentence is not None:
            result['Sentence'] = self.sentence
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.task is not None:
            result['Task'] = self.task
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Examples') is not None:
            self.examples = m.get('Examples')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Sentence') is not None:
            self.sentence = m.get('Sentence')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        return self


class GetOpenNLUHighRecallResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpenNLUHighRecallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOpenNLUHighRecallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOpenNLUHighRecallResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOpenNLUHighRecallResponse, self).to_map()
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
            temp_model = GetOpenNLUHighRecallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperationChMedicalRequest(TeaModel):
    def __init__(self, name=None, service_code=None):
        self.name = name  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOperationChMedicalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetOperationChMedicalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOperationChMedicalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOperationChMedicalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOperationChMedicalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOperationChMedicalResponse, self).to_map()
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
            temp_model = GetOperationChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPosChEcomRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPosChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetPosChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPosChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPosChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPosChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPosChEcomResponse, self).to_map()
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
            temp_model = GetPosChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPosChGeneralRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPosChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetPosChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPosChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPosChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPosChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPosChGeneralResponse, self).to_map()
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
            temp_model = GetPosChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPriceChEcomRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPriceChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetPriceChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPriceChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPriceChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPriceChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPriceChEcomResponse, self).to_map()
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
            temp_model = GetPriceChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSSETestRequest(TeaModel):
    def __init__(self, params=None, service_code=None):
        self.params = params  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSSETestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetSSETestResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSSETestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSSETestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSSETestResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSSETestResponse, self).to_map()
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
            temp_model = GetSSETestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaChGeneralRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSaChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSaChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSaChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSaChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSaChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSaChGeneralResponse, self).to_map()
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
            temp_model = GetSaChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaSeaEcomRequest(TeaModel):
    def __init__(self, language=None, service_code=None, text=None):
        self.language = language  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSaSeaEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSaSeaEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSaSeaEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSaSeaEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSaSeaEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSaSeaEcomResponse, self).to_map()
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
            temp_model = GetSaSeaEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceDataImportStatusRequest(TeaModel):
    def __init__(self, data_import_ids=None):
        self.data_import_ids = data_import_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDataImportStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_import_ids is not None:
            result['DataImportIds'] = self.data_import_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataImportIds') is not None:
            self.data_import_ids = m.get('DataImportIds')
        return self


class GetServiceDataImportStatusShrinkRequest(TeaModel):
    def __init__(self, data_import_ids_shrink=None):
        self.data_import_ids_shrink = data_import_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDataImportStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_import_ids_shrink is not None:
            result['DataImportIds'] = self.data_import_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataImportIds') is not None:
            self.data_import_ids_shrink = m.get('DataImportIds')
        return self


class GetServiceDataImportStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: dict[str, DataValue]
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for v in self.data.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(GetServiceDataImportStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                result['Data'][k] = v.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = {}
        if m.get('Data') is not None:
            for k, v in m.get('Data').items():
                temp_model = DataValue()
                self.data[k] = temp_model.from_map(v)
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetServiceDataImportStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceDataImportStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceDataImportStatusResponse, self).to_map()
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
            temp_model = GetServiceDataImportStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSimilarityChMedicalRequest(TeaModel):
    def __init__(self, origin_q=None, origin_t=None, service_code=None):
        self.origin_q = origin_q  # type: str
        self.origin_t = origin_t  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSimilarityChMedicalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_q is not None:
            result['OriginQ'] = self.origin_q
        if self.origin_t is not None:
            result['OriginT'] = self.origin_t
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginQ') is not None:
            self.origin_q = m.get('OriginQ')
        if m.get('OriginT') is not None:
            self.origin_t = m.get('OriginT')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetSimilarityChMedicalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSimilarityChMedicalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSimilarityChMedicalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSimilarityChMedicalResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSimilarityChMedicalResponse, self).to_map()
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
            temp_model = GetSimilarityChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSummaryChEcomRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSummaryChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSummaryChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSummaryChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSummaryChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSummaryChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSummaryChEcomResponse, self).to_map()
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
            temp_model = GetSummaryChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableQAServiceInfoByIdRequest(TeaModel):
    def __init__(self, service_code=None, service_id=None):
        self.service_code = service_code  # type: str
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTableQAServiceInfoByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetTableQAServiceInfoByIdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTableQAServiceInfoByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTableQAServiceInfoByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTableQAServiceInfoByIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTableQAServiceInfoByIdResponse, self).to_map()
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
            temp_model = GetTableQAServiceInfoByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTcChEcomRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTcChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetTcChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTcChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTcChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTcChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTcChEcomResponse, self).to_map()
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
            temp_model = GetTcChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTcChGeneralRequest(TeaModel):
    def __init__(self, service_code=None, text=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTcChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetTcChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTcChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTcChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTcChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTcChGeneralResponse, self).to_map()
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
            temp_model = GetTcChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTsChEcomRequest(TeaModel):
    def __init__(self, origin_q=None, origin_t=None, service_code=None, type=None):
        self.origin_q = origin_q  # type: str
        self.origin_t = origin_t  # type: str
        self.service_code = service_code  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTsChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_q is not None:
            result['OriginQ'] = self.origin_q
        if self.origin_t is not None:
            result['OriginT'] = self.origin_t
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginQ') is not None:
            self.origin_q = m.get('OriginQ')
        if m.get('OriginT') is not None:
            self.origin_t = m.get('OriginT')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTsChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTsChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTsChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTsChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTsChEcomResponse, self).to_map()
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
            temp_model = GetTsChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserUploadSignRequest(TeaModel):
    def __init__(self, service_code=None):
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserUploadSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetUserUploadSignResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserUploadSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserUploadSignResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserUploadSignResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserUploadSignResponse, self).to_map()
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
            temp_model = GetUserUploadSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChCommentRequest(TeaModel):
    def __init__(self, operation=None, service_code=None, size=None, text=None, tokenizer_id=None, type=None):
        self.operation = operation  # type: str
        self.service_code = service_code  # type: str
        self.size = size  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChCommentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChCommentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChCommentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWeChCommentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWeChCommentResponse, self).to_map()
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
            temp_model = GetWeChCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChEcomRequest(TeaModel):
    def __init__(self, operation=None, service_code=None, size=None, text=None, tokenizer_id=None, type=None):
        self.operation = operation  # type: str
        self.service_code = service_code  # type: str
        self.size = size  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWeChEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWeChEcomResponse, self).to_map()
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
            temp_model = GetWeChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChEntertainmentRequest(TeaModel):
    def __init__(self, operation=None, service_code=None, size=None, text=None, tokenizer_id=None, type=None):
        self.operation = operation  # type: str
        self.service_code = service_code  # type: str
        self.size = size  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChEntertainmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChEntertainmentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChEntertainmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChEntertainmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWeChEntertainmentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWeChEntertainmentResponse, self).to_map()
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
            temp_model = GetWeChEntertainmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChGeneralRequest(TeaModel):
    def __init__(self, operation=None, service_code=None, size=None, text=None, type=None):
        self.operation = operation  # type: str
        self.service_code = service_code  # type: str
        self.size = size  # type: str
        self.text = text  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWeChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWeChGeneralResponse, self).to_map()
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
            temp_model = GetWeChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChSearchRequest(TeaModel):
    def __init__(self, operation=None, service_code=None, size=None, text=None, tokenizer_id=None, type=None):
        self.operation = operation  # type: str
        self.service_code = service_code  # type: str
        self.size = size  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChSearchResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWeChSearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChSearchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWeChSearchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWeChSearchResponse, self).to_map()
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
            temp_model = GetWeChSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsChGeneralRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsChGeneralResponse, self).to_map()
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
            temp_model = GetWsChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEcomCommentRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEcomCommentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEcomCommentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEcomCommentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEcomCommentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedChEcomCommentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedChEcomCommentResponse, self).to_map()
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
            temp_model = GetWsCustomizedChEcomCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEcomContentRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEcomContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEcomContentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEcomContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEcomContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedChEcomContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedChEcomContentResponse, self).to_map()
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
            temp_model = GetWsCustomizedChEcomContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEcomTitleRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEcomTitleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEcomTitleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEcomTitleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEcomTitleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedChEcomTitleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedChEcomTitleResponse, self).to_map()
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
            temp_model = GetWsCustomizedChEcomTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEntertainmentRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEntertainmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEntertainmentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChEntertainmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEntertainmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedChEntertainmentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedChEntertainmentResponse, self).to_map()
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
            temp_model = GetWsCustomizedChEntertainmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChGeneralRequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedChGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedChGeneralResponse, self).to_map()
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
            temp_model = GetWsCustomizedChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChO2ORequest(TeaModel):
    def __init__(self, out_type=None, service_code=None, text=None, tokenizer_id=None):
        self.out_type = out_type  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.tokenizer_id = tokenizer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChO2ORequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChO2OResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedChO2OResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChO2OResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedChO2OResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedChO2OResponse, self).to_map()
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
            temp_model = GetWsCustomizedChO2OResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedSeaEcomRequest(TeaModel):
    def __init__(self, language=None, service_code=None, text=None):
        self.language = language  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedSeaEcomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetWsCustomizedSeaEcomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedSeaEcomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedSeaEcomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedSeaEcomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedSeaEcomResponse, self).to_map()
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
            temp_model = GetWsCustomizedSeaEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedSeaGeneralRequest(TeaModel):
    def __init__(self, language=None, service_code=None, text=None):
        self.language = language  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedSeaGeneralRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetWsCustomizedSeaGeneralResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWsCustomizedSeaGeneralResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedSeaGeneralResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWsCustomizedSeaGeneralResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWsCustomizedSeaGeneralResponse, self).to_map()
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
            temp_model = GetWsCustomizedSeaGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportServiceDataRequest(TeaModel):
    def __init__(self, partition=None, service_id=None, sub_path=None, url=None):
        self.partition = partition  # type: list[dict[str, str]]
        self.service_id = service_id  # type: long
        self.sub_path = sub_path  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServiceDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ImportServiceDataShrinkRequest(TeaModel):
    def __init__(self, partition_shrink=None, service_id=None, sub_path=None, url=None):
        self.partition_shrink = partition_shrink  # type: str
        self.service_id = service_id  # type: long
        self.sub_path = sub_path  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServiceDataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition_shrink is not None:
            result['Partition'] = self.partition_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Partition') is not None:
            self.partition_shrink = m.get('Partition')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ImportServiceDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServiceDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportServiceDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportServiceDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportServiceDataResponse, self).to_map()
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
            temp_model = ImportServiceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportServiceDataV2RequestDocuments(TeaModel):
    def __init__(self, biz_params=None, doc_id=None, file_extension=None, file_name=None, file_path=None,
                 version=None):
        self.biz_params = biz_params  # type: dict[str, str]
        self.doc_id = doc_id  # type: str
        self.file_extension = file_extension  # type: str
        self.file_name = file_name  # type: str
        self.file_path = file_path  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServiceDataV2RequestDocuments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ImportServiceDataV2Request(TeaModel):
    def __init__(self, data_type=None, documents=None, service_id=None):
        self.data_type = data_type  # type: str
        self.documents = documents  # type: list[ImportServiceDataV2RequestDocuments]
        self.service_id = service_id  # type: long

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportServiceDataV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = ImportServiceDataV2RequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ImportServiceDataV2ShrinkRequest(TeaModel):
    def __init__(self, data_type=None, documents_shrink=None, service_id=None):
        self.data_type = data_type  # type: str
        self.documents_shrink = documents_shrink  # type: str
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServiceDataV2ShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ImportServiceDataV2ResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportServiceDataV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportServiceDataV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportServiceDataV2ResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportServiceDataV2Response, self).to_map()
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
            temp_model = ImportServiceDataV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertCustomRequest(TeaModel):
    def __init__(self, api_id=None, custom_file_name=None, custom_url=None, reg_file_name=None, reg_url=None,
                 service_code=None):
        self.api_id = api_id  # type: int
        self.custom_file_name = custom_file_name  # type: str
        self.custom_url = custom_url  # type: str
        self.reg_file_name = reg_file_name  # type: str
        self.reg_url = reg_url  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertCustomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.custom_file_name is not None:
            result['CustomFileName'] = self.custom_file_name
        if self.custom_url is not None:
            result['CustomUrl'] = self.custom_url
        if self.reg_file_name is not None:
            result['RegFileName'] = self.reg_file_name
        if self.reg_url is not None:
            result['RegUrl'] = self.reg_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('CustomFileName') is not None:
            self.custom_file_name = m.get('CustomFileName')
        if m.get('CustomUrl') is not None:
            self.custom_url = m.get('CustomUrl')
        if m.get('RegFileName') is not None:
            self.reg_file_name = m.get('RegFileName')
        if m.get('RegUrl') is not None:
            self.reg_url = m.get('RegUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class InsertCustomResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertCustomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InsertCustomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertCustomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertCustomResponse, self).to_map()
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
            temp_model = InsertCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAlinlpServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenAlinlpServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenAlinlpServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenAlinlpServiceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenAlinlpServiceResponse, self).to_map()
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
            temp_model = OpenAlinlpServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostISConvRewriterRequest(TeaModel):
    def __init__(self, algorithm=None, debug=None, input=None, parameters=None, version=None):
        self.algorithm = algorithm  # type: str
        self.debug = debug  # type: bool
        self.input = input  # type: dict[str, any]
        self.parameters = parameters  # type: dict[str, any]
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostISConvRewriterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input is not None:
            result['Input'] = self.input
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PostISConvRewriterShrinkRequest(TeaModel):
    def __init__(self, algorithm=None, debug=None, input_shrink=None, parameters_shrink=None, version=None):
        self.algorithm = algorithm  # type: str
        self.debug = debug  # type: bool
        self.input_shrink = input_shrink  # type: str
        self.parameters_shrink = parameters_shrink  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostISConvRewriterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PostISConvRewriterResponseBody(TeaModel):
    def __init__(self, data=None, debug_info=None, message=None, request_id=None, status=None):
        self.data = data  # type: dict[str, any]
        self.debug_info = debug_info  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostISConvRewriterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostISConvRewriterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostISConvRewriterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostISConvRewriterResponse, self).to_map()
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
            temp_model = PostISConvRewriterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostISRetrieveRouterRequest(TeaModel):
    def __init__(self, algorithm=None, debug=None, input=None, parameters=None, version=None):
        self.algorithm = algorithm  # type: str
        self.debug = debug  # type: bool
        self.input = input  # type: dict[str, any]
        self.parameters = parameters  # type: dict[str, any]
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostISRetrieveRouterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input is not None:
            result['Input'] = self.input
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PostISRetrieveRouterShrinkRequest(TeaModel):
    def __init__(self, algorithm=None, debug=None, input_shrink=None, parameters_shrink=None, version=None):
        self.algorithm = algorithm  # type: str
        self.debug = debug  # type: bool
        self.input_shrink = input_shrink  # type: str
        self.parameters_shrink = parameters_shrink  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostISRetrieveRouterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PostISRetrieveRouterResponseBody(TeaModel):
    def __init__(self, data=None, debug_info=None, message=None, request_id=None, status=None):
        self.data = data  # type: dict[str, any]
        self.debug_info = debug_info  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostISRetrieveRouterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostISRetrieveRouterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostISRetrieveRouterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostISRetrieveRouterResponse, self).to_map()
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
            temp_model = PostISRetrieveRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSConvSearchTokenGeneratedResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSConvSearchTokenGeneratedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSConvSearchTokenGeneratedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostMSConvSearchTokenGeneratedResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostMSConvSearchTokenGeneratedResponse, self).to_map()
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
            temp_model = PostMSConvSearchTokenGeneratedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSDataProcessingCountRequest(TeaModel):
    def __init__(self, data_ids=None, data_import_id=None, service_id=None):
        self.data_ids = data_ids  # type: list[str]
        self.data_import_id = data_import_id  # type: long
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSDataProcessingCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ids is not None:
            result['DataIds'] = self.data_ids
        if self.data_import_id is not None:
            result['DataImportId'] = self.data_import_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataIds') is not None:
            self.data_ids = m.get('DataIds')
        if m.get('DataImportId') is not None:
            self.data_import_id = m.get('DataImportId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class PostMSDataProcessingCountShrinkRequest(TeaModel):
    def __init__(self, data_ids_shrink=None, data_import_id=None, service_id=None):
        self.data_ids_shrink = data_ids_shrink  # type: str
        self.data_import_id = data_import_id  # type: long
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSDataProcessingCountShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ids_shrink is not None:
            result['DataIds'] = self.data_ids_shrink
        if self.data_import_id is not None:
            result['DataImportId'] = self.data_import_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataIds') is not None:
            self.data_ids_shrink = m.get('DataIds')
        if m.get('DataImportId') is not None:
            self.data_import_id = m.get('DataImportId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList(TeaModel):
    def __init__(self, count=None, error_code=None, op_type=None):
        self.count = count  # type: int
        self.error_code = error_code  # type: str
        self.op_type = op_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses(TeaModel):
    def __init__(self, chunk_num=None, data_id=None, error_data_list=None, op_status=None, status=None,
                 version_value=None):
        self.chunk_num = chunk_num  # type: str
        self.data_id = data_id  # type: str
        self.error_data_list = error_data_list  # type: list[PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList]
        self.op_status = op_status  # type: dict[str, int]
        self.status = status  # type: str
        self.version_value = version_value  # type: str

    def validate(self):
        if self.error_data_list:
            for k in self.error_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_num is not None:
            result['ChunkNum'] = self.chunk_num
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['ErrorDataList'] = []
        if self.error_data_list is not None:
            for k in self.error_data_list:
                result['ErrorDataList'].append(k.to_map() if k else None)
        if self.op_status is not None:
            result['OpStatus'] = self.op_status
        if self.status is not None:
            result['Status'] = self.status
        if self.version_value is not None:
            result['VersionValue'] = self.version_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChunkNum') is not None:
            self.chunk_num = m.get('ChunkNum')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.error_data_list = []
        if m.get('ErrorDataList') is not None:
            for k in m.get('ErrorDataList'):
                temp_model = PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList()
                self.error_data_list.append(temp_model.from_map(k))
        if m.get('OpStatus') is not None:
            self.op_status = m.get('OpStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionValue') is not None:
            self.version_value = m.get('VersionValue')
        return self


class PostMSDataProcessingCountResponseBodyData(TeaModel):
    def __init__(self, data_processed_statuses=None, status=None):
        self.data_processed_statuses = data_processed_statuses  # type: list[PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses]
        self.status = status  # type: str

    def validate(self):
        if self.data_processed_statuses:
            for k in self.data_processed_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PostMSDataProcessingCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataProcessedStatuses'] = []
        if self.data_processed_statuses is not None:
            for k in self.data_processed_statuses:
                result['DataProcessedStatuses'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_processed_statuses = []
        if m.get('DataProcessedStatuses') is not None:
            for k in m.get('DataProcessedStatuses'):
                temp_model = PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses()
                self.data_processed_statuses.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostMSDataProcessingCountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: PostMSDataProcessingCountResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PostMSDataProcessingCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = PostMSDataProcessingCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSDataProcessingCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostMSDataProcessingCountResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostMSDataProcessingCountResponse, self).to_map()
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
            temp_model = PostMSDataProcessingCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSSearchEnhanceRequest(TeaModel):
    def __init__(self, body=None, custom_config_info=None, debug=None, fields=None, filters=None, min_score=None,
                 page=None, queries=None, rank_model_info=None, rows=None, service_id=None, sort=None, type=None, uq=None):
        self.body = body  # type: str
        self.custom_config_info = custom_config_info  # type: dict[str, any]
        self.debug = debug  # type: bool
        self.fields = fields  # type: list[str]
        self.filters = filters  # type: str
        self.min_score = min_score  # type: float
        self.page = page  # type: int
        self.queries = queries  # type: str
        self.rank_model_info = rank_model_info  # type: dict[str, any]
        self.rows = rows  # type: int
        self.service_id = service_id  # type: long
        self.sort = sort  # type: list[str]
        self.type = type  # type: str
        self.uq = uq  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSSearchEnhanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.custom_config_info is not None:
            result['CustomConfigInfo'] = self.custom_config_info
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.page is not None:
            result['Page'] = self.page
        if self.queries is not None:
            result['Queries'] = self.queries
        if self.rank_model_info is not None:
            result['RankModelInfo'] = self.rank_model_info
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.type is not None:
            result['Type'] = self.type
        if self.uq is not None:
            result['Uq'] = self.uq
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('CustomConfigInfo') is not None:
            self.custom_config_info = m.get('CustomConfigInfo')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Queries') is not None:
            self.queries = m.get('Queries')
        if m.get('RankModelInfo') is not None:
            self.rank_model_info = m.get('RankModelInfo')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uq') is not None:
            self.uq = m.get('Uq')
        return self


class PostMSSearchEnhanceShrinkRequest(TeaModel):
    def __init__(self, body=None, custom_config_info_shrink=None, debug=None, fields_shrink=None, filters=None,
                 min_score=None, page=None, queries=None, rank_model_info_shrink=None, rows=None, service_id=None,
                 sort_shrink=None, type=None, uq=None):
        self.body = body  # type: str
        self.custom_config_info_shrink = custom_config_info_shrink  # type: str
        self.debug = debug  # type: bool
        self.fields_shrink = fields_shrink  # type: str
        self.filters = filters  # type: str
        self.min_score = min_score  # type: float
        self.page = page  # type: int
        self.queries = queries  # type: str
        self.rank_model_info_shrink = rank_model_info_shrink  # type: str
        self.rows = rows  # type: int
        self.service_id = service_id  # type: long
        self.sort_shrink = sort_shrink  # type: str
        self.type = type  # type: str
        self.uq = uq  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSSearchEnhanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.custom_config_info_shrink is not None:
            result['CustomConfigInfo'] = self.custom_config_info_shrink
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.fields_shrink is not None:
            result['Fields'] = self.fields_shrink
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.page is not None:
            result['Page'] = self.page
        if self.queries is not None:
            result['Queries'] = self.queries
        if self.rank_model_info_shrink is not None:
            result['RankModelInfo'] = self.rank_model_info_shrink
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.uq is not None:
            result['Uq'] = self.uq
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('CustomConfigInfo') is not None:
            self.custom_config_info_shrink = m.get('CustomConfigInfo')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Fields') is not None:
            self.fields_shrink = m.get('Fields')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Queries') is not None:
            self.queries = m.get('Queries')
        if m.get('RankModelInfo') is not None:
            self.rank_model_info_shrink = m.get('RankModelInfo')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uq') is not None:
            self.uq = m.get('Uq')
        return self


class PostMSSearchEnhanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.http_status_code = http_status_code  # type: int
        self.msg = msg  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSSearchEnhanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSSearchEnhanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostMSSearchEnhanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostMSSearchEnhanceResponse, self).to_map()
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
            temp_model = PostMSSearchEnhanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSServiceDataImportRequestDocuments(TeaModel):
    def __init__(self, biz_params=None, doc_id=None, file_extension=None, file_name=None, file_path=None,
                 version=None):
        self.biz_params = biz_params  # type: dict[str, any]
        self.doc_id = doc_id  # type: str
        self.file_extension = file_extension  # type: str
        self.file_name = file_name  # type: str
        self.file_path = file_path  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSServiceDataImportRequestDocuments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PostMSServiceDataImportRequest(TeaModel):
    def __init__(self, data_type=None, documents=None, service_id=None):
        self.data_type = data_type  # type: str
        self.documents = documents  # type: list[PostMSServiceDataImportRequestDocuments]
        self.service_id = service_id  # type: long

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PostMSServiceDataImportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = PostMSServiceDataImportRequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class PostMSServiceDataImportShrinkRequest(TeaModel):
    def __init__(self, data_type=None, documents_shrink=None, service_id=None):
        self.data_type = data_type  # type: str
        self.documents_shrink = documents_shrink  # type: str
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSServiceDataImportShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class PostMSServiceDataImportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: long
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PostMSServiceDataImportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSServiceDataImportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PostMSServiceDataImportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PostMSServiceDataImportResponse, self).to_map()
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
            temp_model = PostMSServiceDataImportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestTableQARequest(TeaModel):
    def __init__(self, params=None, service_code=None):
        self.params = params  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestTableQARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RequestTableQAResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestTableQAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RequestTableQAResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestTableQAResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestTableQAResponse, self).to_map()
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
            temp_model = RequestTableQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestTableQAOnlineRequest(TeaModel):
    def __init__(self, bot_id=None, params=None, question=None, service_code=None):
        self.bot_id = bot_id  # type: str
        self.params = params  # type: str
        self.question = question  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestTableQAOnlineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot_id is not None:
            result['BotId'] = self.bot_id
        if self.params is not None:
            result['Params'] = self.params
        if self.question is not None:
            result['Question'] = self.question
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RequestTableQAOnlineResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestTableQAOnlineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RequestTableQAOnlineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestTableQAOnlineResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestTableQAOnlineResponse, self).to_map()
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
            temp_model = RequestTableQAOnlineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceDataRequest(TeaModel):
    def __init__(self, conditions=None, service_id=None):
        self.conditions = conditions  # type: dict[str, any]
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateServiceDataShrinkRequest(TeaModel):
    def __init__(self, conditions_shrink=None, service_id=None):
        self.conditions_shrink = conditions_shrink  # type: str
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceDataShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateServiceDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: any
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateServiceDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceDataResponse, self).to_map()
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
            temp_model = UpdateServiceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


