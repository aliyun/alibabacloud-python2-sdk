# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ConfigureSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(self, ip=None, instance_id=None, instance_type=None, password=None, port=None, user_name=None):
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigureSynchronizationJobRequestDestinationEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSynchronizationJobRequestPartitionKey(TeaModel):
    def __init__(self, modify_time_day=None, modify_time_hour=None, modify_time_minute=None,
                 modify_time_month=None, modify_time_year=None):
        self.modify_time_day = modify_time_day  # type: bool
        self.modify_time_hour = modify_time_hour  # type: bool
        self.modify_time_minute = modify_time_minute  # type: bool
        self.modify_time_month = modify_time_month  # type: bool
        self.modify_time_year = modify_time_year  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigureSynchronizationJobRequestPartitionKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time_day is not None:
            result['ModifyTime_Day'] = self.modify_time_day
        if self.modify_time_hour is not None:
            result['ModifyTime_Hour'] = self.modify_time_hour
        if self.modify_time_minute is not None:
            result['ModifyTime_Minute'] = self.modify_time_minute
        if self.modify_time_month is not None:
            result['ModifyTime_Month'] = self.modify_time_month
        if self.modify_time_year is not None:
            result['ModifyTime_Year'] = self.modify_time_year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifyTime_Day') is not None:
            self.modify_time_day = m.get('ModifyTime_Day')
        if m.get('ModifyTime_Hour') is not None:
            self.modify_time_hour = m.get('ModifyTime_Hour')
        if m.get('ModifyTime_Minute') is not None:
            self.modify_time_minute = m.get('ModifyTime_Minute')
        if m.get('ModifyTime_Month') is not None:
            self.modify_time_month = m.get('ModifyTime_Month')
        if m.get('ModifyTime_Year') is not None:
            self.modify_time_year = m.get('ModifyTime_Year')
        return self


class ConfigureSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(self, ip=None, instance_id=None, instance_type=None, owner_id=None, password=None, port=None,
                 role=None, user_name=None):
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.role = role  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigureSynchronizationJobRequestSourceEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSynchronizationJobRequest(TeaModel):
    def __init__(self, destination_endpoint=None, partition_key=None, source_endpoint=None, checkpoint=None,
                 data_initialization=None, migration_reserved=None, owner_id=None, structure_initialization=None,
                 synchronization_direction=None, synchronization_job_id=None, synchronization_job_name=None, synchronization_objects=None):
        self.destination_endpoint = destination_endpoint  # type: ConfigureSynchronizationJobRequestDestinationEndpoint
        self.partition_key = partition_key  # type: ConfigureSynchronizationJobRequestPartitionKey
        self.source_endpoint = source_endpoint  # type: ConfigureSynchronizationJobRequestSourceEndpoint
        self.checkpoint = checkpoint  # type: str
        self.data_initialization = data_initialization  # type: bool
        self.migration_reserved = migration_reserved  # type: str
        self.owner_id = owner_id  # type: str
        self.structure_initialization = structure_initialization  # type: bool
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str
        self.synchronization_job_name = synchronization_job_name  # type: str
        self.synchronization_objects = synchronization_objects  # type: str

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.partition_key:
            self.partition_key.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super(ConfigureSynchronizationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('PartitionKey') is not None:
            temp_model = ConfigureSynchronizationJobRequestPartitionKey()
            self.partition_key = temp_model.from_map(m['PartitionKey'])
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        return self


class ConfigureSynchronizationJobResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigureSynchronizationJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSynchronizationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigureSynchronizationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigureSynchronizationJobResponse, self).to_map()
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
            temp_model = ConfigureSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobAlertRequest(TeaModel):
    def __init__(self, delay_alert_phone=None, delay_alert_status=None, delay_over_seconds=None,
                 error_alert_phone=None, error_alert_status=None, owner_id=None, synchronization_direction=None,
                 synchronization_job_id=None):
        self.delay_alert_phone = delay_alert_phone  # type: str
        self.delay_alert_status = delay_alert_status  # type: str
        self.delay_over_seconds = delay_over_seconds  # type: str
        self.error_alert_phone = error_alert_phone  # type: str
        self.error_alert_status = error_alert_status  # type: str
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigureSynchronizationJobAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class ConfigureSynchronizationJobAlertResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigureSynchronizationJobAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSynchronizationJobAlertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigureSynchronizationJobAlertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigureSynchronizationJobAlertResponse, self).to_map()
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
            temp_model = ConfigureSynchronizationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSynchronizationJobRequestDestinationEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSynchronizationJobRequestSourceEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSynchronizationJobRequest(TeaModel):
    def __init__(self, destination_endpoint=None, source_endpoint=None, client_token=None, dest_region=None,
                 owner_id=None, pay_type=None, period=None, source_region=None, synchronization_job_class=None,
                 topology=None, used_time=None, network_type=None):
        self.destination_endpoint = destination_endpoint  # type: CreateSynchronizationJobRequestDestinationEndpoint
        self.source_endpoint = source_endpoint  # type: CreateSynchronizationJobRequestSourceEndpoint
        self.client_token = client_token  # type: str
        self.dest_region = dest_region  # type: str
        self.owner_id = owner_id  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: str
        self.source_region = source_region  # type: str
        self.synchronization_job_class = synchronization_job_class  # type: str
        self.topology = topology  # type: str
        self.used_time = used_time  # type: int
        self.network_type = network_type  # type: str

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super(CreateSynchronizationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.topology is not None:
            result['Topology'] = self.topology
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.network_type is not None:
            result['networkType'] = self.network_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('SourceEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('Topology') is not None:
            self.topology = m.get('Topology')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        return self


class CreateSynchronizationJobResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None, synchronization_job_id=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSynchronizationJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class CreateSynchronizationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSynchronizationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSynchronizationJobResponse, self).to_map()
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
            temp_model = CreateSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSynchronizationJobRequest(TeaModel):
    def __init__(self, owner_id=None, synchronization_job_id=None):
        self.owner_id = owner_id  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSynchronizationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DeleteSynchronizationJobResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSynchronizationJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSynchronizationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSynchronizationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSynchronizationJobResponse, self).to_map()
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
            temp_model = DeleteSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointSwitchStatusRequest(TeaModel):
    def __init__(self, client_token=None, owner_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.owner_id = owner_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointSwitchStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeEndpointSwitchStatusResponseBody(TeaModel):
    def __init__(self, error_message=None, request_id=None, status=None):
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEndpointSwitchStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEndpointSwitchStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEndpointSwitchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndpointSwitchStatusResponse, self).to_map()
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
            temp_model = DescribeEndpointSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobAlertRequest(TeaModel):
    def __init__(self, client_token=None, owner_id=None, synchronization_direction=None,
                 synchronization_job_id=None):
        self.client_token = client_token  # type: str
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobAlertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobAlertResponseBody(TeaModel):
    def __init__(self, delay_alert_phone=None, delay_alert_status=None, delay_over_seconds=None, err_code=None,
                 err_message=None, error_alert_phone=None, error_alert_status=None, request_id=None, success=None,
                 synchronization_direction=None, synchronization_job_id=None, synchronization_job_name=None):
        self.delay_alert_phone = delay_alert_phone  # type: str
        self.delay_alert_status = delay_alert_status  # type: str
        self.delay_over_seconds = delay_over_seconds  # type: str
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.error_alert_phone = error_alert_phone  # type: str
        self.error_alert_status = error_alert_status  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str
        self.synchronization_job_name = synchronization_job_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobAlertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        return self


class DescribeSynchronizationJobAlertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSynchronizationJobAlertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobAlertResponse, self).to_map()
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
            temp_model = DescribeSynchronizationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobStatusRequest(TeaModel):
    def __init__(self, client_token=None, owner_id=None, synchronization_direction=None,
                 synchronization_job_id=None):
        self.client_token = client_token  # type: str
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(self, error_message=None, percent=None, progress=None, status=None):
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.progress = progress  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(self, checkpoint=None, delay=None, error_message=None, percent=None, status=None):
        self.checkpoint = checkpoint  # type: str
        self.delay = delay  # type: str
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(self, engine_name=None, ip=None, instance_id=None, instance_type=None, port=None, user_name=None):
        self.engine_name = engine_name  # type: str
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.port = port  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobStatusResponseBodyPerformance(TeaModel):
    def __init__(self, flow=None, rps=None):
        self.flow = flow  # type: str
        self.rps = rps  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyPerformance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['FLOW'] = self.flow
        if self.rps is not None:
            result['RPS'] = self.rps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        return self


class DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(self, check_status=None, error_message=None, item_name=None, repair_method=None):
        self.check_status = check_status  # type: str
        self.error_message = error_message  # type: str
        self.item_name = item_name  # type: str
        self.repair_method = repair_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationJobStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(self, detail=None, percent=None, status=None):
        self.detail = detail  # type: list[DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail]
        self.percent = percent  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyPrecheckStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(self, engine_name=None, ip=None, instance_id=None, instance_type=None, port=None, user_name=None):
        self.engine_name = engine_name  # type: str
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.port = port  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodySourceEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(self, error_message=None, percent=None, progress=None, status=None):
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.progress = progress  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjects(TeaModel):
    def __init__(self, new_schema_name=None, schema_name=None, table_excludes=None, table_includes=None):
        self.new_schema_name = new_schema_name  # type: str
        self.schema_name = schema_name  # type: str
        self.table_excludes = table_excludes  # type: list[DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes]
        self.table_includes = table_includes  # type: list[DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes]

    def validate(self):
        if self.table_excludes:
            for k in self.table_excludes:
                if k:
                    k.validate()
        if self.table_includes:
            for k in self.table_includes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBodySynchronizationObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k in self.table_excludes:
                result['TableExcludes'].append(k.to_map() if k else None)
        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k in self.table_includes:
                result['TableIncludes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k in m.get('TableExcludes'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k))
        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k in m.get('TableIncludes'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusResponseBody(TeaModel):
    def __init__(self, checkpoint=None, data_initialization=None, data_initialization_status=None,
                 data_synchronization_status=None, delay=None, destination_endpoint=None, error_message=None, expire_time=None, pay_type=None,
                 performance=None, precheck_status=None, request_id=None, source_endpoint=None, status=None,
                 structure_initialization=None, structure_initialization_status=None, synchronization_direction=None,
                 synchronization_job_class=None, synchronization_job_id=None, synchronization_job_name=None, synchronization_objects=None):
        self.checkpoint = checkpoint  # type: str
        self.data_initialization = data_initialization  # type: str
        self.data_initialization_status = data_initialization_status  # type: DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus
        self.data_synchronization_status = data_synchronization_status  # type: DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus
        self.delay = delay  # type: str
        self.destination_endpoint = destination_endpoint  # type: DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint
        self.error_message = error_message  # type: str
        self.expire_time = expire_time  # type: str
        self.pay_type = pay_type  # type: str
        self.performance = performance  # type: DescribeSynchronizationJobStatusResponseBodyPerformance
        self.precheck_status = precheck_status  # type: DescribeSynchronizationJobStatusResponseBodyPrecheckStatus
        self.request_id = request_id  # type: str
        self.source_endpoint = source_endpoint  # type: DescribeSynchronizationJobStatusResponseBodySourceEndpoint
        self.status = status  # type: str
        self.structure_initialization = structure_initialization  # type: str
        self.structure_initialization_status = structure_initialization_status  # type: DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_class = synchronization_job_class  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str
        self.synchronization_job_name = synchronization_job_name  # type: str
        self.synchronization_objects = synchronization_objects  # type: list[DescribeSynchronizationJobStatusResponseBodySynchronizationObjects]

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSynchronizationJobStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobStatusResponse, self).to_map()
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
            temp_model = DescribeSynchronizationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobsRequest(TeaModel):
    def __init__(self, client_token=None, owner_id=None, page_num=None, page_size=None,
                 synchronization_job_name=None):
        self.client_token = client_token  # type: str
        self.owner_id = owner_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.synchronization_job_name = synchronization_job_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus(TeaModel):
    def __init__(self, error_message=None, percent=None, progress=None, status=None):
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.progress = progress  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus(TeaModel):
    def __init__(self, delay=None, error_message=None, percent=None, status=None):
        self.delay = delay  # type: str
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint(TeaModel):
    def __init__(self, engine_name=None, ip=None, instance_id=None, instance_type=None, port=None, user_name=None):
        self.engine_name = engine_name  # type: str
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.port = port  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance(TeaModel):
    def __init__(self, flow=None, rps=None):
        self.flow = flow  # type: str
        self.rps = rps  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['FLOW'] = self.flow
        if self.rps is not None:
            result['RPS'] = self.rps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail(TeaModel):
    def __init__(self, check_status=None, error_message=None, item_name=None, repair_method=None):
        self.check_status = check_status  # type: str
        self.error_message = error_message  # type: str
        self.item_name = item_name  # type: str
        self.repair_method = repair_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus(TeaModel):
    def __init__(self, detail=None, percent=None, status=None):
        self.detail = detail  # type: list[DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail]
        self.percent = percent  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint(TeaModel):
    def __init__(self, engine_name=None, ip=None, instance_id=None, instance_type=None, port=None, user_name=None):
        self.engine_name = engine_name  # type: str
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.port = port  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus(TeaModel):
    def __init__(self, error_message=None, percent=None, progress=None, status=None):
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.progress = progress  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes(TeaModel):
    def __init__(self, table_name=None):
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects(TeaModel):
    def __init__(self, new_schema_name=None, schema_name=None, table_excludes=None, table_includes=None):
        self.new_schema_name = new_schema_name  # type: str
        self.schema_name = schema_name  # type: str
        self.table_excludes = table_excludes  # type: list[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes]
        self.table_includes = table_includes  # type: list[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes]

    def validate(self):
        if self.table_excludes:
            for k in self.table_excludes:
                if k:
                    k.validate()
        if self.table_includes:
            for k in self.table_includes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k in self.table_excludes:
                result['TableExcludes'].append(k.to_map() if k else None)
        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k in self.table_includes:
                result['TableIncludes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k in m.get('TableExcludes'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k))
        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k in m.get('TableIncludes'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstances(TeaModel):
    def __init__(self, data_initialization=None, data_initialization_status=None,
                 data_synchronization_status=None, delay=None, destination_endpoint=None, error_message=None, expire_time=None, pay_type=None,
                 performance=None, precheck_status=None, source_endpoint=None, status=None, structure_initialization=None,
                 structure_initialization_status=None, synchronization_direction=None, synchronization_job_class=None,
                 synchronization_job_id=None, synchronization_job_name=None, synchronization_objects=None):
        self.data_initialization = data_initialization  # type: str
        self.data_initialization_status = data_initialization_status  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus
        self.data_synchronization_status = data_synchronization_status  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus
        self.delay = delay  # type: str
        self.destination_endpoint = destination_endpoint  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint
        self.error_message = error_message  # type: str
        self.expire_time = expire_time  # type: str
        self.pay_type = pay_type  # type: str
        self.performance = performance  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance
        self.precheck_status = precheck_status  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus
        self.source_endpoint = source_endpoint  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint
        self.status = status  # type: str
        self.structure_initialization = structure_initialization  # type: str
        self.structure_initialization_status = structure_initialization_status  # type: DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_class = synchronization_job_class  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str
        self.synchronization_job_name = synchronization_job_name  # type: str
        self.synchronization_objects = synchronization_objects  # type: list[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects]

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBodySynchronizationInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_record_count=None, request_id=None, synchronization_instances=None,
                 total_record_count=None):
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id  # type: str
        self.synchronization_instances = synchronization_instances  # type: list[DescribeSynchronizationJobsResponseBodySynchronizationInstances]
        self.total_record_count = total_record_count  # type: long

    def validate(self):
        if self.synchronization_instances:
            for k in self.synchronization_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SynchronizationInstances'] = []
        if self.synchronization_instances is not None:
            for k in self.synchronization_instances:
                result['SynchronizationInstances'].append(k.to_map() if k else None)
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.synchronization_instances = []
        if m.get('SynchronizationInstances') is not None:
            for k in m.get('SynchronizationInstances'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstances()
                self.synchronization_instances.append(temp_model.from_map(k))
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSynchronizationJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSynchronizationJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationJobsResponse, self).to_map()
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
            temp_model = DescribeSynchronizationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationObjectModifyStatusRequest(TeaModel):
    def __init__(self, client_token=None, owner_id=None, task_id=None):
        self.client_token = client_token  # type: str
        self.owner_id = owner_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(self, error_message=None, percent=None, progress=None, status=None):
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.progress = progress  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(self, delay=None, error_message=None, percent=None, status=None):
        self.delay = delay  # type: str
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(self, check_status=None, error_message=None, item_name=None, repair_method=None):
        self.check_status = check_status  # type: str
        self.error_message = error_message  # type: str
        self.item_name = item_name  # type: str
        self.repair_method = repair_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(self, detail=None, percent=None, status=None):
        self.detail = detail  # type: list[DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail]
        self.percent = percent  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(self, error_message=None, percent=None, progress=None, status=None):
        self.error_message = error_message  # type: str
        self.percent = percent  # type: str
        self.progress = progress  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBody(TeaModel):
    def __init__(self, data_initialization_status=None, data_synchronization_status=None, error_message=None,
                 precheck_status=None, request_id=None, status=None, structure_initialization_status=None):
        self.data_initialization_status = data_initialization_status  # type: DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus
        self.data_synchronization_status = data_synchronization_status  # type: DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus
        self.error_message = error_message  # type: str
        self.precheck_status = precheck_status  # type: DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.structure_initialization_status = structure_initialization_status  # type: DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeSynchronizationObjectModifyStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSynchronizationObjectModifyStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSynchronizationObjectModifyStatusResponse, self).to_map()
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
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySynchronizationObjectRequest(TeaModel):
    def __init__(self, owner_id=None, synchronization_direction=None, synchronization_job_id=None,
                 synchronization_objects=None):
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str
        self.synchronization_objects = synchronization_objects  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySynchronizationObjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        return self


class ModifySynchronizationObjectResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None, task_id=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySynchronizationObjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifySynchronizationObjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySynchronizationObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySynchronizationObjectResponse, self).to_map()
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
            temp_model = ModifySynchronizationObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSynchronizationJobRequest(TeaModel):
    def __init__(self, owner_id=None, synchronization_direction=None, synchronization_job_id=None):
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSynchronizationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class ResetSynchronizationJobResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSynchronizationJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetSynchronizationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetSynchronizationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetSynchronizationJobResponse, self).to_map()
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
            temp_model = ResetSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSynchronizationJobRequest(TeaModel):
    def __init__(self, owner_id=None, synchronization_direction=None, synchronization_job_id=None):
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSynchronizationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class StartSynchronizationJobResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartSynchronizationJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartSynchronizationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartSynchronizationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartSynchronizationJobResponse, self).to_map()
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
            temp_model = StartSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendSynchronizationJobRequest(TeaModel):
    def __init__(self, owner_id=None, synchronization_direction=None, synchronization_job_id=None):
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendSynchronizationJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class SuspendSynchronizationJobResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendSynchronizationJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendSynchronizationJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SuspendSynchronizationJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuspendSynchronizationJobResponse, self).to_map()
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
            temp_model = SuspendSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSynchronizationEndpointRequestEndpoint(TeaModel):
    def __init__(self, ip=None, instance_id=None, instance_type=None, port=None, type=None):
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.port = port  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchSynchronizationEndpointRequestEndpoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SwitchSynchronizationEndpointRequest(TeaModel):
    def __init__(self, endpoint=None, owner_id=None, synchronization_direction=None, synchronization_job_id=None):
        self.endpoint = endpoint  # type: SwitchSynchronizationEndpointRequestEndpoint
        self.owner_id = owner_id  # type: str
        self.synchronization_direction = synchronization_direction  # type: str
        self.synchronization_job_id = synchronization_job_id  # type: str

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()

    def to_map(self):
        _map = super(SwitchSynchronizationEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            temp_model = SwitchSynchronizationEndpointRequestEndpoint()
            self.endpoint = temp_model.from_map(m['Endpoint'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class SwitchSynchronizationEndpointResponseBody(TeaModel):
    def __init__(self, err_code=None, err_message=None, request_id=None, success=None, task_id=None):
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchSynchronizationEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SwitchSynchronizationEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchSynchronizationEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchSynchronizationEndpointResponse, self).to_map()
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
            temp_model = SwitchSynchronizationEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


