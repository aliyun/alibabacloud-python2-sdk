# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetH5PageTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, end_date=None, start_date=None, time_unit=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetH5PageTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self


class GetH5PageTrendResponseBodyData(TeaModel):
    def __init__(self, analyze_dom=None, app_cache=None, content_trans=None, dns=None, dom_ready=None, fcp=None,
                 first_byte=None, five_second_rate=None, fp=None, load_event=None, load_finish=None, load_resource=None,
                 log_cnt=None, one_second_rate=None, redirect=None, ssl=None, tcp=None, time_point=None, ttfb=None, tti=None,
                 two_second_rate=None, unload=None):
        self.analyze_dom = analyze_dom  # type: float
        self.app_cache = app_cache  # type: float
        self.content_trans = content_trans  # type: float
        self.dns = dns  # type: float
        self.dom_ready = dom_ready  # type: float
        self.fcp = fcp  # type: float
        self.first_byte = first_byte  # type: float
        self.five_second_rate = five_second_rate  # type: float
        self.fp = fp  # type: float
        self.load_event = load_event  # type: float
        self.load_finish = load_finish  # type: float
        self.load_resource = load_resource  # type: float
        self.log_cnt = log_cnt  # type: long
        self.one_second_rate = one_second_rate  # type: float
        self.redirect = redirect  # type: float
        self.ssl = ssl  # type: float
        self.tcp = tcp  # type: float
        self.time_point = time_point  # type: str
        self.ttfb = ttfb  # type: float
        self.tti = tti  # type: float
        self.two_second_rate = two_second_rate  # type: float
        self.unload = unload  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetH5PageTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyze_dom is not None:
            result['analyzeDOM'] = self.analyze_dom
        if self.app_cache is not None:
            result['appCache'] = self.app_cache
        if self.content_trans is not None:
            result['contentTrans'] = self.content_trans
        if self.dns is not None:
            result['dns'] = self.dns
        if self.dom_ready is not None:
            result['domReady'] = self.dom_ready
        if self.fcp is not None:
            result['fcp'] = self.fcp
        if self.first_byte is not None:
            result['firstByte'] = self.first_byte
        if self.five_second_rate is not None:
            result['fiveSecondRate'] = self.five_second_rate
        if self.fp is not None:
            result['fp'] = self.fp
        if self.load_event is not None:
            result['loadEvent'] = self.load_event
        if self.load_finish is not None:
            result['loadFinish'] = self.load_finish
        if self.load_resource is not None:
            result['loadResource'] = self.load_resource
        if self.log_cnt is not None:
            result['logCnt'] = self.log_cnt
        if self.one_second_rate is not None:
            result['oneSecondRate'] = self.one_second_rate
        if self.redirect is not None:
            result['redirect'] = self.redirect
        if self.ssl is not None:
            result['ssl'] = self.ssl
        if self.tcp is not None:
            result['tcp'] = self.tcp
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        if self.ttfb is not None:
            result['ttfb'] = self.ttfb
        if self.tti is not None:
            result['tti'] = self.tti
        if self.two_second_rate is not None:
            result['twoSecondRate'] = self.two_second_rate
        if self.unload is not None:
            result['unload'] = self.unload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyzeDOM') is not None:
            self.analyze_dom = m.get('analyzeDOM')
        if m.get('appCache') is not None:
            self.app_cache = m.get('appCache')
        if m.get('contentTrans') is not None:
            self.content_trans = m.get('contentTrans')
        if m.get('dns') is not None:
            self.dns = m.get('dns')
        if m.get('domReady') is not None:
            self.dom_ready = m.get('domReady')
        if m.get('fcp') is not None:
            self.fcp = m.get('fcp')
        if m.get('firstByte') is not None:
            self.first_byte = m.get('firstByte')
        if m.get('fiveSecondRate') is not None:
            self.five_second_rate = m.get('fiveSecondRate')
        if m.get('fp') is not None:
            self.fp = m.get('fp')
        if m.get('loadEvent') is not None:
            self.load_event = m.get('loadEvent')
        if m.get('loadFinish') is not None:
            self.load_finish = m.get('loadFinish')
        if m.get('loadResource') is not None:
            self.load_resource = m.get('loadResource')
        if m.get('logCnt') is not None:
            self.log_cnt = m.get('logCnt')
        if m.get('oneSecondRate') is not None:
            self.one_second_rate = m.get('oneSecondRate')
        if m.get('redirect') is not None:
            self.redirect = m.get('redirect')
        if m.get('ssl') is not None:
            self.ssl = m.get('ssl')
        if m.get('tcp') is not None:
            self.tcp = m.get('tcp')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        if m.get('ttfb') is not None:
            self.ttfb = m.get('ttfb')
        if m.get('tti') is not None:
            self.tti = m.get('tti')
        if m.get('twoSecondRate') is not None:
            self.two_second_rate = m.get('twoSecondRate')
        if m.get('unload') is not None:
            self.unload = m.get('unload')
        return self


