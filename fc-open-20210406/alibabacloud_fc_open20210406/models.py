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


class AsyncConfigMeta(TeaModel):
    def __init__(self, function_name=None, qualifier=None, service_name=None):
        self.function_name = function_name  # type: str
        self.qualifier = qualifier  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AsyncConfigMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class AvailableAZ(TeaModel):
    def __init__(self, available_azs=None):
        self.available_azs = available_azs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AvailableAZ, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_azs is not None:
            result['availableAZs'] = self.available_azs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('availableAZs') is not None:
            self.available_azs = m.get('availableAZs')
        return self


class CDNEventsTriggerConfig(TeaModel):
    def __init__(self, event_name=None, event_version=None, filter=None, notes=None):
        self.event_name = event_name  # type: str
        self.event_version = event_version  # type: str
        self.filter = filter  # type: dict[str, list[str]]
        self.notes = notes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CDNEventsTriggerConfig, self).to_map()
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
        self.cert_name = cert_name  # type: str
        self.certificate = certificate  # type: str
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


class Code(TeaModel):
    def __init__(self, oss_bucket_name=None, oss_object_name=None, zip_file=None):
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.zip_file = zip_file  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Code, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name
        if self.zip_file is not None:
            result['zipFile'] = self.zip_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')
        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')
        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')
        return self


class CustomContainerConfig(TeaModel):
    def __init__(self, acceleration_type=None, args=None, command=None, image=None, instance_id=None,
                 web_server_mode=None):
        self.acceleration_type = acceleration_type  # type: str
        self.args = args  # type: str
        self.command = command  # type: str
        self.image = image  # type: str
        self.instance_id = instance_id  # type: str
        self.web_server_mode = web_server_mode  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CustomContainerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        if self.web_server_mode is not None:
            result['webServerMode'] = self.web_server_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        if m.get('webServerMode') is not None:
            self.web_server_mode = m.get('webServerMode')
        return self


class CustomContainerConfigInfo(TeaModel):
    def __init__(self, acceleration_info=None, acceleration_type=None, args=None, command=None, image=None,
                 instance_id=None, web_server_mode=None):
        self.acceleration_info = acceleration_info  # type: AccelerationInfo
        self.acceleration_type = acceleration_type  # type: str
        self.args = args  # type: str
        self.command = command  # type: str
        self.image = image  # type: str
        self.instance_id = instance_id  # type: str
        self.web_server_mode = web_server_mode  # type: bool

    def validate(self):
        if self.acceleration_info:
            self.acceleration_info.validate()

    def to_map(self):
        _map = super(CustomContainerConfigInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceleration_info is not None:
            result['accelerationInfo'] = self.acceleration_info.to_map()
        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        if self.image is not None:
            result['image'] = self.image
        if self.instance_id is not None:
            result['instanceID'] = self.instance_id
        if self.web_server_mode is not None:
            result['webServerMode'] = self.web_server_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accelerationInfo') is not None:
            temp_model = AccelerationInfo()
            self.acceleration_info = temp_model.from_map(m['accelerationInfo'])
        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('instanceID') is not None:
            self.instance_id = m.get('instanceID')
        if m.get('webServerMode') is not None:
            self.web_server_mode = m.get('webServerMode')
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
    def __init__(self, args=None, command=None):
        self.args = args  # type: list[str]
        self.command = command  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CustomRuntimeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')
        if m.get('command') is not None:
            self.command = m.get('command')
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


class Error(TeaModel):
    def __init__(self, error_code=None, error_message=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Error, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        return self


class ErrorInfo(TeaModel):
    def __init__(self, error_message=None, stack_trace=None):
        self.error_message = error_message  # type: str
        self.stack_trace = stack_trace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ErrorInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.stack_trace is not None:
            result['stackTrace'] = self.stack_trace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('stackTrace') is not None:
            self.stack_trace = m.get('stackTrace')
        return self


class EventBridgeTriggerConfig(TeaModel):
    def __init__(self, async_invocation_type=None, event_rule_filter_pattern=None, event_source_config=None,
                 trigger_enable=None):
        self.async_invocation_type = async_invocation_type  # type: bool
        self.event_rule_filter_pattern = event_rule_filter_pattern  # type: str
        self.event_source_config = event_source_config  # type: EventSourceConfig
        self.trigger_enable = trigger_enable  # type: bool

    def validate(self):
        if self.event_source_config:
            self.event_source_config.validate()

    def to_map(self):
        _map = super(EventBridgeTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_invocation_type is not None:
            result['asyncInvocationType'] = self.async_invocation_type
        if self.event_rule_filter_pattern is not None:
            result['eventRuleFilterPattern'] = self.event_rule_filter_pattern
        if self.event_source_config is not None:
            result['eventSourceConfig'] = self.event_source_config.to_map()
        if self.trigger_enable is not None:
            result['triggerEnable'] = self.trigger_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('asyncInvocationType') is not None:
            self.async_invocation_type = m.get('asyncInvocationType')
        if m.get('eventRuleFilterPattern') is not None:
            self.event_rule_filter_pattern = m.get('eventRuleFilterPattern')
        if m.get('eventSourceConfig') is not None:
            temp_model = EventSourceConfig()
            self.event_source_config = temp_model.from_map(m['eventSourceConfig'])
        if m.get('triggerEnable') is not None:
            self.trigger_enable = m.get('triggerEnable')
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
    def __init__(self, source_mnsparameters=None, source_rabbit_mqparameters=None,
                 source_rocket_mqparameters=None):
        self.source_mnsparameters = source_mnsparameters  # type: SourceMNSParameters
        self.source_rabbit_mqparameters = source_rabbit_mqparameters  # type: SourceRabbitMQParameters
        self.source_rocket_mqparameters = source_rocket_mqparameters  # type: SourceRocketMQParameters

    def validate(self):
        if self.source_mnsparameters:
            self.source_mnsparameters.validate()
        if self.source_rabbit_mqparameters:
            self.source_rabbit_mqparameters.validate()
        if self.source_rocket_mqparameters:
            self.source_rocket_mqparameters.validate()

    def to_map(self):
        _map = super(EventSourceParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_mnsparameters is not None:
            result['sourceMNSParameters'] = self.source_mnsparameters.to_map()
        if self.source_rabbit_mqparameters is not None:
            result['sourceRabbitMQParameters'] = self.source_rabbit_mqparameters.to_map()
        if self.source_rocket_mqparameters is not None:
            result['sourceRocketMQParameters'] = self.source_rocket_mqparameters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sourceMNSParameters') is not None:
            temp_model = SourceMNSParameters()
            self.source_mnsparameters = temp_model.from_map(m['sourceMNSParameters'])
        if m.get('sourceRabbitMQParameters') is not None:
            temp_model = SourceRabbitMQParameters()
            self.source_rabbit_mqparameters = temp_model.from_map(m['sourceRabbitMQParameters'])
        if m.get('sourceRocketMQParameters') is not None:
            temp_model = SourceRocketMQParameters()
            self.source_rocket_mqparameters = temp_model.from_map(m['sourceRocketMQParameters'])
        return self


class HTTPTriggerConfig(TeaModel):
    def __init__(self, auth_type=None, disable_urlinternet=None, methods=None):
        self.auth_type = auth_type  # type: str
        # 禁用默认公网域名访问的开关，设置为true 时，访问函数默认提供的公网URL地址会返回403错误。设置为 false 则不会有任何影响。
        self.disable_urlinternet = disable_urlinternet  # type: bool
        self.methods = methods  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(HTTPTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet
        if self.methods is not None:
            result['methods'] = self.methods
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        return self


class InstanceLifecycleConfig(TeaModel):
    def __init__(self, pre_freeze=None, pre_stop=None):
        self.pre_freeze = pre_freeze  # type: LifecycleHook
        self.pre_stop = pre_stop  # type: LifecycleHook

    def validate(self):
        if self.pre_freeze:
            self.pre_freeze.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super(InstanceLifecycleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_freeze is not None:
            result['preFreeze'] = self.pre_freeze.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('preFreeze') is not None:
            temp_model = LifecycleHook()
            self.pre_freeze = temp_model.from_map(m['preFreeze'])
        if m.get('preStop') is not None:
            temp_model = LifecycleHook()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class JaegerConfig(TeaModel):
    def __init__(self, endpoint=None):
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JaegerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        return self


class JobConfig(TeaModel):
    def __init__(self, max_retry_time=None, trigger_interval=None):
        self.max_retry_time = max_retry_time  # type: long
        self.trigger_interval = trigger_interval  # type: long

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


class JobLogConfig(TeaModel):
    def __init__(self, logstore=None, project=None):
        self.logstore = logstore  # type: str
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JobLogConfig, self).to_map()
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


class Layer(TeaModel):
    def __init__(self, acl=None, arn=None, arn_v2=None, code=None, code_checksum=None, code_size=None,
                 compatible_runtime=None, create_time=None, description=None, layer_name=None, license=None, version=None):
        self.acl = acl  # type: int
        self.arn = arn  # type: str
        self.arn_v2 = arn_v2  # type: str
        self.code = code  # type: LayerCode
        self.code_checksum = code_checksum  # type: str
        self.code_size = code_size  # type: long
        self.compatible_runtime = compatible_runtime  # type: list[str]
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.layer_name = layer_name  # type: str
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
        if self.arn is not None:
            result['arn'] = self.arn
        if self.arn_v2 is not None:
            result['arnV2'] = self.arn_v2
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
        if self.license is not None:
            result['license'] = self.license
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('arnV2') is not None:
            self.arn_v2 = m.get('arnV2')
        if m.get('code') is not None:
            temp_model = LayerCode()
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
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class LayerCode(TeaModel):
    def __init__(self, location=None, repository_type=None):
        self.location = location  # type: str
        self.repository_type = repository_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LayerCode, self).to_map()
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


class LogTriggerConfig(TeaModel):
    def __init__(self, enable=None, function_parameter=None, job_config=None, log_config=None, source_config=None):
        self.enable = enable  # type: bool
        self.function_parameter = function_parameter  # type: dict[str, str]
        self.job_config = job_config  # type: JobConfig
        self.log_config = log_config  # type: JobLogConfig
        self.source_config = source_config  # type: SourceConfig

    def validate(self):
        if self.job_config:
            self.job_config.validate()
        if self.log_config:
            self.log_config.validate()
        if self.source_config:
            self.source_config.validate()

    def to_map(self):
        _map = super(LogTriggerConfig, self).to_map()
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
            temp_model = JobLogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('sourceConfig') is not None:
            temp_model = SourceConfig()
            self.source_config = temp_model.from_map(m['sourceConfig'])
        return self


class MeteringConfig(TeaModel):
    def __init__(self, log_config=None, payer_id=None, role=None):
        self.log_config = log_config  # type: LogConfig
        self.payer_id = payer_id  # type: str
        self.role = role  # type: str

    def validate(self):
        if self.log_config:
            self.log_config.validate()

    def to_map(self):
        _map = super(MeteringConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.payer_id is not None:
            result['payerId'] = self.payer_id
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class MnsTopicTriggerConfig(TeaModel):
    def __init__(self, filter_tag=None, notify_content_format=None, notify_strategy=None):
        self.filter_tag = filter_tag  # type: str
        self.notify_content_format = notify_content_format  # type: str
        self.notify_strategy = notify_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MnsTopicTriggerConfig, self).to_map()
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


class NASConfigMountPoints(TeaModel):
    def __init__(self, mount_dir=None, server_addr=None):
        self.mount_dir = mount_dir  # type: str
        self.server_addr = server_addr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NASConfigMountPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir
        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')
        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')
        return self


class NASConfig(TeaModel):
    def __init__(self, group_id=None, mount_points=None, user_id=None):
        self.group_id = group_id  # type: int
        self.mount_points = mount_points  # type: list[NASConfigMountPoints]
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
                temp_model = NASConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class OSSMountConfigMountPoints(TeaModel):
    def __init__(self, bucket_name=None, bucket_path=None, endpoint=None, mount_dir=None, read_only=None):
        self.bucket_name = bucket_name  # type: str
        self.bucket_path = bucket_path  # type: str
        self.endpoint = endpoint  # type: str
        self.mount_dir = mount_dir  # type: str
        self.read_only = read_only  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OSSMountConfigMountPoints, self).to_map()
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


class OSSMountConfig(TeaModel):
    def __init__(self, mount_points=None):
        self.mount_points = mount_points  # type: list[OSSMountConfigMountPoints]

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
                temp_model = OSSMountConfigMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        return self


class OSSTriggerConfig(TeaModel):
    def __init__(self, events=None, filter=None):
        self.events = events  # type: list[str]
        self.filter = filter  # type: OSSTriggerFilter

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
            temp_model = OSSTriggerFilter()
            self.filter = temp_model.from_map(m['filter'])
        return self


class OSSTriggerFilter(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: OSSTriggerKey

    def validate(self):
        if self.key:
            self.key.validate()

    def to_map(self):
        _map = super(OSSTriggerFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            temp_model = OSSTriggerKey()
            self.key = temp_model.from_map(m['key'])
        return self


class OSSTriggerKey(TeaModel):
    def __init__(self, prefix=None, suffix=None):
        self.prefix = prefix  # type: str
        self.suffix = suffix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OSSTriggerKey, self).to_map()
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


class OnDemandConfig(TeaModel):
    def __init__(self, maximum_instance_count=None, resource=None):
        self.maximum_instance_count = maximum_instance_count  # type: long
        self.resource = resource  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OnDemandConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class OpenReservedCapacity(TeaModel):
    def __init__(self, created_time=None, cu=None, deadline=None, instance_id=None, is_refunded=None,
                 last_modified_time=None):
        self.created_time = created_time  # type: str
        self.cu = cu  # type: long
        self.deadline = deadline  # type: str
        self.instance_id = instance_id  # type: str
        self.is_refunded = is_refunded  # type: str
        self.last_modified_time = last_modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenReservedCapacity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.cu is not None:
            result['cu'] = self.cu
        if self.deadline is not None:
            result['deadline'] = self.deadline
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_refunded is not None:
            result['isRefunded'] = self.is_refunded
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        if m.get('deadline') is not None:
            self.deadline = m.get('deadline')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isRefunded') is not None:
            self.is_refunded = m.get('isRefunded')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
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


class PathConfig(TeaModel):
    def __init__(self, function_name=None, methods=None, path=None, qualifier=None, rewrite_config=None,
                 service_name=None):
        self.function_name = function_name  # type: str
        self.methods = methods  # type: list[str]
        self.path = path  # type: str
        self.qualifier = qualifier  # type: str
        self.rewrite_config = rewrite_config  # type: RewriteConfig
        self.service_name = service_name  # type: str

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
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
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class PolicyItem(TeaModel):
    def __init__(self, key=None, operator=None, type=None, value=None):
        self.key = key  # type: bytes
        self.operator = operator  # type: bytes
        self.type = type  # type: bytes
        self.value = value  # type: bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super(PolicyItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PreFreeze(TeaModel):
    def __init__(self, handler=None, timeout=None):
        self.handler = handler  # type: str
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreFreeze, self).to_map()
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


class PreStop(TeaModel):
    def __init__(self, handler=None, timeout=None):
        self.handler = handler  # type: str
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreStop, self).to_map()
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


class RdsTriggerConfig(TeaModel):
    def __init__(self, concurrency=None, event_format=None, retry=None, subscription_objects=None):
        self.concurrency = concurrency  # type: long
        self.event_format = event_format  # type: str
        self.retry = retry  # type: long
        self.subscription_objects = subscription_objects  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RdsTriggerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.event_format is not None:
            result['eventFormat'] = self.event_format
        if self.retry is not None:
            result['retry'] = self.retry
        if self.subscription_objects is not None:
            result['subscriptionObjects'] = self.subscription_objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('eventFormat') is not None:
            self.event_format = m.get('eventFormat')
        if m.get('retry') is not None:
            self.retry = m.get('retry')
        if m.get('subscriptionObjects') is not None:
            self.subscription_objects = m.get('subscriptionObjects')
        return self


class Resource(TeaModel):
    def __init__(self, resource_arn=None, tags=None):
        self.resource_arn = resource_arn  # type: str
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(Resource, self).to_map()
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


class RewriteConfigEqualRules(TeaModel):
    def __init__(self, match=None, replacement=None):
        self.match = match  # type: str
        self.replacement = replacement  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RewriteConfigEqualRules, self).to_map()
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


class RewriteConfigRegexRules(TeaModel):
    def __init__(self, match=None, replacement=None):
        self.match = match  # type: str
        self.replacement = replacement  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RewriteConfigRegexRules, self).to_map()
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


