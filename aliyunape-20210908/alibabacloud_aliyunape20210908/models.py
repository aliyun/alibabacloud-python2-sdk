# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApeInnerCommonApiRequest(TeaModel):
    def __init__(self, app_name=None, channel=None, end_time=None, lat=None, lon=None, page_num=None, page_size=None,
                 sp_code=None, start_time=None, station=None):
        # appName
        self.app_name = app_name  # type: str
        # channel
        self.channel = channel  # type: str
        # endTime
        self.end_time = end_time  # type: str
        # lat
        self.lat = lat  # type: str
        # lon
        self.lon = lon  # type: str
        # pageNum
        self.page_num = page_num  # type: int
        # pageSize
        self.page_size = page_size  # type: int
        # spCode
        self.sp_code = sp_code  # type: str
        # startTime
        self.start_time = start_time  # type: str
        # station
        self.station = station  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApeInnerCommonApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sp_code is not None:
            result['SpCode'] = self.sp_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpCode') is not None:
            self.sp_code = m.get('SpCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class ApeInnerCommonApiResponseBody(TeaModel):
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
        _map = super(ApeInnerCommonApiResponseBody, self).to_map()
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


class ApeInnerCommonApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApeInnerCommonApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApeInnerCommonApiResponse, self).to_map()
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
            temp_model = ApeInnerCommonApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApeProvinceStationRefRequest(TeaModel):
    def __init__(self, adcode=None, app_name=None, city=None, cnty=None, country=None, offset=None, page_size=None,
                 province_code=None, province_name=None, station_name=None):
        # adcode
        self.adcode = adcode  # type: long
        # appName
        self.app_name = app_name  # type: str
        # city
        self.city = city  # type: str
        # cnty
        self.cnty = cnty  # type: str
        # country
        self.country = country  # type: str
        # offset
        self.offset = offset  # type: int
        # pageSize
        self.page_size = page_size  # type: int
        # provinceCode
        self.province_code = province_code  # type: long
        # provinceName
        self.province_name = province_name  # type: str
        # stationName
        self.station_name = station_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApeProvinceStationRefRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adcode is not None:
            result['Adcode'] = self.adcode
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.city is not None:
            result['City'] = self.city
        if self.cnty is not None:
            result['Cnty'] = self.cnty
        if self.country is not None:
            result['Country'] = self.country
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.province_code is not None:
            result['ProvinceCode'] = self.province_code
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.station_name is not None:
            result['StationName'] = self.station_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adcode') is not None:
            self.adcode = m.get('Adcode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Cnty') is not None:
            self.cnty = m.get('Cnty')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProvinceCode') is not None:
            self.province_code = m.get('ProvinceCode')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('StationName') is not None:
            self.station_name = m.get('StationName')
        return self


class ApeProvinceStationRefResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, rt=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: any
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
        _map = super(ApeProvinceStationRefResponseBody, self).to_map()
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


class ApeProvinceStationRefResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApeProvinceStationRefResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApeProvinceStationRefResponse, self).to_map()
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
            temp_model = ApeProvinceStationRefResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HistoricalRequest(TeaModel):
    def __init__(self, end_time=None, order_id=None, page_num=None, page_size=None, start_time=None, station=None):
        # endTime
        self.end_time = end_time  # type: str
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # pageNum
        self.page_num = page_num  # type: int
        # pageSize
        self.page_size = page_size  # type: int
        # startTime
        self.start_time = start_time  # type: str
        # 全国（入参单一站点）
        self.station = station  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HistoricalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class HistoricalResponseBody(TeaModel):
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
        _map = super(HistoricalResponseBody, self).to_map()
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


class StationDayRequest(TeaModel):
    def __init__(self, order_id=None, start_forecast=None, station=None):
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
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
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.start_forecast is not None:
            result['StartForecast'] = self.start_forecast
        if self.station is not None:
            result['Station'] = self.station
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('StartForecast') is not None:
            self.start_forecast = m.get('StartForecast')
        if m.get('Station') is not None:
            self.station = m.get('Station')
        return self


class StationDayResponseBody(TeaModel):
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
        _map = super(StationDayResponseBody, self).to_map()
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
    def __init__(self, lat=None, lon=None, order_id=None, start_forecast=None):
        # 纬度，范围为（15°N~59.95°N）
        self.lat = lat  # type: str
        # 经度，范围为（70°E~139.96°E）
        self.lon = lon  # type: str
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # yyyymmdd080000或yyyymmdd200000
        self.start_forecast = start_forecast  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeatherforecastRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.start_forecast is not None:
            result['StartForecast'] = self.start_forecast
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('StartForecast') is not None:
            self.start_forecast = m.get('StartForecast')
        return self


class WeatherforecastResponseBody(TeaModel):
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
        _map = super(WeatherforecastResponseBody, self).to_map()
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


class WeatherforecastTimeRequest(TeaModel):
    def __init__(self, cur_hour=None, lat=None, lon=None, order_id=None):
        # 20210809090000
        self.cur_hour = cur_hour  # type: str
        # 纬度，范围为（15°N~59.95°N
        self.lat = lat  # type: str
        # 经度，范围为（70°E~139.96°E）
        self.lon = lon  # type: str
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeatherforecastTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_hour is not None:
            result['CurHour'] = self.cur_hour
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lon is not None:
            result['Lon'] = self.lon
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurHour') is not None:
            self.cur_hour = m.get('CurHour')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lon') is not None:
            self.lon = m.get('Lon')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class WeatherforecastTimeResponseBody(TeaModel):
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
        _map = super(WeatherforecastTimeResponseBody, self).to_map()
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


class WeathermonitorRequest(TeaModel):
    def __init__(self, cur_hour=None, order_id=None, page_num=None, page_size=None):
        # 气象实况时间 yyyymmddhh0000 （数据最小时间2021-08-16）（小时）	20210817120000
        self.cur_hour = cur_hour  # type: str
        # 用户中心--我的订单--订单请求--实例名称：aliyunape_meteor12_public_cn-0ju2d2hh90b
        self.order_id = order_id  # type: str
        # 页码
        self.page_num = page_num  # type: int
        # 页面条数
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(WeathermonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_hour is not None:
            result['CurHour'] = self.cur_hour
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurHour') is not None:
            self.cur_hour = m.get('CurHour')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class WeathermonitorResponseBody(TeaModel):
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
        _map = super(WeathermonitorResponseBody, self).to_map()
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


