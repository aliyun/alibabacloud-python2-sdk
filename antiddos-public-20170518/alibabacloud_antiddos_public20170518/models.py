# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeBgpPackByIpRequest(TeaModel):
    def __init__(self, ddos_region_id=None, ip=None):
        self.ddos_region_id = ddos_region_id  # type: str
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBgpPackByIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBgpPackByIpResponseBodyDdosbgpInfo(TeaModel):
    def __init__(self, base_threshold=None, ddosbgp_instance_id=None, elastic_threshold=None, expire_time=None,
                 ip=None):
        self.base_threshold = base_threshold  # type: int
        self.ddosbgp_instance_id = ddosbgp_instance_id  # type: str
        self.elastic_threshold = elastic_threshold  # type: int
        self.expire_time = expire_time  # type: long
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBgpPackByIpResponseBodyDdosbgpInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_threshold is not None:
            result['BaseThreshold'] = self.base_threshold
        if self.ddosbgp_instance_id is not None:
            result['DdosbgpInstanceId'] = self.ddosbgp_instance_id
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseThreshold') is not None:
            self.base_threshold = m.get('BaseThreshold')
        if m.get('DdosbgpInstanceId') is not None:
            self.ddosbgp_instance_id = m.get('DdosbgpInstanceId')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBgpPackByIpResponseBody(TeaModel):
    def __init__(self, code=None, ddosbgp_info=None, request_id=None, success=None):
        self.code = code  # type: int
        self.ddosbgp_info = ddosbgp_info  # type: DescribeBgpPackByIpResponseBodyDdosbgpInfo
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.ddosbgp_info:
            self.ddosbgp_info.validate()

    def to_map(self):
        _map = super(DescribeBgpPackByIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ddosbgp_info is not None:
            result['DdosbgpInfo'] = self.ddosbgp_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DdosbgpInfo') is not None:
            temp_model = DescribeBgpPackByIpResponseBodyDdosbgpInfo()
            self.ddosbgp_info = temp_model.from_map(m['DdosbgpInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBgpPackByIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBgpPackByIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBgpPackByIpResponse, self).to_map()
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
            temp_model = DescribeBgpPackByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCapRequest(TeaModel):
    def __init__(self, beg_time=None, ddos_region_id=None, instance_id=None, instance_type=None, internet_ip=None):
        self.beg_time = beg_time  # type: long
        self.ddos_region_id = ddos_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_ip = internet_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beg_time is not None:
            result['BegTime'] = self.beg_time
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BegTime') is not None:
            self.beg_time = m.get('BegTime')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class DescribeCapResponseBodyCapUrl(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCapResponseBodyCapUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeCapResponseBody(TeaModel):
    def __init__(self, cap_url=None, request_id=None):
        self.cap_url = cap_url  # type: DescribeCapResponseBodyCapUrl
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cap_url:
            self.cap_url.validate()

    def to_map(self):
        _map = super(DescribeCapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cap_url is not None:
            result['CapUrl'] = self.cap_url.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CapUrl') is not None:
            temp_model = DescribeCapResponseBodyCapUrl()
            self.cap_url = temp_model.from_map(m['CapUrl'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCapResponse, self).to_map()
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
            temp_model = DescribeCapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosCountRequest(TeaModel):
    def __init__(self, ddos_region_id=None, instance_type=None):
        self.ddos_region_id = ddos_region_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeDdosCountResponseBodyDdosCount(TeaModel):
    def __init__(self, blackhole_count=None, defense_count=None, instacen_count=None):
        self.blackhole_count = blackhole_count  # type: int
        self.defense_count = defense_count  # type: int
        self.instacen_count = instacen_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosCountResponseBodyDdosCount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_count is not None:
            result['BlackholeCount'] = self.blackhole_count
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.instacen_count is not None:
            result['InstacenCount'] = self.instacen_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackholeCount') is not None:
            self.blackhole_count = m.get('BlackholeCount')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('InstacenCount') is not None:
            self.instacen_count = m.get('InstacenCount')
        return self


class DescribeDdosCountResponseBody(TeaModel):
    def __init__(self, ddos_count=None, request_id=None):
        self.ddos_count = ddos_count  # type: DescribeDdosCountResponseBodyDdosCount
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ddos_count:
            self.ddos_count.validate()

    def to_map(self):
        _map = super(DescribeDdosCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_count is not None:
            result['DdosCount'] = self.ddos_count.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosCount') is not None:
            temp_model = DescribeDdosCountResponseBodyDdosCount()
            self.ddos_count = temp_model.from_map(m['DdosCount'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDdosCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDdosCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDdosCountResponse, self).to_map()
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
            temp_model = DescribeDdosCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosCreditRequest(TeaModel):
    def __init__(self, ddos_region_id=None):
        self.ddos_region_id = ddos_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosCreditRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        return self


class DescribeDdosCreditResponseBodyDdosCredit(TeaModel):
    def __init__(self, blackhole_time=None, score=None, score_level=None):
        self.blackhole_time = blackhole_time  # type: int
        self.score = score  # type: int
        self.score_level = score_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosCreditResponseBodyDdosCredit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_time is not None:
            result['BlackholeTime'] = self.blackhole_time
        if self.score is not None:
            result['Score'] = self.score
        if self.score_level is not None:
            result['ScoreLevel'] = self.score_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackholeTime') is not None:
            self.blackhole_time = m.get('BlackholeTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ScoreLevel') is not None:
            self.score_level = m.get('ScoreLevel')
        return self


class DescribeDdosCreditResponseBody(TeaModel):
    def __init__(self, ddos_credit=None, request_id=None, success=None):
        self.ddos_credit = ddos_credit  # type: DescribeDdosCreditResponseBodyDdosCredit
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.ddos_credit:
            self.ddos_credit.validate()

    def to_map(self):
        _map = super(DescribeDdosCreditResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_credit is not None:
            result['DdosCredit'] = self.ddos_credit.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosCredit') is not None:
            temp_model = DescribeDdosCreditResponseBodyDdosCredit()
            self.ddos_credit = temp_model.from_map(m['DdosCredit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDdosCreditResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDdosCreditResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDdosCreditResponse, self).to_map()
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
            temp_model = DescribeDdosCreditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosEventListRequest(TeaModel):
    def __init__(self, current_page=None, ddos_region_id=None, instance_id=None, instance_type=None,
                 internet_ip=None, page_size=None):
        self.current_page = current_page  # type: int
        self.ddos_region_id = ddos_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_ip = internet_ip  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosEventListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDdosEventListResponseBodyDdosEventListDdosEvent(TeaModel):
    def __init__(self, ddos_status=None, ddos_type=None, delay_time=None, end_time=None, start_time=None,
                 un_blackhole_time=None):
        self.ddos_status = ddos_status  # type: str
        self.ddos_type = ddos_type  # type: str
        self.delay_time = delay_time  # type: long
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.un_blackhole_time = un_blackhole_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosEventListResponseBodyDdosEventListDdosEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.un_blackhole_time is not None:
            result['UnBlackholeTime'] = self.un_blackhole_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UnBlackholeTime') is not None:
            self.un_blackhole_time = m.get('UnBlackholeTime')
        return self


class DescribeDdosEventListResponseBodyDdosEventList(TeaModel):
    def __init__(self, ddos_event=None):
        self.ddos_event = ddos_event  # type: list[DescribeDdosEventListResponseBodyDdosEventListDdosEvent]

    def validate(self):
        if self.ddos_event:
            for k in self.ddos_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDdosEventListResponseBodyDdosEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DdosEvent'] = []
        if self.ddos_event is not None:
            for k in self.ddos_event:
                result['DdosEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ddos_event = []
        if m.get('DdosEvent') is not None:
            for k in m.get('DdosEvent'):
                temp_model = DescribeDdosEventListResponseBodyDdosEventListDdosEvent()
                self.ddos_event.append(temp_model.from_map(k))
        return self


class DescribeDdosEventListResponseBody(TeaModel):
    def __init__(self, ddos_event_list=None, request_id=None, total=None):
        self.ddos_event_list = ddos_event_list  # type: DescribeDdosEventListResponseBodyDdosEventList
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.ddos_event_list:
            self.ddos_event_list.validate()

    def to_map(self):
        _map = super(DescribeDdosEventListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_event_list is not None:
            result['DdosEventList'] = self.ddos_event_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosEventList') is not None:
            temp_model = DescribeDdosEventListResponseBodyDdosEventList()
            self.ddos_event_list = temp_model.from_map(m['DdosEventList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosEventListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDdosEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDdosEventListResponse, self).to_map()
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
            temp_model = DescribeDdosEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosThresholdRequest(TeaModel):
    def __init__(self, ddos_region_id=None, ddos_type=None, instance_ids=None, instance_type=None):
        self.ddos_region_id = ddos_region_id  # type: str
        self.ddos_type = ddos_type  # type: str
        self.instance_ids = instance_ids  # type: list[str]
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosThresholdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeDdosThresholdResponseBodyThresholdsThreshold(TeaModel):
    def __init__(self, bps=None, ddos_type=None, elastic_bps=None, instance_id=None, internet_ip=None, is_auto=None,
                 max_bps=None, max_pps=None, pps=None):
        self.bps = bps  # type: int
        self.ddos_type = ddos_type  # type: str
        self.elastic_bps = elastic_bps  # type: int
        self.instance_id = instance_id  # type: str
        self.internet_ip = internet_ip  # type: str
        self.is_auto = is_auto  # type: bool
        self.max_bps = max_bps  # type: int
        self.max_pps = max_pps  # type: int
        self.pps = pps  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosThresholdResponseBodyThresholdsThreshold, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.elastic_bps is not None:
            result['ElasticBps'] = self.elastic_bps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_pps is not None:
            result['MaxPps'] = self.max_pps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('ElasticBps') is not None:
            self.elastic_bps = m.get('ElasticBps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxPps') is not None:
            self.max_pps = m.get('MaxPps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDdosThresholdResponseBodyThresholds(TeaModel):
    def __init__(self, threshold=None):
        self.threshold = threshold  # type: list[DescribeDdosThresholdResponseBodyThresholdsThreshold]

    def validate(self):
        if self.threshold:
            for k in self.threshold:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDdosThresholdResponseBodyThresholds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Threshold'] = []
        if self.threshold is not None:
            for k in self.threshold:
                result['Threshold'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.threshold = []
        if m.get('Threshold') is not None:
            for k in m.get('Threshold'):
                temp_model = DescribeDdosThresholdResponseBodyThresholdsThreshold()
                self.threshold.append(temp_model.from_map(k))
        return self


class DescribeDdosThresholdResponseBody(TeaModel):
    def __init__(self, request_id=None, thresholds=None):
        self.request_id = request_id  # type: str
        self.thresholds = thresholds  # type: DescribeDdosThresholdResponseBodyThresholds

    def validate(self):
        if self.thresholds:
            self.thresholds.validate()

    def to_map(self):
        _map = super(DescribeDdosThresholdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Thresholds') is not None:
            temp_model = DescribeDdosThresholdResponseBodyThresholds()
            self.thresholds = temp_model.from_map(m['Thresholds'])
        return self


class DescribeDdosThresholdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDdosThresholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDdosThresholdResponse, self).to_map()
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
            temp_model = DescribeDdosThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, current_page=None, ddos_region_id=None, ddos_status=None, instance_id=None, instance_ip=None,
                 instance_name=None, instance_type=None, page_size=None):
        self.current_page = current_page  # type: int
        self.ddos_region_id = ddos_region_id  # type: str
        self.ddos_status = ddos_status  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_ip = instance_ip  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceResponseBodyInstanceListInstance(TeaModel):
    def __init__(self, blackhole_threshold=None, defense_bps_threshold=None, defense_pps_threshold=None,
                 elastic_threshold=None, instance_id=None, instance_ip=None, instance_name=None, instance_status=None,
                 instance_type=None, ip_version=None, is_bgppack=None):
        self.blackhole_threshold = blackhole_threshold  # type: int
        self.defense_bps_threshold = defense_bps_threshold  # type: int
        self.defense_pps_threshold = defense_pps_threshold  # type: int
        self.elastic_threshold = elastic_threshold  # type: int
        self.instance_id = instance_id  # type: str
        self.instance_ip = instance_ip  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_status = instance_status  # type: str
        self.instance_type = instance_type  # type: str
        self.ip_version = ip_version  # type: str
        self.is_bgppack = is_bgppack  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceListInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_threshold is not None:
            result['BlackholeThreshold'] = self.blackhole_threshold
        if self.defense_bps_threshold is not None:
            result['DefenseBpsThreshold'] = self.defense_bps_threshold
        if self.defense_pps_threshold is not None:
            result['DefensePpsThreshold'] = self.defense_pps_threshold
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.is_bgppack is not None:
            result['IsBgppack'] = self.is_bgppack
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackholeThreshold') is not None:
            self.blackhole_threshold = m.get('BlackholeThreshold')
        if m.get('DefenseBpsThreshold') is not None:
            self.defense_bps_threshold = m.get('DefenseBpsThreshold')
        if m.get('DefensePpsThreshold') is not None:
            self.defense_pps_threshold = m.get('DefensePpsThreshold')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IsBgppack') is not None:
            self.is_bgppack = m.get('IsBgppack')
        return self


class DescribeInstanceResponseBodyInstanceList(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[DescribeInstanceResponseBodyInstanceListInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeInstanceResponseBodyInstanceListInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, instance_list=None, request_id=None, total=None):
        self.instance_list = instance_list  # type: DescribeInstanceResponseBodyInstanceList
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponse, self).to_map()
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIpAddressRequest(TeaModel):
    def __init__(self, current_page=None, ddos_region_id=None, ddos_status=None, instance_id=None, instance_ip=None,
                 instance_name=None, instance_type=None, page_size=None):
        self.current_page = current_page  # type: int
        self.ddos_region_id = ddos_region_id  # type: str
        self.ddos_status = ddos_status  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_ip = instance_ip  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceIpAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig(TeaModel):
    def __init__(self, blackhole_threshold=None, defense_bps_threshold=None, defense_pps_threshold=None,
                 elastic_threshold=None, instance_ip=None, ip_status=None, ip_version=None, is_bgppack=None, region_id=None):
        self.blackhole_threshold = blackhole_threshold  # type: int
        self.defense_bps_threshold = defense_bps_threshold  # type: int
        self.defense_pps_threshold = defense_pps_threshold  # type: int
        self.elastic_threshold = elastic_threshold  # type: int
        self.instance_ip = instance_ip  # type: str
        self.ip_status = ip_status  # type: str
        self.ip_version = ip_version  # type: str
        self.is_bgppack = is_bgppack  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_threshold is not None:
            result['BlackholeThreshold'] = self.blackhole_threshold
        if self.defense_bps_threshold is not None:
            result['DefenseBpsThreshold'] = self.defense_bps_threshold
        if self.defense_pps_threshold is not None:
            result['DefensePpsThreshold'] = self.defense_pps_threshold
        if self.elastic_threshold is not None:
            result['ElasticThreshold'] = self.elastic_threshold
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.ip_status is not None:
            result['IpStatus'] = self.ip_status
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.is_bgppack is not None:
            result['IsBgppack'] = self.is_bgppack
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackholeThreshold') is not None:
            self.blackhole_threshold = m.get('BlackholeThreshold')
        if m.get('DefenseBpsThreshold') is not None:
            self.defense_bps_threshold = m.get('DefenseBpsThreshold')
        if m.get('DefensePpsThreshold') is not None:
            self.defense_pps_threshold = m.get('DefensePpsThreshold')
        if m.get('ElasticThreshold') is not None:
            self.elastic_threshold = m.get('ElasticThreshold')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('IpStatus') is not None:
            self.ip_status = m.get('IpStatus')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IsBgppack') is not None:
            self.is_bgppack = m.get('IsBgppack')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceIpAddressResponseBodyInstanceList(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, instance_status=None, instance_type=None,
                 ip_address_config=None):
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_status = instance_status  # type: str
        self.instance_type = instance_type  # type: str
        self.ip_address_config = ip_address_config  # type: list[DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig]

    def validate(self):
        if self.ip_address_config:
            for k in self.ip_address_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceIpAddressResponseBodyInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        result['IpAddressConfig'] = []
        if self.ip_address_config is not None:
            for k in self.ip_address_config:
                result['IpAddressConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        self.ip_address_config = []
        if m.get('IpAddressConfig') is not None:
            for k in m.get('IpAddressConfig'):
                temp_model = DescribeInstanceIpAddressResponseBodyInstanceListIpAddressConfig()
                self.ip_address_config.append(temp_model.from_map(k))
        return self


class DescribeInstanceIpAddressResponseBody(TeaModel):
    def __init__(self, instance_list=None, request_id=None, total=None):
        self.instance_list = instance_list  # type: list[DescribeInstanceIpAddressResponseBodyInstanceList]
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceIpAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeInstanceIpAddressResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstanceIpAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceIpAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceIpAddressResponse, self).to_map()
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
            temp_model = DescribeInstanceIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpDdosThresholdRequest(TeaModel):
    def __init__(self, ddos_region_id=None, ddos_type=None, instance_id=None, instance_type=None, internet_ip=None):
        self.ddos_region_id = ddos_region_id  # type: str
        self.ddos_type = ddos_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_ip = internet_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpDdosThresholdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class DescribeIpDdosThresholdResponseBodyThreshold(TeaModel):
    def __init__(self, bps=None, ddos_type=None, elastic_bps=None, instance_id=None, internet_ip=None, is_auto=None,
                 max_bps=None, max_pps=None, pps=None):
        self.bps = bps  # type: int
        self.ddos_type = ddos_type  # type: str
        self.elastic_bps = elastic_bps  # type: int
        self.instance_id = instance_id  # type: str
        self.internet_ip = internet_ip  # type: str
        self.is_auto = is_auto  # type: bool
        self.max_bps = max_bps  # type: int
        self.max_pps = max_pps  # type: int
        self.pps = pps  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpDdosThresholdResponseBodyThreshold, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type
        if self.elastic_bps is not None:
            result['ElasticBps'] = self.elastic_bps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_pps is not None:
            result['MaxPps'] = self.max_pps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')
        if m.get('ElasticBps') is not None:
            self.elastic_bps = m.get('ElasticBps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxPps') is not None:
            self.max_pps = m.get('MaxPps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeIpDdosThresholdResponseBody(TeaModel):
    def __init__(self, request_id=None, threshold=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.threshold = threshold  # type: DescribeIpDdosThresholdResponseBodyThreshold

    def validate(self):
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        _map = super(DescribeIpDdosThresholdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.threshold is not None:
            result['Threshold'] = self.threshold.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Threshold') is not None:
            temp_model = DescribeIpDdosThresholdResponseBodyThreshold()
            self.threshold = temp_model.from_map(m['Threshold'])
        return self


class DescribeIpDdosThresholdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpDdosThresholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpDdosThresholdResponse, self).to_map()
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
            temp_model = DescribeIpDdosThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpLocationServiceRequest(TeaModel):
    def __init__(self, internet_ip=None):
        self.internet_ip = internet_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpLocationServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class DescribeIpLocationServiceResponseBodyInstance(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, instance_type=None, internet_ip=None, region=None):
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_ip = internet_ip  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpLocationServiceResponseBodyInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeIpLocationServiceResponseBody(TeaModel):
    def __init__(self, instance=None, request_id=None):
        # instance model
        self.instance = instance  # type: DescribeIpLocationServiceResponseBodyInstance
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(DescribeIpLocationServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DescribeIpLocationServiceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpLocationServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpLocationServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpLocationServiceResponse, self).to_map()
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
            temp_model = DescribeIpLocationServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, region_en_name=None, region_name=None, region_no=None, region_no_alias=None):
        self.region_en_name = region_en_name  # type: str
        self.region_name = region_name  # type: str
        self.region_no = region_no  # type: str
        self.region_no_alias = region_no_alias  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.region_no_alias is not None:
            result['RegionNoAlias'] = self.region_no_alias
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RegionNoAlias') is not None:
            self.region_no_alias = m.get('RegionNoAlias')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDdosStatusRequest(TeaModel):
    def __init__(self, ddos_region_id=None, instance_id=None, instance_type=None, internet_ip=None):
        self.ddos_region_id = ddos_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_ip = internet_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDdosStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        return self


class ModifyDdosStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDdosStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDdosStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDdosStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDdosStatusResponse, self).to_map()
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
            temp_model = ModifyDdosStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseThresholdRequest(TeaModel):
    def __init__(self, bps=None, ddos_region_id=None, instance_id=None, instance_type=None, internet_ip=None,
                 is_auto=None, pps=None):
        self.bps = bps  # type: int
        self.ddos_region_id = ddos_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_ip = internet_ip  # type: str
        self.is_auto = is_auto  # type: bool
        self.pps = pps  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseThresholdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class ModifyDefenseThresholdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseThresholdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDefenseThresholdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefenseThresholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefenseThresholdResponse, self).to_map()
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
            temp_model = ModifyDefenseThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