class RewriteConfigWildcardRules(TeaModel):
    def __init__(self, match=None, replacement=None):
        self.match = match  # type: str
        self.replacement = replacement  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RewriteConfigWildcardRules, self).to_map()
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


class RewriteConfig(TeaModel):
    def __init__(self, equal_rules=None, regex_rules=None, wildcard_rules=None):
        self.equal_rules = equal_rules  # type: list[RewriteConfigEqualRules]
        self.regex_rules = regex_rules  # type: list[RewriteConfigRegexRules]
        self.wildcard_rules = wildcard_rules  # type: list[RewriteConfigWildcardRules]

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
                temp_model = RewriteConfigEqualRules()
                self.equal_rules.append(temp_model.from_map(k))
        self.regex_rules = []
        if m.get('regexRules') is not None:
            for k in m.get('regexRules'):
                temp_model = RewriteConfigRegexRules()
                self.regex_rules.append(temp_model.from_map(k))
        self.wildcard_rules = []
        if m.get('wildcardRules') is not None:
            for k in m.get('wildcardRules'):
                temp_model = RewriteConfigWildcardRules()
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


class RoutePolicy(TeaModel):
    def __init__(self, condition=None, policy_items=None):
        self.condition = condition  # type: bytes
        self.policy_items = policy_items  # type: PolicyItem

    def validate(self):
        if self.policy_items:
            self.policy_items.validate()

    def to_map(self):
        _map = super(RoutePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.policy_items is not None:
            result['policyItems'] = self.policy_items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('policyItems') is not None:
            temp_model = PolicyItem()
            self.policy_items = temp_model.from_map(m['policyItems'])
        return self


class ScheduledActions(TeaModel):
    def __init__(self, end_time=None, name=None, schedule_expression=None, start_time=None, target=None):
        self.end_time = end_time  # type: str
        self.name = name  # type: str
        self.schedule_expression = schedule_expression  # type: str
        self.start_time = start_time  # type: str
        self.target = target  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScheduledActions, self).to_map()
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
        return self


class SourceConfig(TeaModel):
    def __init__(self, logstore=None):
        self.logstore = logstore  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
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
    def __init__(self, group_id=None, instance_id=None, offset=None, region_id=None, tag=None, timestamp=None,
                 topic=None):
        self.group_id = group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.offset = offset  # type: str
        self.region_id = region_id  # type: str
        self.tag = tag  # type: str
        self.timestamp = timestamp  # type: long
        self.topic = topic  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SourceRocketMQParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupID'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('GroupID') is not None:
            self.group_id = m.get('GroupID')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class StatefulAsyncInvocation(TeaModel):
    def __init__(self, already_retried_times=None, destination_status=None, end_time=None, events=None,
                 function_name=None, instance_id=None, invocation_error_message=None, invocation_id=None,
                 invocation_payload=None, qualifier=None, request_id=None, service_name=None, started_time=None, status=None):
        self.already_retried_times = already_retried_times  # type: long
        self.destination_status = destination_status  # type: str
        self.end_time = end_time  # type: long
        self.events = events  # type: list[StatefulAsyncInvocationEvent]
        self.function_name = function_name  # type: str
        self.instance_id = instance_id  # type: str
        self.invocation_error_message = invocation_error_message  # type: str
        self.invocation_id = invocation_id  # type: str
        self.invocation_payload = invocation_payload  # type: str
        self.qualifier = qualifier  # type: str
        self.request_id = request_id  # type: str
        self.service_name = service_name  # type: str
        self.started_time = started_time  # type: long
        self.status = status  # type: str

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StatefulAsyncInvocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.already_retried_times is not None:
            result['alreadyRetriedTimes'] = self.already_retried_times
        if self.destination_status is not None:
            result['destinationStatus'] = self.destination_status
        if self.end_time is not None:
            result['endTime'] = self.end_time
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.invocation_error_message is not None:
            result['invocationErrorMessage'] = self.invocation_error_message
        if self.invocation_id is not None:
            result['invocationId'] = self.invocation_id
        if self.invocation_payload is not None:
            result['invocationPayload'] = self.invocation_payload
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.started_time is not None:
            result['startedTime'] = self.started_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alreadyRetriedTimes') is not None:
            self.already_retried_times = m.get('alreadyRetriedTimes')
        if m.get('destinationStatus') is not None:
            self.destination_status = m.get('destinationStatus')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = StatefulAsyncInvocationEvent()
                self.events.append(temp_model.from_map(k))
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('invocationErrorMessage') is not None:
            self.invocation_error_message = m.get('invocationErrorMessage')
        if m.get('invocationId') is not None:
            self.invocation_id = m.get('invocationId')
        if m.get('invocationPayload') is not None:
            self.invocation_payload = m.get('invocationPayload')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('startedTime') is not None:
            self.started_time = m.get('startedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class StatefulAsyncInvocationEvent(TeaModel):
    def __init__(self, event_detail=None, event_id=None, status=None, timestamp=None):
        self.event_detail = event_detail  # type: str
        self.event_id = event_id  # type: long
        self.status = status  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StatefulAsyncInvocationEvent, self).to_map()
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


class TLSConfig(TeaModel):
    def __init__(self, cipher_suites=None, max_version=None, min_version=None):
        self.cipher_suites = cipher_suites  # type: list[str]
        self.max_version = max_version  # type: str
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


class TargetTrackingPolicies(TeaModel):
    def __init__(self, end_time=None, max_capacity=None, metric_target=None, metric_type=None, min_capacity=None,
                 name=None, start_time=None):
        self.end_time = end_time  # type: str
        self.max_capacity = max_capacity  # type: long
        self.metric_target = metric_target  # type: float
        self.metric_type = metric_type  # type: str
        self.min_capacity = min_capacity  # type: long
        self.name = name  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TargetTrackingPolicies, self).to_map()
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
        return self


class TimeTriggerConfig(TeaModel):
    def __init__(self, cron_expression=None, enable=None, payload=None):
        self.cron_expression = cron_expression  # type: str
        self.enable = enable  # type: bool
        self.payload = payload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TimeTriggerConfig, self).to_map()
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
    def __init__(self, created_time=None, domain_name=None, invocation_role=None, last_modified_time=None,
                 qualifier=None, source_arn=None, status=None, target_arn=None, trigger_config=None, trigger_id=None,
                 trigger_name=None, trigger_type=None, url_internet=None, url_intranet=None):
        self.created_time = created_time  # type: str
        self.domain_name = domain_name  # type: str
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
        self.url_internet = url_internet  # type: str
        self.url_intranet = url_intranet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Trigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
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
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
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
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
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


