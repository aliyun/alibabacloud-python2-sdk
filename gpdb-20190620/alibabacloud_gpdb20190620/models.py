# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeDBInstanceForDmsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, host=None, owner_id=None, port=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.host = host  # type: str
        self.owner_id = owner_id  # type: long
        self.port = port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceForDmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.host is not None:
            result['Host'] = self.host
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeDBInstanceForDmsResponseBodyInstance(TeaModel):
    def __init__(self, ali_uid=None, bid=None, connection_string=None, db_instance_name=None, db_type=None,
                 description=None, instance_network_type=None, port=None, region=None, v_switch_id=None, version=None,
                 vpc_cloud_instance_id=None, vpc_id=None, vpc_ip=None):
        self.ali_uid = ali_uid  # type: str
        self.bid = bid  # type: str
        self.connection_string = connection_string  # type: str
        self.db_instance_name = db_instance_name  # type: str
        self.db_type = db_type  # type: str
        self.description = description  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.port = port  # type: str
        self.region = region  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.version = version  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_ip = vpc_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceForDmsResponseBodyInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_ip is not None:
            result['VpcIp'] = self.vpc_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcIp') is not None:
            self.vpc_ip = m.get('VpcIp')
        return self


class DescribeDBInstanceForDmsResponseBody(TeaModel):
    def __init__(self, code=None, count=None, http_status_code=None, instance=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.count = count  # type: long
        self.http_status_code = http_status_code  # type: int
        self.instance = instance  # type: DescribeDBInstanceForDmsResponseBodyInstance
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceForDmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
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
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Instance') is not None:
            temp_model = DescribeDBInstanceForDmsResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBInstanceForDmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceForDmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceForDmsResponse, self).to_map()
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
            temp_model = DescribeDBInstanceForDmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSecurityIpsRequest(TeaModel):
    def __init__(self, instance_id=None, owner_id=None):
        self.instance_id = instance_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDBInstanceSecurityIpsResponseBodyResult(TeaModel):
    def __init__(self, group_name=None, white_list=None):
        self.group_name = group_name  # type: str
        self.white_list = white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstanceSecurityIpsResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeDBInstanceSecurityIpsResponseBody(TeaModel):
    def __init__(self, code=None, count=None, http_status_code=None, message=None, request_id=None, result=None,
                 success=None):
        self.code = code  # type: str
        self.count = count  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeDBInstanceSecurityIpsResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSecurityIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeDBInstanceSecurityIpsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBInstanceSecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstanceSecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstanceSecurityIpsResponse, self).to_map()
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
            temp_model = DescribeDBInstanceSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesForDmsRequest(TeaModel):
    def __init__(self, ali_uid=None, owner_id=None):
        self.ali_uid = ali_uid  # type: long
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesForDmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDBInstancesForDmsResponseBodyInstances(TeaModel):
    def __init__(self, ali_uid=None, bid=None, connection_string=None, db_instance_name=None, db_type=None,
                 description=None, instance_network_type=None, port=None, region=None, v_switch_id=None, version=None,
                 vpc_cloud_instance_id=None, vpc_id=None, vpc_ip=None):
        self.ali_uid = ali_uid  # type: str
        # BID。
        self.bid = bid  # type: str
        self.connection_string = connection_string  # type: str
        self.db_instance_name = db_instance_name  # type: str
        self.db_type = db_type  # type: str
        self.description = description  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.port = port  # type: str
        self.region = region  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.version = version  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_ip = vpc_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDBInstancesForDmsResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_ip is not None:
            result['VpcIp'] = self.vpc_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcIp') is not None:
            self.vpc_ip = m.get('VpcIp')
        return self


class DescribeDBInstancesForDmsResponseBody(TeaModel):
    def __init__(self, code=None, count=None, http_status_code=None, instances=None, message=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.count = count  # type: long
        self.http_status_code = http_status_code  # type: int
        self.instances = instances  # type: list[DescribeDBInstancesForDmsResponseBodyInstances]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesForDmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
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
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeDBInstancesForDmsResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBInstancesForDmsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDBInstancesForDmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDBInstancesForDmsResponse, self).to_map()
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
            temp_model = DescribeDBInstancesForDmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSecurityIpsRequest(TeaModel):
    def __init__(self, ali_uid=None, group_name=None, instance_id=None, owner_id=None, while_list=None):
        self.ali_uid = ali_uid  # type: long
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.while_list = while_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSecurityIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.while_list is not None:
            result['WhileList'] = self.while_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('WhileList') is not None:
            self.while_list = m.get('WhileList')
        return self


class ModifyDBInstanceSecurityIpsResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDBInstanceSecurityIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDBInstanceSecurityIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDBInstanceSecurityIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDBInstanceSecurityIpsResponse, self).to_map()
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
            temp_model = ModifyDBInstanceSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


