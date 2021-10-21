# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ExecuteRequest(TeaModel):
    def __init__(self, user_id=None, service_param=None, extend_param=None, order_id=None, app_name=None,
                 request_id=None, channel=None):
        # aliyunPk
        self.user_id = user_id  # type: long
        # serviceParam
        self.service_param = service_param  # type: dict[str, str]
        # extendParam
        self.extend_param = extend_param  # type: dict[str, str]
        # orderId
        self.order_id = order_id  # type: str
        # appName
        self.app_name = app_name  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # source
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service_param is not None:
            result['ServiceParam'] = self.service_param
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ServiceParam') is not None:
            self.service_param = m.get('ServiceParam')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class ExecuteShrinkRequest(TeaModel):
    def __init__(self, user_id=None, service_param_shrink=None, extend_param_shrink=None, order_id=None,
                 app_name=None, request_id=None, channel=None):
        # aliyunPk
        self.user_id = user_id  # type: long
        # serviceParam
        self.service_param_shrink = service_param_shrink  # type: str
        # extendParam
        self.extend_param_shrink = extend_param_shrink  # type: str
        # orderId
        self.order_id = order_id  # type: str
        # appName
        self.app_name = app_name  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # source
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service_param_shrink is not None:
            result['ServiceParam'] = self.service_param_shrink
        if self.extend_param_shrink is not None:
            result['ExtendParam'] = self.extend_param_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ServiceParam') is not None:
            self.service_param_shrink = m.get('ServiceParam')
        if m.get('ExtendParam') is not None:
            self.extend_param_shrink = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class ExecuteResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
    def __init__(self, user_id=None, service_param=None, extend_param=None, order_id=None, app_name=None,
                 request_id=None, channel=None):
        # UserId
        self.user_id = user_id  # type: long
        # 请求参数
        self.service_param = service_param  # type: dict[str, str]
        # 扩展参数
        self.extend_param = extend_param  # type: dict[str, str]
        # orderId
        self.order_id = order_id  # type: str
        # appName
        self.app_name = app_name  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 渠道名称
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorProvinceHourRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service_param is not None:
            result['ServiceParam'] = self.service_param
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ServiceParam') is not None:
            self.service_param = m.get('ServiceParam')
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class WeathermonitorProvinceHourShrinkRequest(TeaModel):
    def __init__(self, user_id=None, service_param_shrink=None, extend_param_shrink=None, order_id=None,
                 app_name=None, request_id=None, channel=None):
        # UserId
        self.user_id = user_id  # type: long
        # 请求参数
        self.service_param_shrink = service_param_shrink  # type: str
        # 扩展参数
        self.extend_param_shrink = extend_param_shrink  # type: str
        # orderId
        self.order_id = order_id  # type: str
        # appName
        self.app_name = app_name  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 渠道名称
        self.channel = channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorProvinceHourShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service_param_shrink is not None:
            result['ServiceParam'] = self.service_param_shrink
        if self.extend_param_shrink is not None:
            result['ExtendParam'] = self.extend_param_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ServiceParam') is not None:
            self.service_param_shrink = m.get('ServiceParam')
        if m.get('ExtendParam') is not None:
            self.extend_param_shrink = m.get('ExtendParam')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class WeathermonitorProvinceHourResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorProvinceHourResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class WeathermonitorRequest(TeaModel):
    def __init__(self, user_id=None, order_id=None, request_id=None, page_size=None, cur_hour=None, page_num=None):
        # UserId
        self.user_id = user_id  # type: long
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 页面条数
        self.page_size = page_size  # type: int
        # 气象实况时间 yyyymmddhh0000 （数据最小时间2021-08-16）（小时）	20210817120000
        self.cur_hour = cur_hour  # type: str
        # 页码
        self.page_num = page_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cur_hour is not None:
            result['CurHour'] = self.cur_hour
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurHour') is not None:
            self.cur_hour = m.get('CurHour')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class WeathermonitorResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WeathermonitorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WeathermonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WeathermonitorResponse, self).to_map()
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
            temp_model = WeathermonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WeatherforecastTimeRequest(TeaModel):
    def __init__(self, user_id=None, order_id=None, request_id=None, lon=None, cur_hour=None, lat=None):
        # UserId
        self.user_id = user_id  # type: long
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 经度，范围为（70°E~139.96°E）
        self.lon = lon  # type: str
        # yyyymmddhh0000
        self.cur_hour = cur_hour  # type: str
        # 纬度，范围为（15°N~59.95°N）
        self.lat = lat  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeatherforecastTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.cur_hour is not None:
            result['CurHour'] = self.cur_hour
        if self.lat is not None:
            result['Lat'] = self.lat
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('CurHour') is not None:
            self.cur_hour = m.get('CurHour')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        return self


class WeatherforecastTimeResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeatherforecastTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WeatherforecastTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WeatherforecastTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WeatherforecastTimeResponse, self).to_map()
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
            temp_model = WeatherforecastTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StationDayRequest(TeaModel):
    def __init__(self, user_id=None, order_id=None, request_id=None, start_forecast=None, station=None):
        # UserId
        self.user_id = user_id  # type: long
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # 气象预测开始时间
        self.start_forecast = start_forecast  # type: str
        # 全国站点（入参单一站点）
        self.station = station  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StationDayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_forecast is not None:
            result['StartForecast'] = self.start_forecast
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartForecast') is not None:
            self.start_forecast = m.get('StartForecast')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class StationDayResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StationDayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StationDayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StationDayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StationDayResponse, self).to_map()
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
            temp_model = StationDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WeatherforecastRequest(TeaModel):
    def __init__(self, user_id=None, order_id=None, request_id=None, start_forecast=None, lon=None, lat=None):
        # UserId
        self.user_id = user_id  # type: long
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # yyyymmdd080000或yyyymmdd200000
        self.start_forecast = start_forecast  # type: str
        # 经度，范围为（70°E~139.96°E）
        self.lon = lon  # type: str
        # 纬度，范围为（15°N~59.95°N）
        self.lat = lat  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeatherforecastRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_forecast is not None:
            result['StartForecast'] = self.start_forecast
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.lat is not None:
            result['Lat'] = self.lat
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartForecast') is not None:
            self.start_forecast = m.get('StartForecast')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        return self


class WeatherforecastResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeatherforecastResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WeatherforecastResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: WeatherforecastResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(WeatherforecastResponse, self).to_map()
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
            temp_model = WeatherforecastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HistoricalRequest(TeaModel):
    def __init__(self, user_id=None, order_id=None, request_id=None, station=None, page_size=None, start_time=None,
                 end_time=None, page_num=None):
        # UserId
        self.user_id = user_id  # type: long
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # station全国（入参单一站点）
        self.station = station  # type: str
        # pageSize是	页面条数
        self.page_size = page_size  # type: int
        # startTimeyyyymmddhh0000（当startTime为空时无数据产出，确认是否入参）
        self.start_time = start_time  # type: int
        # endTimeyyyymmddhh0000 （当endTime为空时无数据产出，确认是否入参）
        self.end_time = end_time  # type: int
        # pageNum页码数
        self.page_num = page_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(HistoricalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.station is not None:
            result['Station'] = self.station
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class HistoricalResponseBody(TeaModel):
    def __init__(self, rt=None, message=None, request_id=None, data=None, code=None, success=None):
        # rt
        self.rt = rt  # type: long
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: list[dict[str, any]]
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HistoricalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HistoricalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HistoricalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HistoricalResponse, self).to_map()
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
            temp_model = HistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


