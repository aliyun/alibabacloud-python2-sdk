# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ExecuteRequest(TeaModel):
    def __init__(self, app_name=None, channel=None, extend_param=None, order_id=None, request_id=None,
                 service_param=None, user_id=None):
        # appName
        self.app_name = app_name  # type: str
        # source
        self.channel = channel  # type: str
        # extendParam
        self.extend_param = extend_param  # type: dict[str, str]
        # orderId
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # serviceParam
        self.service_param = service_param  # type: dict[str, str]
        # aliyunPk
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_param is not None:
            result['ServiceParam'] = self.service_param
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceParam') is not None:
            self.service_param = m.get('ServiceParam')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ExecuteShrinkRequest(TeaModel):
    def __init__(self, app_name=None, channel=None, extend_param_shrink=None, order_id=None, request_id=None,
                 service_param_shrink=None, user_id=None):
        # appName
        self.app_name = app_name  # type: str
        # source
        self.channel = channel  # type: str
        # extendParam
        self.extend_param_shrink = extend_param_shrink  # type: str
        # orderId
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # serviceParam
        self.service_param_shrink = service_param_shrink  # type: str
        # aliyunPk
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.extend_param_shrink is not None:
            result['ExtendParam'] = self.extend_param_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_param_shrink is not None:
            result['ServiceParam'] = self.service_param_shrink
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtendParam') is not None:
            self.extend_param_shrink = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceParam') is not None:
            self.service_param_shrink = m.get('ServiceParam')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ExecuteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # rt
        self.rt = rt  # type: long
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteResponseBody, self).to_map()
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


class ExecuteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteResponse, self).to_map()
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
            temp_model = ExecuteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WeathermonitorProvinceHourRequest(TeaModel):
    def __init__(self, app_name=None, channel=None, extend_param=None, order_id=None, request_id=None,
                 service_param=None, user_id=None):
        # appName
        self.app_name = app_name  # type: str
        # 渠道名称
        self.channel = channel  # type: str
        # 扩展参数
        self.extend_param = extend_param  # type: dict[str, str]
        # orderId
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 请求参数
        self.service_param = service_param  # type: dict[str, str]
        # UserId
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorProvinceHourRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_param is not None:
            result['ServiceParam'] = self.service_param
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceParam') is not None:
            self.service_param = m.get('ServiceParam')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class WeathermonitorProvinceHourShrinkRequest(TeaModel):
    def __init__(self, app_name=None, channel=None, extend_param_shrink=None, order_id=None, request_id=None,
                 service_param_shrink=None, user_id=None):
        # appName
        self.app_name = app_name  # type: str
        # 渠道名称
        self.channel = channel  # type: str
        # 扩展参数
        self.extend_param_shrink = extend_param_shrink  # type: str
        # orderId
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 请求参数
        self.service_param_shrink = service_param_shrink  # type: str
        # UserId
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorProvinceHourShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.extend_param_shrink is not None:
            result['ExtendParam'] = self.extend_param_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_param_shrink is not None:
            result['ServiceParam'] = self.service_param_shrink
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtendParam') is not None:
            self.extend_param_shrink = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceParam') is not None:
            self.service_param_shrink = m.get('ServiceParam')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class WeathermonitorProvinceHourResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # rt
        self.rt = rt  # type: long
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorProvinceHourResponseBody, self).to_map()
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


class WeathermonitorProvinceHourResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WeathermonitorProvinceHourResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WeathermonitorProvinceHourResponse, self).to_map()
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
            temp_model = WeathermonitorProvinceHourResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