class GetH5PageTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetH5PageTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetH5PageTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetH5PageTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetH5PageTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetH5PageTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetH5PageTrendResponse, self).to_map()
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
            temp_model = GetH5PageTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLaunchTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, end_date=None, start_date=None, time_unit=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLaunchTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self


class GetLaunchTrendResponseBodyData(TeaModel):
    def __init__(self, cold_launch_count=None, cold_launch_duration=None, first_launch_count=None,
                 first_launch_duration=None, hot_launch_count=None, hot_launch_duration=None, time_point=None):
        self.cold_launch_count = cold_launch_count  # type: long
        self.cold_launch_duration = cold_launch_duration  # type: float
        self.first_launch_count = first_launch_count  # type: long
        self.first_launch_duration = first_launch_duration  # type: float
        self.hot_launch_count = hot_launch_count  # type: long
        self.hot_launch_duration = hot_launch_duration  # type: float
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLaunchTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cold_launch_count is not None:
            result['coldLaunchCount'] = self.cold_launch_count
        if self.cold_launch_duration is not None:
            result['coldLaunchDuration'] = self.cold_launch_duration
        if self.first_launch_count is not None:
            result['firstLaunchCount'] = self.first_launch_count
        if self.first_launch_duration is not None:
            result['firstLaunchDuration'] = self.first_launch_duration
        if self.hot_launch_count is not None:
            result['hotLaunchCount'] = self.hot_launch_count
        if self.hot_launch_duration is not None:
            result['hotLaunchDuration'] = self.hot_launch_duration
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('coldLaunchCount') is not None:
            self.cold_launch_count = m.get('coldLaunchCount')
        if m.get('coldLaunchDuration') is not None:
            self.cold_launch_duration = m.get('coldLaunchDuration')
        if m.get('firstLaunchCount') is not None:
            self.first_launch_count = m.get('firstLaunchCount')
        if m.get('firstLaunchDuration') is not None:
            self.first_launch_duration = m.get('firstLaunchDuration')
        if m.get('hotLaunchCount') is not None:
            self.hot_launch_count = m.get('hotLaunchCount')
        if m.get('hotLaunchDuration') is not None:
            self.hot_launch_duration = m.get('hotLaunchDuration')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetLaunchTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetLaunchTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLaunchTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetLaunchTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetLaunchTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLaunchTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLaunchTrendResponse, self).to_map()
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
            temp_model = GetLaunchTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNativePageTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, end_date=None, start_date=None, time_unit=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNativePageTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self


