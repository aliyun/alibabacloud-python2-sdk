# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddHDMInstanceRequest(TeaModel):
    def __init__(self, engine=None, flush_account=None, instance_alias=None, instance_area=None, instance_id=None,
                 ip=None, network_type=None, password=None, port=None, region=None, username=None, vpc_id=None,
                 context=None):
        self.engine = engine  # type: str
        self.flush_account = flush_account  # type: str
        self.instance_alias = instance_alias  # type: str
        self.instance_area = instance_area  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: str
        self.network_type = network_type  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.region = region  # type: str
        self.username = username  # type: str
        self.vpc_id = vpc_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddHDMInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.flush_account is not None:
            result['FlushAccount'] = self.flush_account
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('FlushAccount') is not None:
            self.flush_account = m.get('FlushAccount')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class AddHDMInstanceResponseBodyData(TeaModel):
    def __init__(self, caller_uid=None, code=None, error=None, instance_id=None, ip=None, owner_id=None, port=None,
                 role=None, tenant_id=None, token=None, uuid=None, vpc_id=None):
        self.caller_uid = caller_uid  # type: str
        self.code = code  # type: int
        self.error = error  # type: str
        self.instance_id = instance_id  # type: str
        self.ip = ip  # type: str
        self.owner_id = owner_id  # type: str
        self.port = port  # type: int
        self.role = role  # type: str
        self.tenant_id = tenant_id  # type: str
        self.token = token  # type: str
        self.uuid = uuid  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddHDMInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.code is not None:
            result['Code'] = self.code
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.token is not None:
            result['Token'] = self.token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class AddHDMInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: AddHDMInstanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddHDMInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddHDMInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class AddHDMInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddHDMInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddHDMInstanceResponse, self).to_map()
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
            temp_model = AddHDMInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAdamBenchTaskRequest(TeaModel):
    def __init__(self, description=None, dst_instance_id=None, dst_super_account=None, dst_super_password=None,
                 rate=None, request_duration=None, request_start_time=None, src_engine=None, src_engine_version=None,
                 src_max_qps=None, src_mean_qps=None, src_sql_oss_addr=None):
        self.description = description  # type: str
        self.dst_instance_id = dst_instance_id  # type: str
        self.dst_super_account = dst_super_account  # type: str
        self.dst_super_password = dst_super_password  # type: str
        self.rate = rate  # type: int
        self.request_duration = request_duration  # type: long
        self.request_start_time = request_start_time  # type: long
        self.src_engine = src_engine  # type: str
        self.src_engine_version = src_engine_version  # type: str
        self.src_max_qps = src_max_qps  # type: float
        self.src_mean_qps = src_mean_qps  # type: float
        self.src_sql_oss_addr = src_sql_oss_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAdamBenchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id
        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account
        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time
        if self.src_engine is not None:
            result['SrcEngine'] = self.src_engine
        if self.src_engine_version is not None:
            result['SrcEngineVersion'] = self.src_engine_version
        if self.src_max_qps is not None:
            result['SrcMaxQps'] = self.src_max_qps
        if self.src_mean_qps is not None:
            result['SrcMeanQps'] = self.src_mean_qps
        if self.src_sql_oss_addr is not None:
            result['SrcSqlOssAddr'] = self.src_sql_oss_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')
        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')
        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')
        if m.get('SrcEngine') is not None:
            self.src_engine = m.get('SrcEngine')
        if m.get('SrcEngineVersion') is not None:
            self.src_engine_version = m.get('SrcEngineVersion')
        if m.get('SrcMaxQps') is not None:
            self.src_max_qps = m.get('SrcMaxQps')
        if m.get('SrcMeanQps') is not None:
            self.src_mean_qps = m.get('SrcMeanQps')
        if m.get('SrcSqlOssAddr') is not None:
            self.src_sql_oss_addr = m.get('SrcSqlOssAddr')
        return self


class CreateAdamBenchTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAdamBenchTaskResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAdamBenchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAdamBenchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAdamBenchTaskResponse, self).to_map()
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
            temp_model = CreateAdamBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCacheAnalysisJobRequest(TeaModel):
    def __init__(self, backup_set_id=None, instance_id=None, node_id=None):
        self.backup_set_id = backup_set_id  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCacheAnalysisJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(self, bytes=None, count=None, db=None, encoding=None, expiration_time_millis=None, key=None,
                 node_id=None, type=None):
        self.bytes = bytes  # type: long
        self.count = count  # type: long
        self.db = db  # type: int
        self.encoding = encoding  # type: str
        self.expiration_time_millis = expiration_time_millis  # type: long
        self.key = key  # type: str
        self.node_id = node_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeys(TeaModel):
    def __init__(self, key_info=None):
        self.key_info = key_info  # type: list[CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo]

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateCacheAnalysisJobResponseBodyDataBigKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class CreateCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(self, big_keys=None, instance_id=None, job_id=None, message=None, node_id=None, task_state=None):
        self.big_keys = big_keys  # type: CreateCacheAnalysisJobResponseBodyDataBigKeys
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: str
        self.message = message  # type: str
        self.node_id = node_id  # type: str
        self.task_state = task_state  # type: str

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super(CreateCacheAnalysisJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class CreateCacheAnalysisJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateCacheAnalysisJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateCacheAnalysisJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCacheAnalysisJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCacheAnalysisJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCacheAnalysisJobResponse, self).to_map()
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
            temp_model = CreateCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudBenchTasksRequest(TeaModel):
    def __init__(self, amount=None, backup_id=None, backup_time=None, client_type=None, description=None,
                 dst_connection_string=None, dst_instance_id=None, dst_port=None, dst_super_account=None, dst_super_password=None,
                 dst_type=None, dts_job_class=None, dts_job_id=None, end_state=None, gateway_vpc_id=None,
                 gateway_vpc_ip=None, rate=None, request_duration=None, request_end_time=None, request_start_time=None,
                 smart_pressure_time=None, src_instance_id=None, src_public_ip=None, src_super_account=None, src_super_password=None,
                 task_type=None, work_dir=None):
        self.amount = amount  # type: str
        self.backup_id = backup_id  # type: str
        self.backup_time = backup_time  # type: str
        self.client_type = client_type  # type: str
        self.description = description  # type: str
        self.dst_connection_string = dst_connection_string  # type: str
        self.dst_instance_id = dst_instance_id  # type: str
        self.dst_port = dst_port  # type: str
        self.dst_super_account = dst_super_account  # type: str
        self.dst_super_password = dst_super_password  # type: str
        self.dst_type = dst_type  # type: str
        self.dts_job_class = dts_job_class  # type: str
        self.dts_job_id = dts_job_id  # type: str
        self.end_state = end_state  # type: str
        self.gateway_vpc_id = gateway_vpc_id  # type: str
        self.gateway_vpc_ip = gateway_vpc_ip  # type: str
        self.rate = rate  # type: str
        self.request_duration = request_duration  # type: str
        self.request_end_time = request_end_time  # type: str
        self.request_start_time = request_start_time  # type: str
        self.smart_pressure_time = smart_pressure_time  # type: str
        self.src_instance_id = src_instance_id  # type: str
        self.src_public_ip = src_public_ip  # type: str
        self.src_super_account = src_super_account  # type: str
        self.src_super_password = src_super_password  # type: str
        self.task_type = task_type  # type: str
        self.work_dir = work_dir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCloudBenchTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_connection_string is not None:
            result['DstConnectionString'] = self.dst_connection_string
        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account
        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.gateway_vpc_id is not None:
            result['GatewayVpcId'] = self.gateway_vpc_id
        if self.gateway_vpc_ip is not None:
            result['GatewayVpcIp'] = self.gateway_vpc_ip
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.request_end_time is not None:
            result['RequestEndTime'] = self.request_end_time
        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.src_instance_id is not None:
            result['SrcInstanceId'] = self.src_instance_id
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.src_super_account is not None:
            result['SrcSuperAccount'] = self.src_super_account
        if self.src_super_password is not None:
            result['SrcSuperPassword'] = self.src_super_password
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstConnectionString') is not None:
            self.dst_connection_string = m.get('DstConnectionString')
        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')
        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('GatewayVpcId') is not None:
            self.gateway_vpc_id = m.get('GatewayVpcId')
        if m.get('GatewayVpcIp') is not None:
            self.gateway_vpc_ip = m.get('GatewayVpcIp')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('RequestEndTime') is not None:
            self.request_end_time = m.get('RequestEndTime')
        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('SrcInstanceId') is not None:
            self.src_instance_id = m.get('SrcInstanceId')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('SrcSuperAccount') is not None:
            self.src_super_account = m.get('SrcSuperAccount')
        if m.get('SrcSuperPassword') is not None:
            self.src_super_password = m.get('SrcSuperPassword')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class CreateCloudBenchTasksResponseBodyData(TeaModel):
    def __init__(self, task_ids=None):
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCloudBenchTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class CreateCloudBenchTasksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateCloudBenchTasksResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateCloudBenchTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = CreateCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCloudBenchTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCloudBenchTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCloudBenchTasksResponse, self).to_map()
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
            temp_model = CreateCloudBenchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiagnosticReportRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDiagnosticReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateDiagnosticReportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDiagnosticReportResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDiagnosticReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDiagnosticReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDiagnosticReportResponse, self).to_map()
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
            temp_model = CreateDiagnosticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRequestDiagnosisRequest(TeaModel):
    def __init__(self, database=None, instance_id=None, node_id=None, sql=None):
        self.database = database  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.sql = sql  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRequestDiagnosisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sql is not None:
            result['Sql'] = self.sql
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        return self


class CreateRequestDiagnosisResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRequestDiagnosisResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRequestDiagnosisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRequestDiagnosisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRequestDiagnosisResponse, self).to_map()
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
            temp_model = CreateRequestDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCloudBenchTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCloudBenchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteCloudBenchTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCloudBenchTaskResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCloudBenchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCloudBenchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCloudBenchTaskResponse, self).to_map()
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
            temp_model = DeleteCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobRequest(TeaModel):
    def __init__(self, instance_id=None, job_id=None):
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(self, bytes=None, count=None, db=None, encoding=None, expiration_time_millis=None, key=None,
                 node_id=None, type=None):
        self.bytes = bytes  # type: long
        self.count = count  # type: long
        self.db = db  # type: int
        self.encoding = encoding  # type: str
        self.expiration_time_millis = expiration_time_millis  # type: long
        self.key = key  # type: str
        self.node_id = node_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobResponseBodyDataBigKeys(TeaModel):
    def __init__(self, key_info=None):
        self.key_info = key_info  # type: list[DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo]

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponseBodyDataBigKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix(TeaModel):
    def __init__(self, bytes=None, count=None, key_num=None, prefix=None, type=None):
        self.bytes = bytes  # type: long
        self.count = count  # type: long
        self.key_num = key_num  # type: long
        self.prefix = prefix  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.key_num is not None:
            result['KeyNum'] = self.key_num
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes(TeaModel):
    def __init__(self, prefix=None):
        self.prefix = prefix  # type: list[DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix]

    def validate(self):
        if self.prefix:
            for k in self.prefix:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prefix'] = []
        if self.prefix is not None:
            for k in self.prefix:
                result['Prefix'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prefix = []
        if m.get('Prefix') is not None:
            for k in m.get('Prefix'):
                temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix()
                self.prefix.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(self, big_keys=None, instance_id=None, job_id=None, key_prefixes=None, message=None, node_id=None,
                 task_state=None):
        self.big_keys = big_keys  # type: DescribeCacheAnalysisJobResponseBodyDataBigKeys
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: str
        self.key_prefixes = key_prefixes  # type: DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes
        self.message = message  # type: str
        self.node_id = node_id  # type: str
        self.task_state = task_state  # type: str

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.key_prefixes:
            self.key_prefixes.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.key_prefixes is not None:
            result['KeyPrefixes'] = self.key_prefixes.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('KeyPrefixes') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes()
            self.key_prefixes = temp_model.from_map(m['KeyPrefixes'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class DescribeCacheAnalysisJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCacheAnalysisJobResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCacheAnalysisJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobResponse, self).to_map()
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
            temp_model = DescribeCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobsRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, page_no=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo(TeaModel):
    def __init__(self, bytes=None, count=None, db=None, encoding=None, expiration_time_millis=None, key=None,
                 node_id=None, type=None):
        self.bytes = bytes  # type: long
        self.count = count  # type: long
        self.db = db  # type: int
        self.encoding = encoding  # type: str
        self.expiration_time_millis = expiration_time_millis  # type: long
        self.key = key  # type: str
        self.node_id = node_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys(TeaModel):
    def __init__(self, key_info=None):
        self.key_info = key_info  # type: list[DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo]

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob(TeaModel):
    def __init__(self, big_keys=None, instance_id=None, job_id=None, message=None, node_id=None, task_state=None):
        self.big_keys = big_keys  # type: DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: str
        self.message = message  # type: str
        self.node_id = node_id  # type: str
        self.task_state = task_state  # type: str

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataList(TeaModel):
    def __init__(self, cache_analysis_job=None):
        self.cache_analysis_job = cache_analysis_job  # type: list[DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob]

    def validate(self):
        if self.cache_analysis_job:
            for k in self.cache_analysis_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CacheAnalysisJob'] = []
        if self.cache_analysis_job is not None:
            for k in self.cache_analysis_job:
                result['CacheAnalysisJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cache_analysis_job = []
        if m.get('CacheAnalysisJob') is not None:
            for k in m.get('CacheAnalysisJob'):
                temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob()
                self.cache_analysis_job.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: DescribeCacheAnalysisJobsResponseBodyDataList
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCacheAnalysisJobsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCacheAnalysisJobsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCacheAnalysisJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCacheAnalysisJobsResponse, self).to_map()
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
            temp_model = DescribeCacheAnalysisJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudBenchTasksRequest(TeaModel):
    def __init__(self, end_time=None, page_no=None, page_size=None, start_time=None, status=None, task_type=None):
        self.end_time = end_time  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudBenchTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks(TeaModel):
    def __init__(self, archive_job_id=None, archive_oss_table_name=None, archive_state=None, backup_id=None,
                 backup_type=None, bench_step=None, bench_step_status=None, client_gateway_id=None, client_type=None,
                 description=None, dst_instance_uuid=None, dst_ip=None, dst_port=None, dst_type=None, dts_job_class=None,
                 dts_job_id=None, dts_job_name=None, dts_job_state=None, dts_job_status=None, ecs_instance_id=None,
                 end_state=None, error_code=None, error_message=None, external=None, rate=None, request_duration=None,
                 smart_pressure_time=None, source=None, sql_complete_reuse=None, src_instance_area=None, src_instance_uuid=None,
                 src_public_ip=None, state=None, status=None, table_schema=None, task_id=None, task_type=None, topic=None,
                 user_id=None, version=None, work_dir=None):
        self.archive_job_id = archive_job_id  # type: str
        self.archive_oss_table_name = archive_oss_table_name  # type: str
        self.archive_state = archive_state  # type: int
        self.backup_id = backup_id  # type: str
        self.backup_type = backup_type  # type: str
        self.bench_step = bench_step  # type: str
        self.bench_step_status = bench_step_status  # type: str
        self.client_gateway_id = client_gateway_id  # type: str
        self.client_type = client_type  # type: str
        self.description = description  # type: str
        self.dst_instance_uuid = dst_instance_uuid  # type: str
        self.dst_ip = dst_ip  # type: str
        self.dst_port = dst_port  # type: int
        self.dst_type = dst_type  # type: str
        self.dts_job_class = dts_job_class  # type: str
        self.dts_job_id = dts_job_id  # type: str
        self.dts_job_name = dts_job_name  # type: str
        self.dts_job_state = dts_job_state  # type: int
        self.dts_job_status = dts_job_status  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.end_state = end_state  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.external = external  # type: str
        self.rate = rate  # type: int
        self.request_duration = request_duration  # type: long
        self.smart_pressure_time = smart_pressure_time  # type: int
        self.source = source  # type: str
        self.sql_complete_reuse = sql_complete_reuse  # type: str
        self.src_instance_area = src_instance_area  # type: str
        self.src_instance_uuid = src_instance_uuid  # type: str
        self.src_public_ip = src_public_ip  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.table_schema = table_schema  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.topic = topic  # type: str
        self.user_id = user_id  # type: str
        self.version = version  # type: str
        self.work_dir = work_dir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id
        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name
        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step
        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status
        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state
        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.external is not None:
            result['External'] = self.external
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse
        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area
        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')
        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')
        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')
        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')
        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')
        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')
        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')
        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudBenchTasksResponseBodyDataList(TeaModel):
    def __init__(self, cloudbench_tasks=None):
        self.cloudbench_tasks = cloudbench_tasks  # type: list[DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks]

    def validate(self):
        if self.cloudbench_tasks:
            for k in self.cloudbench_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCloudBenchTasksResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cloudbenchTasks'] = []
        if self.cloudbench_tasks is not None:
            for k in self.cloudbench_tasks:
                result['cloudbenchTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cloudbench_tasks = []
        if m.get('cloudbenchTasks') is not None:
            for k in m.get('cloudbenchTasks'):
                temp_model = DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks()
                self.cloudbench_tasks.append(temp_model.from_map(k))
        return self


class DescribeCloudBenchTasksResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: DescribeCloudBenchTasksResponseBodyDataList
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super(DescribeCloudBenchTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = DescribeCloudBenchTasksResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCloudBenchTasksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCloudBenchTasksResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudBenchTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudBenchTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCloudBenchTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudBenchTasksResponse, self).to_map()
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
            temp_model = DescribeCloudBenchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudbenchTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudbenchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeCloudbenchTaskResponseBodyData(TeaModel):
    def __init__(self, archive_job_id=None, archive_oss_table_name=None, archive_state=None, backup_id=None,
                 backup_type=None, bench_step=None, bench_step_status=None, client_gateway_id=None, client_type=None,
                 description=None, dst_instance_uuid=None, dst_ip=None, dst_port=None, dst_type=None, dts_job_class=None,
                 dts_job_id=None, dts_job_name=None, dts_job_state=None, dts_job_status=None, ecs_instance_id=None,
                 end_state=None, error_code=None, error_message=None, external=None, rate=None, request_duration=None,
                 smart_pressure_time=None, source=None, sql_complete_reuse=None, src_instance_area=None, src_instance_uuid=None,
                 src_public_ip=None, state=None, status=None, table_schema=None, task_id=None, task_type=None, topic=None,
                 user_id=None, version=None, work_dir=None):
        self.archive_job_id = archive_job_id  # type: str
        self.archive_oss_table_name = archive_oss_table_name  # type: str
        self.archive_state = archive_state  # type: int
        self.backup_id = backup_id  # type: str
        self.backup_type = backup_type  # type: str
        self.bench_step = bench_step  # type: str
        self.bench_step_status = bench_step_status  # type: str
        self.client_gateway_id = client_gateway_id  # type: str
        self.client_type = client_type  # type: str
        self.description = description  # type: str
        self.dst_instance_uuid = dst_instance_uuid  # type: str
        self.dst_ip = dst_ip  # type: str
        self.dst_port = dst_port  # type: int
        self.dst_type = dst_type  # type: str
        self.dts_job_class = dts_job_class  # type: str
        self.dts_job_id = dts_job_id  # type: str
        self.dts_job_name = dts_job_name  # type: str
        self.dts_job_state = dts_job_state  # type: int
        self.dts_job_status = dts_job_status  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.end_state = end_state  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.external = external  # type: str
        self.rate = rate  # type: long
        self.request_duration = request_duration  # type: long
        self.smart_pressure_time = smart_pressure_time  # type: int
        self.source = source  # type: str
        self.sql_complete_reuse = sql_complete_reuse  # type: str
        self.src_instance_area = src_instance_area  # type: str
        self.src_instance_uuid = src_instance_uuid  # type: str
        self.src_public_ip = src_public_ip  # type: str
        self.state = state  # type: str
        self.status = status  # type: str
        self.table_schema = table_schema  # type: str
        self.task_id = task_id  # type: str
        self.task_type = task_type  # type: str
        self.topic = topic  # type: str
        self.user_id = user_id  # type: str
        self.version = version  # type: str
        self.work_dir = work_dir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudbenchTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id
        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name
        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step
        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status
        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state
        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.external is not None:
            result['External'] = self.external
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse
        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area
        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')
        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')
        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')
        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')
        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')
        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')
        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')
        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudbenchTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCloudbenchTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudbenchTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeCloudbenchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudbenchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCloudbenchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudbenchTaskResponse, self).to_map()
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
            temp_model = DescribeCloudbenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudbenchTaskConfigRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudbenchTaskConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeCloudbenchTaskConfigResponseBodyData(TeaModel):
    def __init__(self, archive_folder=None, bench_cmd=None, client_jar_path=None, jar_on_oss=None, load_cmd=None,
                 meta_file_name=None, meta_file_on_oss=None, meta_file_path=None, parse_cmd=None, parse_file_path=None,
                 rocks_db_path=None, sql_file_name=None, sql_file_on_oss=None, sql_file_path=None, task_id=None, user_id=None,
                 work_dir=None):
        self.archive_folder = archive_folder  # type: str
        self.bench_cmd = bench_cmd  # type: str
        self.client_jar_path = client_jar_path  # type: str
        self.jar_on_oss = jar_on_oss  # type: str
        self.load_cmd = load_cmd  # type: str
        self.meta_file_name = meta_file_name  # type: str
        self.meta_file_on_oss = meta_file_on_oss  # type: str
        self.meta_file_path = meta_file_path  # type: str
        self.parse_cmd = parse_cmd  # type: str
        self.parse_file_path = parse_file_path  # type: str
        self.rocks_db_path = rocks_db_path  # type: str
        self.sql_file_name = sql_file_name  # type: str
        self.sql_file_on_oss = sql_file_on_oss  # type: str
        self.sql_file_path = sql_file_path  # type: str
        self.task_id = task_id  # type: str
        self.user_id = user_id  # type: str
        self.work_dir = work_dir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCloudbenchTaskConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_folder is not None:
            result['ArchiveFolder'] = self.archive_folder
        if self.bench_cmd is not None:
            result['BenchCmd'] = self.bench_cmd
        if self.client_jar_path is not None:
            result['ClientJarPath'] = self.client_jar_path
        if self.jar_on_oss is not None:
            result['JarOnOss'] = self.jar_on_oss
        if self.load_cmd is not None:
            result['LoadCmd'] = self.load_cmd
        if self.meta_file_name is not None:
            result['MetaFileName'] = self.meta_file_name
        if self.meta_file_on_oss is not None:
            result['MetaFileOnOss'] = self.meta_file_on_oss
        if self.meta_file_path is not None:
            result['MetaFilePath'] = self.meta_file_path
        if self.parse_cmd is not None:
            result['ParseCmd'] = self.parse_cmd
        if self.parse_file_path is not None:
            result['ParseFilePath'] = self.parse_file_path
        if self.rocks_db_path is not None:
            result['RocksDbPath'] = self.rocks_db_path
        if self.sql_file_name is not None:
            result['SqlFileName'] = self.sql_file_name
        if self.sql_file_on_oss is not None:
            result['SqlFileOnOss'] = self.sql_file_on_oss
        if self.sql_file_path is not None:
            result['SqlFilePath'] = self.sql_file_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArchiveFolder') is not None:
            self.archive_folder = m.get('ArchiveFolder')
        if m.get('BenchCmd') is not None:
            self.bench_cmd = m.get('BenchCmd')
        if m.get('ClientJarPath') is not None:
            self.client_jar_path = m.get('ClientJarPath')
        if m.get('JarOnOss') is not None:
            self.jar_on_oss = m.get('JarOnOss')
        if m.get('LoadCmd') is not None:
            self.load_cmd = m.get('LoadCmd')
        if m.get('MetaFileName') is not None:
            self.meta_file_name = m.get('MetaFileName')
        if m.get('MetaFileOnOss') is not None:
            self.meta_file_on_oss = m.get('MetaFileOnOss')
        if m.get('MetaFilePath') is not None:
            self.meta_file_path = m.get('MetaFilePath')
        if m.get('ParseCmd') is not None:
            self.parse_cmd = m.get('ParseCmd')
        if m.get('ParseFilePath') is not None:
            self.parse_file_path = m.get('ParseFilePath')
        if m.get('RocksDbPath') is not None:
            self.rocks_db_path = m.get('RocksDbPath')
        if m.get('SqlFileName') is not None:
            self.sql_file_name = m.get('SqlFileName')
        if m.get('SqlFileOnOss') is not None:
            self.sql_file_on_oss = m.get('SqlFileOnOss')
        if m.get('SqlFilePath') is not None:
            self.sql_file_path = m.get('SqlFilePath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudbenchTaskConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeCloudbenchTaskConfigResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeCloudbenchTaskConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeCloudbenchTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudbenchTaskConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCloudbenchTaskConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCloudbenchTaskConfigResponse, self).to_map()
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
            temp_model = DescribeCloudbenchTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosticReportListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, end_time=None, page_no=None, page_size=None, start_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.end_time = end_time  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosticReportListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDiagnosticReportListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiagnosticReportListResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DescribeDiagnosticReportListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDiagnosticReportListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiagnosticReportListResponse, self).to_map()
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
            temp_model = DescribeDiagnosticReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHotBigKeysRequest(TeaModel):
    def __init__(self, console_context=None, instance_id=None, node_id=None):
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHotBigKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotBigKeysResponseBodyDataBigKeysBigKey(TeaModel):
    def __init__(self, db=None, key=None, key_type=None, node_id=None, size=None):
        self.db = db  # type: int
        self.key = key  # type: str
        self.key_type = key_type  # type: str
        self.node_id = node_id  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHotBigKeysResponseBodyDataBigKeysBigKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeHotBigKeysResponseBodyDataBigKeys(TeaModel):
    def __init__(self, big_key=None):
        self.big_key = big_key  # type: list[DescribeHotBigKeysResponseBodyDataBigKeysBigKey]

    def validate(self):
        if self.big_key:
            for k in self.big_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHotBigKeysResponseBodyDataBigKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BigKey'] = []
        if self.big_key is not None:
            for k in self.big_key:
                result['BigKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k in m.get('BigKey'):
                temp_model = DescribeHotBigKeysResponseBodyDataBigKeysBigKey()
                self.big_key.append(temp_model.from_map(k))
        return self


class DescribeHotBigKeysResponseBodyDataHotKeysHotKey(TeaModel):
    def __init__(self, db=None, hot=None, key=None, key_type=None, lfu=None, node_id=None):
        self.db = db  # type: int
        self.hot = hot  # type: str
        self.key = key  # type: str
        self.key_type = key_type  # type: str
        self.lfu = lfu  # type: int
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHotBigKeysResponseBodyDataHotKeysHotKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.lfu is not None:
            result['Lfu'] = self.lfu
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotBigKeysResponseBodyDataHotKeys(TeaModel):
    def __init__(self, hot_key=None):
        self.hot_key = hot_key  # type: list[DescribeHotBigKeysResponseBodyDataHotKeysHotKey]

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHotBigKeysResponseBodyDataHotKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeHotBigKeysResponseBodyDataHotKeysHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeHotBigKeysResponseBodyData(TeaModel):
    def __init__(self, big_key_msg=None, big_keys=None, hot_key_msg=None, hot_keys=None):
        self.big_key_msg = big_key_msg  # type: str
        self.big_keys = big_keys  # type: DescribeHotBigKeysResponseBodyDataBigKeys
        self.hot_key_msg = hot_key_msg  # type: str
        self.hot_keys = hot_keys  # type: DescribeHotBigKeysResponseBodyDataHotKeys

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.hot_keys:
            self.hot_keys.validate()

    def to_map(self):
        _map = super(DescribeHotBigKeysResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_key_msg is not None:
            result['BigKeyMsg'] = self.big_key_msg
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.hot_key_msg is not None:
            result['HotKeyMsg'] = self.hot_key_msg
        if self.hot_keys is not None:
            result['HotKeys'] = self.hot_keys.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BigKeyMsg') is not None:
            self.big_key_msg = m.get('BigKeyMsg')
        if m.get('BigKeys') is not None:
            temp_model = DescribeHotBigKeysResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('HotKeyMsg') is not None:
            self.hot_key_msg = m.get('HotKeyMsg')
        if m.get('HotKeys') is not None:
            temp_model = DescribeHotBigKeysResponseBodyDataHotKeys()
            self.hot_keys = temp_model.from_map(m['HotKeys'])
        return self


class DescribeHotBigKeysResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeHotBigKeysResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeHotBigKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeHotBigKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotBigKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHotBigKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHotBigKeysResponse, self).to_map()
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
            temp_model = DescribeHotBigKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHotKeysRequest(TeaModel):
    def __init__(self, instance_id=None, node_id=None):
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHotKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotKeysResponseBodyDataHotKey(TeaModel):
    def __init__(self, db=None, hot=None, key=None, key_type=None, size=None):
        self.db = db  # type: int
        self.hot = hot  # type: str
        self.key = key  # type: str
        self.key_type = key_type  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHotKeysResponseBodyDataHotKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeHotKeysResponseBodyData(TeaModel):
    def __init__(self, hot_key=None):
        self.hot_key = hot_key  # type: list[DescribeHotKeysResponseBodyDataHotKey]

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHotKeysResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeHotKeysResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeHotKeysResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeHotKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHotKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHotKeysResponse, self).to_map()
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
            temp_model = DescribeHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopBigKeysRequest(TeaModel):
    def __init__(self, console_context=None, end_time=None, instance_id=None, node_id=None, start_time=None):
        self.console_context = console_context  # type: str
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopBigKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopBigKeysResponseBodyDataBigKey(TeaModel):
    def __init__(self, db=None, key=None, key_type=None, node_id=None, size=None):
        self.db = db  # type: int
        self.key = key  # type: str
        self.key_type = key_type  # type: str
        self.node_id = node_id  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopBigKeysResponseBodyDataBigKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeTopBigKeysResponseBodyData(TeaModel):
    def __init__(self, big_key=None):
        self.big_key = big_key  # type: list[DescribeTopBigKeysResponseBodyDataBigKey]

    def validate(self):
        if self.big_key:
            for k in self.big_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTopBigKeysResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BigKey'] = []
        if self.big_key is not None:
            for k in self.big_key:
                result['BigKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k in m.get('BigKey'):
                temp_model = DescribeTopBigKeysResponseBodyDataBigKey()
                self.big_key.append(temp_model.from_map(k))
        return self


class DescribeTopBigKeysResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeTopBigKeysResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeTopBigKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeTopBigKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTopBigKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTopBigKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTopBigKeysResponse, self).to_map()
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
            temp_model = DescribeTopBigKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopHotKeysRequest(TeaModel):
    def __init__(self, console_context=None, end_time=None, instance_id=None, node_id=None, start_time=None):
        self.console_context = console_context  # type: str
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopHotKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopHotKeysResponseBodyDataHotKey(TeaModel):
    def __init__(self, db=None, hot=None, key=None, key_type=None, lfu=None, node_id=None):
        self.db = db  # type: int
        self.hot = hot  # type: str
        self.key = key  # type: str
        self.key_type = key_type  # type: str
        self.lfu = lfu  # type: int
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTopHotKeysResponseBodyDataHotKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.lfu is not None:
            result['Lfu'] = self.lfu
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeTopHotKeysResponseBodyData(TeaModel):
    def __init__(self, hot_key=None):
        self.hot_key = hot_key  # type: list[DescribeTopHotKeysResponseBodyDataHotKey]

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTopHotKeysResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeTopHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeTopHotKeysResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeTopHotKeysResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeTopHotKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DescribeTopHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTopHotKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTopHotKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTopHotKeysResponse, self).to_map()
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
            temp_model = DescribeTopHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAllSqlConcurrencyControlRulesRequest(TeaModel):
    def __init__(self, console_context=None, instance_id=None):
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAllSqlConcurrencyControlRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAllSqlConcurrencyControlRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAllSqlConcurrencyControlRulesResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableAllSqlConcurrencyControlRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableAllSqlConcurrencyControlRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAllSqlConcurrencyControlRulesResponse, self).to_map()
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
            temp_model = DisableAllSqlConcurrencyControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSqlConcurrencyControlRequest(TeaModel):
    def __init__(self, console_context=None, instance_id=None, item_id=None):
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str
        self.item_id = item_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSqlConcurrencyControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class DisableSqlConcurrencyControlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSqlConcurrencyControlResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableSqlConcurrencyControlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableSqlConcurrencyControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableSqlConcurrencyControlResponse, self).to_map()
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
            temp_model = DisableSqlConcurrencyControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSqlConcurrencyControlRequest(TeaModel):
    def __init__(self, concurrency_control_time=None, console_context=None, instance_id=None, max_concurrency=None,
                 sql_keywords=None, sql_type=None):
        self.concurrency_control_time = concurrency_control_time  # type: long
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str
        self.max_concurrency = max_concurrency  # type: long
        self.sql_keywords = sql_keywords  # type: str
        self.sql_type = sql_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSqlConcurrencyControlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class EnableSqlConcurrencyControlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSqlConcurrencyControlResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableSqlConcurrencyControlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableSqlConcurrencyControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableSqlConcurrencyControlResponse, self).to_map()
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
            temp_model = EnableSqlConcurrencyControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncErrorRequestListByCodeRequest(TeaModel):
    def __init__(self, console_context=None, end=None, error_code=None, instance_id=None, node_id=None, start=None):
        self.console_context = console_context  # type: str
        self.end = end  # type: str
        self.error_code = error_code  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncErrorRequestListByCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end is not None:
            result['End'] = self.end
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetAsyncErrorRequestListByCodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncErrorRequestListByCodeResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncErrorRequestListByCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsyncErrorRequestListByCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncErrorRequestListByCodeResponse, self).to_map()
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
            temp_model = GetAsyncErrorRequestListByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncErrorRequestStatByCodeRequest(TeaModel):
    def __init__(self, console_context=None, db_name=None, end=None, instance_id=None, node_id=None, role=None,
                 start=None):
        self.console_context = console_context  # type: str
        self.db_name = db_name  # type: str
        self.end = end  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.role = role  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncErrorRequestStatByCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.role is not None:
            result['Role'] = self.role
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetAsyncErrorRequestStatByCodeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncErrorRequestStatByCodeResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncErrorRequestStatByCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsyncErrorRequestStatByCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncErrorRequestStatByCodeResponse, self).to_map()
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
            temp_model = GetAsyncErrorRequestStatByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncErrorRequestStatResultRequest(TeaModel):
    def __init__(self, console_context=None, db_name=None, end=None, instance_id=None, node_id=None, role=None,
                 sql_id_list=None, start=None):
        self.console_context = console_context  # type: str
        self.db_name = db_name  # type: str
        self.end = end  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.role = role  # type: str
        self.sql_id_list = sql_id_list  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncErrorRequestStatResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.role is not None:
            result['Role'] = self.role
        if self.sql_id_list is not None:
            result['SqlIdList'] = self.sql_id_list
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SqlIdList') is not None:
            self.sql_id_list = m.get('SqlIdList')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetAsyncErrorRequestStatResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncErrorRequestStatResultResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncErrorRequestStatResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAsyncErrorRequestStatResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncErrorRequestStatResultResponse, self).to_map()
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
            temp_model = GetAsyncErrorRequestStatResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoResourceOptimizeConfigRequest(TeaModel):
    def __init__(self, access_key=None, instance_id=None, signature=None, uid=None, user_id=None, context=None):
        self.access_key = access_key  # type: str
        self.instance_id = instance_id  # type: str
        self.signature = signature  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoResourceOptimizeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutoResourceOptimizeConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoResourceOptimizeConfigResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetAutoResourceOptimizeConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAutoResourceOptimizeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAutoResourceOptimizeConfigResponse, self).to_map()
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
            temp_model = GetAutoResourceOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventContentRequest(TeaModel):
    def __init__(self, instance_id=None, span_id=None, context=None):
        self.instance_id = instance_id  # type: str
        self.span_id = span_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutonomousNotifyEventContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventContentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutonomousNotifyEventContentResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventContentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAutonomousNotifyEventContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAutonomousNotifyEventContentResponse, self).to_map()
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
            temp_model = GetAutonomousNotifyEventContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventsInRangeRequest(TeaModel):
    def __init__(self, end_time=None, event_context=None, instance_id=None, level=None, min_level=None, node_id=None,
                 page_offset=None, page_size=None, start_time=None, context=None):
        self.end_time = end_time  # type: str
        self.event_context = event_context  # type: str
        self.instance_id = instance_id  # type: str
        self.level = level  # type: str
        self.min_level = min_level  # type: str
        self.node_id = node_id  # type: str
        self.page_offset = page_offset  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutonomousNotifyEventsInRangeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventsInRangeResponseBodyDataList(TeaModel):
    def __init__(self, t=None):
        self.t = t  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutonomousNotifyEventsInRangeResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.t is not None:
            result['T'] = self.t
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('T') is not None:
            self.t = m.get('T')
        return self


class GetAutonomousNotifyEventsInRangeResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: GetAutonomousNotifyEventsInRangeResponseBodyDataList
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super(GetAutonomousNotifyEventsInRangeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAutonomousNotifyEventsInRangeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetAutonomousNotifyEventsInRangeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAutonomousNotifyEventsInRangeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventsInRangeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAutonomousNotifyEventsInRangeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAutonomousNotifyEventsInRangeResponse, self).to_map()
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
            temp_model = GetAutonomousNotifyEventsInRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEndpointSwitchTaskRequest(TeaModel):
    def __init__(self, task_id=None, uid=None, user_id=None, context=None, access_key=None, signature=None,
                 skip_auth=None, timestamp=None):
        self.task_id = task_id  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str
        self.access_key = access_key  # type: str
        self.signature = signature  # type: str
        self.skip_auth = skip_auth  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEndpointSwitchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetEndpointSwitchTaskResponseBodyData(TeaModel):
    def __init__(self, account_id=None, db_link_id=None, err_msg=None, ori_uuid=None, status=None, task_id=None,
                 uuid=None):
        self.account_id = account_id  # type: str
        self.db_link_id = db_link_id  # type: long
        self.err_msg = err_msg  # type: str
        self.ori_uuid = ori_uuid  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEndpointSwitchTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.db_link_id is not None:
            result['DbLinkId'] = self.db_link_id
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.ori_uuid is not None:
            result['OriUuid'] = self.ori_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbLinkId') is not None:
            self.db_link_id = m.get('DbLinkId')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('OriUuid') is not None:
            self.ori_uuid = m.get('OriUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEndpointSwitchTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: GetEndpointSwitchTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEndpointSwitchTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEndpointSwitchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetEndpointSwitchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEndpointSwitchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEndpointSwitchTaskResponse, self).to_map()
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
            temp_model = GetEndpointSwitchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErrorRequestSampleRequest(TeaModel):
    def __init__(self, console_context=None, db_name=None, end=None, instance_id=None, node_id=None, role=None,
                 sql_id=None, start=None):
        self.console_context = console_context  # type: str
        self.db_name = db_name  # type: str
        self.end = end  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.role = role  # type: str
        self.sql_id = sql_id  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetErrorRequestSampleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.role is not None:
            result['Role'] = self.role
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetErrorRequestSampleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetErrorRequestSampleResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetErrorRequestSampleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetErrorRequestSampleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetErrorRequestSampleResponse, self).to_map()
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
            temp_model = GetErrorRequestSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMAliyunResourceSyncResultRequest(TeaModel):
    def __init__(self, task_id=None, uid=None, user_id=None, context=None, access_key=None, signature=None,
                 skip_auth=None, timestamp=None):
        self.task_id = task_id  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str
        self.access_key = access_key  # type: str
        self.signature = signature  # type: str
        self.skip_auth = skip_auth  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHDMAliyunResourceSyncResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(self, err_msg=None, resource_type=None, success=None, sync_count=None):
        self.err_msg = err_msg  # type: str
        self.resource_type = resource_type  # type: str
        self.success = success  # type: bool
        self.sync_count = sync_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResults(TeaModel):
    def __init__(self, resource_sync_sub_result=None):
        self.resource_sync_sub_result = resource_sync_sub_result  # type: list[GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult]

    def validate(self):
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHDMAliyunResourceSyncResultResponseBodyDataSubResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k in m.get('ResourceSyncSubResult'):
                temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMAliyunResourceSyncResultResponseBodyData(TeaModel):
    def __init__(self, error_msg=None, results=None, sub_results=None, sync_status=None):
        self.error_msg = error_msg  # type: str
        self.results = results  # type: str
        self.sub_results = sub_results  # type: GetHDMAliyunResourceSyncResultResponseBodyDataSubResults
        self.sync_status = sync_status  # type: str

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super(GetHDMAliyunResourceSyncResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('SubResults') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class GetHDMAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: GetHDMAliyunResourceSyncResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHDMAliyunResourceSyncResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetHDMAliyunResourceSyncResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHDMAliyunResourceSyncResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHDMAliyunResourceSyncResultResponse, self).to_map()
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
            temp_model = GetHDMAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMLastAliyunResourceSyncResultRequest(TeaModel):
    def __init__(self, uid=None, user_id=None, context=None, access_key=None, signature=None, skip_auth=None,
                 timestamp=None):
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str
        self.access_key = access_key  # type: str
        self.signature = signature  # type: str
        self.skip_auth = skip_auth  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHDMLastAliyunResourceSyncResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(self, err_msg=None, resource_type=None, success=None, sync_count=None):
        self.err_msg = err_msg  # type: str
        self.resource_type = resource_type  # type: str
        self.success = success  # type: bool
        self.sync_count = sync_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults(TeaModel):
    def __init__(self, resource_sync_sub_result=None):
        self.resource_sync_sub_result = resource_sync_sub_result  # type: list[GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult]

    def validate(self):
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k in m.get('ResourceSyncSubResult'):
                temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyData(TeaModel):
    def __init__(self, error_msg=None, results=None, sub_results=None, sync_status=None):
        self.error_msg = error_msg  # type: str
        self.results = results  # type: str
        self.sub_results = sub_results  # type: GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults
        self.sync_status = sync_status  # type: str

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super(GetHDMLastAliyunResourceSyncResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('SubResults') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: GetHDMLastAliyunResourceSyncResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHDMLastAliyunResourceSyncResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetHDMLastAliyunResourceSyncResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHDMLastAliyunResourceSyncResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHDMLastAliyunResourceSyncResultResponse, self).to_map()
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
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceInspectionsRequest(TeaModel):
    def __init__(self, end_time=None, engine=None, instance_area=None, page_no=None, page_size=None, search_map=None,
                 start_time=None):
        self.end_time = end_time  # type: str
        self.engine = engine  # type: str
        self.instance_area = instance_area  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.search_map = search_map  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceInspectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_map is not None:
            result['SearchMap'] = self.search_map
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchMap') is not None:
            self.search_map = m.get('SearchMap')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance(TeaModel):
    def __init__(self, account_id=None, engine=None, engine_version=None, instance_area=None, instance_class=None,
                 instance_id=None, network_type=None, node_id=None, region=None, uuid=None, vpc_id=None):
        self.account_id = account_id  # type: str
        self.engine = engine  # type: str
        self.engine_version = engine_version  # type: str
        self.instance_area = instance_area  # type: str
        self.instance_class = instance_class  # type: str
        self.instance_id = instance_id  # type: str
        self.network_type = network_type  # type: str
        self.node_id = node_id  # type: str
        self.region = region  # type: str
        self.uuid = uuid  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region is not None:
            result['Region'] = self.region
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceInspectionsResponseBodyDataListBaseInspection(TeaModel):
    def __init__(self, data=None, end_time=None, gmt_create=None, instance=None, score=None, score_map=None,
                 start_time=None):
        self.data = data  # type: dict[str, any]
        self.end_time = end_time  # type: long
        self.gmt_create = gmt_create  # type: long
        self.instance = instance  # type: GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance
        self.score = score  # type: int
        self.score_map = score_map  # type: dict[str, any]
        self.start_time = start_time  # type: long

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super(GetInstanceInspectionsResponseBodyDataListBaseInspection, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.score_map is not None:
            result['ScoreMap'] = self.score_map
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Instance') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ScoreMap') is not None:
            self.score_map = m.get('ScoreMap')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInstanceInspectionsResponseBodyDataList(TeaModel):
    def __init__(self, base_inspection=None):
        self.base_inspection = base_inspection  # type: list[GetInstanceInspectionsResponseBodyDataListBaseInspection]

    def validate(self):
        if self.base_inspection:
            for k in self.base_inspection:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceInspectionsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BaseInspection'] = []
        if self.base_inspection is not None:
            for k in self.base_inspection:
                result['BaseInspection'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.base_inspection = []
        if m.get('BaseInspection') is not None:
            for k in m.get('BaseInspection'):
                temp_model = GetInstanceInspectionsResponseBodyDataListBaseInspection()
                self.base_inspection.append(temp_model.from_map(k))
        return self


class GetInstanceInspectionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total=None):
        self.list = list  # type: GetInstanceInspectionsResponseBodyDataList
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super(GetInstanceInspectionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetInstanceInspectionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetInstanceInspectionsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInstanceInspectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetInstanceInspectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceInspectionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceInspectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceInspectionsResponse, self).to_map()
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
            temp_model = GetInstanceInspectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeDataStatsRequest(TeaModel):
    def __init__(self, asc=None, db_names=None, engine=None, instance_ids=None, keywords=None, logical_operator=None,
                 only_optimized_sql=None, order_by=None, page_no=None, page_size=None, rules=None, sql_ids=None, tag_names=None,
                 time=None):
        self.asc = asc  # type: str
        self.db_names = db_names  # type: str
        self.engine = engine  # type: str
        self.instance_ids = instance_ids  # type: str
        self.keywords = keywords  # type: str
        self.logical_operator = logical_operator  # type: str
        self.only_optimized_sql = only_optimized_sql  # type: str
        self.order_by = order_by  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.rules = rules  # type: str
        self.sql_ids = sql_ids  # type: str
        self.tag_names = tag_names  # type: str
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeDataStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['Asc'] = self.asc
        if self.db_names is not None:
            result['DbNames'] = self.db_names
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator
        if self.only_optimized_sql is not None:
            result['OnlyOptimizedSql'] = self.only_optimized_sql
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.sql_ids is not None:
            result['SqlIds'] = self.sql_ids
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')
        if m.get('OnlyOptimizedSql') is not None:
            self.only_optimized_sql = m.get('OnlyOptimizedSql')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('SqlIds') is not None:
            self.sql_ids = m.get('SqlIds')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetQueryOptimizeDataStatsResponseBodyDataListRuleList(TeaModel):
    def __init__(self, name=None, type=None):
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeDataStatsResponseBodyDataListRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQueryOptimizeDataStatsResponseBodyDataList(TeaModel):
    def __init__(self, avg_lock_time=None, avg_query_time=None, avg_rows_affected=None, avg_rows_examined=None,
                 avg_rows_sent=None, count=None, dbname=None, instance_id=None, max_lock_time=None, max_query_time=None,
                 max_rows_affected=None, max_rows_examined=None, max_rows_sent=None, psql=None, rule_list=None, sql_id=None,
                 sql_sample=None, sql_type=None):
        self.avg_lock_time = avg_lock_time  # type: float
        self.avg_query_time = avg_query_time  # type: float
        self.avg_rows_affected = avg_rows_affected  # type: float
        self.avg_rows_examined = avg_rows_examined  # type: float
        self.avg_rows_sent = avg_rows_sent  # type: float
        self.count = count  # type: int
        self.dbname = dbname  # type: str
        self.instance_id = instance_id  # type: str
        self.max_lock_time = max_lock_time  # type: float
        self.max_query_time = max_query_time  # type: float
        self.max_rows_affected = max_rows_affected  # type: long
        self.max_rows_examined = max_rows_examined  # type: long
        self.max_rows_sent = max_rows_sent  # type: long
        self.psql = psql  # type: str
        self.rule_list = rule_list  # type: list[GetQueryOptimizeDataStatsResponseBodyDataListRuleList]
        self.sql_id = sql_id  # type: str
        self.sql_sample = sql_sample  # type: str
        self.sql_type = sql_type  # type: str

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataStatsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_lock_time is not None:
            result['AvgLockTime'] = self.avg_lock_time
        if self.avg_query_time is not None:
            result['AvgQueryTime'] = self.avg_query_time
        if self.avg_rows_affected is not None:
            result['AvgRowsAffected'] = self.avg_rows_affected
        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined
        if self.avg_rows_sent is not None:
            result['AvgRowsSent'] = self.avg_rows_sent
        if self.count is not None:
            result['Count'] = self.count
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time
        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time
        if self.max_rows_affected is not None:
            result['MaxRowsAffected'] = self.max_rows_affected
        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined
        if self.max_rows_sent is not None:
            result['MaxRowsSent'] = self.max_rows_sent
        if self.psql is not None:
            result['Psql'] = self.psql
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_sample is not None:
            result['SqlSample'] = self.sql_sample
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgLockTime') is not None:
            self.avg_lock_time = m.get('AvgLockTime')
        if m.get('AvgQueryTime') is not None:
            self.avg_query_time = m.get('AvgQueryTime')
        if m.get('AvgRowsAffected') is not None:
            self.avg_rows_affected = m.get('AvgRowsAffected')
        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')
        if m.get('AvgRowsSent') is not None:
            self.avg_rows_sent = m.get('AvgRowsSent')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')
        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')
        if m.get('MaxRowsAffected') is not None:
            self.max_rows_affected = m.get('MaxRowsAffected')
        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')
        if m.get('MaxRowsSent') is not None:
            self.max_rows_sent = m.get('MaxRowsSent')
        if m.get('Psql') is not None:
            self.psql = m.get('Psql')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = GetQueryOptimizeDataStatsResponseBodyDataListRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlSample') is not None:
            self.sql_sample = m.get('SqlSample')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetQueryOptimizeDataStatsResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeDataStatsResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataStatsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeDataStatsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeDataStatsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeDataStatsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataStatsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeDataStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeDataStatsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeDataStatsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataStatsResponse, self).to_map()
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
            temp_model = GetQueryOptimizeDataStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeDataTopRequest(TeaModel):
    def __init__(self, engine=None, instance_ids=None, tag_names=None, time=None, type=None):
        self.engine = engine  # type: str
        self.instance_ids = instance_ids  # type: str
        self.tag_names = tag_names  # type: str
        self.time = time  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeDataTopRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQueryOptimizeDataTopResponseBodyDataList(TeaModel):
    def __init__(self, instance_id=None, type=None, value=None):
        self.instance_id = instance_id  # type: str
        self.type = type  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeDataTopResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetQueryOptimizeDataTopResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeDataTopResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataTopResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeDataTopResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeDataTopResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeDataTopResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataTopResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeDataTopResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeDataTopResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeDataTopResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataTopResponse, self).to_map()
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
            temp_model = GetQueryOptimizeDataTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeDataTrendRequest(TeaModel):
    def __init__(self, end=None, engine=None, instance_ids=None, start=None, tag_names=None):
        self.end = end  # type: str
        self.engine = engine  # type: str
        self.instance_ids = instance_ids  # type: str
        self.start = start  # type: str
        self.tag_names = tag_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeDataTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.start is not None:
            result['Start'] = self.start
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        return self


