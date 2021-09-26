# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ClearInstanceStorageRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, storage_space=None, storage_category=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.storage_space = storage_space  # type: str
        self.storage_category = storage_category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearInstanceStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        return self


class ClearInstanceStorageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearInstanceStorageResponseBody, self).to_map()
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


class ClearInstanceStorageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ClearInstanceStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearInstanceStorageResponse, self).to_map()
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
            temp_model = ClearInstanceStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhiteListRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, ip_version=None, white_list=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.ip_version = ip_version  # type: str
        self.white_list = white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigInstanceWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceWhiteListResponseBody, self).to_map()
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


class ConfigInstanceWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfigInstanceWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigInstanceWhiteListResponse, self).to_map()
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
            temp_model = ConfigInstanceWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogsRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, start_time=None, end_time=None, current_page=None,
                 page_size=None, sort=None, dir=None, db_id=None, query_string=None, payload=None, login_user=None,
                 op_type=None, sip=None, dip=None, result=None, accessid=None, sessionid=None, sqlid=None, db_type=None,
                 sport=None, dport=None, smac=None, dmac=None, db_name=None, client_prg=None, host_name=None,
                 client_user=None, sql_len=None, effect_row=None, cost=None, result_desc=None, data_set=None, alarm_name=None,
                 alarm_level=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.sort = sort  # type: str
        self.dir = dir  # type: str
        self.db_id = db_id  # type: str
        self.query_string = query_string  # type: str
        self.payload = payload  # type: str
        self.login_user = login_user  # type: str
        self.op_type = op_type  # type: str
        self.sip = sip  # type: str
        self.dip = dip  # type: str
        self.result = result  # type: str
        self.accessid = accessid  # type: str
        self.sessionid = sessionid  # type: str
        self.sqlid = sqlid  # type: str
        self.db_type = db_type  # type: str
        self.sport = sport  # type: str
        self.dport = dport  # type: str
        self.smac = smac  # type: str
        self.dmac = dmac  # type: str
        self.db_name = db_name  # type: str
        self.client_prg = client_prg  # type: str
        self.host_name = host_name  # type: str
        self.client_user = client_user  # type: str
        self.sql_len = sql_len  # type: str
        self.effect_row = effect_row  # type: str
        self.cost = cost  # type: str
        self.result_desc = result_desc  # type: str
        self.data_set = data_set  # type: str
        self.alarm_name = alarm_name  # type: str
        self.alarm_level = alarm_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.query_string is not None:
            result['QueryString'] = self.query_string
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.result is not None:
            result['Result'] = self.result
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        if self.sqlid is not None:
            result['Sqlid'] = self.sqlid
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.sql_len is not None:
            result['SqlLen'] = self.sql_len
        if self.effect_row is not None:
            result['EffectRow'] = self.effect_row
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.result_desc is not None:
            result['ResultDesc'] = self.result_desc
        if self.data_set is not None:
            result['DataSet'] = self.data_set
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        if m.get('Sqlid') is not None:
            self.sqlid = m.get('Sqlid')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('SqlLen') is not None:
            self.sql_len = m.get('SqlLen')
        if m.get('EffectRow') is not None:
            self.effect_row = m.get('EffectRow')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('ResultDesc') is not None:
            self.result_desc = m.get('ResultDesc')
        if m.get('DataSet') is not None:
            self.data_set = m.get('DataSet')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class DescribeAuditLogsResponseBodyAuditLogs(TeaModel):
    def __init__(self, client_user=None, effect_row=None, c_5=None, client_prg=None, accessid=None, result_desc=None,
                 sql_len=None, payload=None, c_4=None, date_time=None, db_name=None, data_set=None, sqlid=None,
                 relate_ip=None, alarm_level=None, c_2=None, dip=None, result=None, cost=None, relate_user=None, sip=None,
                 c_3=None, host_name=None, alarm_name=None, pick_ip=None, relate_info=None, pick_user=None, op_type=None,
                 sport=None, data_set_size=None, db_type=None, alarm_flag=None, smac=None, dport=None, c_1=None, dmac=None,
                 login_user=None, sessionid=None):
        self.client_user = client_user  # type: str
        self.effect_row = effect_row  # type: int
        self.c_5 = c_5  # type: str
        self.client_prg = client_prg  # type: str
        self.accessid = accessid  # type: str
        self.result_desc = result_desc  # type: str
        self.sql_len = sql_len  # type: int
        self.payload = payload  # type: str
        self.c_4 = c_4  # type: str
        self.date_time = date_time  # type: str
        self.db_name = db_name  # type: str
        self.data_set = data_set  # type: str
        self.sqlid = sqlid  # type: str
        self.relate_ip = relate_ip  # type: str
        self.alarm_level = alarm_level  # type: int
        self.c_2 = c_2  # type: str
        self.dip = dip  # type: str
        self.result = result  # type: int
        self.cost = cost  # type: int
        self.relate_user = relate_user  # type: str
        self.sip = sip  # type: str
        self.c_3 = c_3  # type: str
        self.host_name = host_name  # type: str
        self.alarm_name = alarm_name  # type: str
        self.pick_ip = pick_ip  # type: str
        self.relate_info = relate_info  # type: str
        self.pick_user = pick_user  # type: str
        self.op_type = op_type  # type: str
        self.sport = sport  # type: int
        self.data_set_size = data_set_size  # type: int
        self.db_type = db_type  # type: str
        self.alarm_flag = alarm_flag  # type: int
        self.smac = smac  # type: int
        self.dport = dport  # type: int
        self.c_1 = c_1  # type: str
        self.dmac = dmac  # type: int
        self.login_user = login_user  # type: str
        self.sessionid = sessionid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAuditLogsResponseBodyAuditLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.effect_row is not None:
            result['EffectRow'] = self.effect_row
        if self.c_5 is not None:
            result['C5'] = self.c_5
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.result_desc is not None:
            result['ResultDesc'] = self.result_desc
        if self.sql_len is not None:
            result['SqlLen'] = self.sql_len
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.c_4 is not None:
            result['C4'] = self.c_4
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.data_set is not None:
            result['DataSet'] = self.data_set
        if self.sqlid is not None:
            result['Sqlid'] = self.sqlid
        if self.relate_ip is not None:
            result['RelateIp'] = self.relate_ip
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        if self.c_2 is not None:
            result['C2'] = self.c_2
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.result is not None:
            result['Result'] = self.result
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.relate_user is not None:
            result['RelateUser'] = self.relate_user
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.c_3 is not None:
            result['C3'] = self.c_3
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.pick_ip is not None:
            result['PickIp'] = self.pick_ip
        if self.relate_info is not None:
            result['RelateInfo'] = self.relate_info
        if self.pick_user is not None:
            result['PickUser'] = self.pick_user
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.data_set_size is not None:
            result['DataSetSize'] = self.data_set_size
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.alarm_flag is not None:
            result['AlarmFlag'] = self.alarm_flag
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.c_1 is not None:
            result['C1'] = self.c_1
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('EffectRow') is not None:
            self.effect_row = m.get('EffectRow')
        if m.get('C5') is not None:
            self.c_5 = m.get('C5')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('ResultDesc') is not None:
            self.result_desc = m.get('ResultDesc')
        if m.get('SqlLen') is not None:
            self.sql_len = m.get('SqlLen')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('C4') is not None:
            self.c_4 = m.get('C4')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DataSet') is not None:
            self.data_set = m.get('DataSet')
        if m.get('Sqlid') is not None:
            self.sqlid = m.get('Sqlid')
        if m.get('RelateIp') is not None:
            self.relate_ip = m.get('RelateIp')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        if m.get('C2') is not None:
            self.c_2 = m.get('C2')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('RelateUser') is not None:
            self.relate_user = m.get('RelateUser')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('C3') is not None:
            self.c_3 = m.get('C3')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('PickIp') is not None:
            self.pick_ip = m.get('PickIp')
        if m.get('RelateInfo') is not None:
            self.relate_info = m.get('RelateInfo')
        if m.get('PickUser') is not None:
            self.pick_user = m.get('PickUser')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('DataSetSize') is not None:
            self.data_set_size = m.get('DataSetSize')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('AlarmFlag') is not None:
            self.alarm_flag = m.get('AlarmFlag')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('C1') is not None:
            self.c_1 = m.get('C1')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        return self


class DescribeAuditLogsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, audit_logs=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.audit_logs = audit_logs  # type: list[DescribeAuditLogsResponseBodyAuditLogs]

    def validate(self):
        if self.audit_logs:
            for k in self.audit_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAuditLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AuditLogs'] = []
        if self.audit_logs is not None:
            for k in self.audit_logs:
                result['AuditLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.audit_logs = []
        if m.get('AuditLogs') is not None:
            for k in m.get('AuditLogs'):
                temp_model = DescribeAuditLogsResponseBodyAuditLogs()
                self.audit_logs.append(temp_model.from_map(k))
        return self


class DescribeAuditLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAuditLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAuditLogsResponse, self).to_map()
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
            temp_model = DescribeAuditLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttribueRequest(TeaModel):
    def __init__(self, lang=None, instance_id=None, region_id=None):
        self.lang = lang  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttribueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttribueResponseBodyInstanceAttribue(TeaModel):
    def __init__(self, vpc_id=None, vswitch_id=None, expire_time=None, instance_id=None, internet_endpoint=None,
                 region_id=None, intranet_endpoint=None, start_time=None, series_code=None, description=None,
                 instance_status=None, license_code=None, public_network_access=None, white_list=None):
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.expire_time = expire_time  # type: long
        self.instance_id = instance_id  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.start_time = start_time  # type: long
        self.series_code = series_code  # type: str
        self.description = description  # type: str
        self.instance_status = instance_status  # type: int
        self.license_code = license_code  # type: str
        self.public_network_access = public_network_access  # type: bool
        self.white_list = white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttribueResponseBodyInstanceAttribue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeInstanceAttribueResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_attribue=None):
        self.request_id = request_id  # type: str
        self.instance_attribue = instance_attribue  # type: DescribeInstanceAttribueResponseBodyInstanceAttribue

    def validate(self):
        if self.instance_attribue:
            self.instance_attribue.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttribueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribue is not None:
            result['InstanceAttribue'] = self.instance_attribue.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribue') is not None:
            temp_model = DescribeInstanceAttribueResponseBodyInstanceAttribue()
            self.instance_attribue = temp_model.from_map(m['InstanceAttribue'])
        return self


class DescribeInstanceAttribueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceAttribueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttribueResponse, self).to_map()
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
            temp_model = DescribeInstanceAttribueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(self, vpc_id=None, vswitch_id=None, expire_time=None, image_version=None, instance_id=None,
                 internet_endpoint=None, region_id=None, intranet_endpoint=None, start_time=None, series_code=None, description=None,
                 instance_status=None, license_code=None, public_network_access=None, white_list=None, ipv_6white_list=None):
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.expire_time = expire_time  # type: long
        self.image_version = image_version  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.start_time = start_time  # type: long
        self.series_code = series_code  # type: str
        self.description = description  # type: str
        self.instance_status = instance_status  # type: str
        self.license_code = license_code  # type: str
        self.public_network_access = public_network_access  # type: bool
        self.white_list = white_list  # type: list[str]
        self.ipv_6white_list = ipv_6white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstanceAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        if self.ipv_6white_list is not None:
            result['Ipv6WhiteList'] = self.ipv_6white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        if m.get('Ipv6WhiteList') is not None:
            self.ipv_6white_list = m.get('Ipv6WhiteList')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_attribute=None):
        self.request_id = request_id  # type: str
        self.instance_attribute = instance_attribute  # type: DescribeInstanceAttributeResponseBodyInstanceAttribute

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponse, self).to_map()
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
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, page_size=None, current_page=None, region_id=None, instance_status=None,
                 resource_group_id=None, instance_id=None, tag=None):
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.region_id = region_id  # type: str
        self.instance_status = instance_status  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.instance_id = instance_id  # type: list[str]
        self.tag = tag  # type: list[DescribeInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, vpc_id=None, vswitch_id=None, expire_time=None, image_version=None, instance_id=None,
                 internet_endpoint=None, region_id=None, intranet_endpoint=None, start_time=None, series_code=None, description=None,
                 instance_status=None, license_code=None, public_network_access=None):
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.expire_time = expire_time  # type: long
        self.image_version = image_version  # type: str
        self.instance_id = instance_id  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.start_time = start_time  # type: long
        self.series_code = series_code  # type: str
        self.description = description  # type: str
        self.instance_status = instance_status  # type: str
        self.license_code = license_code  # type: str
        self.public_network_access = public_network_access  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, instances=None):
        self.total_count = total_count  # type: long
        self.request_id = request_id  # type: str
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStorageRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceStorageResponseBodyInstanceStorages(TeaModel):
    def __init__(self, storage_time=None, storage_capacity=None, storage_category=None, storage_space=None,
                 storage_used=None):
        self.storage_time = storage_time  # type: long
        self.storage_capacity = storage_capacity  # type: long
        self.storage_category = storage_category  # type: str
        self.storage_space = storage_space  # type: str
        self.storage_used = storage_used  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceStorageResponseBodyInstanceStorages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_time is not None:
            result['StorageTime'] = self.storage_time
        if self.storage_capacity is not None:
            result['StorageCapacity'] = self.storage_capacity
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageTime') is not None:
            self.storage_time = m.get('StorageTime')
        if m.get('StorageCapacity') is not None:
            self.storage_capacity = m.get('StorageCapacity')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        return self


class DescribeInstanceStorageResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_storages=None):
        self.request_id = request_id  # type: str
        self.instance_storages = instance_storages  # type: list[DescribeInstanceStorageResponseBodyInstanceStorages]

    def validate(self):
        if self.instance_storages:
            for k in self.instance_storages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceStorageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceStorages'] = []
        if self.instance_storages is not None:
            for k in self.instance_storages:
                result['InstanceStorages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_storages = []
        if m.get('InstanceStorages') is not None:
            for k in m.get('InstanceStorages'):
                temp_model = DescribeInstanceStorageResponseBodyInstanceStorages()
                self.instance_storages.append(temp_model.from_map(k))
        return self


class DescribeInstanceStorageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceStorageResponse, self).to_map()
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
            temp_model = DescribeInstanceStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, region_id=None):
        self.accept_language = accept_language  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_endpoint=None, local_name=None, region_id=None):
        self.region_endpoint = region_endpoint  # type: str
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRenewStatusRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeRenewStatusResponseBodyInstances(TeaModel):
    def __init__(self, renew_status=None, instance_id=None):
        self.renew_status = renew_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenewStatusResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeRenewStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, instances=None):
        self.request_id = request_id  # type: str
        self.instances = instances  # type: list[DescribeRenewStatusResponseBodyInstances]

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenewStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeRenewStatusResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeRenewStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRenewStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRenewStatusResponse, self).to_map()
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
            temp_model = DescribeRenewStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSessionLogsRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, start_time=None, end_time=None, current_page=None,
                 page_size=None, sort=None, dir=None, db_id=None, sip=None, sport=None, login_user=None, dip=None, dport=None,
                 sessionid=None, db_type=None, smac=None, dmac=None, client_prg=None, host_name=None, client_user=None,
                 db_name=None, session_status=None, sql_count=None, req_flow=None, rsp_flow=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.sort = sort  # type: str
        self.dir = dir  # type: str
        self.db_id = db_id  # type: str
        self.sip = sip  # type: str
        self.sport = sport  # type: str
        self.login_user = login_user  # type: str
        self.dip = dip  # type: str
        self.dport = dport  # type: str
        self.sessionid = sessionid  # type: str
        self.db_type = db_type  # type: str
        self.smac = smac  # type: str
        self.dmac = dmac  # type: str
        self.client_prg = client_prg  # type: str
        self.host_name = host_name  # type: str
        self.client_user = client_user  # type: str
        self.db_name = db_name  # type: str
        self.session_status = session_status  # type: str
        self.sql_count = sql_count  # type: str
        self.req_flow = req_flow  # type: str
        self.rsp_flow = rsp_flow  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSessionLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.req_flow is not None:
            result['ReqFlow'] = self.req_flow
        if self.rsp_flow is not None:
            result['RspFlow'] = self.rsp_flow
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('ReqFlow') is not None:
            self.req_flow = m.get('ReqFlow')
        if m.get('RspFlow') is not None:
            self.rsp_flow = m.get('RspFlow')
        return self


