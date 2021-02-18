# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class DescribeGeoipInstanceRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None, instance_id=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeGeoipInstanceResponseBody(TeaModel):
    def __init__(self, expire_timestamp=None, version_code=None, max_qpd=None, max_qps=None, request_id=None,
                 instance_id=None, product_code=None, create_time=None, query_count=None, expire_time=None,
                 create_timestamp=None):
        self.expire_timestamp = expire_timestamp  # type: long
        self.version_code = TeaConverter.to_unicode(version_code)  # type: unicode
        self.max_qpd = max_qpd  # type: long
        self.max_qps = max_qps  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.product_code = TeaConverter.to_unicode(product_code)  # type: unicode
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.query_count = query_count  # type: long
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.create_timestamp = create_timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.max_qpd is not None:
            result['MaxQpd'] = self.max_qpd
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('MaxQpd') is not None:
            self.max_qpd = m.get('MaxQpd')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribeGeoipInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeGeoipInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeGeoipInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGeoipInstanceDataInfosRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None, instance_id=None, location_data_type=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.location_data_type = TeaConverter.to_unicode(location_data_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.location_data_type is not None:
            result['LocationDataType'] = self.location_data_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LocationDataType') is not None:
            self.location_data_type = m.get('LocationDataType')
        return self


class DescribeGeoipInstanceDataInfosResponseBodyDataInfosDataInfo(TeaModel):
    def __init__(self, type=None, update_timestamp=None, update_time=None, version=None, download_count=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.update_timestamp = update_timestamp  # type: long
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.version = TeaConverter.to_unicode(version)  # type: unicode
        self.download_count = download_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.download_count is not None:
            result['DownloadCount'] = self.download_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')
        return self


class DescribeGeoipInstanceDataInfosResponseBodyDataInfos(TeaModel):
    def __init__(self, data_info=None):
        self.data_info = data_info  # type: list[DescribeGeoipInstanceDataInfosResponseBodyDataInfosDataInfo]

    def validate(self):
        if self.data_info:
            for k in self.data_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataInfo'] = []
        if self.data_info is not None:
            for k in self.data_info:
                result['DataInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_info = []
        if m.get('DataInfo') is not None:
            for k in m.get('DataInfo'):
                temp_model = DescribeGeoipInstanceDataInfosResponseBodyDataInfosDataInfo()
                self.data_info.append(temp_model.from_map(k))
        return self


class DescribeGeoipInstanceDataInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, data_infos=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data_infos = data_infos  # type: DescribeGeoipInstanceDataInfosResponseBodyDataInfos

    def validate(self):
        if self.data_infos:
            self.data_infos.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_infos is not None:
            result['DataInfos'] = self.data_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataInfos') is not None:
            temp_model = DescribeGeoipInstanceDataInfosResponseBodyDataInfos()
            self.data_infos = temp_model.from_map(m['DataInfos'])
        return self


class DescribeGeoipInstanceDataInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeGeoipInstanceDataInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeGeoipInstanceDataInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGeoipInstanceDataUrlRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None, instance_id=None, data_type=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.data_type = TeaConverter.to_unicode(data_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        return self


class DescribeGeoipInstanceDataUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, download_url=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.download_url = TeaConverter.to_unicode(download_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        return self


class DescribeGeoipInstanceDataUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeGeoipInstanceDataUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeGeoipInstanceDataUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGeoipInstancesRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeGeoipInstancesResponseBodyGeoipInstancesGeoipInstance(TeaModel):
    def __init__(self, status=None, expire_timestamp=None, expire_time=None, max_qps=None, create_time=None,
                 max_qpd=None, instance_id=None, version_code=None, create_timestamp=None, product_code=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.expire_timestamp = expire_timestamp  # type: long
        self.expire_time = TeaConverter.to_unicode(expire_time)  # type: unicode
        self.max_qps = max_qps  # type: long
        self.create_time = TeaConverter.to_unicode(create_time)  # type: unicode
        self.max_qpd = max_qpd  # type: long
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.version_code = TeaConverter.to_unicode(version_code)  # type: unicode
        self.create_timestamp = create_timestamp  # type: long
        self.product_code = TeaConverter.to_unicode(product_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_timestamp is not None:
            result['ExpireTimestamp'] = self.expire_timestamp
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.max_qpd is not None:
            result['MaxQpd'] = self.max_qpd
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTimestamp') is not None:
            self.expire_timestamp = m.get('ExpireTimestamp')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaxQpd') is not None:
            self.max_qpd = m.get('MaxQpd')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeGeoipInstancesResponseBodyGeoipInstances(TeaModel):
    def __init__(self, geoip_instance=None):
        self.geoip_instance = geoip_instance  # type: list[DescribeGeoipInstancesResponseBodyGeoipInstancesGeoipInstance]

    def validate(self):
        if self.geoip_instance:
            for k in self.geoip_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['GeoipInstance'] = []
        if self.geoip_instance is not None:
            for k in self.geoip_instance:
                result['GeoipInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.geoip_instance = []
        if m.get('GeoipInstance') is not None:
            for k in m.get('GeoipInstance'):
                temp_model = DescribeGeoipInstancesResponseBodyGeoipInstancesGeoipInstance()
                self.geoip_instance.append(temp_model.from_map(k))
        return self


class DescribeGeoipInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, geoip_instances=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.geoip_instances = geoip_instances  # type: DescribeGeoipInstancesResponseBodyGeoipInstances

    def validate(self):
        if self.geoip_instances:
            self.geoip_instances.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.geoip_instances is not None:
            result['GeoipInstances'] = self.geoip_instances.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GeoipInstances') is not None:
            temp_model = DescribeGeoipInstancesResponseBodyGeoipInstances()
            self.geoip_instances = temp_model.from_map(m['GeoipInstances'])
        return self


class DescribeGeoipInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeGeoipInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeGeoipInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGeoipInstanceStatisticsRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None, instance_id=None, start_date=None, end_date=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.start_date = TeaConverter.to_unicode(start_date)  # type: unicode
        self.end_date = TeaConverter.to_unicode(end_date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class DescribeGeoipInstanceStatisticsResponseBodyStatisticsStatistic(TeaModel):
    def __init__(self, timestamp=None, count=None):
        self.timestamp = timestamp  # type: long
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeGeoipInstanceStatisticsResponseBodyStatistics(TeaModel):
    def __init__(self, statistic=None):
        self.statistic = statistic  # type: list[DescribeGeoipInstanceStatisticsResponseBodyStatisticsStatistic]

    def validate(self):
        if self.statistic:
            for k in self.statistic:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Statistic'] = []
        if self.statistic is not None:
            for k in self.statistic:
                result['Statistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.statistic = []
        if m.get('Statistic') is not None:
            for k in m.get('Statistic'):
                temp_model = DescribeGeoipInstanceStatisticsResponseBodyStatisticsStatistic()
                self.statistic.append(temp_model.from_map(k))
        return self


class DescribeGeoipInstanceStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, statistics=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.statistics = statistics  # type: DescribeGeoipInstanceStatisticsResponseBodyStatistics

    def validate(self):
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Statistics') is not None:
            temp_model = DescribeGeoipInstanceStatisticsResponseBodyStatistics()
            self.statistics = temp_model.from_map(m['Statistics'])
        return self


class DescribeGeoipInstanceStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeGeoipInstanceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeGeoipInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpv4LocationRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None, ip=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeIpv4LocationResponseBody(TeaModel):
    def __init__(self, province_en=None, request_id=None, city_en=None, ip=None, isp=None, latitude=None, city=None,
                 county=None, longitude=None, country_en=None, province=None, country=None, country_code=None):
        self.province_en = TeaConverter.to_unicode(province_en)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.city_en = TeaConverter.to_unicode(city_en)  # type: unicode
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.isp = TeaConverter.to_unicode(isp)  # type: unicode
        self.latitude = TeaConverter.to_unicode(latitude)  # type: unicode
        self.city = TeaConverter.to_unicode(city)  # type: unicode
        self.county = TeaConverter.to_unicode(county)  # type: unicode
        self.longitude = TeaConverter.to_unicode(longitude)  # type: unicode
        self.country_en = TeaConverter.to_unicode(country_en)  # type: unicode
        self.province = TeaConverter.to_unicode(province)  # type: unicode
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.country_code = TeaConverter.to_unicode(country_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.province_en is not None:
            result['ProvinceEn'] = self.province_en
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.city_en is not None:
            result['CityEn'] = self.city_en
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.city is not None:
            result['City'] = self.city
        if self.county is not None:
            result['County'] = self.county
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.country_en is not None:
            result['CountryEn'] = self.country_en
        if self.province is not None:
            result['Province'] = self.province
        if self.country is not None:
            result['Country'] = self.country
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvinceEn') is not None:
            self.province_en = m.get('ProvinceEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CityEn') is not None:
            self.city_en = m.get('CityEn')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('County') is not None:
            self.county = m.get('County')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('CountryEn') is not None:
            self.country_en = m.get('CountryEn')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        return self


class DescribeIpv4LocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeIpv4LocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeIpv4LocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpv6LocationRequest(TeaModel):
    def __init__(self, lang=None, user_client_ip=None, ip=None):
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.user_client_ip = TeaConverter.to_unicode(user_client_ip)  # type: unicode
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeIpv6LocationResponseBody(TeaModel):
    def __init__(self, province_en=None, request_id=None, city_en=None, ip=None, isp=None, latitude=None, city=None,
                 county=None, longitude=None, country_en=None, province=None, country=None, country_code=None):
        self.province_en = TeaConverter.to_unicode(province_en)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.city_en = TeaConverter.to_unicode(city_en)  # type: unicode
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.isp = TeaConverter.to_unicode(isp)  # type: unicode
        self.latitude = TeaConverter.to_unicode(latitude)  # type: unicode
        self.city = TeaConverter.to_unicode(city)  # type: unicode
        self.county = TeaConverter.to_unicode(county)  # type: unicode
        self.longitude = TeaConverter.to_unicode(longitude)  # type: unicode
        self.country_en = TeaConverter.to_unicode(country_en)  # type: unicode
        self.province = TeaConverter.to_unicode(province)  # type: unicode
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.country_code = TeaConverter.to_unicode(country_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.province_en is not None:
            result['ProvinceEn'] = self.province_en
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.city_en is not None:
            result['CityEn'] = self.city_en
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.city is not None:
            result['City'] = self.city
        if self.county is not None:
            result['County'] = self.county
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.country_en is not None:
            result['CountryEn'] = self.country_en
        if self.province is not None:
            result['Province'] = self.province
        if self.country is not None:
            result['Country'] = self.country
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvinceEn') is not None:
            self.province_en = m.get('ProvinceEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CityEn') is not None:
            self.city_en = m.get('CityEn')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('County') is not None:
            self.county = m.get('County')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('CountryEn') is not None:
            self.country_en = m.get('CountryEn')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        return self


class DescribeIpv6LocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeIpv6LocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeIpv6LocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