class GetQueryOptimizeDataTrendResponseBodyDataList(TeaModel):
    def __init__(self, kpi=None, timestamp=None, value=None):
        self.kpi = kpi  # type: str
        self.timestamp = timestamp  # type: long
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeDataTrendResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kpi is not None:
            result['Kpi'] = self.kpi
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Kpi') is not None:
            self.kpi = m.get('Kpi')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetQueryOptimizeDataTrendResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeDataTrendResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeDataTrendResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeDataTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeDataTrendResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeDataTrendResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeDataTrendResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeDataTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeDataTrendResponse, self).to_map()
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
            temp_model = GetQueryOptimizeDataTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeExecErrorSampleRequest(TeaModel):
    def __init__(self, engine=None, instance_id=None, sql_id=None, time=None):
        self.engine = engine  # type: str
        self.instance_id = instance_id  # type: str
        self.sql_id = sql_id  # type: str
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorSampleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetQueryOptimizeExecErrorSampleResponseBodyDataList(TeaModel):
    def __init__(self, dbname=None, error_code=None, orig_host=None, sql_id=None, sql_text=None, timestamp=None,
                 user=None):
        self.dbname = dbname  # type: str
        self.error_code = error_code  # type: str
        self.orig_host = orig_host  # type: str
        self.sql_id = sql_id  # type: str
        self.sql_text = sql_text  # type: str
        self.timestamp = timestamp  # type: long
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorSampleResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.orig_host is not None:
            result['OrigHost'] = self.orig_host
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OrigHost') is not None:
            self.orig_host = m.get('OrigHost')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class GetQueryOptimizeExecErrorSampleResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeExecErrorSampleResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorSampleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeExecErrorSampleResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeExecErrorSampleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeExecErrorSampleResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorSampleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeExecErrorSampleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeExecErrorSampleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeExecErrorSampleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorSampleResponse, self).to_map()
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
            temp_model = GetQueryOptimizeExecErrorSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeExecErrorStatsRequest(TeaModel):
    def __init__(self, asc=None, db_names=None, engine=None, instance_ids=None, keywords=None, logical_operator=None,
                 order_by=None, page_no=None, page_size=None, time=None):
        self.asc = asc  # type: str
        self.db_names = db_names  # type: str
        self.engine = engine  # type: str
        self.instance_ids = instance_ids  # type: str
        self.keywords = keywords  # type: str
        self.logical_operator = logical_operator  # type: str
        self.order_by = order_by  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorStatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['Asc'] = self.asc
        if self.db_names is not None:
            result['DbNames'] = self.db_names
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetQueryOptimizeExecErrorStatsResponseBodyDataList(TeaModel):
    def __init__(self, dbname=None, error_code=None, error_count=None, instance_id=None, instance_name=None,
                 sql_id=None, sql_text=None):
        self.dbname = dbname  # type: str
        self.error_code = error_code  # type: str
        self.error_count = error_count  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.sql_id = sql_id  # type: str
        self.sql_text = sql_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorStatsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        return self


class GetQueryOptimizeExecErrorStatsResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeExecErrorStatsResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorStatsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeExecErrorStatsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeExecErrorStatsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeExecErrorStatsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorStatsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeExecErrorStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeExecErrorStatsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeExecErrorStatsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeExecErrorStatsResponse, self).to_map()
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
            temp_model = GetQueryOptimizeExecErrorStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeRuleListRequest(TeaModel):
    def __init__(self, engine=None, instance_ids=None, tag_names=None):
        self.engine = engine  # type: str
        self.instance_ids = instance_ids  # type: str
        self.tag_names = tag_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        return self


class GetQueryOptimizeRuleListResponseBodyDataList(TeaModel):
    def __init__(self, name=None, rule_id=None, type=None):
        self.name = name  # type: str
        self.rule_id = rule_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeRuleListResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQueryOptimizeRuleListResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeRuleListResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeRuleListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeRuleListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeRuleListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeRuleListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeRuleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeRuleListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeRuleListResponse, self).to_map()
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
            temp_model = GetQueryOptimizeRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeSolutionRequest(TeaModel):
    def __init__(self, engine=None, rule_ids=None, sql_id=None):
        self.engine = engine  # type: str
        self.rule_ids = rule_ids  # type: str
        self.sql_id = sql_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeSolutionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class GetQueryOptimizeSolutionResponseBodyDataList(TeaModel):
    def __init__(self, level=None, rule_id=None, solution=None, solution_ext=None):
        self.level = level  # type: str
        self.rule_id = rule_id  # type: str
        self.solution = solution  # type: str
        self.solution_ext = solution_ext  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueryOptimizeSolutionResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.solution_ext is not None:
            result['SolutionExt'] = self.solution_ext
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('SolutionExt') is not None:
            self.solution_ext = m.get('SolutionExt')
        return self


class GetQueryOptimizeSolutionResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetQueryOptimizeSolutionResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeSolutionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeSolutionResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeSolutionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetQueryOptimizeSolutionResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeSolutionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetQueryOptimizeSolutionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeSolutionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueryOptimizeSolutionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueryOptimizeSolutionResponse, self).to_map()
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
            temp_model = GetQueryOptimizeSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestDiagnosisPageRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, node_id=None, page_no=None, page_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.node_id = node_id  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRequestDiagnosisPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetRequestDiagnosisPageResponseBodyDataList(TeaModel):
    def __init__(self, account_id=None, db_schema=None, engine=None, gmt_create=None, gmt_modified=None,
                 message_id=None, param=None, result=None, sql_id=None, state=None, uuid=None):
        self.account_id = account_id  # type: str
        self.db_schema = db_schema  # type: str
        self.engine = engine  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.message_id = message_id  # type: str
        self.param = param  # type: str
        self.result = result  # type: str
        self.sql_id = sql_id  # type: str
        self.state = state  # type: int
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRequestDiagnosisPageResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema
        if self.engine is not None:
            result['engine'] = self.engine
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.param is not None:
            result['param'] = self.param
        if self.result is not None:
            result['result'] = self.result
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.state is not None:
            result['state'] = self.state
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetRequestDiagnosisPageResponseBodyData(TeaModel):
    def __init__(self, extra=None, list=None, page_no=None, page_size=None, total=None):
        self.extra = extra  # type: str
        self.list = list  # type: list[GetRequestDiagnosisPageResponseBodyDataList]
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRequestDiagnosisPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetRequestDiagnosisPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetRequestDiagnosisPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetRequestDiagnosisPageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRequestDiagnosisPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetRequestDiagnosisPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRequestDiagnosisPageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRequestDiagnosisPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRequestDiagnosisPageResponse, self).to_map()
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
            temp_model = GetRequestDiagnosisPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestDiagnosisResultRequest(TeaModel):
    def __init__(self, instance_id=None, message_id=None, node_id=None):
        self.instance_id = instance_id  # type: str
        self.message_id = message_id  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRequestDiagnosisResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class GetRequestDiagnosisResultResponseBodyData(TeaModel):
    def __init__(self, account_id=None, db_schema=None, engine=None, gmt_create=None, gmt_modified=None,
                 message_id=None, param=None, result=None, sql_id=None, state=None, uuid=None):
        self.account_id = account_id  # type: str
        self.db_schema = db_schema  # type: str
        self.engine = engine  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.message_id = message_id  # type: str
        self.param = param  # type: str
        self.result = result  # type: str
        self.sql_id = sql_id  # type: str
        self.state = state  # type: int
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRequestDiagnosisResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema
        if self.engine is not None:
            result['engine'] = self.engine
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.param is not None:
            result['param'] = self.param
        if self.result is not None:
            result['result'] = self.result
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.state is not None:
            result['state'] = self.state
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetRequestDiagnosisResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetRequestDiagnosisResultResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRequestDiagnosisResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetRequestDiagnosisResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRequestDiagnosisResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRequestDiagnosisResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRequestDiagnosisResultResponse, self).to_map()
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
            temp_model = GetRequestDiagnosisResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceOptimizeHistoryListRequest(TeaModel):
    def __init__(self, access_key=None, end_time=None, instance_id=None, page=None, page_size=None, signature=None,
                 start_time=None, uid=None, user_id=None, context=None):
        self.access_key = access_key  # type: str
        self.end_time = end_time  # type: str
        self.instance_id = instance_id  # type: str
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.signature = signature  # type: str
        self.start_time = start_time  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceOptimizeHistoryListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetResourceOptimizeHistoryListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceOptimizeHistoryListResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetResourceOptimizeHistoryListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResourceOptimizeHistoryListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceOptimizeHistoryListResponse, self).to_map()
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
            temp_model = GetResourceOptimizeHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningSqlConcurrencyControlRulesRequest(TeaModel):
    def __init__(self, console_context=None, instance_id=None, page_no=None, page_size=None):
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRunningSqlConcurrencyControlRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules(TeaModel):
    def __init__(self, concurrency_control_time=None, instance_id=None, item_id=None, keywords_hash=None,
                 max_concurrency=None, sql_keywords=None, sql_type=None, start_time=None, status=None, user_id=None):
        self.concurrency_control_time = concurrency_control_time  # type: long
        self.instance_id = instance_id  # type: str
        self.item_id = item_id  # type: long
        self.keywords_hash = keywords_hash  # type: str
        self.max_concurrency = max_concurrency  # type: str
        self.sql_keywords = sql_keywords  # type: str
        self.sql_type = sql_type  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyDataList(TeaModel):
    def __init__(self, running_rules=None):
        self.running_rules = running_rules  # type: list[GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules]

    def validate(self):
        if self.running_rules:
            for k in self.running_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRunningSqlConcurrencyControlRulesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['runningRules'] = []
        if self.running_rules is not None:
            for k in self.running_rules:
                result['runningRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.running_rules = []
        if m.get('runningRules') is not None:
            for k in m.get('runningRules'):
                temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules()
                self.running_rules.append(temp_model.from_map(k))
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyData(TeaModel):
    def __init__(self, list=None, total=None):
        self.list = list  # type: GetRunningSqlConcurrencyControlRulesResponseBodyDataList
        self.total = total  # type: long

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super(GetRunningSqlConcurrencyControlRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetRunningSqlConcurrencyControlRulesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRunningSqlConcurrencyControlRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRunningSqlConcurrencyControlRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRunningSqlConcurrencyControlRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRunningSqlConcurrencyControlRulesResponse, self).to_map()
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
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlConcurrencyControlKeywordsFromSqlTextRequest(TeaModel):
    def __init__(self, console_context=None, instance_id=None, sql_text=None):
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str
        self.sql_text = sql_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlConcurrencyControlKeywordsFromSqlTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        return self


class GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlConcurrencyControlKeywordsFromSqlTextResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSqlConcurrencyControlKeywordsFromSqlTextResponse, self).to_map()
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
            temp_model = GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlConcurrencyControlRulesHistoryRequest(TeaModel):
    def __init__(self, console_context=None, instance_id=None, page_no=None, page_size=None):
        self.console_context = console_context  # type: str
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlConcurrencyControlRulesHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules(TeaModel):
    def __init__(self, concurrency_control_time=None, instance_id=None, item_id=None, keywords_hash=None,
                 max_concurrency=None, sql_keywords=None, sql_type=None, start_time=None, status=None, user_id=None):
        self.concurrency_control_time = concurrency_control_time  # type: long
        self.instance_id = instance_id  # type: str
        self.item_id = item_id  # type: long
        self.keywords_hash = keywords_hash  # type: str
        self.max_concurrency = max_concurrency  # type: long
        self.sql_keywords = sql_keywords  # type: str
        self.sql_type = sql_type  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyDataList(TeaModel):
    def __init__(self, rules=None):
        self.rules = rules  # type: list[GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSqlConcurrencyControlRulesHistoryResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rules = []
        if m.get('rules') is not None:
            for k in m.get('rules'):
                temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyData(TeaModel):
    def __init__(self, list=None, total=None):
        self.list = list  # type: GetSqlConcurrencyControlRulesHistoryResponseBodyDataList
        self.total = total  # type: long

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super(GetSqlConcurrencyControlRulesHistoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetSqlConcurrencyControlRulesHistoryResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSqlConcurrencyControlRulesHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlConcurrencyControlRulesHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSqlConcurrencyControlRulesHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSqlConcurrencyControlRulesHistoryResponse, self).to_map()
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
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlOptimizeAdviceRequest(TeaModel):
    def __init__(self, console_context=None, end_dt=None, engine=None, instance_ids=None, start_dt=None):
        self.console_context = console_context  # type: str
        self.end_dt = end_dt  # type: str
        self.engine = engine  # type: str
        self.instance_ids = instance_ids  # type: str
        self.start_dt = start_dt  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlOptimizeAdviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_dt is not None:
            result['EndDt'] = self.end_dt
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.start_dt is not None:
            result['StartDt'] = self.start_dt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndDt') is not None:
            self.end_dt = m.get('EndDt')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('StartDt') is not None:
            self.start_dt = m.get('StartDt')
        return self


