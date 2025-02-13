# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AccelerationInfo(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccelerationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class Alias(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, created_time=None, description=None,
                 last_modified_time=None, version_id=None):
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        self.alias_name = alias_name  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Alias, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class AsyncConfig(TeaModel):
    def __init__(self, async_task=None, created_time=None, destination_config=None, function_arn=None,
                 last_modified_time=None, max_async_event_age_in_seconds=None, max_async_retry_attempts=None):
        self.async_task = async_task  # type: bool
        self.created_time = created_time  # type: str
        self.destination_config = destination_config  # type: DestinationConfig
        self.function_arn = function_arn  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds  # type: long
        self.max_async_retry_attempts = max_async_retry_attempts  # type: long

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super(AsyncConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task is not None:
            result['asyncTask'] = self.async_task
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        return self


class AsyncTask(TeaModel):
    def __init__(self, already_retried_times=None, destination_status=None, duration_ms=None, end_time=None,
                 events=None, function_arn=None, instance_id=None, qualifier=None, request_id=None, return_payload=None,
                 started_time=None, status=None, task_error_message=None, task_id=None, task_payload=None):
        self.already_retried_times = already_retried_times  # type: long
        self.destination_status = destination_status  # type: str
        self.duration_ms = duration_ms  # type: long
        self.end_time = end_time  # type: long
        self.events = events  # type: list[AsyncTaskEvent]
        self.function_arn = function_arn  # type: str
        self.instance_id = instance_id  # type: str
        self.qualifier = qualifier  # type: str
        self.request_id = request_id  # type: str
        self.return_payload = return_payload  # type: str
        self.started_time = started_time  # type: long
        self.status = status  # type: str
        self.task_error_message = task_error_message  # type: str
        self.task_id = task_id  # type: str
        self.task_payload = task_payload  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AsyncTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_retried_times is not None:
            result['alreadyRetriedTimes'] = self.already_retried_times
        if self.destination_status is not None:
            result['destinationStatus'] = self.destination_status
        if self.duration_ms is not None:
            result['durationMs'] = self.duration_ms
        if self.end_time is not None:
            result['endTime'] = self.end_time
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.return_payload is not None:
            result['returnPayload'] = self.return_payload
        if self.started_time is not None:
            result['startedTime'] = self.started_time
        if self.status is not None:
            result['status'] = self.status
        if self.task_error_message is not None:
            result['taskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_payload is not None:
            result['taskPayload'] = self.task_payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alreadyRetriedTimes') is not None:
            self.already_retried_times = m.get('alreadyRetriedTimes')
        if m.get('destinationStatus') is not None:
            self.destination_status = m.get('destinationStatus')
        if m.get('durationMs') is not None:
            self.duration_ms = m.get('durationMs')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = AsyncTaskEvent()
                self.events.append(temp_model.from_map(k))
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('returnPayload') is not None:
            self.return_payload = m.get('returnPayload')
        if m.get('startedTime') is not None:
            self.started_time = m.get('startedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskErrorMessage') is not None:
            self.task_error_message = m.get('taskErrorMessage')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskPayload') is not None:
            self.task_payload = m.get('taskPayload')
        return self


class AsyncTaskEvent(TeaModel):
    def __init__(self, event_detail=None, event_id=None, status=None, timestamp=None):
        self.event_detail = event_detail  # type: str
        self.event_id = event_id  # type: long
        self.status = status  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsyncTaskEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_detail is not None:
            result['eventDetail'] = self.event_detail
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.status is not None:
            result['status'] = self.status
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventDetail') is not None:
            self.event_detail = m.get('eventDetail')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class AuthConfig(TeaModel):
    def __init__(self, auth_info=None, auth_type=None):
        self.auth_info = auth_info  # type: str
        self.auth_type = auth_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_info is not None:
            result['authInfo'] = self.auth_info
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authInfo') is not None:
            self.auth_info = m.get('authInfo')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        return self


class BatchWindow(TeaModel):
    def __init__(self, count_based_window=None, time_based_window=None):
        self.count_based_window = count_based_window  # type: int
        self.time_based_window = time_based_window  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchWindow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_based_window is not None:
            result['CountBasedWindow'] = self.count_based_window
        if self.time_based_window is not None:
            result['TimeBasedWindow'] = self.time_based_window
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountBasedWindow') is not None:
            self.count_based_window = m.get('CountBasedWindow')
        if m.get('TimeBasedWindow') is not None:
            self.time_based_window = m.get('TimeBasedWindow')
        return self


class CDNTriggerConfig(TeaModel):
    def __init__(self, event_name=None, event_version=None, filter=None, notes=None):
        self.event_name = event_name  # type: str
        self.event_version = event_version  # type: str
        self.filter = filter  # type: dict[str, list[str]]
        self.notes = notes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CDNTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['eventName'] = self.event_name
        if self.event_version is not None:
            result['eventVersion'] = self.event_version
        if self.filter is not None:
            result['filter'] = self.filter
        if self.notes is not None:
            result['notes'] = self.notes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        if m.get('eventVersion') is not None:
            self.event_version = m.get('eventVersion')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('notes') is not None:
            self.notes = m.get('notes')
        return self


class CertConfig(TeaModel):
    def __init__(self, cert_name=None, certificate=None, private_key=None):
        # This parameter is required.
        self.cert_name = cert_name  # type: str
        # This parameter is required.
        self.certificate = certificate  # type: str
        # This parameter is required.
        self.private_key = private_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CertConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['certName'] = self.cert_name
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('certName') is not None:
            self.cert_name = m.get('certName')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        return self


class ConcurrencyConfig(TeaModel):
    def __init__(self, function_arn=None, reserved_concurrency=None):
        self.function_arn = function_arn  # type: str
        self.reserved_concurrency = reserved_concurrency  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConcurrencyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class CreateAliasInput(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, description=None, version_id=None):
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # This parameter is required.
        self.alias_name = alias_name  # type: str
        self.description = description  # type: str
        # This parameter is required.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAliasInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.description is not None:
            result['description'] = self.description
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('aliasName') is not None:
            self.alias_name = m.get('aliasName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class CreateCustomDomainInput(TeaModel):
    def __init__(self, auth_config=None, cert_config=None, domain_name=None, protocol=None, route_config=None,
                 tls_config=None, waf_config=None):
        self.auth_config = auth_config  # type: AuthConfig
        self.cert_config = cert_config  # type: CertConfig
        # This parameter is required.
        self.domain_name = domain_name  # type: str
        self.protocol = protocol  # type: str
        self.route_config = route_config  # type: RouteConfig
        self.tls_config = tls_config  # type: TLSConfig
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(CreateCustomDomainInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class CreateFunctionInput(TeaModel):
    def __init__(self, code=None, cpu=None, custom_container_config=None, custom_dns=None,
                 custom_runtime_config=None, description=None, disk_size=None, environment_variables=None, function_name=None,
                 gpu_config=None, handler=None, instance_concurrency=None, instance_lifecycle_config=None,
                 internet_access=None, layers=None, log_config=None, memory_size=None, nas_config=None, oss_mount_config=None,
                 role=None, runtime=None, tags=None, timeout=None, tracing_config=None, vpc_config=None):
        self.code = code  # type: InputCodeLocation
        self.cpu = cpu  # type: float
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        self.custom_dns = custom_dns  # type: CustomDNS
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        self.description = description  # type: str
        self.disk_size = disk_size  # type: int
        self.environment_variables = environment_variables  # type: dict[str, str]
        # This parameter is required.
        self.function_name = function_name  # type: str
        self.gpu_config = gpu_config  # type: GPUConfig
        # This parameter is required.
        self.handler = handler  # type: str
        self.instance_concurrency = instance_concurrency  # type: int
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        self.internet_access = internet_access  # type: bool
        self.layers = layers  # type: list[str]
        self.log_config = log_config  # type: LogConfig
        self.memory_size = memory_size  # type: int
        self.nas_config = nas_config  # type: NASConfig
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        self.role = role  # type: str
        # This parameter is required.
        self.runtime = runtime  # type: str
        self.tags = tags  # type: list[Tag]
        self.timeout = timeout  # type: int
        self.tracing_config = tracing_config  # type: TracingConfig
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super(CreateFunctionInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.layers is not None:
            result['layers'] = self.layers
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.runtime is not None:
            result['runtime'] = self.runtime
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = InputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuConfig') is not None:
            temp_model = GPUConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateLayerVersionInput(TeaModel):
    def __init__(self, code=None, compatible_runtime=None, description=None, license=None):
        self.code = code  # type: InputCodeLocation
        self.compatible_runtime = compatible_runtime  # type: list[str]
        self.description = description  # type: str
        self.license = license  # type: str

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super(CreateLayerVersionInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.description is not None:
            result['description'] = self.description
        if self.license is not None:
            result['license'] = self.license
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = InputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('license') is not None:
            self.license = m.get('license')
        return self


class CreateTriggerInput(TeaModel):
    def __init__(self, description=None, invocation_role=None, qualifier=None, source_arn=None, trigger_config=None,
                 trigger_name=None, trigger_type=None):
        self.description = description  # type: str
        self.invocation_role = invocation_role  # type: str
        self.qualifier = qualifier  # type: str
        self.source_arn = source_arn  # type: str
        # This parameter is required.
        self.trigger_config = trigger_config  # type: str
        # This parameter is required.
        self.trigger_name = trigger_name  # type: str
        # This parameter is required.
        self.trigger_type = trigger_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class CreateVpcBindingInput(TeaModel):
    def __init__(self, vpc_id=None):
        # This parameter is required.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcBindingInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class CustomContainerConfig(TeaModel):
    def __init__(self, acceleration_info=None, acceleration_type=None, acr_instance_id=None, command=None,
                 entrypoint=None, health_check_config=None, image=None, port=None, registry_config=None,
                 resolved_image_uri=None):
        self.acceleration_info = acceleration_info  # type: AccelerationInfo
        self.acceleration_type = acceleration_type  # type: str
        self.acr_instance_id = acr_instance_id  # type: str
        self.command = command  # type: list[str]
        self.entrypoint = entrypoint  # type: list[str]
        self.health_check_config = health_check_config  # type: CustomHealthCheckConfig
        self.image = image  # type: str
        self.port = port  # type: int
        self.registry_config = registry_config  # type: RegistryConfig
        self.resolved_image_uri = resolved_image_uri  # type: str

    def validate(self):
        if self.acceleration_info:
            self.acceleration_info.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.registry_config:
            self.registry_config.validate()

    def to_map(self):
        _map = super(CustomContainerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_info is not None:
            result['accelerationInfo'] = self.acceleration_info.to_map()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id
        if self.command is not None:
            result['command'] = self.command
        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint
        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()
        if self.image is not None:
            result['image'] = self.image
        if self.port is not None:
            result['port'] = self.port
        if self.registry_config is not None:
            result['registryConfig'] = self.registry_config.to_map()
        if self.resolved_image_uri is not None:
            result['resolvedImageUri'] = self.resolved_image_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accelerationInfo') is not None:
            temp_model = AccelerationInfo()
            self.acceleration_info = temp_model.from_map(m['accelerationInfo'])
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')
        if m.get('healthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['healthCheckConfig'])
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('registryConfig') is not None:
            temp_model = RegistryConfig()
            self.registry_config = temp_model.from_map(m['registryConfig'])
        if m.get('resolvedImageUri') is not None:
            self.resolved_image_uri = m.get('resolvedImageUri')
        return self


class CustomDNS(TeaModel):
    def __init__(self, dns_options=None, name_servers=None, searches=None):
        self.dns_options = dns_options  # type: list[DNSOption]
        self.name_servers = name_servers  # type: list[str]
        self.searches = searches  # type: list[str]

    def validate(self):
        if self.dns_options:
            for k in self.dns_options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CustomDNS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dnsOptions'] = []
        if self.dns_options is not None:
            for k in self.dns_options:
                result['dnsOptions'].append(k.to_map() if k else None)
        if self.name_servers is not None:
            result['nameServers'] = self.name_servers
        if self.searches is not None:
            result['searches'] = self.searches
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dns_options = []
        if m.get('dnsOptions') is not None:
            for k in m.get('dnsOptions'):
                temp_model = DNSOption()
                self.dns_options.append(temp_model.from_map(k))
        if m.get('nameServers') is not None:
            self.name_servers = m.get('nameServers')
        if m.get('searches') is not None:
            self.searches = m.get('searches')
        return self


class CustomDomain(TeaModel):
    def __init__(self, account_id=None, api_version=None, auth_config=None, cert_config=None, created_time=None,
                 domain_name=None, last_modified_time=None, protocol=None, route_config=None, subdomain_count=None,
                 tls_config=None, waf_config=None):
        self.account_id = account_id  # type: str
        self.api_version = api_version  # type: str
        self.auth_config = auth_config  # type: AuthConfig
        self.cert_config = cert_config  # type: CertConfig
        self.created_time = created_time  # type: str
        self.domain_name = domain_name  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.protocol = protocol  # type: str
        self.route_config = route_config  # type: RouteConfig
        self.subdomain_count = subdomain_count  # type: str
        self.tls_config = tls_config  # type: TLSConfig
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(CustomDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.subdomain_count is not None:
            result['subdomainCount'] = self.subdomain_count
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('subdomainCount') is not None:
            self.subdomain_count = m.get('subdomainCount')
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class CustomHealthCheckConfig(TeaModel):
    def __init__(self, failure_threshold=None, http_get_url=None, initial_delay_seconds=None, period_seconds=None,
                 success_threshold=None, timeout_seconds=None):
        self.failure_threshold = failure_threshold  # type: int
        self.http_get_url = http_get_url  # type: str
        self.initial_delay_seconds = initial_delay_seconds  # type: int
        self.period_seconds = period_seconds  # type: int
        self.success_threshold = success_threshold  # type: int
        self.timeout_seconds = timeout_seconds  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CustomHealthCheckConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold
        if self.http_get_url is not None:
            result['httpGetUrl'] = self.http_get_url
        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold
        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')
        if m.get('httpGetUrl') is not None:
            self.http_get_url = m.get('httpGetUrl')
        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')
        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')
        return self


class CustomRuntimeConfig(TeaModel):
    def __init__(self, args=None, command=None, health_check_config=None, port=None):
        self.args = args  # type: list[str]
        self.command = command  # type: list[str]
        self.health_check_config = health_check_config  # type: CustomHealthCheckConfig
        self.port = port  # type: int

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        _map = super(CustomRuntimeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('healthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['healthCheckConfig'])
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class DNSOption(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DNSOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DeadLetterQueue(TeaModel):
    def __init__(self, arn=None):
        self.arn = arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeadLetterQueue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        return self


class DeliveryOption(TeaModel):
    def __init__(self, concurrency=None, event_schema=None):
        self.concurrency = concurrency  # type: long
        self.event_schema = event_schema  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeliveryOption, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.event_schema is not None:
            result['eventSchema'] = self.event_schema
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('eventSchema') is not None:
            self.event_schema = m.get('eventSchema')
        return self


class Destination(TeaModel):
    def __init__(self, destination=None):
        self.destination = destination  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Destination, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        return self


class DestinationConfig(TeaModel):
    def __init__(self, on_failure=None, on_success=None):
        self.on_failure = on_failure  # type: Destination
        self.on_success = on_success  # type: Destination

    def validate(self):
        if self.on_failure:
            self.on_failure.validate()
        if self.on_success:
            self.on_success.validate()

    def to_map(self):
        _map = super(DestinationConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_failure is not None:
            result['onFailure'] = self.on_failure.to_map()
        if self.on_success is not None:
            result['onSuccess'] = self.on_success.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('onFailure') is not None:
            temp_model = Destination()
            self.on_failure = temp_model.from_map(m['onFailure'])
        if m.get('onSuccess') is not None:
            temp_model = Destination()
            self.on_success = temp_model.from_map(m['onSuccess'])
        return self


class EqualRule(TeaModel):
    def __init__(self, match=None, replacement=None):
        # This parameter is required.
        self.match = match  # type: str
        # This parameter is required.
        self.replacement = replacement  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EqualRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match
        if self.replacement is not None:
            result['replacement'] = self.replacement
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')
        return self


class Error(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Error, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EventBridgeTriggerConfig(TeaModel):
    def __init__(self, async_invocation_type=None, event_rule_filter_pattern=None, event_sink_config=None,
                 event_source_config=None, run_options=None, trigger_enable=None):
        self.async_invocation_type = async_invocation_type  # type: bool
        self.event_rule_filter_pattern = event_rule_filter_pattern  # type: str
        self.event_sink_config = event_sink_config  # type: EventSinkConfig
        self.event_source_config = event_source_config  # type: EventSourceConfig
        self.run_options = run_options  # type: RunOptions
        self.trigger_enable = trigger_enable  # type: bool

    def validate(self):
        if self.event_sink_config:
            self.event_sink_config.validate()
        if self.event_source_config:
            self.event_source_config.validate()
        if self.run_options:
            self.run_options.validate()

    def to_map(self):
        _map = super(EventBridgeTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_invocation_type is not None:
            result['asyncInvocationType'] = self.async_invocation_type
        if self.event_rule_filter_pattern is not None:
            result['eventRuleFilterPattern'] = self.event_rule_filter_pattern
        if self.event_sink_config is not None:
            result['eventSinkConfig'] = self.event_sink_config.to_map()
        if self.event_source_config is not None:
            result['eventSourceConfig'] = self.event_source_config.to_map()
        if self.run_options is not None:
            result['runOptions'] = self.run_options.to_map()
        if self.trigger_enable is not None:
            result['triggerEnable'] = self.trigger_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('asyncInvocationType') is not None:
            self.async_invocation_type = m.get('asyncInvocationType')
        if m.get('eventRuleFilterPattern') is not None:
            self.event_rule_filter_pattern = m.get('eventRuleFilterPattern')
        if m.get('eventSinkConfig') is not None:
            temp_model = EventSinkConfig()
            self.event_sink_config = temp_model.from_map(m['eventSinkConfig'])
        if m.get('eventSourceConfig') is not None:
            temp_model = EventSourceConfig()
            self.event_source_config = temp_model.from_map(m['eventSourceConfig'])
        if m.get('runOptions') is not None:
            temp_model = RunOptions()
            self.run_options = temp_model.from_map(m['runOptions'])
        if m.get('triggerEnable') is not None:
            self.trigger_enable = m.get('triggerEnable')
        return self


class EventSinkConfig(TeaModel):
    def __init__(self, delivery_option=None):
        self.delivery_option = delivery_option  # type: DeliveryOption

    def validate(self):
        if self.delivery_option:
            self.delivery_option.validate()

    def to_map(self):
        _map = super(EventSinkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_option is not None:
            result['deliveryOption'] = self.delivery_option.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deliveryOption') is not None:
            temp_model = DeliveryOption()
            self.delivery_option = temp_model.from_map(m['deliveryOption'])
        return self


class EventSourceConfig(TeaModel):
    def __init__(self, event_source_parameters=None, event_source_type=None):
        self.event_source_parameters = event_source_parameters  # type: EventSourceParameters
        self.event_source_type = event_source_type  # type: str

    def validate(self):
        if self.event_source_parameters:
            self.event_source_parameters.validate()

    def to_map(self):
        _map = super(EventSourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_source_parameters is not None:
            result['eventSourceParameters'] = self.event_source_parameters.to_map()
        if self.event_source_type is not None:
            result['eventSourceType'] = self.event_source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventSourceParameters') is not None:
            temp_model = EventSourceParameters()
            self.event_source_parameters = temp_model.from_map(m['eventSourceParameters'])
        if m.get('eventSourceType') is not None:
            self.event_source_type = m.get('eventSourceType')
        return self


class EventSourceParameters(TeaModel):
    def __init__(self, source_dtsparameters=None, source_kafka_parameters=None, source_mnsparameters=None,
                 source_mqttparameters=None, source_rabbit_mqparameters=None, source_rocket_mqparameters=None):
        self.source_dtsparameters = source_dtsparameters  # type: SourceDTSParameters
        self.source_kafka_parameters = source_kafka_parameters  # type: SourceKafkaParameters
        self.source_mnsparameters = source_mnsparameters  # type: SourceMNSParameters
        self.source_mqttparameters = source_mqttparameters  # type: SourceMQTTParameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: SourceRabbitMQParameters
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: SourceRocketMQParameters

    def validate(self):
        if self.source_dtsparameters:
            self.source_dtsparameters.validate()
        if self.source_kafka_parameters:
            self.source_kafka_parameters.validate()
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_mqttparameters:
            self.source_mqttparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()

    def to_map(self):
        _map = super(EventSourceParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_dtsparameters is not None:
            result['sourceDTSParameters'] = self.source_dtsparameters.to_map()
        if self.source_kafka_parameters is not None:
            result['sourceKafkaParameters'] = self.source_kafka_parameters.to_map()
        if self.source_mnsparameters is not None:
            result['sourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_mqttparameters is not None:
            result['sourceMQTTParameters'] = self.source_mqttparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['sourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['sourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sourceDTSParameters') is not None:
            temp_model = SourceDTSParameters()
            self.source_dtsparameters = temp_model.from_map(m['sourceDTSParameters'])
        if m.get('sourceKafkaParameters') is not None:
            temp_model = SourceKafkaParameters()
            self.source_kafka_parameters = temp_model.from_map(m['sourceKafkaParameters'])
        if m.get('sourceMNSParameters') is not None:
            temp_model = SourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['sourceMNSParameters'])
        if m.get('sourceMQTTParameters') is not None:
            temp_model = SourceMQTTParameters()
            self.source_mqttparameters = temp_model.from_map(m['sourceMQTTParameters'])
        if m.get('sourceRabbitMQParameters') is not None:
            temp_model = SourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['sourceRabbitMQParameters'])
        if m.get('sourceRocketMQParameters') is not None:
            temp_model = SourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['sourceRocketMQParameters'])
        return self


class Filter(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: Key

    def validate(self):
        if self.key:
            self.key.validate()

    def to_map(self):
        _map = super(Filter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            temp_model = Key()
            self.key = temp_model.from_map(m['key'])
        return self


class Function(TeaModel):
    def __init__(self, code_checksum=None, code_size=None, cpu=None, created_time=None,
                 custom_container_config=None, custom_dns=None, custom_runtime_config=None, description=None, disk_size=None,
                 environment_variables=None, function_arn=None, function_id=None, function_name=None, gpu_config=None, handler=None,
                 instance_concurrency=None, instance_lifecycle_config=None, internet_access=None, last_modified_time=None,
                 last_update_status=None, last_update_status_reason=None, last_update_status_reason_code=None, layers=None,
                 log_config=None, memory_size=None, nas_config=None, oss_mount_config=None, role=None, runtime=None, state=None,
                 state_reason=None, state_reason_code=None, tags=None, timeout=None, tracing_config=None, vpc_config=None):
        self.code_checksum = code_checksum  # type: str
        self.code_size = code_size  # type: long
        self.cpu = cpu  # type: float
        self.created_time = created_time  # type: str
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        self.custom_dns = custom_dns  # type: CustomDNS
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        self.description = description  # type: str
        self.disk_size = disk_size  # type: int
        self.environment_variables = environment_variables  # type: dict[str, str]
        self.function_arn = function_arn  # type: str
        self.function_id = function_id  # type: str
        self.function_name = function_name  # type: str
        self.gpu_config = gpu_config  # type: GPUConfig
        self.handler = handler  # type: str
        self.instance_concurrency = instance_concurrency  # type: int
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        self.internet_access = internet_access  # type: bool
        self.last_modified_time = last_modified_time  # type: str
        self.last_update_status = last_update_status  # type: str
        self.last_update_status_reason = last_update_status_reason  # type: str
        self.last_update_status_reason_code = last_update_status_reason_code  # type: str
        self.layers = layers  # type: list[FunctionLayer]
        self.log_config = log_config  # type: LogConfig
        self.memory_size = memory_size  # type: int
        self.nas_config = nas_config  # type: NASConfig
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        self.role = role  # type: str
        self.runtime = runtime  # type: str
        self.state = state  # type: str
        self.state_reason = state_reason  # type: str
        self.state_reason_code = state_reason_code  # type: str
        self.tags = tags  # type: list[Tag]
        self.timeout = timeout  # type: int
        self.tracing_config = tracing_config  # type: TracingConfig
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super(Function, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.last_update_status is not None:
            result['lastUpdateStatus'] = self.last_update_status
        if self.last_update_status_reason is not None:
            result['lastUpdateStatusReason'] = self.last_update_status_reason
        if self.last_update_status_reason_code is not None:
            result['lastUpdateStatusReasonCode'] = self.last_update_status_reason_code
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.state is not None:
            result['state'] = self.state
        if self.state_reason is not None:
            result['stateReason'] = self.state_reason
        if self.state_reason_code is not None:
            result['stateReasonCode'] = self.state_reason_code
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuConfig') is not None:
            temp_model = GPUConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lastUpdateStatus') is not None:
            self.last_update_status = m.get('lastUpdateStatus')
        if m.get('lastUpdateStatusReason') is not None:
            self.last_update_status_reason = m.get('lastUpdateStatusReason')
        if m.get('lastUpdateStatusReasonCode') is not None:
            self.last_update_status_reason_code = m.get('lastUpdateStatusReasonCode')
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = FunctionLayer()
                self.layers.append(temp_model.from_map(k))
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateReason') is not None:
            self.state_reason = m.get('stateReason')
        if m.get('stateReasonCode') is not None:
            self.state_reason_code = m.get('stateReasonCode')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class FunctionLayer(TeaModel):
    def __init__(self, arn=None, size=None):
        self.arn = arn  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(FunctionLayer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['arn'] = self.arn
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class GPUConfig(TeaModel):
    def __init__(self, gpu_memory_size=None, gpu_type=None):
        self.gpu_memory_size = gpu_memory_size  # type: int
        self.gpu_type = gpu_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GPUConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.gpu_type is not None:
            result['gpuType'] = self.gpu_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('gpuType') is not None:
            self.gpu_type = m.get('gpuType')
        return self


class GetInstanceLifecycleEventsOutput(TeaModel):
    def __init__(self, events=None, request_id=None):
        self.events = events  # type: list[InstanceEventItem]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceLifecycleEventsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = InstanceEventItem()
                self.events.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetResourceTagsOutput(TeaModel):
    def __init__(self, resouce_type=None, resource_arn=None, tags=None):
        self.resouce_type = resouce_type  # type: str
        self.resource_arn = resource_arn  # type: str
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTagsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resouce_type is not None:
            result['resouceType'] = self.resouce_type
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resouceType') is not None:
            self.resouce_type = m.get('resouceType')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class HTTPTrigger(TeaModel):
    def __init__(self, url_internet=None, url_intranet=None):
        self.url_internet = url_internet  # type: str
        self.url_intranet = url_intranet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HTTPTrigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class HTTPTriggerConfig(TeaModel):
    def __init__(self, auth_config=None, auth_type=None, disable_urlinternet=None, methods=None):
        self.auth_config = auth_config  # type: str
        self.auth_type = auth_type  # type: str
        self.disable_urlinternet = disable_urlinternet  # type: bool
        self.methods = methods  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(HTTPTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class InputCodeLocation(TeaModel):
    def __init__(self, checksum=None, oss_bucket_name=None, oss_object_name=None, zip_file=None):
        self.checksum = checksum  # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.zip_file = zip_file  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InputCodeLocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        if self.zip_file is not None:
            result['zipFile'] = self.zip_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')
        return self


class InstanceEventItem(TeaModel):
    def __init__(self, children=None, level=None, message=None, time=None, type=None):
        self.children = children  # type: list[InstanceEventItem]
        self.level = level  # type: str
        self.message = message  # type: str
        self.time = time  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InstanceEventItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['children'] = []
        if self.children is not None:
            for k in self.children:
                result['children'].append(k.to_map() if k else None)
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.children = []
        if m.get('children') is not None:
            for k in m.get('children'):
                temp_model = InstanceEventItem()
                self.children.append(temp_model.from_map(k))
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InstanceInfo(TeaModel):
    def __init__(self, created_time_ms=None, destroyed_time_ms=None, instance_id=None, qualifier=None, status=None,
                 version_id=None):
        self.created_time_ms = created_time_ms  # type: long
        self.destroyed_time_ms = destroyed_time_ms  # type: long
        self.instance_id = instance_id  # type: str
        self.qualifier = qualifier  # type: str
        self.status = status  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time_ms is not None:
            result['createdTimeMs'] = self.created_time_ms
        if self.destroyed_time_ms is not None:
            result['destroyedTimeMs'] = self.destroyed_time_ms
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.status is not None:
            result['status'] = self.status
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTimeMs') is not None:
            self.created_time_ms = m.get('createdTimeMs')
        if m.get('destroyedTimeMs') is not None:
            self.destroyed_time_ms = m.get('destroyedTimeMs')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class InstanceLifecycleConfig(TeaModel):
    def __init__(self, initializer=None, pre_stop=None):
        self.initializer = initializer  # type: LifecycleHook
        self.pre_stop = pre_stop  # type: LifecycleHook

    def validate(self):
        if self.initializer:
            self.initializer.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super(InstanceLifecycleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initializer is not None:
            result['initializer'] = self.initializer.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('initializer') is not None:
            temp_model = LifecycleHook()
            self.initializer = temp_model.from_map(m['initializer'])
        if m.get('preStop') is not None:
            temp_model = LifecycleHook()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class JobConfig(TeaModel):
    def __init__(self, max_retry_time=None, trigger_interval=None):
        self.max_retry_time = max_retry_time  # type: int
        self.trigger_interval = trigger_interval  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_retry_time is not None:
            result['maxRetryTime'] = self.max_retry_time
        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxRetryTime') is not None:
            self.max_retry_time = m.get('maxRetryTime')
        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')
        return self


class Key(TeaModel):
    def __init__(self, prefix=None, suffix=None):
        self.prefix = prefix  # type: str
        self.suffix = suffix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Key, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.suffix is not None:
            result['suffix'] = self.suffix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        return self


class Layer(TeaModel):
    def __init__(self, acl=None, code=None, code_checksum=None, code_size=None, compatible_runtime=None,
                 create_time=None, description=None, layer_name=None, layer_version_arn=None, license=None, version=None):
        self.acl = acl  # type: str
        self.code = code  # type: OutputCodeLocation
        self.code_checksum = code_checksum  # type: str
        self.code_size = code_size  # type: long
        self.compatible_runtime = compatible_runtime  # type: list[str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        # This parameter is required.
        self.layer_name = layer_name  # type: str
        self.layer_version_arn = layer_version_arn  # type: str
        self.license = license  # type: str
        self.version = version  # type: int

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super(Layer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.code_size is not None:
            result['codeSize'] = self.code_size
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.layer_name is not None:
            result['layerName'] = self.layer_name
        if self.layer_version_arn is not None:
            result['layerVersionArn'] = self.layer_version_arn
        if self.license is not None:
            result['license'] = self.license
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('code') is not None:
            temp_model = OutputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')
        if m.get('layerVersionArn') is not None:
            self.layer_version_arn = m.get('layerVersionArn')
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class LifecycleHook(TeaModel):
    def __init__(self, handler=None, timeout=None):
        self.handler = handler  # type: str
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(LifecycleHook, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class ListAliasesOutput(TeaModel):
    def __init__(self, aliases=None, next_token=None):
        self.aliases = aliases  # type: list[Alias]
        self.next_token = next_token  # type: str

    def validate(self):
        if self.aliases:
            for k in self.aliases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAliasesOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['aliases'] = []
        if self.aliases is not None:
            for k in self.aliases:
                result['aliases'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aliases = []
        if m.get('aliases') is not None:
            for k in m.get('aliases'):
                temp_model = Alias()
                self.aliases.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAsyncInvokeConfigOutput(TeaModel):
    def __init__(self, configs=None, next_token=None):
        self.configs = configs  # type: list[AsyncConfig]
        self.next_token = next_token  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAsyncInvokeConfigOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = AsyncConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAsyncTaskOutput(TeaModel):
    def __init__(self, next_token=None, tasks=None):
        self.next_token = next_token  # type: str
        self.tasks = tasks  # type: list[AsyncTask]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAsyncTaskOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = AsyncTask()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListConcurrencyConfigsOutput(TeaModel):
    def __init__(self, configs=None, next_token=None):
        self.configs = configs  # type: list[ConcurrencyConfig]
        self.next_token = next_token  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConcurrencyConfigsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ConcurrencyConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListCustomDomainOutput(TeaModel):
    def __init__(self, custom_domains=None, next_token=None):
        self.custom_domains = custom_domains  # type: list[CustomDomain]
        self.next_token = next_token  # type: str

    def validate(self):
        if self.custom_domains:
            for k in self.custom_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomDomainOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customDomains'] = []
        if self.custom_domains is not None:
            for k in self.custom_domains:
                result['customDomains'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k in m.get('customDomains'):
                temp_model = CustomDomain()
                self.custom_domains.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionsOutput(TeaModel):
    def __init__(self, functions=None, next_token=None):
        self.functions = functions  # type: list[Function]
        self.next_token = next_token  # type: str

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = Function()
                self.functions.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListInstancesOutput(TeaModel):
    def __init__(self, instances=None, request_id=None):
        self.instances = instances  # type: list[InstanceInfo]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = InstanceInfo()
                self.instances.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListLayerVersionOutput(TeaModel):
    def __init__(self, layers=None, next_version=None):
        self.layers = layers  # type: list[Layer]
        self.next_version = next_version  # type: int

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLayerVersionOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.next_version is not None:
            result['nextVersion'] = self.next_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = Layer()
                self.layers.append(temp_model.from_map(k))
        if m.get('nextVersion') is not None:
            self.next_version = m.get('nextVersion')
        return self


class ListLayersOutput(TeaModel):
    def __init__(self, layers=None, next_token=None):
        self.layers = layers  # type: list[Layer]
        self.next_token = next_token  # type: str

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLayersOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['layers'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.layers = []
        if m.get('layers') is not None:
            for k in m.get('layers'):
                temp_model = Layer()
                self.layers.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListProvisionConfigsOutput(TeaModel):
    def __init__(self, next_token=None, provision_configs=None):
        self.next_token = next_token  # type: str
        self.provision_configs = provision_configs  # type: list[ProvisionConfig]

    def validate(self):
        if self.provision_configs:
            for k in self.provision_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionConfigsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['provisionConfigs'] = []
        if self.provision_configs is not None:
            for k in self.provision_configs:
                result['provisionConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.provision_configs = []
        if m.get('provisionConfigs') is not None:
            for k in m.get('provisionConfigs'):
                temp_model = ProvisionConfig()
                self.provision_configs.append(temp_model.from_map(k))
        return self


class ListTagResourcesOutput(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[TagResource]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesOutput, self).to_map()
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
                temp_model = TagResource()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTaggedResourcesOutput(TeaModel):
    def __init__(self, next_token=None, resources=None):
        self.next_token = next_token  # type: str
        self.resources = resources  # type: list[Resource]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaggedResourcesOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = Resource()
                self.resources.append(temp_model.from_map(k))
        return self


class ListTriggersOutput(TeaModel):
    def __init__(self, next_token=None, triggers=None):
        self.next_token = next_token  # type: str
        self.triggers = triggers  # type: list[Trigger]

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTriggersOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.triggers = []
        if m.get('triggers') is not None:
            for k in m.get('triggers'):
                temp_model = Trigger()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListVersionsOutput(TeaModel):
    def __init__(self, direction=None, next_token=None, versions=None):
        self.direction = direction  # type: str
        self.next_token = next_token  # type: str
        self.versions = versions  # type: list[Version]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVersionsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = Version()
                self.versions.append(temp_model.from_map(k))
        return self


class ListVpcBindingsOutput(TeaModel):
    def __init__(self, vpc_ids=None):
        self.vpc_ids = vpc_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcBindingsOutput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_ids is not None:
            result['vpcIds'] = self.vpc_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self


class LogConfig(TeaModel):
    def __init__(self, enable_instance_metrics=None, enable_request_metrics=None, log_begin_rule=None,
                 logstore=None, project=None):
        self.enable_instance_metrics = enable_instance_metrics  # type: bool
        self.enable_request_metrics = enable_request_metrics  # type: bool
        self.log_begin_rule = log_begin_rule  # type: str
        self.logstore = logstore  # type: str
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_instance_metrics is not None:
            result['enableInstanceMetrics'] = self.enable_instance_metrics
        if self.enable_request_metrics is not None:
            result['enableRequestMetrics'] = self.enable_request_metrics
        if self.log_begin_rule is not None:
            result['logBeginRule'] = self.log_begin_rule
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableInstanceMetrics') is not None:
            self.enable_instance_metrics = m.get('enableInstanceMetrics')
        if m.get('enableRequestMetrics') is not None:
            self.enable_request_metrics = m.get('enableRequestMetrics')
        if m.get('logBeginRule') is not None:
            self.log_begin_rule = m.get('logBeginRule')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class MNSTopicTriggerConfig(TeaModel):
    def __init__(self, filter_tag=None, notify_content_format=None, notify_strategy=None):
        self.filter_tag = filter_tag  # type: str
        self.notify_content_format = notify_content_format  # type: str
        self.notify_strategy = notify_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MNSTopicTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_tag is not None:
            result['filterTag'] = self.filter_tag
        if self.notify_content_format is not None:
            result['notifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('filterTag') is not None:
            self.filter_tag = m.get('filterTag')
        if m.get('notifyContentFormat') is not None:
            self.notify_content_format = m.get('notifyContentFormat')
        if m.get('notifyStrategy') is not None:
            self.notify_strategy = m.get('notifyStrategy')
        return self


class NASConfig(TeaModel):
    def __init__(self, group_id=None, mount_points=None, user_id=None):
        self.group_id = group_id  # type: int
        self.mount_points = mount_points  # type: list[NASMountConfig]
        self.user_id = user_id  # type: int

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NASConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = NASMountConfig()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class NASMountConfig(TeaModel):
    def __init__(self, enable_tls=None, mount_dir=None, server_addr=None):
        self.enable_tls = enable_tls  # type: bool
        self.mount_dir = mount_dir  # type: str
        self.server_addr = server_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NASMountConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tls is not None:
            result['enableTLS'] = self.enable_tls
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableTLS') is not None:
            self.enable_tls = m.get('enableTLS')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class OSSMountConfig(TeaModel):
    def __init__(self, mount_points=None):
        self.mount_points = mount_points  # type: list[OSSMountPoint]

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(OSSMountConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['mountPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k in m.get('mountPoints'):
                temp_model = OSSMountPoint()
                self.mount_points.append(temp_model.from_map(k))
        return self


class OSSMountPoint(TeaModel):
    def __init__(self, bucket_name=None, bucket_path=None, endpoint=None, mount_dir=None, read_only=None):
        self.bucket_name = bucket_name  # type: str
        self.bucket_path = bucket_path  # type: str
        self.endpoint = endpoint  # type: str
        self.mount_dir = mount_dir  # type: str
        self.read_only = read_only  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OSSMountPoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class OSSTriggerConfig(TeaModel):
    def __init__(self, events=None, filter=None):
        self.events = events  # type: list[str]
        self.filter = filter  # type: Filter

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super(OSSTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['events'] = self.events
        if self.filter is not None:
            result['filter'] = self.filter.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('events') is not None:
            self.events = m.get('events')
        if m.get('filter') is not None:
            temp_model = Filter()
            self.filter = temp_model.from_map(m['filter'])
        return self


class OutputCodeLocation(TeaModel):
    def __init__(self, location=None, repository_type=None):
        self.location = location  # type: str
        self.repository_type = repository_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OutputCodeLocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['location'] = self.location
        if self.repository_type is not None:
            result['repositoryType'] = self.repository_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('repositoryType') is not None:
            self.repository_type = m.get('repositoryType')
        return self


class OutputFuncCode(TeaModel):
    def __init__(self, checksum=None, url=None):
        self.checksum = checksum  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OutputFuncCode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checksum is not None:
            result['checksum'] = self.checksum
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class PathConfig(TeaModel):
    def __init__(self, function_name=None, methods=None, path=None, qualifier=None, rewrite_config=None):
        # This parameter is required.
        self.function_name = function_name  # type: str
        self.methods = methods  # type: list[str]
        # This parameter is required.
        self.path = path  # type: str
        self.qualifier = qualifier  # type: str
        self.rewrite_config = rewrite_config  # type: RewriteConfig

    def validate(self):
        if self.rewrite_config:
            self.rewrite_config.validate()

    def to_map(self):
        _map = super(PathConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.methods is not None:
            result['methods'] = self.methods
        if self.path is not None:
            result['path'] = self.path
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.rewrite_config is not None:
            result['rewriteConfig'] = self.rewrite_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('rewriteConfig') is not None:
            temp_model = RewriteConfig()
            self.rewrite_config = temp_model.from_map(m['rewriteConfig'])
        return self


class ProvisionConfig(TeaModel):
    def __init__(self, always_allocate_cpu=None, always_allocate_gpu=None, current=None, current_error=None,
                 default_target=None, function_arn=None, scheduled_actions=None, target=None, target_tracking_policies=None):
        self.always_allocate_cpu = always_allocate_cpu  # type: bool
        self.always_allocate_gpu = always_allocate_gpu  # type: bool
        self.current = current  # type: long
        self.current_error = current_error  # type: str
        self.default_target = default_target  # type: long
        self.function_arn = function_arn  # type: str
        self.scheduled_actions = scheduled_actions  # type: list[ScheduledAction]
        self.target = target  # type: long
        self.target_tracking_policies = target_tracking_policies  # type: list[TargetTrackingPolicy]

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ProvisionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        if self.current is not None:
            result['current'] = self.current
        if self.current_error is not None:
            result['currentError'] = self.current_error
        if self.default_target is not None:
            result['defaultTarget'] = self.default_target
        if self.function_arn is not None:
            result['functionArn'] = self.function_arn
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')
        if m.get('defaultTarget') is not None:
            self.default_target = m.get('defaultTarget')
        if m.get('functionArn') is not None:
            self.function_arn = m.get('functionArn')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledAction()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicy()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class PublishVersionInput(TeaModel):
    def __init__(self, description=None):
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishVersionInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class PutAsyncInvokeConfigInput(TeaModel):
    def __init__(self, async_task=None, destination_config=None, max_async_event_age_in_seconds=None,
                 max_async_retry_attempts=None):
        self.async_task = async_task  # type: bool
        self.destination_config = destination_config  # type: DestinationConfig
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds  # type: long
        self.max_async_retry_attempts = max_async_retry_attempts  # type: long

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super(PutAsyncInvokeConfigInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task is not None:
            result['asyncTask'] = self.async_task
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('asyncTask') is not None:
            self.async_task = m.get('asyncTask')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        return self


class PutConcurrencyInput(TeaModel):
    def __init__(self, reserved_concurrency=None):
        # This parameter is required.
        self.reserved_concurrency = reserved_concurrency  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutConcurrencyInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_concurrency is not None:
            result['reservedConcurrency'] = self.reserved_concurrency
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('reservedConcurrency') is not None:
            self.reserved_concurrency = m.get('reservedConcurrency')
        return self


class PutProvisionConfigInput(TeaModel):
    def __init__(self, always_allocate_cpu=None, always_allocate_gpu=None, default_target=None,
                 scheduled_actions=None, target=None, target_tracking_policies=None):
        self.always_allocate_cpu = always_allocate_cpu  # type: bool
        self.always_allocate_gpu = always_allocate_gpu  # type: bool
        self.default_target = default_target  # type: long
        self.scheduled_actions = scheduled_actions  # type: list[ScheduledAction]
        # This parameter is required.
        self.target = target  # type: long
        self.target_tracking_policies = target_tracking_policies  # type: list[TargetTrackingPolicy]

    def validate(self):
        if self.scheduled_actions:
            for k in self.scheduled_actions:
                if k:
                    k.validate()
        if self.target_tracking_policies:
            for k in self.target_tracking_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PutProvisionConfigInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.always_allocate_gpu is not None:
            result['alwaysAllocateGPU'] = self.always_allocate_gpu
        if self.default_target is not None:
            result['defaultTarget'] = self.default_target
        result['scheduledActions'] = []
        if self.scheduled_actions is not None:
            for k in self.scheduled_actions:
                result['scheduledActions'].append(k.to_map() if k else None)
        if self.target is not None:
            result['target'] = self.target
        result['targetTrackingPolicies'] = []
        if self.target_tracking_policies is not None:
            for k in self.target_tracking_policies:
                result['targetTrackingPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        if m.get('alwaysAllocateGPU') is not None:
            self.always_allocate_gpu = m.get('alwaysAllocateGPU')
        if m.get('defaultTarget') is not None:
            self.default_target = m.get('defaultTarget')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledAction()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicy()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class RegexRule(TeaModel):
    def __init__(self, match=None, replacement=None):
        # This parameter is required.
        self.match = match  # type: str
        # This parameter is required.
        self.replacement = replacement  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegexRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match
        if self.replacement is not None:
            result['replacement'] = self.replacement
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')
        return self


class RegistryAuthConfig(TeaModel):
    def __init__(self, password=None, user_name=None):
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegistryAuthConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class RegistryCertConfig(TeaModel):
    def __init__(self, insecure=None, root_ca_cert_base_64=None):
        self.insecure = insecure  # type: bool
        self.root_ca_cert_base_64 = root_ca_cert_base_64  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegistryCertConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.insecure is not None:
            result['insecure'] = self.insecure
        if self.root_ca_cert_base_64 is not None:
            result['rootCaCertBase64'] = self.root_ca_cert_base_64
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('insecure') is not None:
            self.insecure = m.get('insecure')
        if m.get('rootCaCertBase64') is not None:
            self.root_ca_cert_base_64 = m.get('rootCaCertBase64')
        return self


class RegistryConfig(TeaModel):
    def __init__(self, auth_config=None, cert_config=None, network_config=None):
        self.auth_config = auth_config  # type: RegistryAuthConfig
        self.cert_config = cert_config  # type: RegistryCertConfig
        self.network_config = network_config  # type: RegistryNetworkConfig

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        _map = super(RegistryConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = RegistryAuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = RegistryCertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('networkConfig') is not None:
            temp_model = RegistryNetworkConfig()
            self.network_config = temp_model.from_map(m['networkConfig'])
        return self


class RegistryNetworkConfig(TeaModel):
    def __init__(self, security_group_id=None, v_switch_id=None, vpc_id=None):
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegistryNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class Resource(TeaModel):
    def __init__(self, resouce_type=None, resource_arn=None, tags=None):
        self.resouce_type = resouce_type  # type: str
        self.resource_arn = resource_arn  # type: str
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(Resource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resouce_type is not None:
            result['resouceType'] = self.resouce_type
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resouceType') is not None:
            self.resouce_type = m.get('resouceType')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class RetryStrategy(TeaModel):
    def __init__(self, push_retry_strategy=None):
        self.push_retry_strategy = push_retry_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')
        return self


class RewriteConfig(TeaModel):
    def __init__(self, equal_rules=None, regex_rules=None, wildcard_rules=None):
        self.equal_rules = equal_rules  # type: list[EqualRule]
        self.regex_rules = regex_rules  # type: list[RegexRule]
        self.wildcard_rules = wildcard_rules  # type: list[WildcardRule]

    def validate(self):
        if self.equal_rules:
            for k in self.equal_rules:
                if k:
                    k.validate()
        if self.regex_rules:
            for k in self.regex_rules:
                if k:
                    k.validate()
        if self.wildcard_rules:
            for k in self.wildcard_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RewriteConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['equalRules'] = []
        if self.equal_rules is not None:
            for k in self.equal_rules:
                result['equalRules'].append(k.to_map() if k else None)
        result['regexRules'] = []
        if self.regex_rules is not None:
            for k in self.regex_rules:
                result['regexRules'].append(k.to_map() if k else None)
        result['wildcardRules'] = []
        if self.wildcard_rules is not None:
            for k in self.wildcard_rules:
                result['wildcardRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.equal_rules = []
        if m.get('equalRules') is not None:
            for k in m.get('equalRules'):
                temp_model = EqualRule()
                self.equal_rules.append(temp_model.from_map(k))
        self.regex_rules = []
        if m.get('regexRules') is not None:
            for k in m.get('regexRules'):
                temp_model = RegexRule()
                self.regex_rules.append(temp_model.from_map(k))
        self.wildcard_rules = []
        if m.get('wildcardRules') is not None:
            for k in m.get('wildcardRules'):
                temp_model = WildcardRule()
                self.wildcard_rules.append(temp_model.from_map(k))
        return self


class RouteConfig(TeaModel):
    def __init__(self, routes=None):
        self.routes = routes  # type: list[PathConfig]

    def validate(self):
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RouteConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['routes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.routes = []
        if m.get('routes') is not None:
            for k in m.get('routes'):
                temp_model = PathConfig()
                self.routes.append(temp_model.from_map(k))
        return self


class RunOptions(TeaModel):
    def __init__(self, batch_window=None, dead_letter_queue=None, errors_tolerance=None, mode=None,
                 retry_strategy=None):
        self.batch_window = batch_window  # type: BatchWindow
        self.dead_letter_queue = dead_letter_queue  # type: DeadLetterQueue
        self.errors_tolerance = errors_tolerance  # type: str
        self.mode = mode  # type: str
        self.retry_strategy = retry_strategy  # type: RetryStrategy

    def validate(self):
        if self.batch_window:
            self.batch_window.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.retry_strategy:
            self.retry_strategy.validate()

    def to_map(self):
        _map = super(RunOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_window is not None:
            result['batchWindow'] = self.batch_window.to_map()
        if self.dead_letter_queue is not None:
            result['deadLetterQueue'] = self.dead_letter_queue.to_map()
        if self.errors_tolerance is not None:
            result['errorsTolerance'] = self.errors_tolerance
        if self.mode is not None:
            result['mode'] = self.mode
        if self.retry_strategy is not None:
            result['retryStrategy'] = self.retry_strategy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('batchWindow') is not None:
            temp_model = BatchWindow()
            self.batch_window = temp_model.from_map(m['batchWindow'])
        if m.get('deadLetterQueue') is not None:
            temp_model = DeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m['deadLetterQueue'])
        if m.get('errorsTolerance') is not None:
            self.errors_tolerance = m.get('errorsTolerance')
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('retryStrategy') is not None:
            temp_model = RetryStrategy()
            self.retry_strategy = temp_model.from_map(m['retryStrategy'])
        return self


class SLSTriggerConfig(TeaModel):
    def __init__(self, enable=None, function_parameter=None, job_config=None, log_config=None, source_config=None):
        self.enable = enable  # type: bool
        self.function_parameter = function_parameter  # type: dict[str, str]
        self.job_config = job_config  # type: JobConfig
        self.log_config = log_config  # type: SLSTriggerLogConfig
        self.source_config = source_config  # type: SourceConfig

    def validate(self):
        if self.job_config:
            self.job_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.source_config:
            self.source_config.validate()

    def to_map(self):
        _map = super(SLSTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.function_parameter is not None:
            result['functionParameter'] = self.function_parameter
        if self.job_config is not None:
            result['jobConfig'] = self.job_config.to_map()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.source_config is not None:
            result['sourceConfig'] = self.source_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('functionParameter') is not None:
            self.function_parameter = m.get('functionParameter')
        if m.get('jobConfig') is not None:
            temp_model = JobConfig()
            self.job_config = temp_model.from_map(m['jobConfig'])
        if m.get('logConfig') is not None:
            temp_model = SLSTriggerLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('sourceConfig') is not None:
            temp_model = SourceConfig()
            self.source_config = temp_model.from_map(m['sourceConfig'])
        return self


class SLSTriggerLogConfig(TeaModel):
    def __init__(self, logstore=None, project=None):
        self.logstore = logstore  # type: str
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SLSTriggerLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class ScheduledAction(TeaModel):
    def __init__(self, end_time=None, name=None, schedule_expression=None, start_time=None, target=None,
                 time_zone=None):
        self.end_time = end_time  # type: str
        # This parameter is required.
        self.name = name  # type: str
        # This parameter is required.
        self.schedule_expression = schedule_expression  # type: str
        self.start_time = start_time  # type: str
        # This parameter is required.
        self.target = target  # type: long
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScheduledAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.target is not None:
            result['target'] = self.target
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class SourceConfig(TeaModel):
    def __init__(self, logstore=None, start_time=None):
        self.logstore = logstore  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class SourceDTSParameters(TeaModel):
    def __init__(self, broker_url=None, init_check_point=None, password=None, region_id=None, sid=None, task_id=None,
                 topic=None, username=None):
        self.broker_url = broker_url  # type: str
        self.init_check_point = init_check_point  # type: int
        self.password = password  # type: str
        self.region_id = region_id  # type: str
        self.sid = sid  # type: str
        self.task_id = task_id  # type: str
        self.topic = topic  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceDTSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_url is not None:
            result['BrokerUrl'] = self.broker_url
        if self.init_check_point is not None:
            result['InitCheckPoint'] = self.init_check_point
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerUrl') is not None:
            self.broker_url = m.get('BrokerUrl')
        if m.get('InitCheckPoint') is not None:
            self.init_check_point = m.get('InitCheckPoint')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class SourceKafkaParameters(TeaModel):
    def __init__(self, consumer_group=None, instance_id=None, network=None, offset_reset=None, region_id=None,
                 security_group_id=None, topic=None, v_switch_ids=None, vpc_id=None):
        self.consumer_group = consumer_group  # type: str
        self.instance_id = instance_id  # type: str
        self.network = network  # type: str
        self.offset_reset = offset_reset  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.topic = topic  # type: str
        self.v_switch_ids = v_switch_ids  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceKafkaParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network is not None:
            result['Network'] = self.network
        if self.offset_reset is not None:
            result['OffsetReset'] = self.offset_reset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('OffsetReset') is not None:
            self.offset_reset = m.get('OffsetReset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class SourceMNSParameters(TeaModel):
    def __init__(self, is_base_64decode=None, queue_name=None, region_id=None):
        self.is_base_64decode = is_base_64decode  # type: bool
        self.queue_name = queue_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceMNSParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_base_64decode is not None:
            result['IsBase64Decode'] = self.is_base_64decode
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsBase64Decode') is not None:
            self.is_base_64decode = m.get('IsBase64Decode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SourceMQTTParameters(TeaModel):
    def __init__(self, instance_id=None, region_id=None, topic=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceMQTTParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class SourceRabbitMQParameters(TeaModel):
    def __init__(self, instance_id=None, queue_name=None, region_id=None, virtual_host_name=None):
        self.instance_id = instance_id  # type: str
        self.queue_name = queue_name  # type: str
        self.region_id = region_id  # type: str
        self.virtual_host_name = virtual_host_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceRabbitMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_host_name is not None:
            result['VirtualHostName'] = self.virtual_host_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualHostName') is not None:
            self.virtual_host_name = m.get('VirtualHostName')
        return self


class SourceRocketMQParameters(TeaModel):
    def __init__(self, auth_type=None, filter_type=None, group_id=None, instance_endpoint=None, instance_id=None,
                 instance_network=None, instance_password=None, instance_security_group_id=None, instance_type=None,
                 instance_username=None, instance_vswitch_ids=None, instance_vpc_id=None, offset=None, region_id=None, tag=None,
                 timestamp=None, topic=None):
        self.auth_type = auth_type  # type: str
        self.filter_type = filter_type  # type: str
        self.group_id = group_id  # type: str
        self.instance_endpoint = instance_endpoint  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_network = instance_network  # type: str
        self.instance_password = instance_password  # type: str
        self.instance_security_group_id = instance_security_group_id  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_username = instance_username  # type: str
        self.instance_vswitch_ids = instance_vswitch_ids  # type: str
        self.instance_vpc_id = instance_vpc_id  # type: str
        self.offset = offset  # type: str
        self.region_id = region_id  # type: str
        self.tag = tag  # type: str
        self.timestamp = timestamp  # type: int
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_endpoint is not None:
            result['InstanceEndpoint'] = self.instance_endpoint
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_network is not None:
            result['InstanceNetwork'] = self.instance_network
        if self.instance_password is not None:
            result['InstancePassword'] = self.instance_password
        if self.instance_security_group_id is not None:
            result['InstanceSecurityGroupId'] = self.instance_security_group_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_username is not None:
            result['InstanceUsername'] = self.instance_username
        if self.instance_vswitch_ids is not None:
            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
        if self.instance_vpc_id is not None:
            result['InstanceVpcId'] = self.instance_vpc_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceEndpoint') is not None:
            self.instance_endpoint = m.get('InstanceEndpoint')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNetwork') is not None:
            self.instance_network = m.get('InstanceNetwork')
        if m.get('InstancePassword') is not None:
            self.instance_password = m.get('InstancePassword')
        if m.get('InstanceSecurityGroupId') is not None:
            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsername') is not None:
            self.instance_username = m.get('InstanceUsername')
        if m.get('InstanceVSwitchIds') is not None:
            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
        if m.get('InstanceVpcId') is not None:
            self.instance_vpc_id = m.get('InstanceVpcId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class TLSConfig(TeaModel):
    def __init__(self, cipher_suites=None, max_version=None, min_version=None):
        # This parameter is required.
        self.cipher_suites = cipher_suites  # type: list[str]
        self.max_version = max_version  # type: str
        # This parameter is required.
        self.min_version = min_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TLSConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cipher_suites is not None:
            result['cipherSuites'] = self.cipher_suites
        if self.max_version is not None:
            result['maxVersion'] = self.max_version
        if self.min_version is not None:
            result['minVersion'] = self.min_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cipherSuites') is not None:
            self.cipher_suites = m.get('cipherSuites')
        if m.get('maxVersion') is not None:
            self.max_version = m.get('maxVersion')
        if m.get('minVersion') is not None:
            self.min_version = m.get('minVersion')
        return self


class Tag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tag, self).to_map()
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


class TagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class TagResourceInput(TeaModel):
    def __init__(self, resource_arn=None, tags=None):
        # This parameter is required.
        self.resource_arn = resource_arn  # type: str
        # This parameter is required.
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourceInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self


class TagResourcesInput(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        # This parameter is required.
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        # This parameter is required.
        self.tag = tag  # type: list[Tag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = Tag()
                self.tag.append(temp_model.from_map(k))
        return self


class TargetTrackingPolicy(TeaModel):
    def __init__(self, end_time=None, max_capacity=None, metric_target=None, metric_type=None, min_capacity=None,
                 name=None, start_time=None, time_zone=None):
        self.end_time = end_time  # type: str
        # This parameter is required.
        self.max_capacity = max_capacity  # type: long
        # This parameter is required.
        self.metric_target = metric_target  # type: float
        # This parameter is required.
        self.metric_type = metric_type  # type: str
        # This parameter is required.
        self.min_capacity = min_capacity  # type: long
        # This parameter is required.
        self.name = name  # type: str
        self.start_time = start_time  # type: str
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetTrackingPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_capacity is not None:
            result['maxCapacity'] = self.max_capacity
        if self.metric_target is not None:
            result['metricTarget'] = self.metric_target
        if self.metric_type is not None:
            result['metricType'] = self.metric_type
        if self.min_capacity is not None:
            result['minCapacity'] = self.min_capacity
        if self.name is not None:
            result['name'] = self.name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxCapacity') is not None:
            self.max_capacity = m.get('maxCapacity')
        if m.get('metricTarget') is not None:
            self.metric_target = m.get('metricTarget')
        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')
        if m.get('minCapacity') is not None:
            self.min_capacity = m.get('minCapacity')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class TimerTriggerConfig(TeaModel):
    def __init__(self, cron_expression=None, enable=None, payload=None):
        self.cron_expression = cron_expression  # type: str
        self.enable = enable  # type: bool
        self.payload = payload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TimerTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression
        if self.enable is not None:
            result['enable'] = self.enable
        if self.payload is not None:
            result['payload'] = self.payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        return self


class TracingConfig(TeaModel):
    def __init__(self, params=None, type=None):
        self.params = params  # type: dict[str, str]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TracingConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Trigger(TeaModel):
    def __init__(self, created_time=None, description=None, http_trigger=None, invocation_role=None,
                 last_modified_time=None, qualifier=None, source_arn=None, status=None, target_arn=None, trigger_config=None,
                 trigger_id=None, trigger_name=None, trigger_type=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.http_trigger = http_trigger  # type: HTTPTrigger
        self.invocation_role = invocation_role  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.qualifier = qualifier  # type: str
        self.source_arn = source_arn  # type: str
        self.status = status  # type: str
        self.target_arn = target_arn  # type: str
        self.trigger_config = trigger_config  # type: str
        self.trigger_id = trigger_id  # type: str
        self.trigger_name = trigger_name  # type: str
        self.trigger_type = trigger_type  # type: str

    def validate(self):
        if self.http_trigger:
            self.http_trigger.validate()

    def to_map(self):
        _map = super(Trigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.http_trigger is not None:
            result['httpTrigger'] = self.http_trigger.to_map()
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.status is not None:
            result['status'] = self.status
        if self.target_arn is not None:
            result['targetArn'] = self.target_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('httpTrigger') is not None:
            temp_model = HTTPTrigger()
            self.http_trigger = temp_model.from_map(m['httpTrigger'])
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('targetArn') is not None:
            self.target_arn = m.get('targetArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        return self


class UpdateAliasInput(TeaModel):
    def __init__(self, additional_version_weight=None, description=None, version_id=None):
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        self.description = description  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliasInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.description is not None:
            result['description'] = self.description
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateCustomDomainInput(TeaModel):
    def __init__(self, auth_config=None, cert_config=None, protocol=None, route_config=None, tls_config=None,
                 waf_config=None):
        self.auth_config = auth_config  # type: AuthConfig
        self.cert_config = cert_config  # type: CertConfig
        self.protocol = protocol  # type: str
        self.route_config = route_config  # type: RouteConfig
        self.tls_config = tls_config  # type: TLSConfig
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(UpdateCustomDomainInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()
        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()
        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = AuthConfig()
            self.auth_config = temp_model.from_map(m['authConfig'])
        if m.get('certConfig') is not None:
            temp_model = CertConfig()
            self.cert_config = temp_model.from_map(m['certConfig'])
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('routeConfig') is not None:
            temp_model = RouteConfig()
            self.route_config = temp_model.from_map(m['routeConfig'])
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class UpdateFunctionInput(TeaModel):
    def __init__(self, code=None, cpu=None, custom_container_config=None, custom_dns=None,
                 custom_runtime_config=None, description=None, disk_size=None, environment_variables=None, gpu_config=None, handler=None,
                 instance_concurrency=None, instance_lifecycle_config=None, internet_access=None, layers=None, log_config=None,
                 memory_size=None, nas_config=None, oss_mount_config=None, role=None, runtime=None, timeout=None,
                 tracing_config=None, vpc_config=None):
        self.code = code  # type: InputCodeLocation
        self.cpu = cpu  # type: float
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        self.custom_dns = custom_dns  # type: CustomDNS
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        self.description = description  # type: str
        self.disk_size = disk_size  # type: int
        self.environment_variables = environment_variables  # type: dict[str, str]
        self.gpu_config = gpu_config  # type: GPUConfig
        self.handler = handler  # type: str
        self.instance_concurrency = instance_concurrency  # type: int
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        self.internet_access = internet_access  # type: bool
        self.layers = layers  # type: list[str]
        self.log_config = log_config  # type: LogConfig
        self.memory_size = memory_size  # type: int
        self.nas_config = nas_config  # type: NASConfig
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        self.role = role  # type: str
        self.runtime = runtime  # type: str
        self.timeout = timeout  # type: int
        self.tracing_config = tracing_config  # type: TracingConfig
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.gpu_config:
            self.gpu_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.nas_config:
            self.nas_config.validate()
        if self.oss_mount_config:
            self.oss_mount_config.validate()
        if self.tracing_config:
            self.tracing_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super(UpdateFunctionInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_config is not None:
            result['gpuConfig'] = self.gpu_config.to_map()
        if self.handler is not None:
            result['handler'] = self.handler
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.layers is not None:
            result['layers'] = self.layers
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            temp_model = InputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuConfig') is not None:
            temp_model = GPUConfig()
            self.gpu_config = temp_model.from_map(m['gpuConfig'])
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateTriggerInput(TeaModel):
    def __init__(self, description=None, invocation_role=None, qualifier=None, trigger_config=None):
        self.description = description  # type: str
        self.invocation_role = invocation_role  # type: str
        self.qualifier = qualifier  # type: str
        self.trigger_config = trigger_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        return self


class VPCConfig(TeaModel):
    def __init__(self, role=None, security_group_id=None, v_switch_ids=None, vpc_id=None):
        self.role = role  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VPCConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['role'] = self.role
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class Version(TeaModel):
    def __init__(self, created_time=None, description=None, last_modified_time=None, version_id=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Version, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class WAFConfig(TeaModel):
    def __init__(self, enable_waf=None):
        self.enable_waf = enable_waf  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(WAFConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_waf is not None:
            result['enableWAF'] = self.enable_waf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableWAF') is not None:
            self.enable_waf = m.get('enableWAF')
        return self


class WildcardRule(TeaModel):
    def __init__(self, match=None, replacement=None):
        # This parameter is required.
        self.match = match  # type: str
        # This parameter is required.
        self.replacement = replacement  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WildcardRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['match'] = self.match
        if self.replacement is not None:
            result['replacement'] = self.replacement
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('match') is not None:
            self.match = m.get('match')
        if m.get('replacement') is not None:
            self.replacement = m.get('replacement')
        return self


class CreateAliasRequest(TeaModel):
    def __init__(self, body=None):
        # The request parameters for creating an alias.
        # 
        # This parameter is required.
        self.body = body  # type: CreateAliasInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateAliasInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Alias

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAliasResponse, self).to_map()
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
            temp_model = Alias()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainRequest(TeaModel):
    def __init__(self, body=None):
        # The information about the custom domain name.
        # 
        # This parameter is required.
        self.body = body  # type: CreateCustomDomainInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateCustomDomainInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CustomDomain

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCustomDomainResponse, self).to_map()
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
            temp_model = CustomDomain()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(self, body=None):
        # The information about function configurations.
        # 
        # This parameter is required.
        self.body = body  # type: CreateFunctionInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateFunctionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Function

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFunctionResponse, self).to_map()
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
            temp_model = Function()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionRequest(TeaModel):
    def __init__(self, body=None):
        # The information about layer configurations.
        # 
        # This parameter is required.
        self.body = body  # type: CreateLayerVersionInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLayerVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateLayerVersionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Layer

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLayerVersionResponse, self).to_map()
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(self, body=None):
        # The trigger configurations.
        # 
        # This parameter is required.
        self.body = body  # type: CreateTriggerInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateTriggerInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Trigger

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTriggerResponse, self).to_map()
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
            temp_model = Trigger()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingRequest(TeaModel):
    def __init__(self, body=None):
        # The VPC binding configurations.
        # 
        # This parameter is required.
        self.body = body  # type: CreateVpcBindingInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcBindingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateVpcBindingInput()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcBindingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAliasResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAsyncInvokeConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAsyncInvokeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeleteAsyncInvokeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAsyncInvokeConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteConcurrencyConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConcurrencyConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFunctionVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteLayerVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLayerVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteProvisionConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The function alias or LATEST.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProvisionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class DeleteProvisionConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProvisionConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteVpcBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcBindingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Alias

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAliasResponse, self).to_map()
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
            temp_model = Alias()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncInvokeConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncInvokeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetAsyncInvokeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsyncConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncInvokeConfigResponse, self).to_map()
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
            temp_model = AsyncConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncTaskRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsyncTask

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncTaskResponse, self).to_map()
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
            temp_model = AsyncTask()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConcurrencyConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConcurrencyConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConcurrencyConfigResponse, self).to_map()
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
            temp_model = ConcurrencyConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CustomDomain

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCustomDomainResponse, self).to_map()
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
            temp_model = CustomDomain()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionRequest(TeaModel):
    def __init__(self, qualifier=None):
        # 2023-03-10T10:10:10Z
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Function

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionResponse, self).to_map()
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
            temp_model = Function()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCodeRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetFunctionCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OutputFuncCode

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionCodeResponse, self).to_map()
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
            temp_model = OutputFuncCode()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Layer

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLayerVersionResponse, self).to_map()
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionByArnResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Layer

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLayerVersionByArnResponse, self).to_map()
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
            temp_model = Layer()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The function alias or LATEST.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class GetProvisionConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProvisionConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProvisionConfigResponse, self).to_map()
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
            temp_model = ProvisionConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Trigger

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTriggerResponse, self).to_map()
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
            temp_model = Trigger()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFunctionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_async_task_id=None, x_fc_invocation_type=None, x_fc_log_type=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of the asynchronous task. You must enable the asynchronous task feature in advance.
        # 
        # >  If you use an SDK to invoke a function, we recommend that you specify a business-related ID to facilitate subsequent operations. For example, a video processing function can use video file names as invocation IDs. This way, you can easily check whether a video is successfully processed or terminated before it is processed. The ID can start only with letters or underscores. An ID can contain *letters, digits (0 - 9), underscores*, and hyphens (-). It can be up to 128 characters in length. If you do not specify the ID of the asynchronous invocation, the system automatically generates an ID.
        self.x_fc_async_task_id = x_fc_async_task_id  # type: str
        # The type of function invocation. Valid values: Sync and Async.
        self.x_fc_invocation_type = x_fc_invocation_type  # type: str
        # The log type of function invocation. Valid values: None and Tail.
        self.x_fc_log_type = x_fc_log_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeFunctionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_async_task_id is not None:
            result['x-fc-async-task-id'] = self.x_fc_async_task_id
        if self.x_fc_invocation_type is not None:
            result['x-fc-invocation-type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['x-fc-log-type'] = self.x_fc_log_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-fc-async-task-id') is not None:
            self.x_fc_async_task_id = m.get('x-fc-async-task-id')
        if m.get('x-fc-invocation-type') is not None:
            self.x_fc_invocation_type = m.get('x-fc-invocation-type')
        if m.get('x-fc-log-type') is not None:
            self.x_fc_log_type = m.get('x-fc-log-type')
        return self


class InvokeFunctionRequest(TeaModel):
    def __init__(self, body=None, qualifier=None):
        # The request parameters of function invocation.
        self.body = body  # type: READABLE
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class InvokeFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: READABLE

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeFunctionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ListAliasesRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None):
        # The number of aliases returned.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The alias prefix.
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliasesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAliasesOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAliasesResponse, self).to_map()
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
            temp_model = ListAliasesOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncInvokeConfigsRequest(TeaModel):
    def __init__(self, function_name=None, limit=None, next_token=None):
        # The function name. If you do not configure this parameter, the asynchronous invocation configurations of all functions are displayed.
        self.function_name = function_name  # type: str
        # The maximum number of entries to be returned.
        self.limit = limit  # type: int
        # The paging information. This parameter specifies the start point of the query.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsyncInvokeConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAsyncInvokeConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAsyncInvokeConfigOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAsyncInvokeConfigsResponse, self).to_map()
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
            temp_model = ListAsyncInvokeConfigOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncTasksRequest(TeaModel):
    def __init__(self, include_payload=None, limit=None, next_token=None, prefix=None, qualifier=None,
                 sort_order_by_time=None, started_time_begin=None, started_time_end=None, status=None):
        # Specifies whether to return input parameters of the asynchronous tasks. Valid values:
        # 
        # *   true: returns the `invocationPayload` parameter in the response.
        # *   false: does not return the `invocationPayload` parameter in the response.
        # 
        # >  The `invocationPayload` parameter indicates the input parameters of an asynchronous task.
        self.include_payload = include_payload  # type: bool
        # The number of asynchronous tasks to return. The default value is 20. Valid values: [1,100].
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The ID prefix of asynchronous tasks. If this parameter is specified, a list of asynchronous tasks whose IDs match the prefix is returned.
        self.prefix = prefix  # type: str
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str
        # The order in which the returned asynchronous tasks are sorted.
        # 
        # *   asc: in ascending order.
        # *   desc: in descending order.
        self.sort_order_by_time = sort_order_by_time  # type: str
        # The start time of the period during which the asynchronous tasks are initiated.
        self.started_time_begin = started_time_begin  # type: long
        # The end time of the period during which the asynchronous tasks are initiated.
        self.started_time_end = started_time_end  # type: long
        # The state of asynchronous tasks. The following items list the states of an asynchronous task:
        # 
        # *   Enqueued: The asynchronous invocation is enqueued and is waiting to be executed.
        # *   Succeeded: The invocation is successful.
        # *   Failed: The invocation fails.
        # *   Running: The invocation is being executed.
        # *   Stopped: The invocation is terminated.
        # *   Stopping: The invocation is being terminated.
        # *   Invalid: The invocation is invalid and not executed due to specific reasons. For example, the function is deleted.
        # *   Expired: The maximum validity period of messages is specified for asynchronous invocation. The invocation is discarded and not executed because the specified maximum validity period has elapsed.
        # *   Retrying: The asynchronous invocation is being retried due to an execution error.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsyncTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_payload is not None:
            result['includePayload'] = self.include_payload
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.sort_order_by_time is not None:
            result['sortOrderByTime'] = self.sort_order_by_time
        if self.started_time_begin is not None:
            result['startedTimeBegin'] = self.started_time_begin
        if self.started_time_end is not None:
            result['startedTimeEnd'] = self.started_time_end
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('includePayload') is not None:
            self.include_payload = m.get('includePayload')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sortOrderByTime') is not None:
            self.sort_order_by_time = m.get('sortOrderByTime')
        if m.get('startedTimeBegin') is not None:
            self.started_time_begin = m.get('startedTimeBegin')
        if m.get('startedTimeEnd') is not None:
            self.started_time_end = m.get('startedTimeEnd')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAsyncTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAsyncTaskOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAsyncTasksResponse, self).to_map()
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
            temp_model = ListAsyncTaskOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConcurrencyConfigsRequest(TeaModel):
    def __init__(self, function_name=None, limit=None, next_token=None):
        # The function name. If you leave this parameter empty, the concurrency configurations of all functions are returned.
        self.function_name = function_name  # type: str
        # The maximum number of entries returned.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConcurrencyConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListConcurrencyConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConcurrencyConfigsOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConcurrencyConfigsResponse, self).to_map()
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
            temp_model = ListConcurrencyConfigsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomDomainsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None):
        # The number of custom domain names returned.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The domain name prefix.
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListCustomDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomDomainOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomDomainsResponse, self).to_map()
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
            temp_model = ListCustomDomainOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionVersionsRequest(TeaModel):
    def __init__(self, direction=None, limit=None, next_token=None):
        # The sorting mode of function versions. Valid values: BACKWARD and FORWARD.
        self.direction = direction  # type: str
        # The number of function versions that are returned.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVersionsOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionVersionsResponse, self).to_map()
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
            temp_model = ListVersionsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(self, fc_version=None, limit=None, next_token=None, prefix=None):
        # The version of Function Compute to which the functions belong. Valid values: v3 and v2. v3: only lists functions of Function Compute 3.0. v2: only lists functions of Function Compute 2.0. By default, this parameter is left empty and functions in both Function Compute 2.0 and Function Compute 3.0 are listed.
        self.fc_version = fc_version  # type: str
        # The number of functions to return. The minimum value is 1 and the maximum value is 100.
        self.limit = limit  # type: int
        # The pagination token.
        self.next_token = next_token  # type: str
        # The prefix of the function name.
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_version is not None:
            result['fcVersion'] = self.fc_version
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fcVersion') is not None:
            self.fc_version = m.get('fcVersion')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionsOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionsResponse, self).to_map()
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
            temp_model = ListFunctionsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, end_time_ms=None, instance_ids=None, instance_status=None, limit=None, qualifier=None,
                 start_key=None, start_time_ms=None, with_all_active=None):
        self.end_time_ms = end_time_ms  # type: long
        self.instance_ids = instance_ids  # type: list[str]
        self.instance_status = instance_status  # type: list[str]
        self.limit = limit  # type: str
        # The function version or alias.
        self.qualifier = qualifier  # type: str
        self.start_key = start_key  # type: str
        self.start_time_ms = start_time_ms  # type: long
        # Specifies whether to list all instances. Valid values: true and false.
        self.with_all_active = with_all_active  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_ms is not None:
            result['endTimeMs'] = self.end_time_ms
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.limit is not None:
            result['limit'] = self.limit
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.start_key is not None:
            result['startKey'] = self.start_key
        if self.start_time_ms is not None:
            result['startTimeMs'] = self.start_time_ms
        if self.with_all_active is not None:
            result['withAllActive'] = self.with_all_active
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTimeMs') is not None:
            self.end_time_ms = m.get('endTimeMs')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        if m.get('startTimeMs') is not None:
            self.start_time_ms = m.get('startTimeMs')
        if m.get('withAllActive') is not None:
            self.with_all_active = m.get('withAllActive')
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(self, end_time_ms=None, instance_ids_shrink=None, instance_status_shrink=None, limit=None,
                 qualifier=None, start_key=None, start_time_ms=None, with_all_active=None):
        self.end_time_ms = end_time_ms  # type: long
        self.instance_ids_shrink = instance_ids_shrink  # type: str
        self.instance_status_shrink = instance_status_shrink  # type: str
        self.limit = limit  # type: str
        # The function version or alias.
        self.qualifier = qualifier  # type: str
        self.start_key = start_key  # type: str
        self.start_time_ms = start_time_ms  # type: long
        # Specifies whether to list all instances. Valid values: true and false.
        self.with_all_active = with_all_active  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time_ms is not None:
            result['endTimeMs'] = self.end_time_ms
        if self.instance_ids_shrink is not None:
            result['instanceIds'] = self.instance_ids_shrink
        if self.instance_status_shrink is not None:
            result['instanceStatus'] = self.instance_status_shrink
        if self.limit is not None:
            result['limit'] = self.limit
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.start_key is not None:
            result['startKey'] = self.start_key
        if self.start_time_ms is not None:
            result['startTimeMs'] = self.start_time_ms
        if self.with_all_active is not None:
            result['withAllActive'] = self.with_all_active
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTimeMs') is not None:
            self.end_time_ms = m.get('endTimeMs')
        if m.get('instanceIds') is not None:
            self.instance_ids_shrink = m.get('instanceIds')
        if m.get('instanceStatus') is not None:
            self.instance_status_shrink = m.get('instanceStatus')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        if m.get('startTimeMs') is not None:
            self.start_time_ms = m.get('startTimeMs')
        if m.get('withAllActive') is not None:
            self.with_all_active = m.get('withAllActive')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
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
            temp_model = ListInstancesOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayerVersionsRequest(TeaModel):
    def __init__(self, limit=None, start_version=None):
        # The number of versions to be returned.
        self.limit = limit  # type: int
        # The initial version of the layer.
        self.start_version = start_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLayerVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.start_version is not None:
            result['startVersion'] = self.start_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('startVersion') is not None:
            self.start_version = m.get('startVersion')
        return self


class ListLayerVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLayerVersionOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLayerVersionsResponse, self).to_map()
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
            temp_model = ListLayerVersionOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, official=None, prefix=None, public=None):
        # The number of layers that are returned
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # Specifies whether the layer is official. Valid values: true and false.
        self.official = official  # type: str
        # The name prefix of the layer.
        self.prefix = prefix  # type: str
        # Specifies whether the layer is public. Valid values: true and false.
        self.public = public  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLayersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.official is not None:
            result['official'] = self.official
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('official') is not None:
            self.official = m.get('official')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class ListLayersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLayersOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLayersResponse, self).to_map()
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
            temp_model = ListLayersOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionConfigsRequest(TeaModel):
    def __init__(self, function_name=None, limit=None, next_token=None):
        # The name of the function. If this parameter is not specified, the provisioned configurations of all functions are listed.
        self.function_name = function_name  # type: str
        # Number of provisioned configurations to return.
        self.limit = limit  # type: int
        # A pagination token.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListProvisionConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProvisionConfigsOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProvisionConfigsResponse, self).to_map()
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
            temp_model = ListProvisionConfigsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The tag value.
        # 
        # The tag value can be up to 128 characters in length and can be an empty string.
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
    def __init__(self, limit=None, next_token=None, resource_id=None, resource_type=None, tag=None):
        # The number of resources to return.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type  # type: str
        # The tags.
        # 
        # You can query up to 20 tags at a time.
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
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, resource_id_shrink=None, resource_type=None, tag_shrink=None):
        # The number of resources to return.
        self.limit = limit  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The resource IDs.
        self.resource_id_shrink = resource_id_shrink  # type: str
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type  # type: str
        # The tags.
        # 
        # You can query up to 20 tags at a time.
        self.tag_shrink = tag_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None):
        # The number of triggers returned.
        self.limit = limit  # type: int
        # The token for the next page.
        self.next_token = next_token  # type: str
        # The trigger name prefix.
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTriggersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        return self


class ListTriggersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTriggersOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTriggersResponse, self).to_map()
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
            temp_model = ListTriggersOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcBindingsOutput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcBindingsResponse, self).to_map()
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
            temp_model = ListVpcBindingsOutput()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFunctionVersionRequest(TeaModel):
    def __init__(self, body=None):
        # The information about the function version.
        # 
        # This parameter is required.
        self.body = body  # type: PublishVersionInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishFunctionVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PublishVersionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFunctionVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Version

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishFunctionVersionResponse, self).to_map()
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
            temp_model = Version()
            self.body = temp_model.from_map(m['body'])
        return self


class PutAsyncInvokeConfigRequest(TeaModel):
    def __init__(self, body=None, qualifier=None):
        # The asynchronous invocation configurations.
        # 
        # This parameter is required.
        self.body = body  # type: PutAsyncInvokeConfigInput
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutAsyncInvokeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PutAsyncInvokeConfigInput()
            self.body = temp_model.from_map(m['body'])
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutAsyncInvokeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AsyncConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutAsyncInvokeConfigResponse, self).to_map()
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
            temp_model = AsyncConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class PutConcurrencyConfigRequest(TeaModel):
    def __init__(self, body=None):
        # The concurrency configurations.
        # 
        # This parameter is required.
        self.body = body  # type: PutConcurrencyInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutConcurrencyConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PutConcurrencyInput()
            self.body = temp_model.from_map(m['body'])
        return self


class PutConcurrencyConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConcurrencyConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutConcurrencyConfigResponse, self).to_map()
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
            temp_model = ConcurrencyConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLayerACLRequest(TeaModel):
    def __init__(self, acl=None, public=None):
        # Specify the access permission of the layer. A value of 1 indicates public and a value of 0 indicates private. The default value is 0.
        self.acl = acl  # type: str
        # Specify whether the layer is a public layer. Valid values: true and false.
        self.public = public  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutLayerACLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class PutLayerACLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutLayerACLResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PutProvisionConfigRequest(TeaModel):
    def __init__(self, body=None, qualifier=None):
        # The provisioned instance configurations.
        # 
        # This parameter is required.
        self.body = body  # type: PutProvisionConfigInput
        # The function alias or LATEST.
        self.qualifier = qualifier  # type: str

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutProvisionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = PutProvisionConfigInput()
            self.body = temp_model.from_map(m['body'])
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutProvisionConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProvisionConfig

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutProvisionConfigResponse, self).to_map()
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
            temp_model = ProvisionConfig()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAsyncTaskRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the function.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class StopAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAsyncTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, body=None):
        # The configuration of the resource tag.
        # 
        # This parameter is required.
        self.body = body  # type: TagResourcesInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TagResourcesInput()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_type=None, tag_key=None):
        # Specifies whether to delete all tags.
        self.all = all  # type: bool
        # The resource identifiers.
        # 
        # This parameter is required.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type  # type: str
        # The tag to remove. You can specify a maximum of 50 tags.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(self, all=None, resource_id_shrink=None, resource_type=None, tag_key_shrink=None):
        # Specifies whether to delete all tags.
        self.all = all  # type: bool
        # The resource identifiers.
        # 
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink  # type: str
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type  # type: str
        # The tag to remove. You can specify a maximum of 50 tags.
        self.tag_key_shrink = tag_key_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id_shrink is not None:
            result['ResourceId'] = self.resource_id_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key_shrink is not None:
            result['TagKey'] = self.tag_key_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id_shrink = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key_shrink = m.get('TagKey')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(self, body=None):
        # The alias information to be updated.
        # 
        # This parameter is required.
        self.body = body  # type: UpdateAliasInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateAliasInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Alias

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAliasResponse, self).to_map()
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
            temp_model = Alias()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainRequest(TeaModel):
    def __init__(self, body=None):
        # The information about the custom domain name.
        # 
        # This parameter is required.
        self.body = body  # type: UpdateCustomDomainInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateCustomDomainInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CustomDomain

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCustomDomainResponse, self).to_map()
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
            temp_model = CustomDomain()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(self, body=None):
        # The function information
        # 
        # This parameter is required.
        self.body = body  # type: UpdateFunctionInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateFunctionInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Function

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFunctionResponse, self).to_map()
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
            temp_model = Function()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(self, body=None):
        # The trigger configurations.
        # 
        # This parameter is required.
        self.body = body  # type: UpdateTriggerInput

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateTriggerInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Trigger

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTriggerResponse, self).to_map()
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
            temp_model = Trigger()
            self.body = temp_model.from_map(m['body'])
        return self