class VendorConfig(TeaModel):
    def __init__(self, metering_config=None):
        self.metering_config = metering_config  # type: MeteringConfig

    def validate(self):
        if self.metering_config:
            self.metering_config.validate()

    def to_map(self):
        _map = super(VendorConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metering_config is not None:
            result['meteringConfig'] = self.metering_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('meteringConfig') is not None:
            temp_model = MeteringConfig()
            self.metering_config = temp_model.from_map(m['meteringConfig'])
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


class ClaimGPUInstanceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClaimGPUInstanceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ClaimGPUInstanceRequest(TeaModel):
    def __init__(self, disk_performance_level=None, disk_size_gigabytes=None, image_id=None, instance_type=None,
                 internet_bandwidth_out=None, password=None, role=None, sg_id=None, source_cidr_ip=None, tcp_port_range=None,
                 udp_port_range=None, vpc_id=None, vsw_id=None):
        # The disk performance level of the GPU rendering instance.
        self.disk_performance_level = disk_performance_level  # type: str
        # The system disk space of the GPU rendering instance.
        self.disk_size_gigabytes = disk_size_gigabytes  # type: str
        # The image ID of the GPU-rendered instance.
        self.image_id = image_id  # type: str
        # The specifications of the GPU rendering instance.
        self.instance_type = instance_type  # type: str
        # The outbound Internet bandwidth of the GPU rendering instance.
        self.internet_bandwidth_out = internet_bandwidth_out  # type: str
        # The password of the GPU rendering instance.
        self.password = password  # type: str
        # The role of the user.
        self.role = role  # type: str
        # The ID of the security group.
        self.sg_id = sg_id  # type: str
        # The source IPv4 CIDR block of the GPU rendering instance.
        self.source_cidr_ip = source_cidr_ip  # type: str
        # The range of TCP ports that are open to the security group of the GPU rendering instance.
        self.tcp_port_range = tcp_port_range  # type: list[str]
        # The range of UDP ports that are open to the security group of the GPU rendering instance.
        self.udp_port_range = udp_port_range  # type: list[str]
        # The ID of the VPC in which the instance resides.
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch.
        self.vsw_id = vsw_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClaimGPUInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_performance_level is not None:
            result['diskPerformanceLevel'] = self.disk_performance_level
        if self.disk_size_gigabytes is not None:
            result['diskSizeGigabytes'] = self.disk_size_gigabytes
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth_out is not None:
            result['internetBandwidthOut'] = self.internet_bandwidth_out
        if self.password is not None:
            result['password'] = self.password
        if self.role is not None:
            result['role'] = self.role
        if self.sg_id is not None:
            result['sgId'] = self.sg_id
        if self.source_cidr_ip is not None:
            result['sourceCidrIp'] = self.source_cidr_ip
        if self.tcp_port_range is not None:
            result['tcpPortRange'] = self.tcp_port_range
        if self.udp_port_range is not None:
            result['udpPortRange'] = self.udp_port_range
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('diskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('diskPerformanceLevel')
        if m.get('diskSizeGigabytes') is not None:
            self.disk_size_gigabytes = m.get('diskSizeGigabytes')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidthOut') is not None:
            self.internet_bandwidth_out = m.get('internetBandwidthOut')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('sgId') is not None:
            self.sg_id = m.get('sgId')
        if m.get('sourceCidrIp') is not None:
            self.source_cidr_ip = m.get('sourceCidrIp')
        if m.get('tcpPortRange') is not None:
            self.tcp_port_range = m.get('tcpPortRange')
        if m.get('udpPortRange') is not None:
            self.udp_port_range = m.get('udpPortRange')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')
        return self


class ClaimGPUInstanceResponseBody(TeaModel):
    def __init__(self, created_time=None, instance_id=None, public_ip=None):
        # The time when the product instance is created.
        self.created_time = created_time  # type: str
        # The ID of the instance that you query.
        self.instance_id = instance_id  # type: str
        # The public IP address of the server.
        self.public_ip = public_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClaimGPUInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        return self


class ClaimGPUInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClaimGPUInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClaimGPUInstanceResponse, self).to_map()
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
            temp_model = ClaimGPUInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAliasHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAliasHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateAliasRequest(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, description=None, resolve_policy=None,
                 route_policy=None, version_id=None):
        # The canary release version to which the alias points and the weight of the canary release version.
        # 
        # *   The canary release version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # The name of the alias.  The name contains only letters, digits, hyphens (-), and underscores (\_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).  The name cannot be **LATEST**.
        self.alias_name = alias_name  # type: str
        # The description of the alias.
        self.description = description  # type: str
        # The canary release mode. Valid values:
        # 
        # *   **Random**: random canary release. This is the default value.
        # *   **Content**: rule-based canary release.
        self.resolve_policy = resolve_policy  # type: str
        # The canary release rule. Traffic that meets the canary release rule is routed to the canary release instance.
        self.route_policy = route_policy  # type: RoutePolicy
        # The ID of the version to which the alias points.
        self.version_id = version_id  # type: str

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

    def to_map(self):
        _map = super(CreateAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.alias_name is not None:
            result['aliasName'] = self.alias_name
        if self.description is not None:
            result['description'] = self.description
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class CreateAliasResponseBody(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, created_time=None, description=None,
                 last_modified_time=None, version_id=None):
        # The canary release version to which the alias points and the weight of the canary release version.
        # 
        # *   The canary release version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # The name of the alias.
        self.alias_name = alias_name  # type: str
        # The time when the alias was created.
        self.created_time = created_time  # type: str
        # The description of the alias.
        self.description = description  # type: str
        # The time when the alias was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The ID of the version to which the alias points.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAliasResponseBody, self).to_map()
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


class CreateAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomDomainHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCustomDomainHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateCustomDomainRequest(TeaModel):
    def __init__(self, cert_config=None, domain_name=None, protocol=None, route_config=None, tls_config=None,
                 waf_config=None):
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config  # type: CertConfig
        # The domain name.
        self.domain_name = domain_name  # type: str
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol  # type: str
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config  # type: RouteConfig
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config  # type: TLSConfig
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(CreateCustomDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateCustomDomainResponseBody(TeaModel):
    def __init__(self, account_id=None, api_version=None, cert_config=None, created_time=None, domain_name=None,
                 last_modified_time=None, protocol=None, route_config=None, tls_config=None, waf_config=None):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The version of the API.
        self.api_version = api_version  # type: str
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config  # type: CertConfig
        # The time when the domain name was added.
        self.created_time = created_time  # type: str
        # The domain name.
        self.domain_name = domain_name  # type: str
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol  # type: str
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config  # type: RouteConfig
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config  # type: TLSConfig
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(CreateCustomDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class CreateCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCustomDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_code_checksum=None, x_fc_date=None,
                 x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The CRC-64 value of the function code package.
        self.x_fc_code_checksum = x_fc_code_checksum  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request. The value is the same as that of the requestId parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFunctionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(self, ca_port=None, code=None, cpu=None, custom_container_config=None, custom_dns=None,
                 custom_health_check_config=None, custom_runtime_config=None, description=None, disk_size=None, environment_variables=None,
                 function_name=None, gpu_memory_size=None, handler=None, initialization_timeout=None, initializer=None,
                 instance_concurrency=None, instance_lifecycle_config=None, instance_soft_concurrency=None, instance_type=None,
                 layers=None, memory_size=None, runtime=None, timeout=None):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port  # type: int
        # The code of the function. The code must be packaged into a ZIP file. Choose **code** or **customContainerConfig** for the function.
        self.code = code  # type: Code
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu  # type: float
        # The configurations of the custom container runtime. After you configure the custom container runtime, Function Compute can execute the function in a container created from a custom image. Choose **code** or **customContainerConfig** for the function.
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        # The custom Domain Name System (DNS) configurations of the function.
        self.custom_dns = custom_dns  # type: CustomDNS
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config  # type: CustomHealthCheckConfig
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        # The description of the function.
        self.description = description  # type: str
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size  # type: int
        # The environment variables that you configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Overview](~~69777~~).
        self.environment_variables = environment_variables  # type: dict[str, str]
        # The name of the function. The name can contain letters, digits, underscores (\_), and hyphens (-) only. The name cannot start with a digit or a hyphen (-). The name must be 1 to 64 characters in length.
        self.function_name = function_name  # type: str
        self.gpu_memory_size = gpu_memory_size  # type: int
        # The handler of the function. The format varies based on the programming language. For more information, see [Function handlers](~~157704~~).
        self.handler = handler  # type: str
        # The timeout period for the execution of the initializer function. Unit: seconds. Default value: 3. Valid values: 1 to 300. When this period expires, the execution of the initializer function is terminated.
        self.initialization_timeout = initialization_timeout  # type: int
        # The handler of the initializer function. For more information, see [Initializer functions](~~157704~~).
        self.initializer = initializer  # type: str
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency  # type: int
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the number of the soft concurrency, the instance scale-up is triggered. For example, if your instance requires a long term to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of **instanceConcurrency**.
        self.instance_soft_concurrency = instance_soft_concurrency  # type: int
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        self.instance_type = instance_type  # type: str
        # An array that consists of the information of layers.
        # 
        # >  Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file with the same name in the layer with a larger subscript.
        self.layers = layers  # type: list[str]
        # The memory size for the function. Unit: MB. The memory size must be a multiple of 64 MB. The memory size varies based on the function instance type. For more information, see [Instance types](~~179379~~).
        self.memory_size = memory_size  # type: int
        # The runtime environment of the function. Valid values: **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore2.1**, **custom** and **custom-container**.
        self.runtime = runtime  # type: str
        # The timeout period for the execution of the function. Unit: seconds. Default value: 3. Minimum value: 1. When this period ends, the execution of the function is terminated.
        self.timeout = timeout  # type: int

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super(CreateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
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
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
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
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(self, ca_port=None, code_checksum=None, code_size=None, cpu=None, created_time=None,
                 custom_container_config=None, custom_dns=None, custom_health_check_config=None, custom_runtime_config=None,
                 description=None, disk_size=None, environment_variables=None, function_id=None, function_name=None,
                 gpu_memory_size=None, handler=None, initialization_timeout=None, initializer=None, instance_concurrency=None,
                 instance_lifecycle_config=None, instance_soft_concurrency=None, instance_type=None, last_modified_time=None, layers=None,
                 memory_size=None, runtime=None, timeout=None):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port  # type: int
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum  # type: str
        # The size of the function code package that is returned by the system. Unit: byte.
        self.code_size = code_size  # type: long
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu  # type: float
        # The time when the function was created.
        self.created_time = created_time  # type: str
        # The configurations of the custom container runtime. After you configure the custom container runtime, Function Compute can execute the function in a container created from a custom image.
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns  # type: CustomDNS
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config  # type: CustomHealthCheckConfig
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        # The description of the function.
        self.description = description  # type: str
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size  # type: int
        # The environment variables that you configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Overview](~~69777~~).
        self.environment_variables = environment_variables  # type: dict[str, str]
        # The unique ID generated by the system for the function.
        self.function_id = function_id  # type: str
        # The name of the function.
        self.function_name = function_name  # type: str
        self.gpu_memory_size = gpu_memory_size  # type: int
        # The handler of the function.
        self.handler = handler  # type: str
        # The timeout period for the execution of the initializer function. Unit: seconds. Default value: 3. Minimum value: 1. When this period ends, the execution of the initializer function is terminated.
        self.initialization_timeout = initialization_timeout  # type: int
        # The handler of the initializer function. The format is determined by the programming language.
        self.initializer = initializer  # type: str
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency  # type: int
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the number of the soft concurrency, the instance scale-up is triggered. For example, if your instance requires a long term to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of **instanceConcurrency**.
        self.instance_soft_concurrency = instance_soft_concurrency  # type: int
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        self.instance_type = instance_type  # type: str
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # An array that consists of the information of layers.
        # 
        # >  Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file with the same name in the layer with a larger subscript.
        self.layers = layers  # type: list[str]
        # The memory size for the function. Unit: MB.
        self.memory_size = memory_size  # type: int
        # The runtime environment of the function. Valid values: **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore2.1**, **custom** and **custom-container**.
        self.runtime = runtime  # type: str
        # The timeout period for the execution of the function. Unit: seconds. Default value: 60. Valid values: 1 to 600. When this period expires, the execution of the function is terminated.
        self.timeout = timeout  # type: int

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super(CreateFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
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
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFunctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayerVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLayerVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateLayerVersionRequest(TeaModel):
    def __init__(self, code=None, compatible_runtime=None, description=None):
        # The code of the layer.
        self.code = code  # type: Code
        # The list of runtime environments that are supported by the layer.
        self.compatible_runtime = compatible_runtime  # type: list[str]
        # The description of the layer.
        self.description = description  # type: str

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super(CreateLayerVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code.to_map()
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['Code'])
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateLayerVersionResponseBody(TeaModel):
    def __init__(self, acl=None, arn=None, code=None, code_checksum=None, codesize=None, compatible_runtime=None,
                 create_time=None, description=None, layer_name=None, version=None):
        # The access mode of the layer.
        self.acl = acl  # type: int
        # The name of the layer.
        self.arn = arn  # type: str
        # The information about the layer code package.
        self.code = code  # type: OutputCodeLocation
        # The checksum of the layer code package.
        self.code_checksum = code_checksum  # type: str
        # The size of the layer code package. Unit: Byte.
        self.codesize = codesize  # type: long
        # The list of runtime environments that are supported by the layer.
        self.compatible_runtime = compatible_runtime  # type: list[str]
        # The time when the layer version was created. The time follows the **yyyy-MM-ddTHH:mm:ssZ** format.
        self.create_time = create_time  # type: str
        # The description of the layer version.
        self.description = description  # type: str
        # The name of the layer.
        self.layer_name = layer_name  # type: str
        # The version of the layer.
        self.version = version  # type: int

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        _map = super(CreateLayerVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.arn is not None:
            result['arn'] = self.arn
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum
        if self.codesize is not None:
            result['codesize'] = self.codesize
        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.layer_name is not None:
            result['layerName'] = self.layer_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('arn') is not None:
            self.arn = m.get('arn')
        if m.get('code') is not None:
            temp_model = OutputCodeLocation()
            self.code = temp_model.from_map(m['code'])
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codesize') is not None:
            self.codesize = m.get('codesize')
        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateLayerVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLayerVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateLayerVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, description=None, internet_access=None, log_config=None, nas_config=None,
                 oss_mount_config=None, role=None, service_name=None, tracing_config=None, vpc_config=None):
        # The description of the service.
        self.description = description  # type: str
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # - **true**: allows functions in the specified service to access the Internet. Default value: true.
        # - **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access  # type: bool
        # The log configuration. Function Compute writes function execution logs to the specified Logstore.
        self.log_config = log_config  # type: LogConfig
        # The configuration of the Apsara File Storage NAS (NAS) file system. The configurations allow functions in the specified service to access the NAS file system.
        self.nas_config = nas_config  # type: NASConfig
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role  # type: str
        # The name of the service. The name contains only letters, digits, hyphens (-), and underscores (_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).
        self.service_name = service_name  # type: str
        # The configurations of Tracing Analysis. After Function Compute is integrated with Tracing Analysis, you can record the duration of a request in Function Compute, view the cold start time of a function, and record the execution duration of a function. For more information, see [Tracing Analysis](~~189804~~).
        self.tracing_config = tracing_config  # type: TracingConfig
        # The VPC configurations. The configurations allow functions in the specified service to access the specified VPC.
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
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
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, internet_access=None, last_modified_time=None,
                 log_config=None, nas_config=None, oss_mount_config=None, role=None, service_id=None, service_name=None,
                 tracing_config=None, vpc_config=None):
        # The time when the service was created.
        self.created_time = created_time  # type: str
        # The description of the service.
        self.description = description  # type: str
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access  # type: bool
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The log configuration. Function Compute writes function execution logs to the specified Logstore.
        self.log_config = log_config  # type: LogConfig
        # The configuration of the NAS file system. The configurations allow functions in the specified service to access the NAS file system.
        self.nas_config = nas_config  # type: NASConfig
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role  # type: str
        # The unique ID generated by the system for the service.
        self.service_id = service_id  # type: str
        # The name of the service.
        self.service_name = service_name  # type: str
        # The configuration of Tracing Analysis. After Function Compute is integrated with Tracing Analysis, you can record the duration of a request in Function Compute, view the cold start time of a function, and record the execution duration of a function. For more information, see [Tracing Analysis](~~189804~~).
        self.tracing_config = tracing_config  # type: TracingConfig
        # The VPC configurations. The configurations allow functions in the specified service to access the specified VPC.
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
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
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceResponse, self).to_map()
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(self, description=None, invocation_role=None, qualifier=None, source_arn=None, trigger_config=None,
                 trigger_name=None, trigger_type=None):
        # The description of the trigger.
        self.description = description  # type: str
        # The role that is used by the event source such as OSS to invoke the function. For more information, see [Overview](~~53102~~).
        self.invocation_role = invocation_role  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The Alibaba Cloud Resource Name (ARN) of the event source for the trigger.
        self.source_arn = source_arn  # type: str
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   OSS trigger: [OSSTriggerConfig](javascript:void\(0\)).
        # *   Log Service trigger: [LogTriggerConfig](javascript:void\(0\)).
        # *   Time trigger: [TimeTriggerConfig](javascript:void\(0\)).
        # *   HTTP trigger: [HTTPTriggerConfig](javascript:void\(0\)).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](javascript:void\(0\)).
        # *   MNS topic trigger: [MnsTopicTriggerConfig](javascript:void\(0\)).
        self.trigger_config = trigger_config  # type: str
        # The name of the trigger. The name contains only letters, digits, hyphens (-), and underscores (\_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).
        self.trigger_name = trigger_name  # type: str
        # The type of the trigger. Valid values:
        # 
        # *   **oss**: OSS event trigger. For more information, see [Overview](~~62922~~).
        # *   **log**: Log Service trigger. For more information, see [Overview](~~84386~~).
        # *   **timer**: time trigger. For more information, see [Overview](~~68172~~).
        # *   **http**: HTTP trigger. For more information, see [Overview](~~71229~~).
        # *   **tablestore**: Tablestore trigger. For more information, see [Overview](~~100092~~).
        # *   **cdn_events**: CDN event trigger. For more information, see [Overview](~~73333~~).
        # *   **mns_topic**: MNS topic trigger. For more information, see [Overview](~~97032~~).
        self.trigger_type = trigger_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerRequest, self).to_map()
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


class CreateTriggerResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, domain_name=None, invocation_role=None,
                 last_modified_time=None, qualifier=None, source_arn=None, trigger_config=None, trigger_id=None, trigger_name=None,
                 trigger_type=None, url_internet=None, url_intranet=None):
        # The time when the trigger was created.
        self.created_time = created_time  # type: str
        # The description of the trigger.
        self.description = description  # type: str
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name  # type: str
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role  # type: str
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The version of the service.
        self.qualifier = qualifier  # type: str
        # The ARN of the event source.
        self.source_arn = source_arn  # type: str
        # The configurations of the trigger. The configurations vary based on the trigger type.
        self.trigger_config = trigger_config  # type: str
        # The unique ID of the trigger.
        self.trigger_id = trigger_id  # type: str
        # The name of the trigger. The name contains only letters, digits, hyphens (-), and underscores (\_). The name must be 1 to 128 characters in length and cannot start with a digit or hyphen (-).
        self.trigger_name = trigger_name  # type: str
        # The trigger type, such as **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, and **mns_topic**.
        self.trigger_type = trigger_type  # type: str
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet  # type: str
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcBindingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcBindingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class CreateVpcBindingRequest(TeaModel):
    def __init__(self, vpc_id=None):
        # The ID of the VPC to be bound.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcBindingRequest, self).to_map()
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


class CreateVpcBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteAliasHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # If the ETag specified in the request matches the ETag value of the object, OSS transmits the object and returns 200 OK. If the ETag specified in the request does not match the ETag value of the object, OSS returns 412 Precondition Failed. 
        # The ETag value of a resource is used to check whether the resource has changed. You can check data integrity by using the ETag value. 
        # Default value: null
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAliasHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteCustomDomainHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCustomDomainHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteFunctionHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ETag value of the resource. This value is used to ensure that the modified resource is consistent with the resource to be modified. The ETag value is returned in the responses of the CREATE, GET, and UPDATE operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API. The value is the same as that of the requestId parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionAsyncInvokeConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The qualifier.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionAsyncInvokeConfigRequest, self).to_map()
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


class DeleteFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteFunctionAsyncInvokeConfigResponse, self).to_map()
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


class DeleteFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # If the ETag specified in the request matches the ETag value of the OndemandConfig, FC returns 200 OK. If the ETag specified in the request does not match the ETag value of the object, FC returns 412 Precondition Failed.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The start time when the function is invoked. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API, which is also the unique ID of the request.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionOnDemandConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteFunctionOnDemandConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The alias of the service or LATEST.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFunctionOnDemandConfigRequest, self).to_map()
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


class DeleteFunctionOnDemandConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteFunctionOnDemandConfigResponse, self).to_map()
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


class DeleteLayerVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLayerVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteLayerVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteServiceHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ETag value of the service. This value is used to ensure that the modified service is consistent with the service to be modified. The ETag value is returned in the responses of the [CreateService](~~175256~~), [UpdateService](~~188167~~), and [GetService](~~189225~~) operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteServiceResponse, self).to_map()
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


class DeleteServiceVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteServiceVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteServiceVersionResponse, self).to_map()
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


class DeleteTriggerHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # This parameter is used to ensure that the modified resource is consistent with the resource to be modified. You can obtain the parameter value from the responses of [CreateTrigger](~~415729~~), [GetTrigger](~~415732~~), and [UpdateTrigger](~~415731~~) operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTriggerHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteVpcBindingHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcBindingHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeleteVpcBindingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeregisterEventSourceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterEventSourceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class DeregisterEventSourceRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterEventSourceRequest, self).to_map()
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


class DeregisterEventSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeregisterEventSourceResponse, self).to_map()
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


class GetAccountSettingsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountSettingsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetAccountSettingsResponseBody(TeaModel):
    def __init__(self, available_azs=None, default_role=None):
        # The list of zones.
        self.available_azs = available_azs  # type: list[str]
        # The default RAM role.
        self.default_role = default_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountSettingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_azs is not None:
            result['availableAZs'] = self.available_azs
        if self.default_role is not None:
            result['defaultRole'] = self.default_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('availableAZs') is not None:
            self.available_azs = m.get('availableAZs')
        if m.get('defaultRole') is not None:
            self.default_role = m.get('defaultRole')
        return self


class GetAccountSettingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountSettingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountSettingsResponse, self).to_map()
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
            temp_model = GetAccountSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAliasHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The start time when the function is invoked. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAliasHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetAliasResponseBody(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, created_time=None, description=None,
                 last_modified_time=None, resolve_policy=None, route_policy=None, version_id=None):
        # The canary release version to which the alias points and the weight of the canary release version. 
        # 
        # - The canary release version takes effect only when the function is invoked. 
        # - The value consists of a version number and the corresponding weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # The name of the alias.
        self.alias_name = alias_name  # type: str
        # The time when the alias was created.
        self.created_time = created_time  # type: str
        # The description of the alias.
        self.description = description  # type: str
        # The time when the alias was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The canary release mode. Valid values:
        # 
        # - **Random**: random canary release. This is the default value.
        # - **Content**: rule-based canary release.
        self.resolve_policy = resolve_policy  # type: str
        # Canary release rule. The traffic that meets the conditions of the canary release rule is diverted to the canary release instances.
        self.route_policy = route_policy  # type: RoutePolicy
        # The version to which the alias points.
        self.version_id = version_id  # type: str

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

    def to_map(self):
        _map = super(GetAliasResponseBody, self).to_map()
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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class GetAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomDomainHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomDomainHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetCustomDomainResponseBody(TeaModel):
    def __init__(self, account_id=None, api_version=None, cert_config=None, created_time=None, domain_name=None,
                 last_modified_time=None, protocol=None, route_config=None, tls_config=None, waf_config=None):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The version of the API.
        self.api_version = api_version  # type: str
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config  # type: CertConfig
        # The time when the custom domain name was created.
        self.created_time = created_time  # type: str
        # The domain name.
        self.domain_name = domain_name  # type: str
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol  # type: str
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config  # type: RouteConfig
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config  # type: TLSConfig
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(GetCustomDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class GetCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCustomDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service.
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


class GetFunctionResponseBody(TeaModel):
    def __init__(self, ca_port=None, code_checksum=None, code_size=None, cpu=None, created_time=None,
                 custom_container_config=None, custom_dns=None, custom_health_check_config=None, custom_runtime_config=None,
                 description=None, disk_size=None, environment_variables=None, function_id=None, function_name=None,
                 gpu_memory_size=None, handler=None, initialization_timeout=None, initializer=None, instance_concurrency=None,
                 instance_lifecycle_config=None, instance_soft_concurrency=None, instance_type=None, last_modified_time=None, layers=None,
                 layers_arn_v2=None, memory_size=None, runtime=None, timeout=None):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port  # type: int
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum  # type: str
        # The size of the function code package. Unit: byte.
        self.code_size = code_size  # type: long
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu  # type: float
        # The time when the function was created.
        self.created_time = created_time  # type: str
        # The configurations of the custom container runtime. After you configure the custom container runtime, Function Compute can execute the function in a container created from a custom image.
        self.custom_container_config = custom_container_config  # type: CustomContainerConfigInfo
        # The custom Domain Name System (DNS) configurations of the function.
        self.custom_dns = custom_dns  # type: CustomDNS
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config  # type: CustomHealthCheckConfig
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        # The description of the function.
        self.description = description  # type: str
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size  # type: int
        # The environment variables that you configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Overview](~~69777~~).
        self.environment_variables = environment_variables  # type: dict[str, str]
        # The ID that is generated by the system for the function. Each function ID is unique in Function Compute.
        self.function_id = function_id  # type: str
        # The name of the function.
        self.function_name = function_name  # type: str
        self.gpu_memory_size = gpu_memory_size  # type: int
        # The handler of the function. For more information, see [Function handler](~~157704~~).
        self.handler = handler  # type: str
        # The timeout period for the execution of the initializer function. Unit: seconds. Default value: 3. Valid values: 1 to 300. When this period ends, the execution of the initializer function is terminated.
        self.initialization_timeout = initialization_timeout  # type: int
        # The handler of the initializer function. The format of the value is determined by the programming language that you use. For more information, see [Initializer function](~~157704~~).
        self.initializer = initializer  # type: str
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency  # type: int
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the number of the soft concurrency, the instance scale-up is triggered. For example, if your instance requires a long term to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of **instanceConcurrency**.
        self.instance_soft_concurrency = instance_soft_concurrency  # type: int
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        self.instance_type = instance_type  # type: str
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # An array that consists of the information of layers.
        # 
        # >  Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file with the same name in the layer with a larger subscript.
        self.layers = layers  # type: list[str]
        self.layers_arn_v2 = layers_arn_v2  # type: list[str]
        # The memory size for the function. Unit: MB. The memory size must be a multiple of 64 MB. The memory size varies based on the function instance type. For more information, see [Instance types](~~179379~~).
        self.memory_size = memory_size  # type: int
        # The runtime environment of the function. Valid values: **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore2.1**, **custom** and **custom-container**.
        self.runtime = runtime  # type: str
        # The timeout period for the execution of the function. Unit: seconds. Default value: 60. Valid values: 1 to 600. When this period expires, the execution of the function is terminated.
        self.timeout = timeout  # type: int

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super(GetFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.layers_arn_v2 is not None:
            result['layersArnV2'] = self.layers_arn_v2
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')
        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfigInfo()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('layersArnV2') is not None:
            self.layers_arn_v2 = m.get('layersArnV2')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the Function Compute is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionAsyncInvokeConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The qualifier.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionAsyncInvokeConfigRequest, self).to_map()
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


class GetFunctionAsyncInvokeConfigResponseBody(TeaModel):
    def __init__(self, created_time=None, destination_config=None, function=None, last_modified_time=None,
                 max_async_event_age_in_seconds=None, max_async_retry_attempts=None, qualifier=None, service=None, stateful_invocation=None):
        # The time when the desktop group was created.
        self.created_time = created_time  # type: str
        # The configuration structure of the destination for asynchronous invocations.
        self.destination_config = destination_config  # type: DestinationConfig
        # The name of the function.
        self.function = function  # type: str
        # The time when the configuration was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The maximum validity period of a message.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds  # type: long
        # The maximum number of retries allowed after an asynchronous invocation fails.
        self.max_async_retry_attempts = max_async_retry_attempts  # type: long
        # The version or alias of the service to which the function belongs.
        self.qualifier = qualifier  # type: str
        # The name of the service.
        self.service = service  # type: str
        # Indicates whether the asynchronous task feature is enabled.
        # 
        # *   **true**: The asynchronous task feature is enabled.
        # *   **false**: The asynchronous task feature is disabled.
        self.stateful_invocation = stateful_invocation  # type: bool

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super(GetFunctionAsyncInvokeConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class GetFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionAsyncInvokeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionAsyncInvokeConfigResponse, self).to_map()
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
            temp_model = GetFunctionAsyncInvokeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionCodeHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCodeHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionCodeRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service.
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


class GetFunctionCodeResponseBody(TeaModel):
    def __init__(self, checksum=None, url=None):
        # The CRC-64 value of the function code package.
        self.checksum = checksum  # type: str
        # The URL of the function code package.
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionCodeResponseBody, self).to_map()
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


class GetFunctionCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFunctionCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the yyyy-mm-ddhh:mm:ss format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API, which is also the unique ID of the request.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionOnDemandConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetFunctionOnDemandConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The alias of the service or LATEST.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionOnDemandConfigRequest, self).to_map()
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


class GetFunctionOnDemandConfigResponseBody(TeaModel):
    def __init__(self, maximum_instance_count=None, resource=None):
        # The maximum number of instances.
        self.maximum_instance_count = maximum_instance_count  # type: long
        # The description of the resource.
        self.resource = resource  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFunctionOnDemandConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class GetFunctionOnDemandConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFunctionOnDemandConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFunctionOnDemandConfigResponse, self).to_map()
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
            temp_model = GetFunctionOnDemandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayerVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLayerVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetLayerVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Layer

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetProvisionConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The start time when the function is invoked. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProvisionConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetProvisionConfigRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The name of the alias.
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


class GetProvisionConfigResponseBody(TeaModel):
    def __init__(self, always_allocate_cpu=None, current=None, current_error=None, resource=None,
                 scheduled_actions=None, target=None, target_tracking_policies=None):
        # Specifies whether to always allocate CPU to a function instance.
        self.always_allocate_cpu = always_allocate_cpu  # type: bool
        # The actual number of provisioned instances.
        self.current = current  # type: long
        # The error message returned if a provisioned instance fails to be created.
        self.current_error = current_error  # type: str
        # The description of the resource.
        self.resource = resource  # type: str
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions  # type: list[ScheduledActions]
        # The expected number of provisioned instances.
        self.target = target  # type: long
        # The configurations of metric-based auto scaling.
        self.target_tracking_policies = target_tracking_policies  # type: list[TargetTrackingPolicies]

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
        _map = super(GetProvisionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.current_error is not None:
            result['currentError'] = self.current_error
        if self.resource is not None:
            result['resource'] = self.resource
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
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class GetProvisionConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProvisionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetProvisionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTagsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTagsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetResourceTagsRequest(TeaModel):
    def __init__(self, resource_arn=None):
        # The Alibaba Cloud Resource Name (ARN) of the resource. 
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource. You can manage tags only for services for top level resources.
        self.resource_arn = resource_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        return self


class GetResourceTagsResponseBody(TeaModel):
    def __init__(self, resource_arn=None, tags=None):
        # The ARN of the resource. 
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource.
        self.resource_arn = resource_arn  # type: str
        # The tag dictionary.
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceTagsResponseBody, self).to_map()
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


class GetResourceTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceTagsResponse, self).to_map()
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
            temp_model = GetResourceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetServiceRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceRequest, self).to_map()
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


class GetServiceResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, internet_access=None, last_modified_time=None,
                 log_config=None, nas_config=None, oss_mount_config=None, role=None, service_id=None, service_name=None,
                 tracing_config=None, vpc_config=None):
        # The time when the service was created.
        self.created_time = created_time  # type: str
        # The description of the service.
        self.description = description  # type: str
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access  # type: bool
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The log configuration, which specifies a Logstore to store function execution logs.
        self.log_config = log_config  # type: LogConfig
        # The configuration of the NAS file system. The configuration allows functions in the specified service in Function Compute to access the NAS file system.
        self.nas_config = nas_config  # type: NASConfig
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        # The RAM role that is used to grant required permissions to Function Compute. Scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role  # type: str
        # The unique ID generated by the system for the service.
        self.service_id = service_id  # type: str
        # The name of the service.
        self.service_name = service_name  # type: str
        # The configurations of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config  # type: TracingConfig
        # The VPC configuration. The configuration allows a function to access the specified VPC.
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
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
        _map = super(GetServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceResponse, self).to_map()
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatefulAsyncInvocationHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_code_checksum=None, x_fc_date=None,
                 x_fc_invocation_type=None, x_fc_log_type=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The CRC-64 value of the function code package. This value is used to check data integrity. The value is automatically calculated by the tool.
        self.x_fc_code_checksum = x_fc_code_checksum  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The invocation method. 
        # 
        # - **Sync**: synchronous invocation 
        # - **Async**: asynchronous invocation
        self.x_fc_invocation_type = x_fc_invocation_type  # type: str
        # The method used to return logs. Valid values: 
        # 
        # - **Tail**: returns the last 4 KB of logs that are generated for the current request. 
        # - **None**: does not return logs for the current request. This is the default value.
        self.x_fc_log_type = x_fc_log_type  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStatefulAsyncInvocationHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetStatefulAsyncInvocationRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service to which the asynchronous task belongs.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStatefulAsyncInvocationRequest, self).to_map()
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


class GetStatefulAsyncInvocationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StatefulAsyncInvocation

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStatefulAsyncInvocationResponse, self).to_map()
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
            temp_model = StatefulAsyncInvocation()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTriggerHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTriggerHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class GetTriggerResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, domain_name=None, invocation_role=None,
                 last_modified_time=None, qualifier=None, source_arn=None, trigger_config=None, trigger_id=None, trigger_name=None,
                 trigger_type=None, url_internet=None, url_intranet=None):
        # The time when the trigger was created.
        self.created_time = created_time  # type: str
        # The description of the trigger.
        self.description = description  # type: str
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name  # type: str
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role  # type: str
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The ARN of the event source.
        self.source_arn = source_arn  # type: str
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   OSS trigger: [OSSTriggerConfig](javascript:void\(0\)).
        # *   Log Service trigger: [LogTriggerConfig](javascript:void\(0\)).
        # *   Time trigger: [TimeTriggerConfig](javascript:void\(0\)).
        # *   HTTP trigger: [HTTPTriggerConfig](javascript:void\(0\)).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](javascript:void\(0\)).
        # *   MNS topic trigger: [MnsTopicTriggerConfig](javascript:void\(0\)).
        self.trigger_config = trigger_config  # type: str
        # The unique ID of the trigger.
        self.trigger_id = trigger_id  # type: str
        # The name of the trigger.
        self.trigger_name = trigger_name  # type: str
        # The trigger type, such as **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, and **mns_topic**.
        self.trigger_type = trigger_type  # type: str
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet  # type: str
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class GetTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFunctionHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_invocation_type=None,
                 x_fc_log_type=None, x_fc_stateful_async_invocation_id=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The method used to invoke the function. Valid values:
        # 
        # *   **Sync**: synchronous
        # *   **Async**: asynchronous
        self.x_fc_invocation_type = x_fc_invocation_type  # type: str
        # The method used to return logs. Valid values:
        # 
        # *   **Tail**: returns the last 4 KB of logs that are generated for the current request.
        # *   **None**: No logs are returned for the current request. Default value: None.
        self.x_fc_log_type = x_fc_log_type  # type: str
        # The ID of the asynchronous task. You must enable the asynchronous task feature in advance.
        # 
        # > When you use an SDK to invoke a function, we recommend that you specify a business-related ID to facilitate subsequent operations. For example, you can use the video name as the invocation ID for a video-processing function. This way, you can use the ID to check whether the video is processed or terminate the processing of the video. The ID must start with a letter or an underscore (\_) and can contain letters, digits, underscores (\_), and hyphens (-). The ID can be up to 128 characters in length. If you do not specify the ID of the asynchronous invocation, Function Compute automatically generates an ID.
        self.x_fc_stateful_async_invocation_id = x_fc_stateful_async_invocation_id  # type: str
        # The trace ID of the request for Function Compute API. The value is the same as that of the **requestId** parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeFunctionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_stateful_async_invocation_id is not None:
            result['X-Fc-Stateful-Async-Invocation-Id'] = self.x_fc_stateful_async_invocation_id
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Stateful-Async-Invocation-Id') is not None:
            self.x_fc_stateful_async_invocation_id = m.get('X-Fc-Stateful-Async-Invocation-Id')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class InvokeFunctionRequest(TeaModel):
    def __init__(self, body=None, qualifier=None):
        # The event to be processed by the function. Set this parameter to a binary string. Function Compute passes the event to the function for processing.
        self.body = body  # type: bytes
        # The version or alias of the service.
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
        self.body = body  # type: bytes

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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


class ListAliasesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The start time when the function is invoked. Specify the time in the yyyy-mm-ddhh:mm:ss format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAliasesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListAliasesRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None, start_key=None):
        # The maximum number of resources to return.
        self.limit = limit  # type: int
        # The token used to obtain more results.
        self.next_token = next_token  # type: str
        # The prefix.
        self.prefix = prefix  # type: str
        # The starting position of the result list.
        self.start_key = start_key  # type: str

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListAliasesResponseBodyAliases(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, created_time=None, description=None,
                 last_modified_time=None, resolve_policy=None, route_policy=None, version_id=None):
        # The weight of the canary release version.
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # The name of the alias.
        self.alias_name = alias_name  # type: str
        # The creation time.
        self.created_time = created_time  # type: str
        # The description of the alias.
        self.description = description  # type: str
        # The last update time.
        self.last_modified_time = last_modified_time  # type: str
        self.resolve_policy = resolve_policy  # type: str
        self.route_policy = route_policy  # type: RoutePolicy
        # The ID of the version.
        self.version_id = version_id  # type: str

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

    def to_map(self):
        _map = super(ListAliasesResponseBodyAliases, self).to_map()
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
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
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
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListAliasesResponseBody(TeaModel):
    def __init__(self, aliases=None, next_token=None):
        # The list of aliases.
        self.aliases = aliases  # type: list[ListAliasesResponseBodyAliases]
        # The token used to obtain more results.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.aliases:
            for k in self.aliases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAliasesResponseBody, self).to_map()
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
                temp_model = ListAliasesResponseBodyAliases()
                self.aliases.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListAliasesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAliasesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomDomainsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomDomainsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListCustomDomainsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None, start_key=None):
        # The maximum number of resources to return. Valid values: \[0,100]. Default value: 20. The number of returned results is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token that is required for pagination. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # The prefix that the returned domain names must contain.
        self.prefix = prefix  # type: str
        # The starting position of the result list. The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListCustomDomainsResponseBodyCustomDomains(TeaModel):
    def __init__(self, account_id=None, api_version=None, cert_config=None, created_time=None, domain_name=None,
                 last_modified_time=None, protocol=None, route_config=None, tls_config=None, waf_config=None):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The version of the API.
        self.api_version = api_version  # type: str
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config  # type: CertConfig
        # The time when the custom domain name was created.
        self.created_time = created_time  # type: str
        # The domain name.
        self.domain_name = domain_name  # type: str
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The protocol type that is supported by the custom domain name.
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol  # type: str
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config  # type: RouteConfig
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config  # type: TLSConfig
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(ListCustomDomainsResponseBodyCustomDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class ListCustomDomainsResponseBody(TeaModel):
    def __init__(self, custom_domains=None, next_token=None):
        # The information about custom domain names.
        self.custom_domains = custom_domains  # type: list[ListCustomDomainsResponseBodyCustomDomains]
        # The pagination token to use to request the next page of results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.custom_domains:
            for k in self.custom_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomDomainsResponseBody, self).to_map()
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
                temp_model = ListCustomDomainsResponseBodyCustomDomains()
                self.custom_domains.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListCustomDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListCustomDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventSourcesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventSourcesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListEventSourcesRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventSourcesRequest, self).to_map()
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


class ListEventSourcesResponseBodyEventSources(TeaModel):
    def __init__(self, created_time=None, source_arn=None):
        # The time when the event source was created.
        self.created_time = created_time  # type: str
        # The ARN of the event source.
        self.source_arn = source_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEventSourcesResponseBodyEventSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        return self


class ListEventSourcesResponseBody(TeaModel):
    def __init__(self, event_sources=None):
        # The information about event sources.
        self.event_sources = event_sources  # type: list[ListEventSourcesResponseBodyEventSources]

    def validate(self):
        if self.event_sources:
            for k in self.event_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEventSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['eventSources'] = []
        if self.event_sources is not None:
            for k in self.event_sources:
                result['eventSources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_sources = []
        if m.get('eventSources') is not None:
            for k in m.get('eventSources'):
                temp_model = ListEventSourcesResponseBodyEventSources()
                self.event_sources.append(temp_model.from_map(k))
        return self


class ListEventSourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEventSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEventSourcesResponse, self).to_map()
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
            temp_model = ListEventSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionAsyncInvokeConfigsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_code_checksum=None, x_fc_date=None,
                 x_fc_invocation_type=None, x_fc_log_type=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The CRC-64 value of the function code package. This value is used to check data integrity. The value is automatically calculated by the tool.
        self.x_fc_code_checksum = x_fc_code_checksum  # type: str
        # The time when the Function Compute is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The invocation method.
        # 
        # *   **Sync**: synchronous
        # *   **Async**: asynchronous
        self.x_fc_invocation_type = x_fc_invocation_type  # type: str
        # The method used to return logs. Valid values:
        # 
        # *   **Tail**: returns the last 4 KB of logs that are generated for the current request.
        # *   **None**: No logs are returned for the current request. Default value: None.
        self.x_fc_log_type = x_fc_log_type  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionAsyncInvokeConfigsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListFunctionAsyncInvokeConfigsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None):
        # The maximum number of resources to return.
        self.limit = limit  # type: int
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionAsyncInvokeConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionAsyncInvokeConfigsResponseBodyConfigs(TeaModel):
    def __init__(self, created_time=None, destination_config=None, function=None, last_modified_time=None,
                 max_async_event_age_in_seconds=None, max_async_retry_attempts=None, qualifier=None, service=None, stateful_invocation=None):
        # The time when the desktop group was created.
        self.created_time = created_time  # type: str
        # The configuration structure of the destination for asynchronous invocations. If you have not configured this parameter, this parameter is null.
        self.destination_config = destination_config  # type: DestinationConfig
        # The name of the function.
        self.function = function  # type: str
        # The time when the configuration was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The maximum validity period of a message. If you have not configured this parameter, this parameter is null.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds  # type: long
        # The maximum number of retries allowed after an asynchronous invocation fails. If you have not configured this parameter, this parameter is null.
        self.max_async_retry_attempts = max_async_retry_attempts  # type: long
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The name of the service.
        self.service = service  # type: str
        # Indicates whether the asynchronous task feature is enabled.
        # 
        # *   **true**: The asynchronous task feature is enabled.
        # *   **false**: The asynchronous task feature is disabled.
        # 
        # If you have not configured this parameter, this parameter is null.
        self.stateful_invocation = stateful_invocation  # type: bool

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super(ListFunctionAsyncInvokeConfigsResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class ListFunctionAsyncInvokeConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, next_token=None):
        # The list of asynchronous invocation configurations.
        self.configs = configs  # type: list[ListFunctionAsyncInvokeConfigsResponseBodyConfigs]
        # The token used to obtain more results.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionAsyncInvokeConfigsResponseBody, self).to_map()
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
                temp_model = ListFunctionAsyncInvokeConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionAsyncInvokeConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionAsyncInvokeConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFunctionAsyncInvokeConfigsResponse, self).to_map()
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
            temp_model = ListFunctionAsyncInvokeConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None, qualifier=None, start_key=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # The prefix that the names of returned resources must contain.
        self.prefix = prefix  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFunctionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListFunctionsResponseBodyFunctions(TeaModel):
    def __init__(self, ca_port=None, code_checksum=None, code_size=None, cpu=None, created_time=None,
                 custom_container_config=None, custom_health_check_config=None, description=None, disk_size=None,
                 environment_variables=None, function_id=None, function_name=None, gpu_memory_size=None, handler=None,
                 initialization_timeout=None, initializer=None, instance_concurrency=None, instance_lifecycle_config=None,
                 instance_soft_concurrency=None, instance_type=None, last_modified_time=None, layers=None, memory_size=None, runtime=None,
                 timeout=None):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port  # type: int
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum  # type: str
        # The size of the function code package that is returned by the system. Unit: byte.
        self.code_size = code_size  # type: long
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu  # type: float
        # The time when the function was created.
        self.created_time = created_time  # type: str
        # The configurations of the custom container runtime.
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        # The custom health check configuration of the function. This parameter is applicable only to custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config  # type: CustomHealthCheckConfig
        # The description of the function.
        self.description = description  # type: str
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size  # type: int
        # The environment variables that you configured for the function. You can obtain the values of the environment variables from the function.
        self.environment_variables = environment_variables  # type: dict[str, str]
        # The unique ID generated by the system for the function.
        self.function_id = function_id  # type: str
        # The name of the function.
        self.function_name = function_name  # type: str
        self.gpu_memory_size = gpu_memory_size  # type: int
        # The handler of the function.
        self.handler = handler  # type: str
        # The timeout period for the execution of the initializer function. Unit: seconds. Default value: 3. Valid values: 1 to 300. When this period ends, the execution of the initializer function is terminated.
        self.initialization_timeout = initialization_timeout  # type: int
        # The handler of the initializer function. The format of the value is determined by the programming language that you use. For more information, see [Initializer function](~~157704~~).
        self.initializer = initializer  # type: str
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency  # type: int
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the number of the soft concurrency, the instance scale-up is triggered. For example, if your instance requires a long term to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of **instanceConcurrency**.
        self.instance_soft_concurrency = instance_soft_concurrency  # type: int
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        self.instance_type = instance_type  # type: str
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # An array that consists of the information of layers.
        # 
        # >  Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file with the same name in the layer with a larger subscript.
        self.layers = layers  # type: list[str]
        # The memory size for the function. Unit: MB.
        self.memory_size = memory_size  # type: int
        # The runtime environment of the function. Valid values: **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore2.1**, **custom** and **custom-container**.
        self.runtime = runtime  # type: str
        # The timeout period for the execution of the function. Unit: seconds. Default value: 60. Valid values: 1 to 600. When this period expires, the execution of the function is terminated.
        self.timeout = timeout  # type: int

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super(ListFunctionsResponseBodyFunctions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
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
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(self, functions=None, next_token=None):
        # The information about functions.
        self.functions = functions  # type: list[ListFunctionsResponseBodyFunctions]
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFunctionsResponseBody, self).to_map()
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
                temp_model = ListFunctionsResponseBodyFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFunctionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, instance_ids=None, limit=None, qualifier=None):
        # The IDs of the instance.
        self.instance_ids = instance_ids  # type: list[str]
        # The maximum number of resources to return. Valid values: \[0,1000].
        # 
        # The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The version or alias.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.limit is not None:
            result['limit'] = self.limit
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, instance_id=None, version_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The version of the service to which the instance belongs. If the instance belongs to the LATEST alias, 0 is returned as the version.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None):
        # The information about instances.
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayerVersionsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLayerVersionsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListLayerVersionsRequest(TeaModel):
    def __init__(self, limit=None, start_version=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The initial version of the layer.
        self.start_version = start_version  # type: int

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


class ListLayerVersionsResponseBody(TeaModel):
    def __init__(self, layers=None, next_version=None):
        # The information about layer versions.
        self.layers = layers  # type: list[Layer]
        # The initial version of the layer for the next query.
        self.next_version = next_version  # type: int

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLayerVersionsResponseBody, self).to_map()
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


class ListLayerVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLayerVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLayerVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayersHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLayersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListLayersRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, official=None, prefix=None, public=None, start_key=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned configurations is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token required to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # Specifies whether to obtain the official public layer. When the official parameter is set to true, the public field does not take effect. The default value is false.
        self.official = official  # type: bool
        # The name prefix of the layer. The names of returned resources must contain the prefix. If the name prefix is a, the names of returned resources must start with a.
        self.prefix = prefix  # type: str
        # Specifies whether to obtain only the common layer. Default value: false.
        self.public = public  # type: bool
        # The name of the start layer. The returned layers are sorted in alphabetical order, and the layers that include and follow the layer specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
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
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListLayersResponseBody(TeaModel):
    def __init__(self, layers=None, next_token=None):
        # The information about layers.
        self.layers = layers  # type: list[Layer]
        # The name of the start layer for the next query, which is also the token used to obtain more results.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLayersResponseBody, self).to_map()
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


class ListLayersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLayersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnDemandConfigsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOnDemandConfigsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListOnDemandConfigsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None, start_key=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # The prefix that the names of returned resources must contain. If the name prefix is a, the names of returned resources must start with a.
        self.prefix = prefix  # type: str
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOnDemandConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListOnDemandConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, next_token=None):
        # The information about the provisioned configuration.
        self.configs = configs  # type: list[OnDemandConfig]
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOnDemandConfigsResponseBody, self).to_map()
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
                temp_model = OnDemandConfig()
                self.configs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListOnDemandConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOnDemandConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOnDemandConfigsResponse, self).to_map()
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
            temp_model = ListOnDemandConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionConfigsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionConfigsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListProvisionConfigsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, qualifier=None, service_name=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: long
        # The token used to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token  # type: str
        # The qualifier of the service to which resources belong. The qualifier must be aliasName and used together with the serviceName parameter.
        self.qualifier = qualifier  # type: str
        # The name of the service to which resources belong.
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProvisionConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListProvisionConfigsResponseBodyProvisionConfigs(TeaModel):
    def __init__(self, always_allocate_cpu=None, current=None, current_error=None, resource=None,
                 scheduled_actions=None, target=None, target_tracking_policies=None):
        # Specifies whether to always allocate CPU to a function instance.
        self.always_allocate_cpu = always_allocate_cpu  # type: bool
        # The actual number of provisioned instances.
        self.current = current  # type: long
        # The error message returned if a provisioned instance fails to be created.
        self.current_error = current_error  # type: str
        # The description of the resource.
        self.resource = resource  # type: str
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions  # type: list[ScheduledActions]
        # The expected number of provisioned instances.
        self.target = target  # type: long
        # The configurations of metric-based auto scaling.
        self.target_tracking_policies = target_tracking_policies  # type: list[TargetTrackingPolicies]

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
        _map = super(ListProvisionConfigsResponseBodyProvisionConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.current_error is not None:
            result['currentError'] = self.current_error
        if self.resource is not None:
            result['resource'] = self.resource
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
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsResponseBody(TeaModel):
    def __init__(self, next_token=None, provision_configs=None):
        # The token used to obtain more results.
        self.next_token = next_token  # type: str
        # The information about provisioned instances.
        self.provision_configs = provision_configs  # type: list[ListProvisionConfigsResponseBodyProvisionConfigs]

    def validate(self):
        if self.provision_configs:
            for k in self.provision_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProvisionConfigsResponseBody, self).to_map()
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
                temp_model = ListProvisionConfigsResponseBodyProvisionConfigs()
                self.provision_configs.append(temp_model.from_map(k))
        return self


class ListProvisionConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProvisionConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListProvisionConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReservedCapacitiesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the Function Compute API is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListReservedCapacitiesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListReservedCapacitiesRequest(TeaModel):
    def __init__(self, limit=None, next_token=None):
        # The maximum number of resources to return. Valid values: \[1, 100].
        self.limit = limit  # type: str
        # The token that determines the start point of the query.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListReservedCapacitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListReservedCapacitiesResponseBody(TeaModel):
    def __init__(self, next_token=None, reserved_capacities=None):
        # The token used to obtain more results.
        self.next_token = next_token  # type: str
        # The information about subscription instances.
        self.reserved_capacities = reserved_capacities  # type: list[OpenReservedCapacity]

    def validate(self):
        if self.reserved_capacities:
            for k in self.reserved_capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListReservedCapacitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['reservedCapacities'] = []
        if self.reserved_capacities is not None:
            for k in self.reserved_capacities:
                result['reservedCapacities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.reserved_capacities = []
        if m.get('reservedCapacities') is not None:
            for k in m.get('reservedCapacities'):
                temp_model = OpenReservedCapacity()
                self.reserved_capacities.append(temp_model.from_map(k))
        return self


class ListReservedCapacitiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListReservedCapacitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListReservedCapacitiesResponse, self).to_map()
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
            temp_model = ListReservedCapacitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceVersionsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceVersionsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListServiceVersionsRequest(TeaModel):
    def __init__(self, direction=None, limit=None, next_token=None, start_key=None):
        # The order in which the returned versions are sorted. Valid values:
        #   - **FORWARD**: in ascending order. 
        #   - **BACKWARD**: in descending order. This is the default value.
        self.direction = direction  # type: str
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # The starting position of the result list. The returned resources are sorted based on the version number, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['direction'] = self.direction
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListServiceVersionsResponseBodyVersions(TeaModel):
    def __init__(self, created_time=None, description=None, last_modified_time=None, version_id=None):
        # The time when the service version was created.
        self.created_time = created_time  # type: str
        # The description of the service version.
        self.description = description  # type: str
        # The time when the service version was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The version of the service.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceVersionsResponseBodyVersions, self).to_map()
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