class GetNativePageTrendResponseBodyData(TeaModel):
    def __init__(self, avg_load_duration=None, crash_rate=None, load_cnt=None, slow_load_rate=None, time_point=None):
        self.avg_load_duration = avg_load_duration  # type: float
        self.crash_rate = crash_rate  # type: float
        self.load_cnt = load_cnt  # type: long
        self.slow_load_rate = slow_load_rate  # type: float
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNativePageTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_load_duration is not None:
            result['avgLoadDuration'] = self.avg_load_duration
        if self.crash_rate is not None:
            result['crashRate'] = self.crash_rate
        if self.load_cnt is not None:
            result['loadCnt'] = self.load_cnt
        if self.slow_load_rate is not None:
            result['slowLoadRate'] = self.slow_load_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avgLoadDuration') is not None:
            self.avg_load_duration = m.get('avgLoadDuration')
        if m.get('crashRate') is not None:
            self.crash_rate = m.get('crashRate')
        if m.get('loadCnt') is not None:
            self.load_cnt = m.get('loadCnt')
        if m.get('slowLoadRate') is not None:
            self.slow_load_rate = m.get('slowLoadRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetNativePageTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetNativePageTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetNativePageTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetNativePageTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetNativePageTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNativePageTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNativePageTrendResponse, self).to_map()
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
            temp_model = GetNativePageTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetworkTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, end_date=None, start_date=None, time_unit=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetworkTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self


class GetNetworkTrendResponseBodyData(TeaModel):
    def __init__(self, avg_cost=None, avg_response_time=None, avg_transform_bytes=None, request_per_minute=None,
                 time_point=None):
        self.avg_cost = avg_cost  # type: float
        self.avg_response_time = avg_response_time  # type: float
        self.avg_transform_bytes = avg_transform_bytes  # type: float
        self.request_per_minute = request_per_minute  # type: float
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetworkTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_cost is not None:
            result['avgCost'] = self.avg_cost
        if self.avg_response_time is not None:
            result['avgResponseTime'] = self.avg_response_time
        if self.avg_transform_bytes is not None:
            result['avgTransformBytes'] = self.avg_transform_bytes
        if self.request_per_minute is not None:
            result['requestPerMinute'] = self.request_per_minute
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avgCost') is not None:
            self.avg_cost = m.get('avgCost')
        if m.get('avgResponseTime') is not None:
            self.avg_response_time = m.get('avgResponseTime')
        if m.get('avgTransformBytes') is not None:
            self.avg_transform_bytes = m.get('avgTransformBytes')
        if m.get('requestPerMinute') is not None:
            self.request_per_minute = m.get('requestPerMinute')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetNetworkTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetNetworkTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetNetworkTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetNetworkTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetNetworkTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNetworkTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNetworkTrendResponse, self).to_map()
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
            temp_model = GetNetworkTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, end_date=None, start_date=None, type=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStatTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetStatTrendResponseBodyData(TeaModel):
    def __init__(self, affected_user_count=None, affected_user_rate=None, error_count=None, error_rate=None,
                 time_point=None):
        self.affected_user_count = affected_user_count  # type: long
        self.affected_user_rate = affected_user_rate  # type: float
        self.error_count = error_count  # type: long
        self.error_rate = error_rate  # type: float
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStatTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['affectedUserCount'] = self.affected_user_count
        if self.affected_user_rate is not None:
            result['affectedUserRate'] = self.affected_user_rate
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('affectedUserCount') is not None:
            self.affected_user_count = m.get('affectedUserCount')
        if m.get('affectedUserRate') is not None:
            self.affected_user_rate = m.get('affectedUserRate')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetStatTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetStatTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetStatTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetStatTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetStatTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStatTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStatTrendResponse, self).to_map()
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
            temp_model = GetStatTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSymUploadParamRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, file_name=None, file_type=None, flutter_name=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.flutter_name = flutter_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSymUploadParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.flutter_name is not None:
            result['flutterName'] = self.flutter_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('flutterName') is not None:
            self.flutter_name = m.get('flutterName')
        return self


class GetSymUploadParamResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, callback=None, key=None, policy=None, signature=None, upload_address=None):
        self.access_key_id = access_key_id  # type: str
        self.callback = callback  # type: str
        self.key = key  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str
        self.upload_address = upload_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSymUploadParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.callback is not None:
            result['callback'] = self.callback
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.upload_address is not None:
            result['uploadAddress'] = self.upload_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('callback') is not None:
            self.callback = m.get('callback')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('uploadAddress') is not None:
            self.upload_address = m.get('uploadAddress')
        return self


class GetSymUploadParamResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None, trace_id=None):
        self.code = code  # type: long
        # data
        self.data = data  # type: GetSymUploadParamResponseBodyData
        self.msg = msg  # type: str
        self.success = success  # type: bool
        # traceId
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSymUploadParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetSymUploadParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetSymUploadParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSymUploadParamResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSymUploadParamResponse, self).to_map()
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
            temp_model = GetSymUploadParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTodayStatTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, type=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTodayStatTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTodayStatTrendResponseBodyData(TeaModel):
    def __init__(self, affected_user_count=None, affected_user_rate=None, error_count=None, error_rate=None,
                 time_point=None):
        self.affected_user_count = affected_user_count  # type: long
        self.affected_user_rate = affected_user_rate  # type: float
        self.error_count = error_count  # type: long
        self.error_rate = error_rate  # type: float
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTodayStatTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['affectedUserCount'] = self.affected_user_count
        if self.affected_user_rate is not None:
            result['affectedUserRate'] = self.affected_user_rate
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('affectedUserCount') is not None:
            self.affected_user_count = m.get('affectedUserCount')
        if m.get('affectedUserRate') is not None:
            self.affected_user_rate = m.get('affectedUserRate')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetTodayStatTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetTodayStatTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTodayStatTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetTodayStatTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTodayStatTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTodayStatTrendResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTodayStatTrendResponse, self).to_map()
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
            temp_model = GetTodayStatTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertPlanRequest(TeaModel):
    def __init__(self, data_source_id=None, plan_id=None, versions=None):
        self.data_source_id = data_source_id  # type: str
        self.plan_id = plan_id  # type: long
        self.versions = versions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.versions is not None:
            result['versions'] = self.versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        return self


class UpdateAlertPlanResponseBody(TeaModel):
    def __init__(self, code=None, msg=None, success=None):
        self.code = code  # type: long
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAlertPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateAlertPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAlertPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAlertPlanResponse, self).to_map()
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
            temp_model = UpdateAlertPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadSymbolFileRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, file_name=None, file_type=None, flutter_name=None,
                 oss_url=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.flutter_name = flutter_name  # type: str
        self.oss_url = oss_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadSymbolFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.flutter_name is not None:
            result['flutterName'] = self.flutter_name
        if self.oss_url is not None:
            result['ossUrl'] = self.oss_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('flutterName') is not None:
            self.flutter_name = m.get('flutterName')
        if m.get('ossUrl') is not None:
            self.oss_url = m.get('ossUrl')
        return self


class UploadSymbolFileAdvanceRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, file_name=None, file_type=None, flutter_name=None,
                 oss_url_object=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.flutter_name = flutter_name  # type: str
        self.oss_url_object = oss_url_object  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadSymbolFileAdvanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.flutter_name is not None:
            result['flutterName'] = self.flutter_name
        if self.oss_url_object is not None:
            result['ossUrl'] = self.oss_url_object
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('flutterName') is not None:
            self.flutter_name = m.get('flutterName')
        if m.get('ossUrl') is not None:
            self.oss_url_object = m.get('ossUrl')
        return self


class UploadSymbolFileResponseBody(TeaModel):
    def __init__(self, code=None, msg=None, request_id=None, success=None, trace_id=None):
        # code
        self.code = code  # type: long
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        # traceId
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadSymbolFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class UploadSymbolFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadSymbolFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadSymbolFileResponse, self).to_map()
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
            temp_model = UploadSymbolFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