class DescribeSessionLogsResponseBodySessionLogs(TeaModel):
    def __init__(self, client_user=None, session_status=None, c_5=None, client_prg=None, accessid=None, c_4=None,
                 db_name=None, request_flow=None, pro_con=None, c_2=None, dip=None, sip=None, c_3=None, host_name=None,
                 response_flow=None, encode=None, normal_end=None, end_time=None, sport=None, start_time=None, db_type=None,
                 str_info=None, sql_count=None, smac=None, dport=None, dmac=None, c_1=None, login_user=None, sessionid=None):
        self.client_user = client_user  # type: str
        self.session_status = session_status  # type: int
        self.c_5 = c_5  # type: str
        self.client_prg = client_prg  # type: str
        self.accessid = accessid  # type: str
        self.c_4 = c_4  # type: str
        self.db_name = db_name  # type: str
        self.request_flow = request_flow  # type: int
        self.pro_con = pro_con  # type: int
        self.c_2 = c_2  # type: str
        self.dip = dip  # type: str
        self.sip = sip  # type: str
        self.c_3 = c_3  # type: str
        self.host_name = host_name  # type: str
        self.response_flow = response_flow  # type: int
        self.encode = encode  # type: str
        self.normal_end = normal_end  # type: int
        self.end_time = end_time  # type: int
        self.sport = sport  # type: int
        self.start_time = start_time  # type: int
        self.db_type = db_type  # type: str
        self.str_info = str_info  # type: str
        self.sql_count = sql_count  # type: int
        self.smac = smac  # type: int
        self.dport = dport  # type: int
        self.dmac = dmac  # type: int
        self.c_1 = c_1  # type: str
        self.login_user = login_user  # type: str
        self.sessionid = sessionid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSessionLogsResponseBodySessionLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.c_5 is not None:
            result['C5'] = self.c_5
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.c_4 is not None:
            result['C4'] = self.c_4
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.request_flow is not None:
            result['RequestFlow'] = self.request_flow
        if self.pro_con is not None:
            result['ProCon'] = self.pro_con
        if self.c_2 is not None:
            result['C2'] = self.c_2
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.c_3 is not None:
            result['C3'] = self.c_3
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.response_flow is not None:
            result['ResponseFlow'] = self.response_flow
        if self.encode is not None:
            result['Encode'] = self.encode
        if self.normal_end is not None:
            result['NormalEnd'] = self.normal_end
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.str_info is not None:
            result['StrInfo'] = self.str_info
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.c_1 is not None:
            result['C1'] = self.c_1
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('C5') is not None:
            self.c_5 = m.get('C5')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('C4') is not None:
            self.c_4 = m.get('C4')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RequestFlow') is not None:
            self.request_flow = m.get('RequestFlow')
        if m.get('ProCon') is not None:
            self.pro_con = m.get('ProCon')
        if m.get('C2') is not None:
            self.c_2 = m.get('C2')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('C3') is not None:
            self.c_3 = m.get('C3')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ResponseFlow') is not None:
            self.response_flow = m.get('ResponseFlow')
        if m.get('Encode') is not None:
            self.encode = m.get('Encode')
        if m.get('NormalEnd') is not None:
            self.normal_end = m.get('NormalEnd')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('StrInfo') is not None:
            self.str_info = m.get('StrInfo')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('C1') is not None:
            self.c_1 = m.get('C1')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        return self


class DescribeSessionLogsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, session_logs=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.session_logs = session_logs  # type: list[DescribeSessionLogsResponseBodySessionLogs]

    def validate(self):
        if self.session_logs:
            for k in self.session_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSessionLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SessionLogs'] = []
        if self.session_logs is not None:
            for k in self.session_logs:
                result['SessionLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.session_logs = []
        if m.get('SessionLogs') is not None:
            for k in m.get('SessionLogs'):
                temp_model = DescribeSessionLogsResponseBodySessionLogs()
                self.session_logs.append(temp_model.from_map(k))
        return self


class DescribeSessionLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSessionLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSessionLogsResponse, self).to_map()
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
            temp_model = DescribeSessionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstancePublicAccessRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableInstancePublicAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableInstancePublicAccessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableInstancePublicAccessResponseBody, self).to_map()
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


class DisableInstancePublicAccessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableInstancePublicAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableInstancePublicAccessResponse, self).to_map()
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
            temp_model = DisableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstancePublicAccessRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInstancePublicAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableInstancePublicAccessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInstancePublicAccessResponseBody, self).to_map()
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


class EnableInstancePublicAccessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableInstancePublicAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableInstancePublicAccessResponse, self).to_map()
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
            temp_model = EnableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadAuthRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GenerateUploadAuthResponseBodyUploadConfig(TeaModel):
    def __init__(self, signature=None, file_path=None, policy=None, expire_time=None, upload_host=None,
                 access_id=None):
        self.signature = signature  # type: str
        self.file_path = file_path  # type: str
        self.policy = policy  # type: str
        self.expire_time = expire_time  # type: long
        self.upload_host = upload_host  # type: str
        self.access_id = access_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadAuthResponseBodyUploadConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        return self


class GenerateUploadAuthResponseBody(TeaModel):
    def __init__(self, request_id=None, upload_config=None):
        self.request_id = request_id  # type: str
        self.upload_config = upload_config  # type: GenerateUploadAuthResponseBodyUploadConfig

    def validate(self):
        if self.upload_config:
            self.upload_config.validate()

    def to_map(self):
        _map = super(GenerateUploadAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_config is not None:
            result['UploadConfig'] = self.upload_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadConfig') is not None:
            temp_model = GenerateUploadAuthResponseBodyUploadConfig()
            self.upload_config = temp_model.from_map(m['UploadConfig'])
        return self


class GenerateUploadAuthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateUploadAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUploadAuthResponse, self).to_map()
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
            temp_model = GenerateUploadAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantServiceRoleRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantServiceRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GrantServiceRoleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantServiceRoleResponseBody, self).to_map()
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


class GrantServiceRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GrantServiceRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantServiceRoleResponse, self).to_map()
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
            temp_model = GrantServiceRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, page_size=None, current_page=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_count=None, tag_key=None):
        self.tag_count = tag_count  # type: int
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBodyTagKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, tag_keys=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.tag_keys = tag_keys  # type: list[ListTagKeysResponseBodyTagKeys]

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagKeysResponse, self).to_map()
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, next_token=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_value=None, resource_type=None, resource_id=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, description=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponseBody, self).to_map()
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponse, self).to_map()
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
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceStorageRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, storage_space=None, storage_category=None,
                 storage_time=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.storage_space = storage_space  # type: str
        self.storage_category = storage_category  # type: str
        self.storage_time = storage_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceStorageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        if self.storage_time is not None:
            result['StorageTime'] = self.storage_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        if m.get('StorageTime') is not None:
            self.storage_time = m.get('StorageTime')
        return self


class ModifyInstanceStorageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceStorageResponseBody, self).to_map()
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


class ModifyInstanceStorageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceStorageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceStorageResponse, self).to_map()
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
            temp_model = ModifyInstanceStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, resource_id=None, resource_group_id=None, resource_type=None, region_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_type = resource_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponse, self).to_map()
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, service_code=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RefundInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundInstanceResponseBody, self).to_map()
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


class RefundInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefundInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundInstanceResponse, self).to_map()
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
            temp_model = RefundInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, vswitch_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
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


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartInstanceResponse, self).to_map()
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