class ListServiceVersionsResponseBody(TeaModel):
    def __init__(self, direction=None, next_token=None, versions=None):
        # The order in which the returned versions are sorted. Valid values:
        #   - **FORWARD**: in ascending order. 
        #   - **BACKWARD**: in descending order. This is the default value.
        self.direction = direction  # type: str
        # The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # The list of versions.
        self.versions = versions  # type: list[ListServiceVersionsResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceVersionsResponseBody, self).to_map()
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
                temp_model = ListServiceVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListServiceVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceVersionsResponse, self).to_map()
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
            temp_model = ListServiceVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None, start_key=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned configurations is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The starting position of the query. If this parameter is left empty, the query starts from the beginning. You do not need to specify this parameter in the first query. If the number of asynchronous tasks exceeds the limit, the nextToken parameter is returned, the value of which can be used in subsequent calls to obtain more results.
        self.next_token = next_token  # type: str
        # The prefix that the names of returned resources must contain. If the name prefix is a, the names of returned resources must start with a.
        self.prefix = prefix  # type: str
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(self, created_time=None, description=None, internet_access=None, last_modified_time=None,
                 log_config=None, nas_config=None, oss_mount_config=None, role=None, service_id=None, service_name=None,
                 tracing_config=None, vpc_config=None):
        # The time when the service was created.
        self.created_time = created_time  # type: str
        # The description of the service.
        self.description = description  # type: str
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access  # type: bool
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The log configuration, which specifies a Logstore to store function execution logs.
        self.log_config = log_config  # type: LogConfig
        # The configurations of the NAS file system. The configuration allows functions in the specified service in Function Compute to access the NAS file system.
        self.nas_config = nas_config  # type: NASConfig
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role  # type: str
        # The unique ID generated by the system for the service.
        self.service_id = service_id  # type: str
        # The name of the service.
        self.service_name = service_name  # type: str
        # The configurations of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config  # type: TracingConfig
        # The VPC configuration. The configuration allows a function to access the specified VPC.
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
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
        _map = super(ListServicesResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, next_token=None, services=None):
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token  # type: str
        # The information about a service.
        self.services = services  # type: list[ListServicesResponseBodyServices]

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServicesResponse, self).to_map()
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatefulAsyncInvocationFunctionsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationFunctionsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListStatefulAsyncInvocationFunctionsRequest(TeaModel):
    def __init__(self, limit=None, next_token=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The starting position of the query. If this parameter is left empty, the query starts from the beginning. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationFunctionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationFunctionsResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None):
        # The details of returned data.
        self.data = data  # type: list[AsyncConfigMeta]
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationFunctionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = AsyncConfigMeta()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationFunctionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListStatefulAsyncInvocationFunctionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationFunctionsResponse, self).to_map()
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
            temp_model = ListStatefulAsyncInvocationFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStatefulAsyncInvocationsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_code_checksum=None, x_fc_date=None,
                 x_fc_invocation_type=None, x_fc_log_type=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The CRC-64 value of the function code package. This value is used to check data integrity. The value is automatically calculated by the tool.
        self.x_fc_code_checksum = x_fc_code_checksum  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The invocation method. 
        # 
        # - **Sync**: synchronous invocation 
        # - **Async**: asynchronous invocation
        self.x_fc_invocation_type = x_fc_invocation_type  # type: str
        # The method used to return logs. Valid values: 
        # 
        # - **Tail**: returns the last 4 KB of logs that are generated for the current request. 
        # - **None**: does not return logs for the current request. This is the default value.
        self.x_fc_log_type = x_fc_log_type  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_invocation_type is not None:
            result['X-Fc-Invocation-Type'] = self.x_fc_invocation_type
        if self.x_fc_log_type is not None:
            result['X-Fc-Log-Type'] = self.x_fc_log_type
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Invocation-Type') is not None:
            self.x_fc_invocation_type = m.get('X-Fc-Invocation-Type')
        if m.get('X-Fc-Log-Type') is not None:
            self.x_fc_log_type = m.get('X-Fc-Log-Type')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListStatefulAsyncInvocationsRequest(TeaModel):
    def __init__(self, include_payload=None, invocation_id_prefix=None, limit=None, next_token=None, qualifier=None,
                 sort_order_by_time=None, started_time_begin=None, started_time_end=None, status=None):
        # - **true**: returns the invocationPayload parameter in the response. 
        # - **false**: does not return the invocationPayload parameter in the response. 
        # 
        # > The `invocationPayload` parameter indicates the input parameters of an asynchronous task.
        self.include_payload = include_payload  # type: bool
        # The name prefix of the asynchronous invocation. The names of returned resources must contain the prefix. For example, if invocationidPrefix is set to job, the names of returned resources must start with job.
        self.invocation_id_prefix = invocation_id_prefix  # type: str
        # The maximum number of asynchronous invocations to return. Valid values: [1, 100]. Default value: 50.
        self.limit = limit  # type: int
        # The token used to obtain more results. If the number of resources exceeds the limit, the nextToken parameter is returned. You can include the parameter in subsequent calls to obtain more results. You do not need to provide this parameter in the first call.
        self.next_token = next_token  # type: str
        # The version or alias of the service to which the asynchronous task belongs.
        self.qualifier = qualifier  # type: str
        # The order in which the returned asynchronous invocations are sorted. Valid values:
        # 
        # - **asc**: in ascending order 
        # - **desc**: in descending order
        self.sort_order_by_time = sort_order_by_time  # type: str
        # The start time of the asynchronous task.
        self.started_time_begin = started_time_begin  # type: long
        # The end time of the asynchronous task.
        self.started_time_end = started_time_end  # type: long
        # The status of the asynchronous task. 
        # 
        # - **Enqueued**: The asynchronous invocation is enqueued and is waiting to be executed. 
        # - **Succeeded**: The invocation is successful. 
        # - **Failed**: The invocation fails. 
        # - **Running**: The invocation is being executed. 
        # - **Stopped**: The invocation is terminated. 
        # - **Stopping**: The invocation is being terminated. 
        # - **Invalid**: The invocation is invalid and not executed due to specific reasons. For example, the function is deleted. 
        # - **Expired**: The maximum validity period of messages is specified for asynchronous invocation. The invocation is discarded and not executed because the specified maximum validity period of messages expires. 
        # - **Retrying**: The asynchronous invocation is being retried due to an execution error.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_payload is not None:
            result['includePayload'] = self.include_payload
        if self.invocation_id_prefix is not None:
            result['invocationIdPrefix'] = self.invocation_id_prefix
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
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
        if m.get('invocationIdPrefix') is not None:
            self.invocation_id_prefix = m.get('invocationIdPrefix')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
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


class ListStatefulAsyncInvocationsResponseBody(TeaModel):
    def __init__(self, invocations=None, next_token=None):
        # The information about asynchronous tasks.
        self.invocations = invocations  # type: list[StatefulAsyncInvocation]
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['invocations'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invocations = []
        if m.get('invocations') is not None:
            for k in m.get('invocations'):
                temp_model = StatefulAsyncInvocation()
                self.invocations.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListStatefulAsyncInvocationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListStatefulAsyncInvocationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListStatefulAsyncInvocationsResponse, self).to_map()
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
            temp_model = ListStatefulAsyncInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaggedResourcesHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaggedResourcesHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListTaggedResourcesRequest(TeaModel):
    def __init__(self, limit=None, next_token=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token used to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTaggedResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListTaggedResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, resources=None):
        # The token used to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token  # type: str
        # The information about tagged services.
        self.resources = resources  # type: list[Resource]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTaggedResourcesResponseBody, self).to_map()
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


class ListTaggedResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTaggedResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTaggedResourcesResponse, self).to_map()
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
            temp_model = ListTaggedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTriggersHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTriggersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListTriggersRequest(TeaModel):
    def __init__(self, limit=None, next_token=None, prefix=None, start_key=None):
        # The maximum number of resources to return. Default value: 20. Maximum value: 100. The number of returned resources is less than or equal to the specified number.
        self.limit = limit  # type: int
        # The token required to obtain more results. You do not need to provide this parameter in the first call. The tokens for subsequent queries are obtained from the returned results.
        self.next_token = next_token  # type: str
        # The prefix that the names of returned resources must contain.
        self.prefix = prefix  # type: str
        # The returned resources are sorted in alphabetical order, and the resources that include and follow the resource specified by the startKey parameter are returned.
        self.start_key = start_key  # type: str

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
        if self.start_key is not None:
            result['startKey'] = self.start_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('startKey') is not None:
            self.start_key = m.get('startKey')
        return self


class ListTriggersResponseBodyTriggers(TeaModel):
    def __init__(self, created_time=None, description=None, domain_name=None, invocation_role=None,
                 last_modified_time=None, qualifier=None, source_arn=None, trigger_config=None, trigger_id=None, trigger_name=None,
                 trigger_type=None, url_internet=None, url_intranet=None):
        # The time when the trigger was created.
        self.created_time = created_time  # type: str
        # The description of the trigger.
        self.description = description  # type: str
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name  # type: str
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role  # type: str
        # The time when the trigger was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The ARN of the event source.
        self.source_arn = source_arn  # type: str
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   OSS trigger: [OSSTriggerConfig](javascript:void\(0\)).
        # *   Log Service trigger: [LogTriggerConfig](javascript:void\(0\)).
        # *   Time trigger: [TimeTriggerConfig](javascript:void\(0\)).
        # *   HTTP trigger: [HTTPTriggerConfig](javascript:void\(0\)).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](javascript:void\(0\)).
        # *   MNS topic trigger: [MnsTopicTriggerConfig](javascript:void\(0\)).
        self.trigger_config = trigger_config  # type: str
        # The unique ID of the trigger.
        self.trigger_id = trigger_id  # type: str
        # The name of the trigger.
        self.trigger_name = trigger_name  # type: str
        # The trigger type, such as **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, and **mns_topic**.
        self.trigger_type = trigger_type  # type: str
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet  # type: str
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTriggersResponseBodyTriggers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class ListTriggersResponseBody(TeaModel):
    def __init__(self, next_token=None, triggers=None):
        # The token used to obtain more results. If this parameter is left empty, all the results are returned.
        self.next_token = next_token  # type: str
        # The information about triggers.
        self.triggers = triggers  # type: list[ListTriggersResponseBodyTriggers]

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTriggersResponseBody, self).to_map()
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
                temp_model = ListTriggersResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListTriggersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTriggersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcBindingsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcBindingsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ListVpcBindingsResponseBody(TeaModel):
    def __init__(self, vpc_ids=None):
        # The IDs of bound VPCs.
        self.vpc_ids = vpc_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcBindingsResponseBody, self).to_map()
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


class ListVpcBindingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcBindingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListVpcBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishServiceVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ETag value of the service. This value is used to ensure that the modified service is consistent with the service to be modified. The ETag value is returned in the responses of the [CreateService](~~175256~~), [UpdateService](~~188167~~), and [GetService](~~189225~~) operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The start time when the function is invoked. Specify the time in the yyyy-mm-ddhh:mm:ss format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishServiceVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PublishServiceVersionRequest(TeaModel):
    def __init__(self, description=None):
        # The description of the service version.
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishServiceVersionRequest, self).to_map()
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


class PublishServiceVersionResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, last_modified_time=None, version_id=None):
        # The time when the service version was created.
        self.created_time = created_time  # type: str
        # The description of the service version.
        self.description = description  # type: str
        # The time when the service version was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The version of the service.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishServiceVersionResponseBody, self).to_map()
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


class PublishServiceVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublishServiceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishServiceVersionResponse, self).to_map()
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
            temp_model = PublishServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutFunctionAsyncInvokeConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutFunctionAsyncInvokeConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutFunctionAsyncInvokeConfigRequest(TeaModel):
    def __init__(self, destination_config=None, max_async_event_age_in_seconds=None,
                 max_async_retry_attempts=None, stateful_invocation=None, qualifier=None):
        # The configuration structure of the destination for asynchronous invocation.
        self.destination_config = destination_config  # type: DestinationConfig
        # The maximum validity period of messages. Valid values: 1 to 2592000. Unit: seconds.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds  # type: long
        # The maximum number of retries allowed after an asynchronous invocation fails. Default value: 3. Valid values: 0 to 8.
        self.max_async_retry_attempts = max_async_retry_attempts  # type: long
        # Specifies whether to enable the asynchronous task feature. 
        # 
        # - **true**: enables the asynchronous task feature. 
        # - **false**: does not enable the asynchronous task feature.
        self.stateful_invocation = stateful_invocation  # type: bool
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super(PutFunctionAsyncInvokeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutFunctionAsyncInvokeConfigResponseBody(TeaModel):
    def __init__(self, created_time=None, destination_config=None, function=None, last_modified_time=None,
                 max_async_event_age_in_seconds=None, max_async_retry_attempts=None, qualifier=None, service=None, stateful_invocation=None):
        # The creation time.
        self.created_time = created_time  # type: str
        # The configuration structure of the destination for asynchronous invocation.
        self.destination_config = destination_config  # type: DestinationConfig
        # The name of the function.
        self.function = function  # type: str
        # The time when the configuration was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The maximum validity period of messages.
        self.max_async_event_age_in_seconds = max_async_event_age_in_seconds  # type: long
        # The maximum number of retries allowed after an asynchronous invocation fails.
        self.max_async_retry_attempts = max_async_retry_attempts  # type: long
        # The qualifier.
        self.qualifier = qualifier  # type: str
        # The name of the service.
        self.service = service  # type: str
        # Specifies whether to enable the asynchronous task feature. 
        # 
        # - **true**: enables the asynchronous task feature. 
        # - **false**: does not enable the asynchronous task feature.
        self.stateful_invocation = stateful_invocation  # type: bool

    def validate(self):
        if self.destination_config:
            self.destination_config.validate()

    def to_map(self):
        _map = super(PutFunctionAsyncInvokeConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.destination_config is not None:
            result['destinationConfig'] = self.destination_config.to_map()
        if self.function is not None:
            result['function'] = self.function
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.max_async_event_age_in_seconds is not None:
            result['maxAsyncEventAgeInSeconds'] = self.max_async_event_age_in_seconds
        if self.max_async_retry_attempts is not None:
            result['maxAsyncRetryAttempts'] = self.max_async_retry_attempts
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.service is not None:
            result['service'] = self.service
        if self.stateful_invocation is not None:
            result['statefulInvocation'] = self.stateful_invocation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('destinationConfig') is not None:
            temp_model = DestinationConfig()
            self.destination_config = temp_model.from_map(m['destinationConfig'])
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('maxAsyncEventAgeInSeconds') is not None:
            self.max_async_event_age_in_seconds = m.get('maxAsyncEventAgeInSeconds')
        if m.get('maxAsyncRetryAttempts') is not None:
            self.max_async_retry_attempts = m.get('maxAsyncRetryAttempts')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('statefulInvocation') is not None:
            self.stateful_invocation = m.get('statefulInvocation')
        return self


class PutFunctionAsyncInvokeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutFunctionAsyncInvokeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutFunctionAsyncInvokeConfigResponse, self).to_map()
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
            temp_model = PutFunctionAsyncInvokeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutFunctionOnDemandConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # If the ETag specified in the request matches the ETag value of the OndemandConfig, FC returns 200 OK. If the ETag specified in the request does not match the ETag value of the object, FC returns 412 Precondition Failed.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The start time when the function is invoked. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API, which is also the unique ID of the request.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutFunctionOnDemandConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutFunctionOnDemandConfigRequest(TeaModel):
    def __init__(self, maximum_instance_count=None, qualifier=None):
        # The maximum number of on-demand instances. For more information, see [Instance scaling limits](~~185038~~).
        self.maximum_instance_count = maximum_instance_count  # type: long
        # The alias of the service or LATEST.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutFunctionOnDemandConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutFunctionOnDemandConfigResponseBody(TeaModel):
    def __init__(self, maximum_instance_count=None, resource=None):
        # The maximum number of instances.
        self.maximum_instance_count = maximum_instance_count  # type: long
        # The description of the resource.
        self.resource = resource  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutFunctionOnDemandConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class PutFunctionOnDemandConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutFunctionOnDemandConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutFunctionOnDemandConfigResponse, self).to_map()
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
            temp_model = PutFunctionOnDemandConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLayerACLHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request for Function Compute API.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutLayerACLHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutLayerACLRequest(TeaModel):
    def __init__(self, public=None):
        # Specifies whether the layer is public.
        # 
        # *   **true**: Public.
        # *   **false**: Not public.
        self.public = public  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutLayerACLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class PutLayerACLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class PutProvisionConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutProvisionConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class PutProvisionConfigRequest(TeaModel):
    def __init__(self, always_allocate_cpu=None, scheduled_actions=None, target=None,
                 target_tracking_policies=None, qualifier=None):
        # Specifies whether to always allocate CPU resources. Default value: true.
        self.always_allocate_cpu = always_allocate_cpu  # type: bool
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions  # type: list[ScheduledActions]
        # The number of provisioned instances. Value range: [1,100000].
        self.target = target  # type: long
        # The configurations of metric-based auto scaling.
        self.target_tracking_policies = target_tracking_policies  # type: list[TargetTrackingPolicies]
        # The name of the alias.
        self.qualifier = qualifier  # type: str

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
        _map = super(PutProvisionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
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
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class PutProvisionConfigResponseBody(TeaModel):
    def __init__(self, always_allocate_cpu=None, current=None, resource=None, scheduled_actions=None, target=None,
                 target_tracking_policies=None):
        # Specifies whether to always allocate CPU to a function instance.
        self.always_allocate_cpu = always_allocate_cpu  # type: bool
        # The actual number of provisioned instances.
        self.current = current  # type: long
        # The description of the resource.
        self.resource = resource  # type: str
        # The configurations of scheduled auto scaling.
        self.scheduled_actions = scheduled_actions  # type: list[ScheduledActions]
        # The expected number of provisioned instances.
        self.target = target  # type: long
        # The configurations of metric-based auto scaling.
        self.target_tracking_policies = target_tracking_policies  # type: list[TargetTrackingPolicies]

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
        _map = super(PutProvisionConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu
        if self.current is not None:
            result['current'] = self.current
        if self.resource is not None:
            result['resource'] = self.resource
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
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        self.scheduled_actions = []
        if m.get('scheduledActions') is not None:
            for k in m.get('scheduledActions'):
                temp_model = ScheduledActions()
                self.scheduled_actions.append(temp_model.from_map(k))
        if m.get('target') is not None:
            self.target = m.get('target')
        self.target_tracking_policies = []
        if m.get('targetTrackingPolicies') is not None:
            for k in m.get('targetTrackingPolicies'):
                temp_model = TargetTrackingPolicies()
                self.target_tracking_policies.append(temp_model.from_map(k))
        return self


class PutProvisionConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutProvisionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PutProvisionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterEventSourceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterEventSourceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class RegisterEventSourceRequest(TeaModel):
    def __init__(self, source_arn=None, qualifier=None):
        # The Alibaba Cloud Resource Name (ARN) of the event source.
        self.source_arn = source_arn  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterEventSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        return self


class RegisterEventSourceResponseBody(TeaModel):
    def __init__(self, created_time=None, source_arn=None):
        # The time when the event source was created.
        self.created_time = created_time  # type: str
        # The ARN of the event source.
        self.source_arn = source_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterEventSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        return self


class RegisterEventSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterEventSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterEventSourceResponse, self).to_map()
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
            temp_model = RegisterEventSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseGPUInstanceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format of the value is: EEE,d MMM yyyy HH:mm:ss GMT.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseGPUInstanceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class ReleaseGPUInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(ReleaseGPUInstanceResponse, self).to_map()
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


class StopStatefulAsyncInvocationHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStatefulAsyncInvocationHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class StopStatefulAsyncInvocationRequest(TeaModel):
    def __init__(self, qualifier=None):
        # The version or alias of the service to which the asynchronous task belongs.
        self.qualifier = qualifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStatefulAsyncInvocationRequest, self).to_map()
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


class StopStatefulAsyncInvocationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(StopStatefulAsyncInvocationResponse, self).to_map()
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


class TagResourceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the function is invoked. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class TagResourceRequest(TeaModel):
    def __init__(self, resource_arn=None, tags=None):
        # The ARN of the resource.
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource. You can manage tags only for services for top level resources.
        self.resource_arn = resource_arn  # type: str
        # The tag dictionary.
        self.tags = tags  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourceRequest, self).to_map()
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


class TagResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(TagResourceResponse, self).to_map()
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


class UntagResourceHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when Function Compute API is called. Specify the time in the **EEE,d MMM yyyy HH:mm:ss GMT** format.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UntagResourceRequest(TeaModel):
    def __init__(self, all=None, resource_arn=None, tag_keys=None):
        # Specifies whether to remove all tags. This parameter takes effect only when no tag key is specified. Valid values:
        #   - **true**: removes all tags. 
        #   - **false**: does not remove all tags.
        self.all = all  # type: bool
        # The ARN of the resource. 
        # 
        # > You can use the value of this parameter to query the information about the resource, such as the account, service, and region information of the resource. You can manage tags only for services for top level resources.
        self.resource_arn = resource_arn  # type: str
        # The keys of the tags that you want to remove.
        self.tag_keys = tag_keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn
        if self.tag_keys is not None:
            result['tagKeys'] = self.tag_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')
        if m.get('tagKeys') is not None:
            self.tag_keys = m.get('tagKeys')
        return self


class UntagResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(UntagResourceResponse, self).to_map()
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


class UpdateAliasHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # If the ETag specified in the request matches the ETag value of the object, the object and 200 OK are returned. Otherwise, 412 Precondition Failed is returned.
        # 
        # The ETag value of an object is used to check data integrity of the object. This parameter is empty by default.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the invocation request of Function Compute.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliasHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateAliasRequest(TeaModel):
    def __init__(self, additional_version_weight=None, description=None, resolve_policy=None, route_policy=None,
                 version_id=None):
        # The canary release version to which the alias points and the weight of the canary release version.
        # 
        # *   The canary release version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # The description of the alias.
        self.description = description  # type: str
        # The canary release mode. Valid values:
        # 
        # *   **Random**: random canary release. This is the default value.
        # *   **Content**: rule-based canary release.
        self.resolve_policy = resolve_policy  # type: str
        # The canary release rule. Traffic that meets the canary release rule is routed to the canary release instance.
        self.route_policy = route_policy  # type: RoutePolicy
        # The ID of the version to which the alias points.
        self.version_id = version_id  # type: str

    def validate(self):
        if self.route_policy:
            self.route_policy.validate()

    def to_map(self):
        _map = super(UpdateAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_version_weight is not None:
            result['additionalVersionWeight'] = self.additional_version_weight
        if self.description is not None:
            result['description'] = self.description
        if self.resolve_policy is not None:
            result['resolvePolicy'] = self.resolve_policy
        if self.route_policy is not None:
            result['routePolicy'] = self.route_policy.to_map()
        if self.version_id is not None:
            result['versionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalVersionWeight') is not None:
            self.additional_version_weight = m.get('additionalVersionWeight')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('resolvePolicy') is not None:
            self.resolve_policy = m.get('resolvePolicy')
        if m.get('routePolicy') is not None:
            temp_model = RoutePolicy()
            self.route_policy = temp_model.from_map(m['routePolicy'])
        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')
        return self


class UpdateAliasResponseBody(TeaModel):
    def __init__(self, additional_version_weight=None, alias_name=None, created_time=None, description=None,
                 last_modified_time=None, version_id=None):
        # The canary release version to which the alias points and the weight of the canary release version.
        # 
        # *   The canary release version takes effect only when the function is invoked.
        # *   The value consists of a version number and a specific weight. For example, 2:0.05 indicates that when a function is invoked, Version 2 is the canary release version, 5% of the traffic is distributed to the canary release version, and 95% of the traffic is distributed to the major version.
        self.additional_version_weight = additional_version_weight  # type: dict[str, float]
        # The name of the alias.
        self.alias_name = alias_name  # type: str
        # The time when the alias was created.
        self.created_time = created_time  # type: str
        # The description of the alias.
        self.description = description  # type: str
        # The time when the alias was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The ID of the version to which the alias points.
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAliasResponseBody, self).to_map()
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


class UpdateAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAliasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomDomainHeaders(TeaModel):
    def __init__(self, common_headers=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the operation is called. The format is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCustomDomainHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateCustomDomainRequest(TeaModel):
    def __init__(self, cert_config=None, protocol=None, route_config=None, tls_config=None, waf_config=None):
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config  # type: CertConfig
        # The protocol types supported by the domain name. Valid values:
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: Both HTTP and HTTPS are supported.
        self.protocol = protocol  # type: str
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config  # type: RouteConfig
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config  # type: TLSConfig
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(UpdateCustomDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateCustomDomainResponseBody(TeaModel):
    def __init__(self, account_id=None, api_version=None, cert_config=None, created_time=None, domain_name=None,
                 last_modified_time=None, protocol=None, route_config=None, tls_config=None, waf_config=None):
        # The ID of your Alibaba Cloud account.
        self.account_id = account_id  # type: str
        # The version of the API.
        self.api_version = api_version  # type: str
        # The configurations of the HTTPS certificate.
        self.cert_config = cert_config  # type: CertConfig
        # The time when the custom domain name was created.
        self.created_time = created_time  # type: str
        # The domain name.
        self.domain_name = domain_name  # type: str
        # The time when the domain name was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The protocol type that is supported by the custom domain name.
        # 
        # *   **HTTP**: Only HTTP is supported.
        # *   **HTTPS**: Only HTTPS is supported.
        # *   **HTTP,HTTPS**: HTTP and HTTPS are supported.
        self.protocol = protocol  # type: str
        # The route table that maps the paths to functions when the functions are invoked by using the custom domain name.
        self.route_config = route_config  # type: RouteConfig
        # The Transport Layer Security (TLS) configuration.
        self.tls_config = tls_config  # type: TLSConfig
        # The Web Application Firewall (WAF) configuration.
        self.waf_config = waf_config  # type: WAFConfig

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(UpdateCustomDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
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
        if m.get('tlsConfig') is not None:
            temp_model = TLSConfig()
            self.tls_config = temp_model.from_map(m['tlsConfig'])
        if m.get('wafConfig') is not None:
            temp_model = WAFConfig()
            self.waf_config = temp_model.from_map(m['wafConfig'])
        return self


class UpdateCustomDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCustomDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_code_checksum=None,
                 x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The ETag value of the resource. The value is used to ensure that the modified resource is consistent with the resource to be modified. The ETag value is returned in the responses of the [CreateFunction](~~415747~~), [GetFunction](~~415750~~), and [UpdateFunction](~~415749~~) operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The CRC-64 value of the function code package.
        self.x_fc_code_checksum = x_fc_code_checksum  # type: str
        # The time on which the function is invoked. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The trace ID of the request. The value is the same as that of the requestId parameter in the response.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFunctionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_code_checksum is not None:
            result['X-Fc-Code-Checksum'] = self.x_fc_code_checksum
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Code-Checksum') is not None:
            self.x_fc_code_checksum = m.get('X-Fc-Code-Checksum')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(self, instance_concurrency=None, ca_port=None, code=None, cpu=None, custom_container_config=None,
                 custom_dns=None, custom_health_check_config=None, custom_runtime_config=None, description=None,
                 disk_size=None, environment_variables=None, gpu_memory_size=None, handler=None, initialization_timeout=None,
                 initializer=None, instance_lifecycle_config=None, instance_soft_concurrency=None, instance_type=None,
                 layers=None, memory_size=None, runtime=None, timeout=None):
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency  # type: int
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port  # type: int
        # **Function code packages** can be provided with the following two methods. You must use only one of the methods in a request.
        # 
        # *   Specify the name of the **Object Storage Service (OSS) bucket** and **object** where the code package is stored.
        # *   Specify that the **zipFile** parameter is used as the Base64-encoded content of the ZIP file.
        self.code = code  # type: Code
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu  # type: float
        # The configuration of the custom container. After you configure the custom container, Function Compute can execute functions in a container created from a custom image.
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns  # type: CustomDNS
        # The custom health check configurations of the function. This parameter is applicable to only custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config  # type: CustomHealthCheckConfig
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        # The description of the function.
        self.description = description  # type: str
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size  # type: int
        # The environment variables that are configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Environment variables](~~69777~~).
        self.environment_variables = environment_variables  # type: dict[str, str]
        self.gpu_memory_size = gpu_memory_size  # type: int
        # The handler of the function. The format varies based on the programming language. For more information, see [Function handlers](~~157704~~).
        self.handler = handler  # type: str
        # The timeout period for the execution of the initializer function. Unit: seconds. Default value: 3. Minimum value: 1. When the period ends, the execution of the initializer function is terminated.
        self.initialization_timeout = initialization_timeout  # type: int
        # The handler of the initializer function. The format is determined by the programming language. For more information, see [Function handlers](~~157704~~).
        self.initializer = initializer  # type: str
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the number of the soft concurrency, the instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency  # type: int
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        self.instance_type = instance_type  # type: str
        # The information about layers.
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name and a larger subscript in the layer.
        self.layers = layers  # type: list[str]
        # The memory size for the function. Unit: MB. The memory size must be a multiple of 64 MB. The memory size varies based on the function instance type. For more information, see [Instance types](~~179379~~).
        self.memory_size = memory_size  # type: int
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom** and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime  # type: str
        # The timeout period for the execution of the function. Unit: seconds. Default value: 3. Minimum value: 1. When the period ends, the execution of the function is terminated.
        self.timeout = timeout  # type: int

    def validate(self):
        if self.code:
            self.code.validate()
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super(UpdateFunctionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
        if self.code is not None:
            result['code'] = self.code.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.custom_container_config is not None:
            result['customContainerConfig'] = self.custom_container_config.to_map()
        if self.custom_dns is not None:
            result['customDNS'] = self.custom_dns.to_map()
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
        if m.get('code') is not None:
            temp_model = Code()
            self.code = temp_model.from_map(m['code'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('customContainerConfig') is not None:
            temp_model = CustomContainerConfig()
            self.custom_container_config = temp_model.from_map(m['customContainerConfig'])
        if m.get('customDNS') is not None:
            temp_model = CustomDNS()
            self.custom_dns = temp_model.from_map(m['customDNS'])
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(self, ca_port=None, code_checksum=None, code_size=None, cpu=None, created_time=None,
                 custom_container_config=None, custom_dns=None, custom_health_check_config=None, custom_runtime_config=None,
                 description=None, disk_size=None, environment_variables=None, function_id=None, function_name=None,
                 gpu_memory_size=None, handler=None, initialization_timeout=None, initializer=None, instance_concurrency=None,
                 instance_lifecycle_config=None, instance_soft_concurrency=None, instance_type=None, last_modified_time=None, layers=None,
                 memory_size=None, runtime=None, timeout=None):
        # The port on which the HTTP server listens for the custom runtime or custom container runtime.
        self.ca_port = ca_port  # type: int
        # The CRC-64 value of the function code package.
        self.code_checksum = code_checksum  # type: str
        # The size of the function code package that is returned by the system. Unit: byte.
        self.code_size = code_size  # type: long
        # The number of vCPUs of the function. The value must be a multiple of 0.05.
        self.cpu = cpu  # type: float
        # The time when the function is created.
        self.created_time = created_time  # type: str
        # The configurations of the custom container runtime. After you configure the custom container runtime, Function Compute can execute the function in a container created from a custom image.
        self.custom_container_config = custom_container_config  # type: CustomContainerConfig
        # The custom DNS configurations of the function.
        self.custom_dns = custom_dns  # type: CustomDNS
        # The custom health check configurations of the function. This parameter is applicable to only custom runtimes and custom containers.
        self.custom_health_check_config = custom_health_check_config  # type: CustomHealthCheckConfig
        # The configurations of the custom runtime.
        self.custom_runtime_config = custom_runtime_config  # type: CustomRuntimeConfig
        # The description of the function.
        self.description = description  # type: str
        # The disk size of the function. Unit: MB. Valid values: 512 and 10240.
        self.disk_size = disk_size  # type: int
        # The environment variables that are configured for the function. You can obtain the values of the environment variables from the function. For more information, see [Environment variables](~~69777~~).
        self.environment_variables = environment_variables  # type: dict[str, str]
        # The unique ID that is generated by the system for the function.
        self.function_id = function_id  # type: str
        # The name of the function.
        self.function_name = function_name  # type: str
        self.gpu_memory_size = gpu_memory_size  # type: int
        # The handler of the function.
        self.handler = handler  # type: str
        # The timeout period for the execution of the initializer function. Unit: seconds. Default value: 3. Minimum value: 1. When the period ends, the execution of the initializer function is terminated.
        self.initialization_timeout = initialization_timeout  # type: int
        # The handler of the initializer function. The format is determined by the programming language.
        self.initializer = initializer  # type: str
        # The number of requests that can be concurrently processed by a single instance.
        self.instance_concurrency = instance_concurrency  # type: int
        # The lifecycle configurations of the instance.
        self.instance_lifecycle_config = instance_lifecycle_config  # type: InstanceLifecycleConfig
        # The soft concurrency of the instance. You can use this parameter to implement graceful scale-up of instances. If the number of concurrent requests on an instance is greater than the number of the soft concurrency, the instance scale-up is triggered. For example, if your instance requires a long time to start, you can specify a suitable soft concurrency to start the instance in advance.
        # 
        # The value must be less than or equal to that of the **instanceConcurrency** parameter.
        self.instance_soft_concurrency = instance_soft_concurrency  # type: int
        # The instance type of the function. Valid values:
        # 
        # *   **e1**: elastic instance
        # *   **c1**: performance instance
        self.instance_type = instance_type  # type: str
        # The time when the function was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The information about layers.
        # 
        # > Multiple layers are merged based on the order of array subscripts. The content of a layer with a smaller subscript overwrites the file that has the same name and a larger subscript in the layer.
        self.layers = layers  # type: list[str]
        # The memory size that is configured for the function. Unit: MB.
        self.memory_size = memory_size  # type: int
        # The runtime environment of the function. Valid values: **nodejs16**, **nodejs14**, **nodejs12**, **nodejs10**, **nodejs8**, **nodejs6**, **nodejs4.4**, **python3.9**, **python3**, **python2.7**, **java11**, **java8**, **go1**, **php7.2**, **dotnetcore3.1**, **dotnetcore2.1**, **custom** and **custom-container**. For more information, see [Supported function runtime environments](~~73338~~).
        self.runtime = runtime  # type: str
        # The timeout period for the execution. Unit: seconds.
        self.timeout = timeout  # type: int

    def validate(self):
        if self.custom_container_config:
            self.custom_container_config.validate()
        if self.custom_dns:
            self.custom_dns.validate()
        if self.custom_health_check_config:
            self.custom_health_check_config.validate()
        if self.custom_runtime_config:
            self.custom_runtime_config.validate()
        if self.instance_lifecycle_config:
            self.instance_lifecycle_config.validate()

    def to_map(self):
        _map = super(UpdateFunctionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_port is not None:
            result['caPort'] = self.ca_port
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
        if self.custom_health_check_config is not None:
            result['customHealthCheckConfig'] = self.custom_health_check_config.to_map()
        if self.custom_runtime_config is not None:
            result['customRuntimeConfig'] = self.custom_runtime_config.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.disk_size is not None:
            result['diskSize'] = self.disk_size
        if self.environment_variables is not None:
            result['environmentVariables'] = self.environment_variables
        if self.function_id is not None:
            result['functionId'] = self.function_id
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.gpu_memory_size is not None:
            result['gpuMemorySize'] = self.gpu_memory_size
        if self.handler is not None:
            result['handler'] = self.handler
        if self.initialization_timeout is not None:
            result['initializationTimeout'] = self.initialization_timeout
        if self.initializer is not None:
            result['initializer'] = self.initializer
        if self.instance_concurrency is not None:
            result['instanceConcurrency'] = self.instance_concurrency
        if self.instance_lifecycle_config is not None:
            result['instanceLifecycleConfig'] = self.instance_lifecycle_config.to_map()
        if self.instance_soft_concurrency is not None:
            result['instanceSoftConcurrency'] = self.instance_soft_concurrency
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.layers is not None:
            result['layers'] = self.layers
        if self.memory_size is not None:
            result['memorySize'] = self.memory_size
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('caPort') is not None:
            self.ca_port = m.get('caPort')
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
        if m.get('customHealthCheckConfig') is not None:
            temp_model = CustomHealthCheckConfig()
            self.custom_health_check_config = temp_model.from_map(m['customHealthCheckConfig'])
        if m.get('customRuntimeConfig') is not None:
            temp_model = CustomRuntimeConfig()
            self.custom_runtime_config = temp_model.from_map(m['customRuntimeConfig'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diskSize') is not None:
            self.disk_size = m.get('diskSize')
        if m.get('environmentVariables') is not None:
            self.environment_variables = m.get('environmentVariables')
        if m.get('functionId') is not None:
            self.function_id = m.get('functionId')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('gpuMemorySize') is not None:
            self.gpu_memory_size = m.get('gpuMemorySize')
        if m.get('handler') is not None:
            self.handler = m.get('handler')
        if m.get('initializationTimeout') is not None:
            self.initialization_timeout = m.get('initializationTimeout')
        if m.get('initializer') is not None:
            self.initializer = m.get('initializer')
        if m.get('instanceConcurrency') is not None:
            self.instance_concurrency = m.get('instanceConcurrency')
        if m.get('instanceLifecycleConfig') is not None:
            temp_model = InstanceLifecycleConfig()
            self.instance_lifecycle_config = temp_model.from_map(m['instanceLifecycleConfig'])
        if m.get('instanceSoftConcurrency') is not None:
            self.instance_soft_concurrency = m.get('instanceSoftConcurrency')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('layers') is not None:
            self.layers = m.get('layers')
        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFunctionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # The value used to ensure that the modified service is consistent with the service to be modified. The value is obtained from the responses of the [CreateService](~~175256~~), [UpdateService](~~188167~~), and [GetService](~~189225~~) operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the Function Compute API is called. The format is **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(self, description=None, internet_access=None, log_config=None, nas_config=None,
                 oss_mount_config=None, role=None, tracing_config=None, vpc_config=None):
        # The description of the service.
        self.description = description  # type: str
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access  # type: bool
        # The log configuration. Function Compute writes function execution logs to the specified Logstore.
        self.log_config = log_config  # type: LogConfig
        # The configurations of the NAS file system. The configurations allow functions to access the specified NAS resources.
        self.nas_config = nas_config  # type: NASConfig
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role  # type: str
        # The configurations of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config  # type: TracingConfig
        # The virtual private cloud (VPC) configuration, which allows functions in the specified service in Function Compute to access the specified VPC.
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
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
        _map = super(UpdateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, internet_access=None, last_modified_time=None,
                 log_config=None, nas_config=None, oss_mount_config=None, role=None, service_id=None, service_name=None,
                 tracing_config=None, vpc_config=None):
        # The time when the service was created.
        self.created_time = created_time  # type: str
        # The description of the service.
        self.description = description  # type: str
        # Specifies whether to allow functions to access the Internet. Valid values:
        # 
        # *   **true**: allows functions in the specified service to access the Internet.
        # *   **false**: does not allow functions in the specified service to access the Internet.
        self.internet_access = internet_access  # type: bool
        # The time when the service was last modified.
        self.last_modified_time = last_modified_time  # type: str
        # The log configuration, which specifies a Logstore to store function execution logs.
        self.log_config = log_config  # type: LogConfig
        # The configurations of the NAS file system. The configuration allows functions in the specified service in Function Compute to access the NAS file system.
        self.nas_config = nas_config  # type: NASConfig
        # The OSS mount configurations.
        self.oss_mount_config = oss_mount_config  # type: OSSMountConfig
        # The RAM role that is used to grant required permissions to Function Compute. The RAM role is used in the following scenarios:
        # 
        # *   Sends function execution logs to your Logstore.
        # *   Generates a token for a function to access other cloud resources during function execution.
        self.role = role  # type: str
        # The unique ID generated by the system for the service.
        self.service_id = service_id  # type: str
        # The name of the service.
        self.service_name = service_name  # type: str
        # The configurations of Tracing Analysis. After you configure Tracing Analysis for a service in Function Compute, you can record the execution duration of a request, view the amount of cold start time for a function, and record the execution duration of a function. For more information, see [Overview](~~189804~~).
        self.tracing_config = tracing_config  # type: TracingConfig
        # The VPC configuration. The configuration allows a function to access the specified VPC.
        self.vpc_config = vpc_config  # type: VPCConfig

    def validate(self):
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
        _map = super(UpdateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.internet_access is not None:
            result['internetAccess'] = self.internet_access
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.log_config is not None:
            result['logConfig'] = self.log_config.to_map()
        if self.nas_config is not None:
            result['nasConfig'] = self.nas_config.to_map()
        if self.oss_mount_config is not None:
            result['ossMountConfig'] = self.oss_mount_config.to_map()
        if self.role is not None:
            result['role'] = self.role
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.tracing_config is not None:
            result['tracingConfig'] = self.tracing_config.to_map()
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('internetAccess') is not None:
            self.internet_access = m.get('internetAccess')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('logConfig') is not None:
            temp_model = LogConfig()
            self.log_config = temp_model.from_map(m['logConfig'])
        if m.get('nasConfig') is not None:
            temp_model = NASConfig()
            self.nas_config = temp_model.from_map(m['nasConfig'])
        if m.get('ossMountConfig') is not None:
            temp_model = OSSMountConfig()
            self.oss_mount_config = temp_model.from_map(m['ossMountConfig'])
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('tracingConfig') is not None:
            temp_model = TracingConfig()
            self.tracing_config = temp_model.from_map(m['tracingConfig'])
        if m.get('vpcConfig') is not None:
            temp_model = VPCConfig()
            self.vpc_config = temp_model.from_map(m['vpcConfig'])
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceResponse, self).to_map()
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTriggerHeaders(TeaModel):
    def __init__(self, common_headers=None, if_match=None, x_fc_account_id=None, x_fc_date=None, x_fc_trace_id=None):
        self.common_headers = common_headers  # type: dict[str, str]
        # This parameter is used to ensure that the modified resource is consistent with the resource to be modified. You can obtain the parameter value from the responses of [CreateTrigger](~~190054~~), [GetTrigger](~~190056~~), and [UpdateTrigger](~~190055~~) operations.
        self.if_match = if_match  # type: str
        # The ID of your Alibaba Cloud account.
        self.x_fc_account_id = x_fc_account_id  # type: str
        # The time when the request is initiated on the client. The format of the value is: **EEE,d MMM yyyy HH:mm:ss GMT**.
        self.x_fc_date = x_fc_date  # type: str
        # The custom request ID.
        self.x_fc_trace_id = x_fc_trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.if_match is not None:
            result['If-Match'] = self.if_match
        if self.x_fc_account_id is not None:
            result['X-Fc-Account-Id'] = self.x_fc_account_id
        if self.x_fc_date is not None:
            result['X-Fc-Date'] = self.x_fc_date
        if self.x_fc_trace_id is not None:
            result['X-Fc-Trace-Id'] = self.x_fc_trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('If-Match') is not None:
            self.if_match = m.get('If-Match')
        if m.get('X-Fc-Account-Id') is not None:
            self.x_fc_account_id = m.get('X-Fc-Account-Id')
        if m.get('X-Fc-Date') is not None:
            self.x_fc_date = m.get('X-Fc-Date')
        if m.get('X-Fc-Trace-Id') is not None:
            self.x_fc_trace_id = m.get('X-Fc-Trace-Id')
        return self


class UpdateTriggerRequest(TeaModel):
    def __init__(self, description=None, invocation_role=None, qualifier=None, trigger_config=None):
        # The description of the trigger.
        self.description = description  # type: str
        # The role that is used by the event source such as OSS to invoke the function. For more information, see [Overview](~~53102~~).
        self.invocation_role = invocation_role  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The configurations of the trigger. The configurations vary based on the trigger type. For more information about the format, see the following topics:
        # 
        # *   OSS trigger: [OSSTriggerConfig](javascript:void\(0\)).
        # *   Log Service trigger: [LogTriggerConfig](javascript:void\(0\)).
        # *   Time trigger: [TimeTriggerConfig](javascript:void\(0\)).
        # *   HTTP trigger: [HTTPTriggerConfig](javascript:void\(0\)).
        # *   Tablestore trigger: Specify the **SourceArn** parameter and leave this parameter empty.
        # *   Alibaba Cloud CDN event trigger: [CDNEventsTriggerConfig](javascript:void\(0\)).
        # *   MNS topic trigger: [MnsTopicTriggerConfig](javascript:void\(0\)).
        self.trigger_config = trigger_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerRequest, self).to_map()
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


class UpdateTriggerResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, domain_name=None, invocation_role=None,
                 last_modified_time=None, qualifier=None, source_arn=None, trigger_config=None, trigger_id=None, trigger_name=None,
                 trigger_type=None, url_internet=None, url_intranet=None):
        # The time when the audio or video file was created.
        self.created_time = created_time  # type: str
        # The description of the trigger.
        self.description = description  # type: str
        # The domain name used to invoke the function by using HTTP. You can add this domain name as the prefix to the endpoint of Function Compute. This way, you can invoke the function that corresponds to the trigger by using HTTP. For example, `{domainName}.cn-shanghai.fc.aliyuncs.com`.
        self.domain_name = domain_name  # type: str
        # The ARN of the RAM role that is used by the event source to invoke the function.
        self.invocation_role = invocation_role  # type: str
        # The last modification time.
        self.last_modified_time = last_modified_time  # type: str
        # The version or alias of the service.
        self.qualifier = qualifier  # type: str
        # The ARN of the event source.
        self.source_arn = source_arn  # type: str
        # The configurations of the trigger. The configurations vary based on the trigger type.
        self.trigger_config = trigger_config  # type: str
        # The unique ID of the trigger.
        self.trigger_id = trigger_id  # type: str
        # The name of the trigger.
        self.trigger_name = trigger_name  # type: str
        # The trigger type, such as **oss**, **log**, **tablestore**, **timer**, **http**, **cdn_events**, and **mns_topic**.
        self.trigger_type = trigger_type  # type: str
        # The public domain address. You can access HTTP triggers over the Internet by using HTTP or HTTPS.
        self.url_internet = url_internet  # type: str
        # The private endpoint. In a VPC, you can access HTTP triggers by using HTTP or HTTPS.
        self.url_intranet = url_intranet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domainName'] = self.domain_name
        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn
        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config
        if self.trigger_id is not None:
            result['triggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name
        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet
        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')
        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')
        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')
        if m.get('triggerId') is not None:
            self.trigger_id = m.get('triggerId')
        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')
        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')
        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')
        return self


class UpdateTriggerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