class GetSqlOptimizeAdviceResponseBodyData(TeaModel):
    def __init__(self, create_time=None, download_url=None, expire_time=None, status=None, status_code=None,
                 task_id=None):
        self.create_time = create_time  # type: str
        self.download_url = download_url  # type: str
        self.expire_time = expire_time  # type: str
        self.status = status  # type: str
        self.status_code = status_code  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlOptimizeAdviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetSqlOptimizeAdviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetSqlOptimizeAdviceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSqlOptimizeAdviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetSqlOptimizeAdviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlOptimizeAdviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSqlOptimizeAdviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSqlOptimizeAdviceResponse, self).to_map()
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
            temp_model = GetSqlOptimizeAdviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCloudBenchTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunCloudBenchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RunCloudBenchTaskResponseBodyDataPreCheckItem(TeaModel):
    def __init__(self, code=None, details=None, message=None, name=None, order=None, status=None):
        self.code = code  # type: int
        self.details = details  # type: str
        self.message = message  # type: str
        self.name = name  # type: str
        self.order = order  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunCloudBenchTaskResponseBodyDataPreCheckItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class RunCloudBenchTaskResponseBodyData(TeaModel):
    def __init__(self, pre_check_item=None):
        self.pre_check_item = pre_check_item  # type: list[RunCloudBenchTaskResponseBodyDataPreCheckItem]

    def validate(self):
        if self.pre_check_item:
            for k in self.pre_check_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RunCloudBenchTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PreCheckItem'] = []
        if self.pre_check_item is not None:
            for k in self.pre_check_item:
                result['PreCheckItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pre_check_item = []
        if m.get('PreCheckItem') is not None:
            for k in m.get('PreCheckItem'):
                temp_model = RunCloudBenchTaskResponseBodyDataPreCheckItem()
                self.pre_check_item.append(temp_model.from_map(k))
        return self


class RunCloudBenchTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: RunCloudBenchTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RunCloudBenchTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = RunCloudBenchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RunCloudBenchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RunCloudBenchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunCloudBenchTaskResponse, self).to_map()
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
            temp_model = RunCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCloudBenchTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCloudBenchTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopCloudBenchTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCloudBenchTaskResponseBody, self).to_map()
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopCloudBenchTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopCloudBenchTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopCloudBenchTaskResponse, self).to_map()
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
            temp_model = StopCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopOrRollbackOptimizeTaskRequest(TeaModel):
    def __init__(self, access_key=None, instance_id=None, signature=None, stop_or_rollback=None, task_type=None,
                 task_uuid=None, uid=None, user_id=None, context=None):
        self.access_key = access_key  # type: str
        self.instance_id = instance_id  # type: str
        self.signature = signature  # type: str
        self.stop_or_rollback = stop_or_rollback  # type: str
        self.task_type = task_type  # type: str
        self.task_uuid = task_uuid  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopOrRollbackOptimizeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.stop_or_rollback is not None:
            result['StopOrRollback'] = self.stop_or_rollback
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StopOrRollback') is not None:
            self.stop_or_rollback = m.get('StopOrRollback')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class StopOrRollbackOptimizeTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopOrRollbackOptimizeTaskResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class StopOrRollbackOptimizeTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopOrRollbackOptimizeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopOrRollbackOptimizeTaskResponse, self).to_map()
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
            temp_model = StopOrRollbackOptimizeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncHDMAliyunResourceRequest(TeaModel):
    def __init__(self, async=None, resource_types=None, uid=None, user_id=None, wait_for_modify_security_ips=None,
                 context=None, access_key=None, signature=None, skip_auth=None, timestamp=None):
        self.async = async  # type: str
        self.resource_types = resource_types  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.wait_for_modify_security_ips = wait_for_modify_security_ips  # type: str
        self.context = context  # type: str
        self.access_key = access_key  # type: str
        self.signature = signature  # type: str
        self.skip_auth = skip_auth  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncHDMAliyunResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async is not None:
            result['Async'] = self.async
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.wait_for_modify_security_ips is not None:
            result['WaitForModifySecurityIps'] = self.wait_for_modify_security_ips
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async = m.get('Async')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WaitForModifySecurityIps') is not None:
            self.wait_for_modify_security_ips = m.get('WaitForModifySecurityIps')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class SyncHDMAliyunResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncHDMAliyunResourceResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class SyncHDMAliyunResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncHDMAliyunResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncHDMAliyunResourceResponse, self).to_map()
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
            temp_model = SyncHDMAliyunResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TurnOffAutoResourceOptimizeRequest(TeaModel):
    def __init__(self, access_key=None, instance_id=None, signature=None, uid=None, user_id=None, context=None):
        self.access_key = access_key  # type: str
        self.instance_id = instance_id  # type: str
        self.signature = signature  # type: str
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TurnOffAutoResourceOptimizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class TurnOffAutoResourceOptimizeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TurnOffAutoResourceOptimizeResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class TurnOffAutoResourceOptimizeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TurnOffAutoResourceOptimizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TurnOffAutoResourceOptimizeResponse, self).to_map()
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
            temp_model = TurnOffAutoResourceOptimizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoResourceOptimizeConfigRequest(TeaModel):
    def __init__(self, access_key=None, auto_defragment=None, auto_duplicate_index_delete=None, instance_id=None,
                 signature=None, table_fragmentation_ratio=None, table_space_size=None, uid=None, user_id=None, context=None):
        self.access_key = access_key  # type: str
        self.auto_defragment = auto_defragment  # type: int
        self.auto_duplicate_index_delete = auto_duplicate_index_delete  # type: int
        self.instance_id = instance_id  # type: str
        self.signature = signature  # type: str
        self.table_fragmentation_ratio = table_fragmentation_ratio  # type: float
        self.table_space_size = table_space_size  # type: float
        self.uid = uid  # type: str
        self.user_id = user_id  # type: str
        self.context = context  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutoResourceOptimizeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment
        if self.auto_duplicate_index_delete is not None:
            result['AutoDuplicateIndexDelete'] = self.auto_duplicate_index_delete
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')
        if m.get('AutoDuplicateIndexDelete') is not None:
            self.auto_duplicate_index_delete = m.get('AutoDuplicateIndexDelete')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class UpdateAutoResourceOptimizeConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAutoResourceOptimizeConfigResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class UpdateAutoResourceOptimizeConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAutoResourceOptimizeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAutoResourceOptimizeConfigResponse, self).to_map()
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
            temp_model = UpdateAutoResourceOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


