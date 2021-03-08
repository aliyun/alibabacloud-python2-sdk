# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class CreateHiTSDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, app_key=None, zone_id=None, instance_name=None, instance_alias=None,
                 instance_class=None, instance_storage=None, pay_type=None, vpcid=None, v_switch_id=None, max_timeline_limit=None,
                 instance_tps=None, engine_type=None, max_series_per_database=None, max_database_limit=None, pricing_cycle=None,
                 duration=None, tsdbversion=None, disk_category=None, client_token=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.app_key = TeaConverter.to_unicode(app_key)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.instance_alias = TeaConverter.to_unicode(instance_alias)  # type: unicode
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode
        self.instance_storage = TeaConverter.to_unicode(instance_storage)  # type: unicode
        self.pay_type = TeaConverter.to_unicode(pay_type)  # type: unicode
        self.vpcid = TeaConverter.to_unicode(vpcid)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.max_timeline_limit = TeaConverter.to_unicode(max_timeline_limit)  # type: unicode
        self.instance_tps = TeaConverter.to_unicode(instance_tps)  # type: unicode
        self.engine_type = TeaConverter.to_unicode(engine_type)  # type: unicode
        self.max_series_per_database = TeaConverter.to_unicode(max_series_per_database)  # type: unicode
        self.max_database_limit = TeaConverter.to_unicode(max_database_limit)  # type: unicode
        self.pricing_cycle = TeaConverter.to_unicode(pricing_cycle)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.tsdbversion = TeaConverter.to_unicode(tsdbversion)  # type: unicode
        self.disk_category = TeaConverter.to_unicode(disk_category)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.max_timeline_limit is not None:
            result['MaxTimelineLimit'] = self.max_timeline_limit
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.max_series_per_database is not None:
            result['MaxSeriesPerDatabase'] = self.max_series_per_database
        if self.max_database_limit is not None:
            result['MaxDatabaseLimit'] = self.max_database_limit
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.tsdbversion is not None:
            result['TSDBVersion'] = self.tsdbversion
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('MaxTimelineLimit') is not None:
            self.max_timeline_limit = m.get('MaxTimelineLimit')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('MaxSeriesPerDatabase') is not None:
            self.max_series_per_database = m.get('MaxSeriesPerDatabase')
        if m.get('MaxDatabaseLimit') is not None:
            self.max_database_limit = m.get('MaxDatabaseLimit')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('TSDBVersion') is not None:
            self.tsdbversion = m.get('TSDBVersion')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateHiTSDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateHiTSDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateHiTSDBInstanceResponseBody

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
            temp_model = CreateHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHiTSDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, app_key=None, instance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.app_key = TeaConverter.to_unicode(app_key)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteHiTSDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHiTSDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteHiTSDBInstanceResponseBody

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
            temp_model = DeleteHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, app_key=None, instance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.app_key = TeaConverter.to_unicode(app_key)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeHiTSDBInstanceResponseBodySecurityIpList(TeaModel):
    def __init__(self, ip=None):
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeHiTSDBInstanceResponseBody(TeaModel):
    def __init__(self, auto_renew=None, gmt_created=None, cpu_number=None, mem_size=None, network_type=None,
                 gmt_expire=None, instance_alias=None, instance_status=None, expired_time=None, payment_type=None,
                 max_timeline_limit=None, public_connection_string=None, engine_type=None, instance_tps=None, status=None,
                 instance_storage=None, request_id=None, zone_id=None, instance_id=None, create_time=None, disk_category=None,
                 instance_class=None, vswitch_id=None, series=None, vpc_id=None, charge_type=None, security_ip_list=None,
                 instance_description=None, region_id=None, connection_string=None):
        self.auto_renew = TeaConverter.to_unicode(auto_renew)  # type: unicode
        self.gmt_created = TeaConverter.to_unicode(gmt_created)  # type: unicode
        self.cpu_number = TeaConverter.to_unicode(cpu_number)  # type: unicode
        self.mem_size = TeaConverter.to_unicode(mem_size)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.gmt_expire = TeaConverter.to_unicode(gmt_expire)  # type: unicode
        self.instance_alias = TeaConverter.to_unicode(instance_alias)  # type: unicode
        self.instance_status = TeaConverter.to_unicode(instance_status)  # type: unicode
        self.expired_time = expired_time  # type: long
        self.payment_type = TeaConverter.to_unicode(payment_type)  # type: unicode
        self.max_timeline_limit = TeaConverter.to_unicode(max_timeline_limit)  # type: unicode
        self.public_connection_string = TeaConverter.to_unicode(public_connection_string)  # type: unicode
        self.engine_type = TeaConverter.to_unicode(engine_type)  # type: unicode
        self.instance_tps = TeaConverter.to_unicode(instance_tps)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.instance_storage = TeaConverter.to_unicode(instance_storage)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.create_time = create_time  # type: long
        self.disk_category = TeaConverter.to_unicode(disk_category)  # type: unicode
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode
        self.vswitch_id = TeaConverter.to_unicode(vswitch_id)  # type: unicode
        self.series = series  # type: int
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.security_ip_list = security_ip_list  # type: list[DescribeHiTSDBInstanceResponseBodySecurityIpList]
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.connection_string = TeaConverter.to_unicode(connection_string)  # type: unicode

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.cpu_number is not None:
            result['CpuNumber'] = self.cpu_number
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.max_timeline_limit is not None:
            result['MaxTimelineLimit'] = self.max_timeline_limit
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.series is not None:
            result['Series'] = self.series
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k in self.security_ip_list:
                result['SecurityIpList'].append(k.to_map() if k else None)
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('CpuNumber') is not None:
            self.cpu_number = m.get('CpuNumber')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('MaxTimelineLimit') is not None:
            self.max_timeline_limit = m.get('MaxTimelineLimit')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k in m.get('SecurityIpList'):
                temp_model = DescribeHiTSDBInstanceResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k))
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        return self


class DescribeHiTSDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeHiTSDBInstanceResponseBody

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
            temp_model = DescribeHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceListRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, app_key=None, query_str=None, status_list=None, page_number=None, page_size=None,
                 engine_type=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.app_key = TeaConverter.to_unicode(app_key)  # type: unicode
        self.query_str = TeaConverter.to_unicode(query_str)  # type: unicode
        self.status_list = TeaConverter.to_unicode(status_list)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.engine_type = TeaConverter.to_unicode(engine_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        return self


class DescribeHiTSDBInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(self, vpc_id=None, status=None, max_series_per_database=None, payment_type=None, engine_type=None,
                 vswitch_id=None, instance_class=None, create_time=None, user_id=None, charge_type=None, instance_storage=None,
                 network_type=None, instance_id=None, lock_mode=None, instance_description=None, region_id=None,
                 gmt_created=None, instance_alias=None, instance_tps=None, expired_time=None, zone_id=None,
                 instance_status=None, gmt_expire=None):
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.max_series_per_database = TeaConverter.to_unicode(max_series_per_database)  # type: unicode
        self.payment_type = TeaConverter.to_unicode(payment_type)  # type: unicode
        self.engine_type = TeaConverter.to_unicode(engine_type)  # type: unicode
        self.vswitch_id = TeaConverter.to_unicode(vswitch_id)  # type: unicode
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode
        self.create_time = create_time  # type: long
        self.user_id = TeaConverter.to_unicode(user_id)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.instance_storage = TeaConverter.to_unicode(instance_storage)  # type: unicode
        self.network_type = TeaConverter.to_unicode(network_type)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.lock_mode = TeaConverter.to_unicode(lock_mode)  # type: unicode
        self.instance_description = TeaConverter.to_unicode(instance_description)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.gmt_created = TeaConverter.to_unicode(gmt_created)  # type: unicode
        self.instance_alias = TeaConverter.to_unicode(instance_alias)  # type: unicode
        self.instance_tps = TeaConverter.to_unicode(instance_tps)  # type: unicode
        self.expired_time = expired_time  # type: long
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode
        self.instance_status = TeaConverter.to_unicode(instance_status)  # type: unicode
        self.gmt_expire = TeaConverter.to_unicode(gmt_expire)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.max_series_per_database is not None:
            result['MaxSeriesPerDatabase'] = self.max_series_per_database
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MaxSeriesPerDatabase') is not None:
            self.max_series_per_database = m.get('MaxSeriesPerDatabase')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        return self


class DescribeHiTSDBInstanceListResponseBody(TeaModel):
    def __init__(self, request_id=None, page_size=None, page_number=None, total=None, instance_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.total = total  # type: int
        self.instance_list = instance_list  # type: list[DescribeHiTSDBInstanceListResponseBodyInstanceList]

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeHiTSDBInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class DescribeHiTSDBInstanceListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeHiTSDBInstanceListResponseBody

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
            temp_model = DescribeHiTSDBInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceSecurityIpListRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, group_name=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.group_name = TeaConverter.to_unicode(group_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeHiTSDBInstanceSecurityIpListResponseBodySecurityIpList(TeaModel):
    def __init__(self, ip=None):
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeHiTSDBInstanceSecurityIpListResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.security_ip_list = security_ip_list  # type: list[DescribeHiTSDBInstanceSecurityIpListResponseBodySecurityIpList]

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k in self.security_ip_list:
                result['SecurityIpList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k in m.get('SecurityIpList'):
                temp_model = DescribeHiTSDBInstanceSecurityIpListResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k))
        return self


class DescribeHiTSDBInstanceSecurityIpListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeHiTSDBInstanceSecurityIpListResponseBody

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
            temp_model = DescribeHiTSDBInstanceSecurityIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, accept_language=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.accept_language = TeaConverter.to_unicode(accept_language)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = TeaConverter.to_unicode(local_name)  # type: unicode
        self.region_endpoint = TeaConverter.to_unicode(region_endpoint)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
    def __init__(self, request_id=None, regions=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRegionsResponseBody

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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, language=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.language = TeaConverter.to_unicode(language)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeZonesResponseBodyZoneListZoneModel(TeaModel):
    def __init__(self, local_name=None, zone_id=None):
        self.local_name = TeaConverter.to_unicode(local_name)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZoneList(TeaModel):
    def __init__(self, zone_model=None):
        self.zone_model = zone_model  # type: list[DescribeZonesResponseBodyZoneListZoneModel]

    def validate(self):
        if self.zone_model:
            for k in self.zone_model:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ZoneModel'] = []
        if self.zone_model is not None:
            for k in self.zone_model:
                result['ZoneModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone_model = []
        if m.get('ZoneModel') is not None:
            for k in m.get('ZoneModel'):
                temp_model = DescribeZonesResponseBodyZoneListZoneModel()
                self.zone_model.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zone_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.zone_list = zone_list  # type: DescribeZonesResponseBodyZoneList

    def validate(self):
        if self.zone_list:
            self.zone_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneList') is not None:
            temp_model = DescribeZonesResponseBodyZoneList()
            self.zone_list = temp_model.from_map(m['ZoneList'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeZonesResponseBody

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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHiTSDBInstanceClassRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, app_key=None, instance_id=None, instance_class=None, instance_storage=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.app_key = TeaConverter.to_unicode(app_key)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.instance_class = TeaConverter.to_unicode(instance_class)  # type: unicode
        self.instance_storage = TeaConverter.to_unicode(instance_storage)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        return self


class ModifyHiTSDBInstanceClassResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHiTSDBInstanceClassResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyHiTSDBInstanceClassResponseBody

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
            temp_model = ModifyHiTSDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHiTSDBInstanceSecurityIpListRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, security_ip_list=None, group_name=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.security_ip_list = TeaConverter.to_unicode(security_ip_list)  # type: unicode
        self.group_name = TeaConverter.to_unicode(group_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ModifyHiTSDBInstanceSecurityIpListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHiTSDBInstanceSecurityIpListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyHiTSDBInstanceSecurityIpListResponseBody

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
            temp_model = ModifyHiTSDBInstanceSecurityIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameHiTSDBInstanceAliasRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, app_key=None, instance_id=None, instance_alias=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.app_key = TeaConverter.to_unicode(app_key)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.instance_alias = TeaConverter.to_unicode(instance_alias)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        return self


class RenameHiTSDBInstanceAliasResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenameHiTSDBInstanceAliasResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RenameHiTSDBInstanceAliasResponseBody

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
            temp_model = RenameHiTSDBInstanceAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewTSDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, region_id=None, instance_id=None, pricing_cycle=None, duration=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.pricing_cycle = TeaConverter.to_unicode(pricing_cycle)  # type: unicode
        self.duration = duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class RenewTSDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewTSDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RenewTSDBInstanceResponseBody

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
            temp_model = RenewTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartHiTSDBInstanceRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestartHiTSDBInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartHiTSDBInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RestartHiTSDBInstanceResponseBody

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
            temp_model = RestartHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchHiTSDBInstancePublicNetRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 owner_account=None, instance_id=None, switch_action=None):
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.switch_action = switch_action  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.switch_action is not None:
            result['SwitchAction'] = self.switch_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SwitchAction') is not None:
            self.switch_action = m.get('SwitchAction')
        return self


class SwitchHiTSDBInstancePublicNetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchHiTSDBInstancePublicNetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SwitchHiTSDBInstancePublicNetResponseBody

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
            temp_model = SwitchHiTSDBInstancePublicNetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


