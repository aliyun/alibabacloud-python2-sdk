# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, group_id=None, protocol=None, config=None):
        self.owner_id = owner_id  # type: long
        self.group_id = group_id  # type: str
        self.protocol = protocol  # type: str
        self.config = config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class AddDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDeviceResponse, self).to_map()
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
            temp_model = AddDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None, source_url=None,
                 start_time=None, end_time=None, always=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.always = always  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.always is not None:
            result['Always'] = self.always
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Always') is not None:
            self.always = m.get('Always')
        return self


class AddVsPullStreamInfoConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVsPullStreamInfoConfigResponseBody, self).to_map()
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


class AddVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddVsPullStreamInfoConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddVsPullStreamInfoConfigResponse, self).to_map()
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
            temp_model = AddVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindDirectoriesRequest(TeaModel):
    def __init__(self, owner_id=None, directory_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.directory_id = directory_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchBindDirectoriesResponseBodyResults(TeaModel):
    def __init__(self, error=None, directory_id=None, device_id=None):
        self.error = error  # type: str
        self.directory_id = directory_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindDirectoriesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchBindDirectoriesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchBindDirectoriesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindDirectoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchBindDirectoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchBindDirectoriesResponse, self).to_map()
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
            temp_model = BatchBindDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindParentPlatformDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, parent_platform_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindParentPlatformDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchBindParentPlatformDevicesResponseBodyResults(TeaModel):
    def __init__(self, error=None, parent_platform_id=None, device_id=None):
        self.error = error  # type: str
        self.parent_platform_id = parent_platform_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindParentPlatformDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchBindParentPlatformDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchBindParentPlatformDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindParentPlatformDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindParentPlatformDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindParentPlatformDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchBindParentPlatformDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchBindParentPlatformDevicesResponse, self).to_map()
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
            temp_model = BatchBindParentPlatformDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindPurchasedDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, region=None, group_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.group_id = group_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindPurchasedDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchBindPurchasedDevicesResponseBodyResults(TeaModel):
    def __init__(self, error=None, group_id=None, device_id=None, region=None):
        self.error = error  # type: str
        self.group_id = group_id  # type: str
        self.device_id = device_id  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindPurchasedDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class BatchBindPurchasedDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchBindPurchasedDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindPurchasedDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindPurchasedDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindPurchasedDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchBindPurchasedDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchBindPurchasedDevicesResponse, self).to_map()
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
            temp_model = BatchBindPurchasedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, template_id=None, instance_id=None, instance_type=None, apply_all=None,
                 replace=None):
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.apply_all = apply_all  # type: bool
        self.replace = replace  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.replace is not None:
            result['Replace'] = self.replace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        return self


class BatchBindTemplateResponseBodyBindings(TeaModel):
    def __init__(self, error=None, instance_id=None, instance_type=None, template_id=None):
        self.error = error  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindTemplateResponseBodyBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchBindTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, bindings=None):
        self.request_id = request_id  # type: str
        self.bindings = bindings  # type: list[BatchBindTemplateResponseBodyBindings]

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = BatchBindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class BatchBindTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchBindTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchBindTemplateResponse, self).to_map()
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
            temp_model = BatchBindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindTemplatesRequest(TeaModel):
    def __init__(self, owner_id=None, template_id=None, template_type=None, instance_id=None, instance_type=None,
                 apply_all=None, replace=None):
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.apply_all = apply_all  # type: bool
        self.replace = replace  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.replace is not None:
            result['Replace'] = self.replace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        return self


class BatchBindTemplatesResponseBodyResults(TeaModel):
    def __init__(self, error=None, instance_id=None, instance_type=None, template_id=None):
        self.error = error  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindTemplatesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchBindTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchBindTemplatesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchBindTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindTemplatesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchBindTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchBindTemplatesResponse, self).to_map()
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
            temp_model = BatchBindTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchDeleteDevicesResponseBodyResults(TeaModel):
    def __init__(self, error=None, id=None):
        self.error = error  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchDeleteDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchDeleteDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchDeleteDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchDeleteDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchDeleteDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchDeleteDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteDevicesResponse, self).to_map()
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
            temp_model = BatchDeleteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteVsDomainConfigsRequest(TeaModel):
    def __init__(self, owner_id=None, domain_names=None, function_names=None):
        self.owner_id = owner_id  # type: long
        self.domain_names = domain_names  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteVsDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class BatchDeleteVsDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteVsDomainConfigsResponseBody, self).to_map()
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


class BatchDeleteVsDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchDeleteVsDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteVsDomainConfigsResponse, self).to_map()
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
            temp_model = BatchDeleteVsDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchForbidVsStreamRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, channel=None, live_stream_type=None, oneshot=None,
                 control_stream_action=None, resume_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.channel = channel  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.oneshot = oneshot  # type: str
        self.control_stream_action = control_stream_action  # type: str
        self.resume_time = resume_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchForbidVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')
        return self


class BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels(TeaModel):
    def __init__(self, channel=None):
        self.channel = channel  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo(TeaModel):
    def __init__(self, result=None, count=None, detail=None, channels=None):
        self.result = result  # type: str
        self.count = count  # type: int
        self.detail = detail  # type: str
        self.channels = channels  # type: BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super(BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.count is not None:
            result['Count'] = self.count
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Channels') is not None:
            temp_model = BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        return self


class BatchForbidVsStreamResponseBodyForbidResult(TeaModel):
    def __init__(self, forbid_result_info=None):
        self.forbid_result_info = forbid_result_info  # type: list[BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo]

    def validate(self):
        if self.forbid_result_info:
            for k in self.forbid_result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchForbidVsStreamResponseBodyForbidResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForbidResultInfo'] = []
        if self.forbid_result_info is not None:
            for k in self.forbid_result_info:
                result['ForbidResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.forbid_result_info = []
        if m.get('ForbidResultInfo') is not None:
            for k in m.get('ForbidResultInfo'):
                temp_model = BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo()
                self.forbid_result_info.append(temp_model.from_map(k))
        return self


class BatchForbidVsStreamResponseBody(TeaModel):
    def __init__(self, request_id=None, forbid_result=None):
        self.request_id = request_id  # type: str
        self.forbid_result = forbid_result  # type: BatchForbidVsStreamResponseBodyForbidResult

    def validate(self):
        if self.forbid_result:
            self.forbid_result.validate()

    def to_map(self):
        _map = super(BatchForbidVsStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.forbid_result is not None:
            result['ForbidResult'] = self.forbid_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ForbidResult') is not None:
            temp_model = BatchForbidVsStreamResponseBodyForbidResult()
            self.forbid_result = temp_model.from_map(m['ForbidResult'])
        return self


class BatchForbidVsStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchForbidVsStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchForbidVsStreamResponse, self).to_map()
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
            temp_model = BatchForbidVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchResumeVsStreamRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, channel=None, live_stream_type=None,
                 control_stream_action=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.channel = channel  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.control_stream_action = control_stream_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchResumeVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        return self


class BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels(TeaModel):
    def __init__(self, channel=None):
        self.channel = channel  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo(TeaModel):
    def __init__(self, result=None, count=None, detail=None, channels=None):
        self.result = result  # type: str
        self.count = count  # type: int
        self.detail = detail  # type: str
        self.channels = channels  # type: BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super(BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        if self.count is not None:
            result['Count'] = self.count
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Channels') is not None:
            temp_model = BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        return self


class BatchResumeVsStreamResponseBodyResumeResult(TeaModel):
    def __init__(self, resume_result_info=None):
        self.resume_result_info = resume_result_info  # type: list[BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo]

    def validate(self):
        if self.resume_result_info:
            for k in self.resume_result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchResumeVsStreamResponseBodyResumeResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResumeResultInfo'] = []
        if self.resume_result_info is not None:
            for k in self.resume_result_info:
                result['ResumeResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resume_result_info = []
        if m.get('ResumeResultInfo') is not None:
            for k in m.get('ResumeResultInfo'):
                temp_model = BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo()
                self.resume_result_info.append(temp_model.from_map(k))
        return self


class BatchResumeVsStreamResponseBody(TeaModel):
    def __init__(self, request_id=None, resume_result=None):
        self.request_id = request_id  # type: str
        self.resume_result = resume_result  # type: BatchResumeVsStreamResponseBodyResumeResult

    def validate(self):
        if self.resume_result:
            self.resume_result.validate()

    def to_map(self):
        _map = super(BatchResumeVsStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resume_result is not None:
            result['ResumeResult'] = self.resume_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResumeResult') is not None:
            temp_model = BatchResumeVsStreamResponseBodyResumeResult()
            self.resume_result = temp_model.from_map(m['ResumeResult'])
        return self


class BatchResumeVsStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchResumeVsStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchResumeVsStreamResponse, self).to_map()
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
            temp_model = BatchResumeVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetVsDomainConfigsRequest(TeaModel):
    def __init__(self, owner_id=None, domain_names=None, functions=None):
        self.owner_id = owner_id  # type: long
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetVsDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        return self


class BatchSetVsDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetVsDomainConfigsResponseBody, self).to_map()
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


class BatchSetVsDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchSetVsDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetVsDomainConfigsResponse, self).to_map()
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
            temp_model = BatchSetVsDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchStartDevicesResponseBodyResultsStreams(TeaModel):
    def __init__(self, error=None, name=None, id=None):
        self.error = error  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDevicesResponseBodyResultsStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchStartDevicesResponseBodyResults(TeaModel):
    def __init__(self, id=None, streams=None):
        self.id = id  # type: str
        self.streams = streams  # type: list[BatchStartDevicesResponseBodyResultsStreams]

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchStartDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = BatchStartDevicesResponseBodyResultsStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class BatchStartDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchStartDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchStartDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStartDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStartDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStartDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStartDevicesResponse, self).to_map()
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
            temp_model = BatchStartDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartStreamsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchStartStreamsResponseBodyResults(TeaModel):
    def __init__(self, error=None, name=None, id=None):
        self.error = error  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartStreamsResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchStartStreamsResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchStartStreamsResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchStartStreamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStartStreamsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStartStreamsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStartStreamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStartStreamsResponse, self).to_map()
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
            temp_model = BatchStartStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, start_time=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class BatchStopDevicesResponseBodyResultsStreams(TeaModel):
    def __init__(self, error=None, name=None, id=None):
        self.error = error  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDevicesResponseBodyResultsStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchStopDevicesResponseBodyResults(TeaModel):
    def __init__(self, id=None, streams=None):
        self.id = id  # type: str
        self.streams = streams  # type: list[BatchStopDevicesResponseBodyResultsStreams]

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchStopDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = BatchStopDevicesResponseBodyResultsStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class BatchStopDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchStopDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchStopDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStopDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStopDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStopDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopDevicesResponse, self).to_map()
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
            temp_model = BatchStopDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopStreamsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, start_time=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class BatchStopStreamsResponseBodyResults(TeaModel):
    def __init__(self, error=None, name=None, id=None):
        self.error = error  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopStreamsResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchStopStreamsResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchStopStreamsResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchStopStreamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStopStreamsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStopStreamsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStopStreamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopStreamsResponse, self).to_map()
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
            temp_model = BatchStopStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindDirectoriesRequest(TeaModel):
    def __init__(self, owner_id=None, directory_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.directory_id = directory_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchUnbindDirectoriesResponseBodyResults(TeaModel):
    def __init__(self, error=None, directory_id=None, device_id=None):
        self.error = error  # type: str
        self.directory_id = directory_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindDirectoriesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchUnbindDirectoriesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchUnbindDirectoriesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUnbindDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindDirectoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUnbindDirectoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUnbindDirectoriesResponse, self).to_map()
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
            temp_model = BatchUnbindDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindParentPlatformDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, parent_platform_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindParentPlatformDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchUnbindParentPlatformDevicesResponseBodyResults(TeaModel):
    def __init__(self, error=None, parent_platform_id=None, device_id=None):
        self.error = error  # type: str
        self.parent_platform_id = parent_platform_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindParentPlatformDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchUnbindParentPlatformDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchUnbindParentPlatformDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUnbindParentPlatformDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindParentPlatformDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindParentPlatformDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUnbindParentPlatformDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUnbindParentPlatformDevicesResponse, self).to_map()
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
            temp_model = BatchUnbindParentPlatformDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindPurchasedDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindPurchasedDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchUnbindPurchasedDevicesResponseBodyResults(TeaModel):
    def __init__(self, error=None, device_id=None):
        self.error = error  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindPurchasedDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BatchUnbindPurchasedDevicesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchUnbindPurchasedDevicesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUnbindPurchasedDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindPurchasedDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindPurchasedDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUnbindPurchasedDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUnbindPurchasedDevicesResponse, self).to_map()
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
            temp_model = BatchUnbindPurchasedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, template_id=None, template_type=None, instance_id=None, instance_type=None):
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class BatchUnbindTemplateResponseBodyBindings(TeaModel):
    def __init__(self, error=None, instance_id=None, instance_type=None, template_id=None):
        self.error = error  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplateResponseBodyBindings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchUnbindTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, bindings=None):
        self.request_id = request_id  # type: str
        self.bindings = bindings  # type: list[BatchUnbindTemplateResponseBodyBindings]

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUnbindTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = BatchUnbindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class BatchUnbindTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUnbindTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUnbindTemplateResponse, self).to_map()
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
            temp_model = BatchUnbindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindTemplatesRequest(TeaModel):
    def __init__(self, owner_id=None, template_id=None, template_type=None, instance_id=None, instance_type=None):
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class BatchUnbindTemplatesResponseBodyResults(TeaModel):
    def __init__(self, error=None, template_type=None, instance_id=None, instance_type=None, template_id=None):
        self.error = error  # type: str
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplatesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchUnbindTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[BatchUnbindTemplatesResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchUnbindTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindTemplatesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUnbindTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUnbindTemplatesResponse, self).to_map()
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
            temp_model = BatchUnbindTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindDirectoryRequest(TeaModel):
    def __init__(self, owner_id=None, directory_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.directory_id = directory_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BindDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindDirectoryResponseBody, self).to_map()
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


class BindDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindDirectoryResponse, self).to_map()
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
            temp_model = BindDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindParentPlatformDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, parent_platform_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindParentPlatformDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BindParentPlatformDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindParentPlatformDeviceResponseBody, self).to_map()
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


class BindParentPlatformDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindParentPlatformDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindParentPlatformDeviceResponse, self).to_map()
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
            temp_model = BindParentPlatformDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPurchasedDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, region=None, group_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.group_id = group_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindPurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BindPurchasedDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindPurchasedDeviceResponseBody, self).to_map()
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


class BindPurchasedDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindPurchasedDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindPurchasedDeviceResponse, self).to_map()
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
            temp_model = BindPurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, template_id=None, template_type=None, instance_id=None, instance_type=None,
                 apply_all=None, replace=None):
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.apply_all = apply_all  # type: bool
        self.replace = replace  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.replace is not None:
            result['Replace'] = self.replace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        return self


class BindTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, instance_type=None, template_id=None):
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BindTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindTemplateResponse, self).to_map()
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
            temp_model = BindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinuousAdjustRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, iris=None, focus=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.iris = iris  # type: str
        self.focus = focus  # type: str
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinuousAdjustRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.iris is not None:
            result['Iris'] = self.iris
        if self.focus is not None:
            result['Focus'] = self.focus
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Iris') is not None:
            self.iris = m.get('Iris')
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class ContinuousAdjustResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinuousAdjustResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ContinuousAdjustResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ContinuousAdjustResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContinuousAdjustResponse, self).to_map()
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
            temp_model = ContinuousAdjustResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinuousMoveRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, pan=None, tilt=None, zoom=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.pan = pan  # type: str
        self.tilt = tilt  # type: str
        self.zoom = zoom  # type: str
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinuousMoveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.pan is not None:
            result['Pan'] = self.pan
        if self.tilt is not None:
            result['Tilt'] = self.tilt
        if self.zoom is not None:
            result['Zoom'] = self.zoom
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Pan') is not None:
            self.pan = m.get('Pan')
        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')
        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class ContinuousMoveResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinuousMoveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ContinuousMoveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ContinuousMoveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ContinuousMoveResponse, self).to_map()
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
            temp_model = ContinuousMoveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, group_id=None, parent_id=None, directory_id=None,
                 type=None, auto_start=None, gb_id=None, ip=None, port=None, url=None, username=None, password=None,
                 vendor=None, dsn=None, longitude=None, latitude=None, auto_pos=None, pos_interval=None, alarm_method=None,
                 params=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.parent_id = parent_id  # type: str
        self.directory_id = directory_id  # type: str
        self.type = type  # type: str
        self.auto_start = auto_start  # type: bool
        self.gb_id = gb_id  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: long
        self.url = url  # type: str
        self.username = username  # type: str
        self.password = password  # type: str
        self.vendor = vendor  # type: str
        self.dsn = dsn  # type: str
        self.longitude = longitude  # type: str
        self.latitude = latitude  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.pos_interval = pos_interval  # type: long
        self.alarm_method = alarm_method  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeviceResponse, self).to_map()
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
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, channel_id=None, object_type=None, alarm=None, sub_alarm=None,
                 start_time=None, end_time=None, expire=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.channel_id = channel_id  # type: int
        self.object_type = object_type  # type: int
        self.alarm = alarm  # type: int
        self.sub_alarm = sub_alarm  # type: int
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.expire = expire  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.alarm is not None:
            result['Alarm'] = self.alarm
        if self.sub_alarm is not None:
            result['SubAlarm'] = self.sub_alarm
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire is not None:
            result['Expire'] = self.expire
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Alarm') is not None:
            self.alarm = m.get('Alarm')
        if m.get('SubAlarm') is not None:
            self.sub_alarm = m.get('SubAlarm')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        return self


class CreateDeviceAlarmResponseBody(TeaModel):
    def __init__(self, url=None, alarm_id=None, request_id=None, expire=None, alarm_delay=None):
        self.url = url  # type: str
        self.alarm_id = alarm_id  # type: str
        self.request_id = request_id  # type: str
        self.expire = expire  # type: long
        self.alarm_delay = alarm_delay  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.alarm_delay is not None:
            result['AlarmDelay'] = self.alarm_delay
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('AlarmDelay') is not None:
            self.alarm_delay = m.get('AlarmDelay')
        return self


class CreateDeviceAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDeviceAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeviceAlarmResponse, self).to_map()
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
            temp_model = CreateDeviceAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceSnapshotRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None, stream_id=None, mode=None, snapshot_config=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str
        self.stream_id = stream_id  # type: str
        self.mode = mode  # type: str
        self.snapshot_config = snapshot_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SnapshotConfig') is not None:
            self.snapshot_config = m.get('SnapshotConfig')
        return self


class CreateDeviceSnapshotResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeviceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDeviceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDeviceSnapshotResponse, self).to_map()
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
            temp_model = CreateDeviceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDirectoryRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, group_id=None, parent_id=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class CreateDirectoryResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDirectoryResponse, self).to_map()
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
            temp_model = CreateDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, app=None, region=None, in_protocol=None,
                 out_protocol=None, push_domain=None, play_domain=None, lazy_pull=None, callback=None, capture_interval=None,
                 capture_image=None, capture_video=None, capture_oss_bucket=None, capture_oss_path=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.app = app  # type: str
        self.region = region  # type: str
        self.in_protocol = in_protocol  # type: str
        self.out_protocol = out_protocol  # type: str
        self.push_domain = push_domain  # type: str
        self.play_domain = play_domain  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.callback = callback  # type: str
        self.capture_interval = capture_interval  # type: int
        self.capture_image = capture_image  # type: int
        self.capture_video = capture_video  # type: int
        self.capture_oss_bucket = capture_oss_bucket  # type: str
        self.capture_oss_path = capture_oss_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.app is not None:
            result['App'] = self.app
        if self.region is not None:
            result['Region'] = self.region
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.capture_image is not None:
            result['CaptureImage'] = self.capture_image
        if self.capture_video is not None:
            result['CaptureVideo'] = self.capture_video
        if self.capture_oss_bucket is not None:
            result['CaptureOssBucket'] = self.capture_oss_bucket
        if self.capture_oss_path is not None:
            result['CaptureOssPath'] = self.capture_oss_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('CaptureImage') is not None:
            self.capture_image = m.get('CaptureImage')
        if m.get('CaptureVideo') is not None:
            self.capture_video = m.get('CaptureVideo')
        if m.get('CaptureOssBucket') is not None:
            self.capture_oss_bucket = m.get('CaptureOssBucket')
        if m.get('CaptureOssPath') is not None:
            self.capture_oss_path = m.get('CaptureOssPath')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, gb_id=None, gb_ip=None, request_id=None, gb_port=None, id=None):
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.request_id = request_id  # type: str
        self.gb_port = gb_port  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupResponse, self).to_map()
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParentPlatformRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, protocol=None, gb_id=None, ip=None, port=None,
                 client_auth=None, client_username=None, client_password=None, auto_start=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.protocol = protocol  # type: str
        self.gb_id = gb_id  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: long
        self.client_auth = client_auth  # type: bool
        self.client_username = client_username  # type: str
        self.client_password = client_password  # type: str
        self.auto_start = auto_start  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        return self


class CreateParentPlatformResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParentPlatformResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParentPlatformResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateParentPlatformResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateParentPlatformResponse, self).to_map()
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
            temp_model = CreateParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamSnapshotRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, location=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class CreateStreamSnapshotResponseBody(TeaModel):
    def __init__(self, oss_object=None, request_id=None, width=None, height=None, url=None, timestamp=None,
                 oss_bucket=None, format=None, oss_endpoint=None, id=None):
        self.oss_object = oss_object  # type: str
        self.request_id = request_id  # type: str
        self.width = width  # type: long
        self.height = height  # type: long
        self.url = url  # type: str
        self.timestamp = timestamp  # type: long
        self.oss_bucket = oss_bucket  # type: str
        self.format = format  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.format is not None:
            result['Format'] = self.format
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateStreamSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateStreamSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStreamSnapshotResponse, self).to_map()
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
            temp_model = CreateStreamSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, name=None, description=None, type=None, region=None, oss_bucket=None,
                 oss_endpoint=None, oss_file_prefix=None, trigger=None, start_time=None, end_time=None, interval=None,
                 retention=None, file_format=None, jpg_overwrite=None, jpg_sequence=None, jpg_on_demand=None, mp_4=None,
                 flv=None, hls_m3u_8=None, hls_ts=None, callback=None, trans_configs_json=None):
        self.owner_id = owner_id  # type: long
        self.name = name  # type: str
        self.description = description  # type: str
        self.type = type  # type: str
        self.region = region  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.trigger = trigger  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: long
        self.retention = retention  # type: long
        self.file_format = file_format  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.mp_4 = mp_4  # type: str
        self.flv = flv  # type: str
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.hls_ts = hls_ts  # type: str
        self.callback = callback  # type: str
        self.trans_configs_json = trans_configs_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTemplateResponse, self).to_map()
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBucketRequest(TeaModel):
    def __init__(self, owner_id=None, bucket_name=None):
        self.owner_id = owner_id  # type: long
        self.bucket_name = bucket_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class DeleteBucketResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBucketResponseBody, self).to_map()
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


class DeleteBucketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBucketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBucketResponse, self).to_map()
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
            temp_model = DeleteBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeviceResponseBody, self).to_map()
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


class DeleteDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDeviceResponse, self).to_map()
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
            temp_model = DeleteDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoryRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDirectoryResponseBody, self).to_map()
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


class DeleteDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDirectoryResponse, self).to_map()
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
            temp_model = DeleteDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupResponseBody, self).to_map()
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


class DeleteGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupResponse, self).to_map()
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParentPlatformRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteParentPlatformResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParentPlatformResponseBody, self).to_map()
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


class DeleteParentPlatformResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteParentPlatformResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteParentPlatformResponse, self).to_map()
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
            temp_model = DeleteParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePresetRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, preset_id=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.preset_id = preset_id  # type: str
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePresetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class DeletePresetResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePresetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePresetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePresetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePresetResponse, self).to_map()
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
            temp_model = DeletePresetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateResponseBody, self).to_map()
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


class DeleteTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTemplateResponse, self).to_map()
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DeleteVsPullStreamInfoConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVsPullStreamInfoConfigResponseBody, self).to_map()
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


class DeleteVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVsPullStreamInfoConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVsPullStreamInfoConfigResponse, self).to_map()
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
            temp_model = DeleteVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVsStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVsStreamsNotifyUrlConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteVsStreamsNotifyUrlConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVsStreamsNotifyUrlConfigResponseBody, self).to_map()
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


class DeleteVsStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVsStreamsNotifyUrlConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVsStreamsNotifyUrlConfigResponse, self).to_map()
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
            temp_model = DeleteVsStreamsNotifyUrlConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountStatRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAccountStatResponseBody(TeaModel):
    def __init__(self, template_num=None, group_limit=None, request_id=None, template_limit=None, group_num=None,
                 id=None):
        self.template_num = template_num  # type: long
        self.group_limit = group_limit  # type: long
        self.request_id = request_id  # type: str
        self.template_limit = template_limit  # type: long
        self.group_num = group_num  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_num is not None:
            result['TemplateNum'] = self.template_num
        if self.group_limit is not None:
            result['GroupLimit'] = self.group_limit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_limit is not None:
            result['TemplateLimit'] = self.template_limit
        if self.group_num is not None:
            result['GroupNum'] = self.group_num
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateNum') is not None:
            self.template_num = m.get('TemplateNum')
        if m.get('GroupLimit') is not None:
            self.group_limit = m.get('GroupLimit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateLimit') is not None:
            self.template_limit = m.get('TemplateLimit')
        if m.get('GroupNum') is not None:
            self.group_num = m.get('GroupNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeAccountStatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAccountStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccountStatResponse, self).to_map()
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
            temp_model = DescribeAccountStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, include_stats=None, include_directory=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.include_stats = include_stats  # type: bool
        self.include_directory = include_directory  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')
        return self


class DescribeDeviceResponseBodyStats(TeaModel):
    def __init__(self, failed_num=None, stream_num=None, channel_num=None, online_num=None, offline_num=None):
        self.failed_num = failed_num  # type: long
        self.stream_num = stream_num  # type: long
        self.channel_num = channel_num  # type: long
        self.online_num = online_num  # type: long
        self.offline_num = offline_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceResponseBodyStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')
        return self


class DescribeDeviceResponseBodyDirectory(TeaModel):
    def __init__(self, parent_id=None, description=None, group_id=None, name=None, created_time=None, id=None):
        self.parent_id = parent_id  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceResponseBodyDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDeviceResponseBody(TeaModel):
    def __init__(self, type=None, status=None, alarm_method=None, dsn=None, port=None, pos_interval=None,
                 parent_id=None, password=None, auto_pos=None, params=None, request_id=None, description=None, enabled=None,
                 name=None, channel_sync_time=None, created_time=None, directory_id=None, registered_time=None,
                 protocol=None, ip=None, url=None, auto_start=None, vendor=None, gb_id=None, group_id=None, longitude=None,
                 latitude=None, id=None, username=None, stats=None, directory=None):
        self.type = type  # type: str
        self.status = status  # type: str
        self.alarm_method = alarm_method  # type: str
        self.dsn = dsn  # type: str
        self.port = port  # type: long
        self.pos_interval = pos_interval  # type: long
        self.parent_id = parent_id  # type: str
        self.password = password  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.params = params  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.enabled = enabled  # type: bool
        self.name = name  # type: str
        self.channel_sync_time = channel_sync_time  # type: str
        self.created_time = created_time  # type: str
        self.directory_id = directory_id  # type: str
        self.registered_time = registered_time  # type: str
        self.protocol = protocol  # type: str
        self.ip = ip  # type: str
        self.url = url  # type: str
        self.auto_start = auto_start  # type: bool
        self.vendor = vendor  # type: str
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.longitude = longitude  # type: str
        self.latitude = latitude  # type: str
        self.id = id  # type: str
        self.username = username  # type: str
        self.stats = stats  # type: DescribeDeviceResponseBodyStats
        self.directory = directory  # type: DescribeDeviceResponseBodyDirectory

    def validate(self):
        if self.stats:
            self.stats.validate()
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(DescribeDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.params is not None:
            result['Params'] = self.params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.url is not None:
            result['Url'] = self.url
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Stats') is not None:
            temp_model = DescribeDeviceResponseBodyStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Directory') is not None:
            temp_model = DescribeDeviceResponseBodyDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        return self


class DescribeDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeviceResponse, self).to_map()
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
            temp_model = DescribeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceChannelsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribeDeviceChannelsResponseBodyChannels(TeaModel):
    def __init__(self, stream_status=None, gb_id=None, params=None, device_id=None, channel_id=None,
                 device_status=None, name=None, stream_id=None):
        self.stream_status = stream_status  # type: str
        self.gb_id = gb_id  # type: str
        self.params = params  # type: str
        self.device_id = device_id  # type: str
        self.channel_id = channel_id  # type: long
        self.device_status = device_status  # type: str
        self.name = name  # type: str
        self.stream_id = stream_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceChannelsResponseBodyChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.params is not None:
            result['Params'] = self.params
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.name is not None:
            result['Name'] = self.name
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class DescribeDeviceChannelsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 channels=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.channels = channels  # type: list[DescribeDeviceChannelsResponseBodyChannels]

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeviceChannelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = DescribeDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        return self


class DescribeDeviceChannelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDeviceChannelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeviceChannelsResponse, self).to_map()
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
            temp_model = DescribeDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceGatewayRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, client_ip=None, expire=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.client_ip = client_ip  # type: str
        self.expire = expire  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.expire is not None:
            result['Expire'] = self.expire
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        return self


class DescribeDeviceGatewayResponseBody(TeaModel):
    def __init__(self, host=None, token=None, request_id=None, port=None, protocol=None):
        self.host = host  # type: str
        self.token = token  # type: str
        self.request_id = request_id  # type: str
        self.port = port  # type: long
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.token is not None:
            result['Token'] = self.token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeDeviceGatewayResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDeviceGatewayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeviceGatewayResponse, self).to_map()
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
            temp_model = DescribeDeviceGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, type=None, group_id=None, parent_id=None, directory_id=None,
                 gb_id=None, status=None, vendor=None, sort_by=None, sort_direction=None, page_size=None, page_num=None,
                 include_stats=None, include_directory=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.group_id = group_id  # type: str
        self.parent_id = parent_id  # type: str
        self.directory_id = directory_id  # type: str
        self.gb_id = gb_id  # type: str
        self.status = status  # type: str
        self.vendor = vendor  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long
        self.include_stats = include_stats  # type: bool
        self.include_directory = include_directory  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')
        return self


class DescribeDevicesResponseBodyDevicesStats(TeaModel):
    def __init__(self, failed_num=None, stream_num=None, channel_num=None, online_num=None, offline_num=None):
        self.failed_num = failed_num  # type: long
        self.stream_num = stream_num  # type: long
        self.channel_num = channel_num  # type: long
        self.online_num = online_num  # type: long
        self.offline_num = offline_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyDevicesStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')
        return self


class DescribeDevicesResponseBodyDevicesDirectory(TeaModel):
    def __init__(self, parent_id=None, description=None, group_id=None, name=None, created_time=None, id=None):
        self.parent_id = parent_id  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyDevicesDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDevicesResponseBodyDevices(TeaModel):
    def __init__(self, type=None, status=None, alarm_method=None, dsn=None, port=None, pos_interval=None,
                 parent_id=None, password=None, auto_pos=None, params=None, description=None, enabled=None, name=None,
                 channel_sync_time=None, created_time=None, directory_id=None, registered_time=None, protocol=None, ip=None, url=None,
                 auto_start=None, vendor=None, gb_id=None, group_id=None, longitude=None, latitude=None, id=None, username=None,
                 stats=None, directory=None):
        self.type = type  # type: str
        self.status = status  # type: str
        self.alarm_method = alarm_method  # type: str
        self.dsn = dsn  # type: str
        self.port = port  # type: long
        self.pos_interval = pos_interval  # type: long
        self.parent_id = parent_id  # type: str
        self.password = password  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.params = params  # type: str
        self.description = description  # type: str
        self.enabled = enabled  # type: bool
        self.name = name  # type: str
        self.channel_sync_time = channel_sync_time  # type: str
        self.created_time = created_time  # type: str
        self.directory_id = directory_id  # type: str
        self.registered_time = registered_time  # type: str
        self.protocol = protocol  # type: str
        self.ip = ip  # type: str
        self.url = url  # type: str
        self.auto_start = auto_start  # type: bool
        self.vendor = vendor  # type: str
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.longitude = longitude  # type: str
        self.latitude = latitude  # type: str
        self.id = id  # type: str
        self.username = username  # type: str
        self.stats = stats  # type: DescribeDevicesResponseBodyDevicesStats
        self.directory = directory  # type: DescribeDevicesResponseBodyDevicesDirectory

    def validate(self):
        if self.stats:
            self.stats.validate()
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.params is not None:
            result['Params'] = self.params
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.url is not None:
            result['Url'] = self.url
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.id is not None:
            result['Id'] = self.id
        if self.username is not None:
            result['Username'] = self.username
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Stats') is not None:
            temp_model = DescribeDevicesResponseBodyDevicesStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Directory') is not None:
            temp_model = DescribeDevicesResponseBodyDevicesDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        return self


class DescribeDevicesResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 devices=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.devices = devices  # type: list[DescribeDevicesResponseBodyDevices]

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class DescribeDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDevicesResponse, self).to_map()
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
            temp_model = DescribeDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceURLRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, stream=None, out_protocol=None, mode=None, type=None, auth=None,
                 expire=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.stream = stream  # type: str
        self.out_protocol = out_protocol  # type: str
        self.mode = mode  # type: str
        self.type = type  # type: str
        self.auth = auth  # type: bool
        self.expire = expire  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.type is not None:
            result['Type'] = self.type
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.expire is not None:
            result['Expire'] = self.expire
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        return self


class DescribeDeviceURLResponseBody(TeaModel):
    def __init__(self, url=None, request_id=None, expire_time=None):
        self.url = url  # type: str
        self.request_id = request_id  # type: str
        self.expire_time = expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class DescribeDeviceURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDeviceURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeviceURLResponse, self).to_map()
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
            temp_model = DescribeDeviceURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, owner_id=None, group_id=None, parent_id=None, sort_by=None, sort_direction=None,
                 page_size=None, page_num=None, no_pagination=None):
        self.owner_id = owner_id  # type: long
        self.group_id = group_id  # type: str
        self.parent_id = parent_id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long
        self.no_pagination = no_pagination  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.no_pagination is not None:
            result['NoPagination'] = self.no_pagination
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('NoPagination') is not None:
            self.no_pagination = m.get('NoPagination')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(self, parent_id=None, description=None, group_id=None, name=None, created_time=None, id=None):
        self.parent_id = parent_id  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBodyDirectories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 directories=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.directories = directories  # type: list[DescribeDirectoriesResponseBodyDirectories]

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDirectoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponse, self).to_map()
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
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoryRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDirectoryResponseBody(TeaModel):
    def __init__(self, parent_id=None, request_id=None, description=None, group_id=None, name=None,
                 created_time=None, id=None):
        self.parent_id = parent_id  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDirectoryResponse, self).to_map()
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
            temp_model = DescribeDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, include_stats=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.include_stats = include_stats  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        return self


class DescribeGroupResponseBodyStats(TeaModel):
    def __init__(self, platform_num=None, device_num=None, ipc_num=None, ied_num=None):
        self.platform_num = platform_num  # type: long
        self.device_num = device_num  # type: long
        self.ipc_num = ipc_num  # type: long
        self.ied_num = ied_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupResponseBodyStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num
        if self.ied_num is not None:
            result['IedNum'] = self.ied_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')
        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')
        return self


class DescribeGroupResponseBody(TeaModel):
    def __init__(self, status=None, lazy_pull=None, callback=None, request_id=None, description=None, app=None,
                 region=None, enabled=None, in_protocol=None, out_protocol=None, name=None, push_domain=None,
                 created_time=None, capture_video=None, play_domain=None, capture_interval=None, gb_port=None, gb_id=None,
                 gb_ip=None, capture_image=None, alias_id=None, capture_oss_bucket=None, capture_oss_path=None, id=None,
                 gb_tcp_ports=None, gb_udp_ports=None, stats=None):
        self.status = status  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.callback = callback  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.app = app  # type: str
        self.region = region  # type: str
        self.enabled = enabled  # type: bool
        self.in_protocol = in_protocol  # type: str
        self.out_protocol = out_protocol  # type: str
        self.name = name  # type: str
        self.push_domain = push_domain  # type: str
        self.created_time = created_time  # type: str
        self.capture_video = capture_video  # type: int
        self.play_domain = play_domain  # type: str
        self.capture_interval = capture_interval  # type: int
        self.gb_port = gb_port  # type: long
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.capture_image = capture_image  # type: int
        self.alias_id = alias_id  # type: str
        self.capture_oss_bucket = capture_oss_bucket  # type: str
        self.capture_oss_path = capture_oss_path  # type: str
        self.id = id  # type: str
        self.gb_tcp_ports = gb_tcp_ports  # type: list[str]
        self.gb_udp_ports = gb_udp_ports  # type: list[str]
        self.stats = stats  # type: DescribeGroupResponseBodyStats

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super(DescribeGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.app is not None:
            result['App'] = self.app
        if self.region is not None:
            result['Region'] = self.region
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.name is not None:
            result['Name'] = self.name
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.capture_video is not None:
            result['CaptureVideo'] = self.capture_video
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.capture_image is not None:
            result['CaptureImage'] = self.capture_image
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id
        if self.capture_oss_bucket is not None:
            result['CaptureOssBucket'] = self.capture_oss_bucket
        if self.capture_oss_path is not None:
            result['CaptureOssPath'] = self.capture_oss_path
        if self.id is not None:
            result['Id'] = self.id
        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports
        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CaptureVideo') is not None:
            self.capture_video = m.get('CaptureVideo')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('CaptureImage') is not None:
            self.capture_image = m.get('CaptureImage')
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')
        if m.get('CaptureOssBucket') is not None:
            self.capture_oss_bucket = m.get('CaptureOssBucket')
        if m.get('CaptureOssPath') is not None:
            self.capture_oss_path = m.get('CaptureOssPath')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')
        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')
        if m.get('Stats') is not None:
            temp_model = DescribeGroupResponseBodyStats()
            self.stats = temp_model.from_map(m['Stats'])
        return self


class DescribeGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGroupResponse, self).to_map()
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
            temp_model = DescribeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, region=None, in_protocol=None, status=None, sort_by=None,
                 sort_direction=None, page_size=None, page_num=None, include_stats=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.region = region  # type: str
        self.in_protocol = in_protocol  # type: str
        self.status = status  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long
        self.include_stats = include_stats  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        return self


class DescribeGroupsResponseBodyGroupsStats(TeaModel):
    def __init__(self, platform_num=None, device_num=None, ipc_num=None, ied_num=None):
        self.platform_num = platform_num  # type: long
        self.device_num = device_num  # type: long
        self.ipc_num = ipc_num  # type: long
        self.ied_num = ied_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupsResponseBodyGroupsStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num
        if self.ied_num is not None:
            result['IedNum'] = self.ied_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')
        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')
        return self


class DescribeGroupsResponseBodyGroups(TeaModel):
    def __init__(self, status=None, lazy_pull=None, play_domain=None, gb_port=None, capture_interval=None,
                 callback=None, gb_id=None, gb_ip=None, capture_image=None, description=None, region=None, app=None,
                 alias_id=None, enabled=None, in_protocol=None, capture_oss_path=None, capture_oss_bucket=None,
                 out_protocol=None, push_domain=None, name=None, created_time=None, capture_video=None, id=None,
                 gb_tcp_ports=None, gb_udp_ports=None, stats=None):
        self.status = status  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.play_domain = play_domain  # type: str
        self.gb_port = gb_port  # type: long
        self.capture_interval = capture_interval  # type: int
        self.callback = callback  # type: str
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.capture_image = capture_image  # type: int
        self.description = description  # type: str
        self.region = region  # type: str
        self.app = app  # type: str
        self.alias_id = alias_id  # type: str
        self.enabled = enabled  # type: bool
        self.in_protocol = in_protocol  # type: str
        self.capture_oss_path = capture_oss_path  # type: str
        self.capture_oss_bucket = capture_oss_bucket  # type: str
        self.out_protocol = out_protocol  # type: str
        self.push_domain = push_domain  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.capture_video = capture_video  # type: int
        self.id = id  # type: str
        self.gb_tcp_ports = gb_tcp_ports  # type: list[str]
        self.gb_udp_ports = gb_udp_ports  # type: list[str]
        self.stats = stats  # type: DescribeGroupsResponseBodyGroupsStats

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super(DescribeGroupsResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.capture_image is not None:
            result['CaptureImage'] = self.capture_image
        if self.description is not None:
            result['Description'] = self.description
        if self.region is not None:
            result['Region'] = self.region
        if self.app is not None:
            result['App'] = self.app
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.capture_oss_path is not None:
            result['CaptureOssPath'] = self.capture_oss_path
        if self.capture_oss_bucket is not None:
            result['CaptureOssBucket'] = self.capture_oss_bucket
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.capture_video is not None:
            result['CaptureVideo'] = self.capture_video
        if self.id is not None:
            result['Id'] = self.id
        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports
        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('CaptureImage') is not None:
            self.capture_image = m.get('CaptureImage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('CaptureOssPath') is not None:
            self.capture_oss_path = m.get('CaptureOssPath')
        if m.get('CaptureOssBucket') is not None:
            self.capture_oss_bucket = m.get('CaptureOssBucket')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CaptureVideo') is not None:
            self.capture_video = m.get('CaptureVideo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')
        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')
        if m.get('Stats') is not None:
            temp_model = DescribeGroupsResponseBodyGroupsStats()
            self.stats = temp_model.from_map(m['Stats'])
        return self


class DescribeGroupsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 groups=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.groups = groups  # type: list[DescribeGroupsResponseBodyGroups]

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        return self


class DescribeGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGroupsResponse, self).to_map()
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
            temp_model = DescribeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeParentPlatformResponseBody(TeaModel):
    def __init__(self, status=None, client_port=None, client_gb_id=None, protocol=None, ip=None, port=None,
                 client_password=None, client_username=None, auto_start=None, client_auth=None, gb_id=None, request_id=None,
                 description=None, client_ip=None, name=None, created_time=None, id=None):
        self.status = status  # type: str
        self.client_port = client_port  # type: long
        self.client_gb_id = client_gb_id  # type: str
        self.protocol = protocol  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: long
        self.client_password = client_password  # type: str
        self.client_username = client_username  # type: str
        self.auto_start = auto_start  # type: bool
        self.client_auth = client_auth  # type: bool
        self.gb_id = gb_id  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.client_ip = client_ip  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeParentPlatformResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParentPlatformResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParentPlatformResponse, self).to_map()
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
            temp_model = DescribeParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, sort_by=None, sort_direction=None, page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribeParentPlatformDevicesResponseBodyDevices(TeaModel):
    def __init__(self, parent_id=None, gb_id=None, group_id=None, name=None, id=None):
        self.parent_id = parent_id  # type: str
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeParentPlatformDevicesResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 devices=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.devices = devices  # type: list[DescribeParentPlatformDevicesResponseBodyDevices]

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParentPlatformDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeParentPlatformDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class DescribeParentPlatformDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParentPlatformDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParentPlatformDevicesResponse, self).to_map()
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
            temp_model = DescribeParentPlatformDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformsRequest(TeaModel):
    def __init__(self, owner_id=None, gb_id=None, status=None, sort_by=None, sort_direction=None, page_size=None,
                 page_num=None):
        self.owner_id = owner_id  # type: long
        self.gb_id = gb_id  # type: str
        self.status = status  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribeParentPlatformsResponseBodyPlatforms(TeaModel):
    def __init__(self, status=None, client_port=None, protocol=None, client_gb_id=None, ip=None, port=None,
                 client_username=None, client_password=None, auto_start=None, client_auth=None, gb_id=None, description=None,
                 client_ip=None, name=None, created_time=None, id=None):
        self.status = status  # type: str
        self.client_port = client_port  # type: long
        self.protocol = protocol  # type: str
        self.client_gb_id = client_gb_id  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: long
        self.client_username = client_username  # type: str
        self.client_password = client_password  # type: str
        self.auto_start = auto_start  # type: bool
        self.client_auth = client_auth  # type: bool
        self.gb_id = gb_id  # type: str
        self.description = description  # type: str
        self.client_ip = client_ip  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformsResponseBodyPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.description is not None:
            result['Description'] = self.description
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeParentPlatformsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 platforms=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.platforms = platforms  # type: list[DescribeParentPlatformsResponseBodyPlatforms]

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParentPlatformsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['Platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.platforms = []
        if m.get('Platforms') is not None:
            for k in m.get('Platforms'):
                temp_model = DescribeParentPlatformsResponseBodyPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class DescribeParentPlatformsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeParentPlatformsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParentPlatformsResponse, self).to_map()
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
            temp_model = DescribeParentPlatformsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePresetsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePresetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class DescribePresetsResponseBodyPresets(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePresetsResponseBodyPresets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribePresetsResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None, presets=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str
        self.presets = presets  # type: list[DescribePresetsResponseBodyPresets]

    def validate(self):
        if self.presets:
            for k in self.presets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePresetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Presets'] = []
        if self.presets is not None:
            for k in self.presets:
                result['Presets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.presets = []
        if m.get('Presets') is not None:
            for k in m.get('Presets'):
                temp_model = DescribePresetsResponseBodyPresets()
                self.presets.append(temp_model.from_map(k))
        return self


class DescribePresetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePresetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePresetsResponse, self).to_map()
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
            temp_model = DescribePresetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribePurchasedDeviceResponseBody(TeaModel):
    def __init__(self, type=None, sub_type=None, vendor=None, request_id=None, description=None, register_code=None,
                 group_id=None, group_name=None, region=None, name=None, created_time=None, id=None, order_id=None):
        self.type = type  # type: str
        self.sub_type = sub_type  # type: str
        self.vendor = vendor  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.register_code = register_code  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.region = region  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region is not None:
            result['Region'] = self.region
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DescribePurchasedDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePurchasedDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePurchasedDeviceResponse, self).to_map()
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
            temp_model = DescribePurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedDevicesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, type=None, sub_type=None, group_id=None, vendor=None,
                 sort_by=None, sort_direction=None, page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.sub_type = sub_type  # type: str
        self.group_id = group_id  # type: str
        self.vendor = vendor  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribePurchasedDevicesResponseBodyDevices(TeaModel):
    def __init__(self, type=None, sub_type=None, vendor=None, description=None, register_code=None, group_id=None,
                 group_name=None, region=None, name=None, created_time=None, id=None, order_id=None):
        self.type = type  # type: str
        self.sub_type = sub_type  # type: str
        self.vendor = vendor  # type: str
        self.description = description  # type: str
        self.register_code = register_code  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.region = region  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.description is not None:
            result['Description'] = self.description
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region is not None:
            result['Region'] = self.region
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DescribePurchasedDevicesResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 devices=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.devices = devices  # type: list[DescribePurchasedDevicesResponseBodyDevices]

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePurchasedDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribePurchasedDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        return self


class DescribePurchasedDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePurchasedDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePurchasedDevicesResponse, self).to_map()
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
            temp_model = DescribePurchasedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordsRequest(TeaModel):
    def __init__(self, owner_id=None, type=None, stream_id=None, start_time=None, end_time=None, private_bucket=None,
                 sort_by=None, sort_direction=None, page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.type = type  # type: str
        self.stream_id = stream_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.private_bucket = private_bucket  # type: bool
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.private_bucket is not None:
            result['PrivateBucket'] = self.private_bucket
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PrivateBucket') is not None:
            self.private_bucket = m.get('PrivateBucket')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribeRecordsResponseBodyRecords(TeaModel):
    def __init__(self, type=None, height=None, url=None, oss_bucket=None, file_format=None, stream_id=None,
                 oss_object=None, end_time=None, start_time=None, width=None, template_id=None, id=None, oss_endpoint=None):
        self.type = type  # type: str
        self.height = height  # type: long
        self.url = url  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.file_format = file_format  # type: str
        self.stream_id = stream_id  # type: str
        self.oss_object = oss_object  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.width = width  # type: long
        self.template_id = template_id  # type: str
        self.id = id  # type: str
        self.oss_endpoint = oss_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordsResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.height is not None:
            result['Height'] = self.height
        if self.url is not None:
            result['Url'] = self.url
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.width is not None:
            result['Width'] = self.width
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        return self


class DescribeRecordsResponseBody(TeaModel):
    def __init__(self, page_num=None, request_id=None, next_start_time=None, page_size=None, total_count=None,
                 page_count=None, records=None):
        self.page_num = page_num  # type: long
        self.request_id = request_id  # type: str
        self.next_start_time = next_start_time  # type: str
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.records = records  # type: list[DescribeRecordsResponseBodyRecords]

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecordsResponse, self).to_map()
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
            temp_model = DescribeRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeStreamResponseBody(TeaModel):
    def __init__(self, status=None, play_domain=None, protocol=None, device_id=None, height=None, request_id=None,
                 group_id=None, width=None, app=None, enabled=None, name=None, push_domain=None, created_time=None, id=None):
        self.status = status  # type: str
        self.play_domain = play_domain  # type: str
        self.protocol = protocol  # type: str
        self.device_id = device_id  # type: str
        self.height = height  # type: int
        self.request_id = request_id  # type: str
        self.group_id = group_id  # type: str
        self.width = width  # type: int
        self.app = app  # type: str
        self.enabled = enabled  # type: bool
        self.name = name  # type: str
        self.push_domain = push_domain  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.height is not None:
            result['Height'] = self.height
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.width is not None:
            result['Width'] = self.width
        if self.app is not None:
            result['App'] = self.app
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStreamResponse, self).to_map()
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
            temp_model = DescribeStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, group_id=None, device_id=None, parent_id=None, name=None, domain=None,
                 app=None, sort_by=None, sort_direction=None, page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.group_id = group_id  # type: str
        self.device_id = device_id  # type: str
        self.parent_id = parent_id  # type: str
        self.name = name  # type: str
        self.domain = domain  # type: str
        self.app = app  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.name is not None:
            result['Name'] = self.name
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.app is not None:
            result['App'] = self.app
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribeStreamsResponseBodyStreams(TeaModel):
    def __init__(self, status=None, play_domain=None, protocol=None, device_id=None, height=None, group_id=None,
                 app=None, width=None, enabled=None, name=None, push_domain=None, created_time=None, id=None):
        self.status = status  # type: str
        self.play_domain = play_domain  # type: str
        self.protocol = protocol  # type: str
        self.device_id = device_id  # type: str
        self.height = height  # type: int
        self.group_id = group_id  # type: str
        self.app = app  # type: str
        self.width = width  # type: int
        self.enabled = enabled  # type: bool
        self.name = name  # type: str
        self.push_domain = push_domain  # type: str
        self.created_time = created_time  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamsResponseBodyStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.height is not None:
            result['Height'] = self.height
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.app is not None:
            result['App'] = self.app
        if self.width is not None:
            result['Width'] = self.width
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeStreamsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 streams=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.streams = streams  # type: list[DescribeStreamsResponseBodyStreams]

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeStreamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = DescribeStreamsResponseBodyStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class DescribeStreamsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeStreamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStreamsResponse, self).to_map()
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
            temp_model = DescribeStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamURLRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, type=None, out_protocol=None, out_host_type=None, location=None,
                 auth=None, auth_key=None, expire=None, start_time=None, end_time=None, transcode=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.type = type  # type: str
        self.out_protocol = out_protocol  # type: str
        self.out_host_type = out_host_type  # type: str
        self.location = location  # type: str
        self.auth = auth  # type: bool
        self.auth_key = auth_key  # type: str
        self.expire = expire  # type: long
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.transcode = transcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.out_host_type is not None:
            result['OutHostType'] = self.out_host_type
        if self.location is not None:
            result['Location'] = self.location
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OutHostType') is not None:
            self.out_host_type = m.get('OutHostType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        return self


class DescribeStreamURLResponseBody(TeaModel):
    def __init__(self, url=None, request_id=None, expire_time=None):
        self.url = url  # type: str
        self.request_id = request_id  # type: str
        self.expire_time = expire_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class DescribeStreamURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeStreamURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStreamURLResponse, self).to_map()
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
            temp_model = DescribeStreamURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamVodListRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamVodListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeStreamVodListResponseBodyRecords(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamVodListResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeStreamVodListResponseBody(TeaModel):
    def __init__(self, request_id=None, records=None):
        self.request_id = request_id  # type: str
        self.records = records  # type: list[DescribeStreamVodListResponseBodyRecords]

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeStreamVodListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeStreamVodListResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeStreamVodListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeStreamVodListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStreamVodListResponse, self).to_map()
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
            temp_model = DescribeStreamVodListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTemplateResponseBodyTransConfigs(TeaModel):
    def __init__(self, gop=None, width=None, video_bitrate=None, height=None, video_codec=None, fps=None, name=None,
                 id=None):
        self.gop = gop  # type: long
        self.width = width  # type: long
        self.video_bitrate = video_bitrate  # type: long
        self.height = height  # type: long
        self.video_codec = video_codec  # type: str
        self.fps = fps  # type: long
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateResponseBodyTransConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gop is not None:
            result['Gop'] = self.gop
        if self.width is not None:
            result['Width'] = self.width
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.height is not None:
            result['Height'] = self.height
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gop') is not None:
            self.gop = m.get('Gop')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTemplateResponseBody(TeaModel):
    def __init__(self, type=None, trigger=None, hls_ts=None, mp_4=None, jpg_overwrite=None, callback=None,
                 request_id=None, description=None, region=None, retention=None, hls_m3u_8=None, name=None, flv=None,
                 created_time=None, oss_endpoint=None, oss_file_prefix=None, jpg_on_demand=None, oss_bucket=None,
                 file_format=None, jpg_sequence=None, end_time=None, start_time=None, interval=None, id=None, trans_configs=None):
        self.type = type  # type: str
        self.trigger = trigger  # type: str
        self.hls_ts = hls_ts  # type: str
        self.mp_4 = mp_4  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.callback = callback  # type: str
        self.request_id = request_id  # type: str
        self.description = description  # type: str
        self.region = region  # type: str
        self.retention = retention  # type: long
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.name = name  # type: str
        self.flv = flv  # type: str
        self.created_time = created_time  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.file_format = file_format  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.interval = interval  # type: long
        self.id = id  # type: str
        self.trans_configs = trans_configs  # type: list[DescribeTemplateResponseBodyTransConfigs]

    def validate(self):
        if self.trans_configs:
            for k in self.trans_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.name is not None:
            result['Name'] = self.name
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.id is not None:
            result['Id'] = self.id
        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k in self.trans_configs:
                result['TransConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k in m.get('TransConfigs'):
                temp_model = DescribeTemplateResponseBodyTransConfigs()
                self.trans_configs.append(temp_model.from_map(k))
        return self


class DescribeTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTemplateResponse, self).to_map()
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
            temp_model = DescribeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, type=None, instance_id=None, sort_by=None, sort_direction=None,
                 page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.type = type  # type: str
        self.instance_id = instance_id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class DescribeTemplatesResponseBodyTemplatesTransConfigs(TeaModel):
    def __init__(self, gop=None, width=None, video_bitrate=None, height=None, video_codec=None, fps=None, name=None,
                 id=None):
        self.gop = gop  # type: long
        self.width = width  # type: long
        self.video_bitrate = video_bitrate  # type: long
        self.height = height  # type: long
        self.video_codec = video_codec  # type: str
        self.fps = fps  # type: long
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesResponseBodyTemplatesTransConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gop is not None:
            result['Gop'] = self.gop
        if self.width is not None:
            result['Width'] = self.width
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.height is not None:
            result['Height'] = self.height
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gop') is not None:
            self.gop = m.get('Gop')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, type=None, trigger=None, oss_file_prefix=None, hls_ts=None, mp_4=None, jpg_on_demand=None,
                 oss_bucket=None, jpg_sequence=None, jpg_overwrite=None, file_format=None, callback=None, end_time=None,
                 start_time=None, interval=None, description=None, region=None, retention=None, hls_m3u_8=None, flv=None,
                 name=None, created_time=None, oss_endpoint=None, id=None, trans_configs=None):
        self.type = type  # type: str
        self.trigger = trigger  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.hls_ts = hls_ts  # type: str
        self.mp_4 = mp_4  # type: str
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.file_format = file_format  # type: str
        self.callback = callback  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.interval = interval  # type: long
        self.description = description  # type: str
        self.region = region  # type: str
        self.retention = retention  # type: long
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.flv = flv  # type: str
        self.name = name  # type: str
        self.created_time = created_time  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.id = id  # type: str
        self.trans_configs = trans_configs  # type: list[DescribeTemplatesResponseBodyTemplatesTransConfigs]

    def validate(self):
        if self.trans_configs:
            for k in self.trans_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.description is not None:
            result['Description'] = self.description
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.name is not None:
            result['Name'] = self.name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.id is not None:
            result['Id'] = self.id
        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k in self.trans_configs:
                result['TransConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k in m.get('TransConfigs'):
                temp_model = DescribeTemplatesResponseBodyTemplatesTransConfigs()
                self.trans_configs.append(temp_model.from_map(k))
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 templates=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.templates = templates  # type: list[DescribeTemplatesResponseBodyTemplates]

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTemplatesResponse, self).to_map()
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
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodStreamURLRequest(TeaModel):
    def __init__(self, owner_id=None, url=None, tx_id=None):
        self.owner_id = owner_id  # type: long
        self.url = url  # type: str
        self.tx_id = tx_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodStreamURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.url is not None:
            result['Url'] = self.url
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        return self


class DescribeVodStreamURLResponseBody(TeaModel):
    def __init__(self, url=None, out_protocol=None, request_id=None, port=None, tx_id=None):
        self.url = url  # type: str
        self.out_protocol = out_protocol  # type: str
        self.request_id = request_id  # type: str
        self.port = port  # type: long
        self.tx_id = tx_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodStreamURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.port is not None:
            result['Port'] = self.port
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        return self


class DescribeVodStreamURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVodStreamURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodStreamURLResponse, self).to_map()
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
            temp_model = DescribeVodStreamURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsCertificateDetailRequest(TeaModel):
    def __init__(self, owner_id=None, cert_name=None):
        self.owner_id = owner_id  # type: long
        self.cert_name = cert_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        return self


class DescribeVsCertificateDetailResponseBody(TeaModel):
    def __init__(self, cert_name=None, key=None, cert=None, cert_id=None, request_id=None):
        self.cert_name = cert_name  # type: str
        self.key = key  # type: str
        self.cert = cert  # type: str
        self.cert_id = cert_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsCertificateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsCertificateDetailResponse, self).to_map()
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
            temp_model = DescribeVsCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsCertificateListRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, last_time=None, fingerprint=None, cert_name=None, issuer=None, cert_id=None, common=None):
        self.last_time = last_time  # type: long
        self.fingerprint = fingerprint  # type: str
        self.cert_name = cert_name  # type: str
        self.issuer = issuer  # type: str
        self.cert_id = cert_id  # type: long
        self.common = common  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateListResponseBodyCertificateListModelCertList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.common is not None:
            result['Common'] = self.common
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        return self


class DescribeVsCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, count=None, cert_list=None):
        self.count = count  # type: int
        self.cert_list = cert_list  # type: list[DescribeVsCertificateListResponseBodyCertificateListModelCertList]

    def validate(self):
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsCertificateListResponseBodyCertificateListModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = DescribeVsCertificateListResponseBodyCertificateListModelCertList()
                self.cert_list.append(temp_model.from_map(k))
        return self


class DescribeVsCertificateListResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_list_model=None):
        self.request_id = request_id  # type: str
        self.certificate_list_model = certificate_list_model  # type: DescribeVsCertificateListResponseBodyCertificateListModel

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeVsCertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeVsCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        return self


class DescribeVsCertificateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsCertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsCertificateListResponse, self).to_map()
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
            temp_model = DescribeVsCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainBpsDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, bps_value=None, time_stamp=None):
        self.bps_value = bps_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_value is not None:
            result['BpsValue'] = self.bps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsValue') is not None:
            self.bps_value = m.get('BpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainBpsDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeVsDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainCertificateInfoRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, status=None, cert_life=None, cert_expire_time=None, sslpub=None, cert_type=None,
                 server_certificate_status=None, cert_domain_name=None, cert_name=None, cert_org=None, domain_name=None):
        self.status = status  # type: str
        self.cert_life = cert_life  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.sslpub = sslpub  # type: str
        self.cert_type = cert_type  # type: str
        self.server_certificate_status = server_certificate_status  # type: str
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoResponseBodyCertInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainCertificateInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, cert_infos=None):
        self.request_id = request_id  # type: str
        self.cert_infos = cert_infos  # type: DescribeVsDomainCertificateInfoResponseBodyCertInfos

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertInfos') is not None:
            temp_model = DescribeVsDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        return self


class DescribeVsDomainCertificateInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainCertificateInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoResponse, self).to_map()
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
            temp_model = DescribeVsDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainConfigsRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, function_names=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeVsDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, status=None, config_id=None, function_name=None, function_args=None):
        self.status = status  # type: str
        self.config_id = config_id  # type: str
        self.function_name = function_name  # type: str
        self.function_args = function_args  # type: list[DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs]

    def validate(self):
        if self.function_args:
            for k in self.function_args:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainConfigsResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        return self


class DescribeVsDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = request_id  # type: str
        self.domain_configs = domain_configs  # type: list[DescribeVsDomainConfigsResponseBodyDomainConfigs]

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeVsDomainConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        return self


class DescribeVsDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainConfigsResponse, self).to_map()
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
            temp_model = DescribeVsDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainDetailRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsDomainDetailResponseBodyDomainConfig(TeaModel):
    def __init__(self, gmt_created=None, description=None, sslprotocol=None, region=None, scope=None, cname=None,
                 domain_status=None, gmt_modified=None, domain_name=None, domain_type=None):
        self.gmt_created = gmt_created  # type: str
        self.description = description  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.region = region  # type: str
        self.scope = scope  # type: str
        self.cname = cname  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_type = domain_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainDetailResponseBodyDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.region is not None:
            result['Region'] = self.region
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        return self


class DescribeVsDomainDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_config=None):
        self.request_id = request_id  # type: str
        self.domain_config = domain_config  # type: DescribeVsDomainDetailResponseBodyDomainConfig

    def validate(self):
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        _map = super(DescribeVsDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainConfig') is not None:
            temp_model = DescribeVsDomainDetailResponseBodyDomainConfig()
            self.domain_config = temp_model.from_map(m['DomainConfig'])
        return self


class DescribeVsDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainDetailResponse, self).to_map()
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
            temp_model = DescribeVsDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainPvDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvDataResponseBodyPvDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeVsDomainPvDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 pv_data_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.pv_data_interval = pv_data_interval  # type: DescribeVsDomainPvDataResponseBodyPvDataInterval

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeVsDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        return self


class DescribeVsDomainPvDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainPvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainPvUvDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo(TeaModel):
    def __init__(self, pv=None, time_stamp=None, uv=None):
        self.pv = pv  # type: str
        self.time_stamp = time_stamp  # type: str
        self.uv = uv  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pv is not None:
            result['PV'] = self.pv
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.uv is not None:
            result['UV'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PV') is not None:
            self.pv = m.get('PV')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        return self


class DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos(TeaModel):
    def __init__(self, pv_uv_data_info=None):
        self.pv_uv_data_info = pv_uv_data_info  # type: list[DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo]

    def validate(self):
        if self.pv_uv_data_info:
            for k in self.pv_uv_data_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PvUvDataInfo'] = []
        if self.pv_uv_data_info is not None:
            for k in self.pv_uv_data_info:
                result['PvUvDataInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pv_uv_data_info = []
        if m.get('PvUvDataInfo') is not None:
            for k in m.get('PvUvDataInfo'):
                temp_model = DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo()
                self.pv_uv_data_info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainPvUvDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 pv_uv_data_infos=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.pv_uv_data_infos = pv_uv_data_infos  # type: DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos

    def validate(self):
        if self.pv_uv_data_infos:
            self.pv_uv_data_infos.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.pv_uv_data_infos is not None:
            result['PvUvDataInfos'] = self.pv_uv_data_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('PvUvDataInfos') is not None:
            temp_model = DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos()
            self.pv_uv_data_infos = temp_model.from_map(m['PvUvDataInfos'])
        return self


class DescribeVsDomainPvUvDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainPvUvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainPvUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainRecordDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule(TeaModel):
    def __init__(self, record_value=None, time_stamp=None):
        self.record_value = record_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_value is not None:
            result['RecordValue'] = self.record_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainRecordDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None,
                 record_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.record_data_per_interval = record_data_per_interval  # type: DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval

    def validate(self):
        if self.record_data_per_interval:
            self.record_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.record_data_per_interval is not None:
            result['RecordDataPerInterval'] = self.record_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RecordDataPerInterval') is not None:
            temp_model = DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval()
            self.record_data_per_interval = temp_model.from_map(m['RecordDataPerInterval'])
        return self


class DescribeVsDomainRecordDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainRecordDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainRegionDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(self, total_query=None, total_bytes=None, avg_response_rate=None, avg_response_time=None,
                 req_err_rate=None, avg_object_size=None, bps=None, qps=None, region_ename=None, region=None, proportion=None,
                 bytes_proportion=None):
        self.total_query = total_query  # type: str
        self.total_bytes = total_bytes  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.req_err_rate = req_err_rate  # type: str
        self.avg_object_size = avg_object_size  # type: str
        self.bps = bps  # type: str
        self.qps = qps  # type: str
        self.region_ename = region_ename  # type: str
        self.region = region  # type: str
        self.proportion = proportion  # type: str
        self.bytes_proportion = bytes_proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataResponseBodyValueRegionProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.region is not None:
            result['Region'] = self.region
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        return self


class DescribeVsDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(self, region_proportion_data=None):
        self.region_proportion_data = region_proportion_data  # type: list[DescribeVsDomainRegionDataResponseBodyValueRegionProportionData]

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataResponseBodyValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionProportionData'] = []
        if self.region_proportion_data is not None:
            for k in self.region_proportion_data:
                result['RegionProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_proportion_data = []
        if m.get('RegionProportionData') is not None:
            for k in m.get('RegionProportionData'):
                temp_model = DescribeVsDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeVsDomainRegionDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 value=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.value = value  # type: DescribeVsDomainRegionDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('Value') is not None:
            temp_model = DescribeVsDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeVsDomainRegionDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainRegionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainReqBpsDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, req_bps_value=None):
        self.time_stamp = time_stamp  # type: str
        self.req_bps_value = req_bps_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.req_bps_value is not None:
            result['ReqBpsValue'] = self.req_bps_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('ReqBpsValue') is not None:
            self.req_bps_value = m.get('ReqBpsValue')
        return self


class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainReqBpsDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 req_bps_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.req_bps_data_per_interval = req_bps_data_per_interval  # type: DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval

    def validate(self):
        if self.req_bps_data_per_interval:
            self.req_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.req_bps_data_per_interval is not None:
            result['ReqBpsDataPerInterval'] = self.req_bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('ReqBpsDataPerInterval') is not None:
            temp_model = DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval()
            self.req_bps_data_per_interval = temp_model.from_map(m['ReqBpsDataPerInterval'])
        return self


class DescribeVsDomainReqBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainReqBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainReqBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainReqTrafficDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, req_traffic_value=None, time_stamp=None):
        self.req_traffic_value = req_traffic_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_traffic_value is not None:
            result['ReqTrafficValue'] = self.req_traffic_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReqTrafficValue') is not None:
            self.req_traffic_value = m.get('ReqTrafficValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainReqTrafficDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 req_traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.req_traffic_data_per_interval = req_traffic_data_per_interval  # type: DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval

    def validate(self):
        if self.req_traffic_data_per_interval:
            self.req_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.req_traffic_data_per_interval is not None:
            result['ReqTrafficDataPerInterval'] = self.req_traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('ReqTrafficDataPerInterval') is not None:
            temp_model = DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval()
            self.req_traffic_data_per_interval = temp_model.from_map(m['ReqTrafficDataPerInterval'])
        return self


class DescribeVsDomainReqTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainReqTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainReqTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainSnapshotDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule(TeaModel):
    def __init__(self, snapshot_value=None, time_stamp=None):
        self.snapshot_value = snapshot_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_value is not None:
            result['SnapshotValue'] = self.snapshot_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SnapshotValue') is not None:
            self.snapshot_value = m.get('SnapshotValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainSnapshotDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None,
                 snapshot_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.snapshot_data_per_interval = snapshot_data_per_interval  # type: DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval

    def validate(self):
        if self.snapshot_data_per_interval:
            self.snapshot_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.snapshot_data_per_interval is not None:
            result['SnapshotDataPerInterval'] = self.snapshot_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SnapshotDataPerInterval') is not None:
            temp_model = DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval()
            self.snapshot_data_per_interval = temp_model.from_map(m['SnapshotDataPerInterval'])
        return self


class DescribeVsDomainSnapshotDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainSnapshotDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainSnapshotDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainTrafficDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, traffic_value=None, time_stamp=None):
        self.traffic_value = traffic_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainTrafficDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 traffic_data_per_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeVsDomainTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainUvDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainUvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainUvDataResponseBodyUvDataInterval, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeVsDomainUvDataResponseBody(TeaModel):
    def __init__(self, end_time=None, start_time=None, request_id=None, domain_name=None, data_interval=None,
                 uv_data_interval=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_name = domain_name  # type: str
        self.data_interval = data_interval  # type: str
        self.uv_data_interval = uv_data_interval  # type: DescribeVsDomainUvDataResponseBodyUvDataInterval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainUvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('UvDataInterval') is not None:
            temp_model = DescribeVsDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        return self


class DescribeVsDomainUvDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainUvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainUvDataResponse, self).to_map()
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
            temp_model = DescribeVsDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(self, end_time=None, app_name=None, source_url=None, start_time=None, stream_name=None,
                 domain_name=None):
        self.end_time = end_time  # type: str
        self.app_name = app_name  # type: str
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList(TeaModel):
    def __init__(self, live_app_record=None):
        self.live_app_record = live_app_record  # type: list[DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord]

    def validate(self):
        if self.live_app_record:
            for k in self.live_app_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k in self.live_app_record:
                result['LiveAppRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_app_record = []
        if m.get('LiveAppRecord') is not None:
            for k in m.get('LiveAppRecord'):
                temp_model = DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k))
        return self


class DescribeVsPullStreamInfoConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, live_app_record_list=None):
        self.request_id = request_id  # type: str
        self.live_app_record_list = live_app_record_list  # type: DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LiveAppRecordList') is not None:
            temp_model = DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m['LiveAppRecordList'])
        return self


class DescribeVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsPullStreamInfoConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigResponse, self).to_map()
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
            temp_model = DescribeVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStorageUsageDataRequest(TeaModel):
    def __init__(self, owner_id=None, bucket=None, split_by=None, interval=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.bucket = bucket  # type: str
        self.split_by = split_by  # type: str
        self.interval = interval  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.split_by is not None:
            result['SplitBy'] = self.split_by
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule(TeaModel):
    def __init__(self, storage_data_value=None, time_stamp=None, bucket=None):
        self.storage_data_value = storage_data_value  # type: int
        self.time_stamp = time_stamp  # type: str
        self.bucket = bucket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_data_value is not None:
            result['StorageDataValue'] = self.storage_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageDataValue') is not None:
            self.storage_data_value = m.get('StorageDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        return self


class DescribeVsStorageUsageDataResponseBodyStorageUsage(TeaModel):
    def __init__(self, storage_usage_data_module=None):
        self.storage_usage_data_module = storage_usage_data_module  # type: list[DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule]

    def validate(self):
        if self.storage_usage_data_module:
            for k in self.storage_usage_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataResponseBodyStorageUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StorageUsageDataModule'] = []
        if self.storage_usage_data_module is not None:
            for k in self.storage_usage_data_module:
                result['StorageUsageDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.storage_usage_data_module = []
        if m.get('StorageUsageDataModule') is not None:
            for k in m.get('StorageUsageDataModule'):
                temp_model = DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule()
                self.storage_usage_data_module.append(temp_model.from_map(k))
        return self


class DescribeVsStorageUsageDataResponseBody(TeaModel):
    def __init__(self, request_id=None, storage_usage=None):
        self.request_id = request_id  # type: str
        self.storage_usage = storage_usage  # type: DescribeVsStorageUsageDataResponseBodyStorageUsage

    def validate(self):
        if self.storage_usage:
            self.storage_usage.validate()

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageUsage') is not None:
            temp_model = DescribeVsStorageUsageDataResponseBodyStorageUsage()
            self.storage_usage = temp_model.from_map(m['StorageUsage'])
        return self


class DescribeVsStorageUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsStorageUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataResponse, self).to_map()
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
            temp_model = DescribeVsStorageUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig(TeaModel):
    def __init__(self, auth_type=None, auth_key=None, domain_name=None, notify_url=None):
        self.auth_type = auth_type  # type: str
        self.auth_key = auth_key  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        return self


class DescribeVsStreamsNotifyUrlConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, live_streams_notify_config=None):
        self.request_id = request_id  # type: str
        self.live_streams_notify_config = live_streams_notify_config  # type: DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig

    def validate(self):
        if self.live_streams_notify_config:
            self.live_streams_notify_config.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.live_streams_notify_config is not None:
            result['LiveStreamsNotifyConfig'] = self.live_streams_notify_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LiveStreamsNotifyConfig') is not None:
            temp_model = DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig()
            self.live_streams_notify_config = temp_model.from_map(m['LiveStreamsNotifyConfig'])
        return self


class DescribeVsStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsStreamsNotifyUrlConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigResponse, self).to_map()
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
            temp_model = DescribeVsStreamsNotifyUrlConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStreamsOnlineListRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None, page_size=None,
                 page_num=None, stream_type=None, start_time=None, end_time=None, query_type=None, order_by=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str
        self.page_size = page_size  # type: int
        self.page_num = page_num  # type: int
        self.stream_type = stream_type  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.query_type = query_type  # type: str
        self.order_by = order_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        return self


class DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo(TeaModel):
    def __init__(self, publish_time=None, app_name=None, publish_type=None, publish_url=None, transcoded=None,
                 stream_name=None, domain_name=None, transcode_id=None, publish_domain=None):
        self.publish_time = publish_time  # type: str
        self.app_name = app_name  # type: str
        self.publish_type = publish_type  # type: str
        self.publish_url = publish_url  # type: str
        self.transcoded = transcoded  # type: str
        self.stream_name = stream_name  # type: str
        self.domain_name = domain_name  # type: str
        self.transcode_id = transcode_id  # type: str
        self.publish_domain = publish_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url
        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id
        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')
        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')
        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')
        return self


class DescribeVsStreamsOnlineListResponseBodyOnlineInfo(TeaModel):
    def __init__(self, live_stream_online_info=None):
        self.live_stream_online_info = live_stream_online_info  # type: list[DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo]

    def validate(self):
        if self.live_stream_online_info:
            for k in self.live_stream_online_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListResponseBodyOnlineInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveStreamOnlineInfo'] = []
        if self.live_stream_online_info is not None:
            for k in self.live_stream_online_info:
                result['LiveStreamOnlineInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_stream_online_info = []
        if m.get('LiveStreamOnlineInfo') is not None:
            for k in m.get('LiveStreamOnlineInfo'):
                temp_model = DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo()
                self.live_stream_online_info.append(temp_model.from_map(k))
        return self


class DescribeVsStreamsOnlineListResponseBody(TeaModel):
    def __init__(self, total_page=None, page_num=None, page_size=None, request_id=None, total_num=None,
                 online_info=None):
        self.total_page = total_page  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int
        self.online_info = online_info  # type: DescribeVsStreamsOnlineListResponseBodyOnlineInfo

    def validate(self):
        if self.online_info:
            self.online_info.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.online_info is not None:
            result['OnlineInfo'] = self.online_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('OnlineInfo') is not None:
            temp_model = DescribeVsStreamsOnlineListResponseBodyOnlineInfo()
            self.online_info = temp_model.from_map(m['OnlineInfo'])
        return self


class DescribeVsStreamsOnlineListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsStreamsOnlineListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListResponse, self).to_map()
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
            temp_model = DescribeVsStreamsOnlineListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStreamsPublishListRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None, page_size=None, page_number=None, stream_type=None, query_type=None, order_by=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.stream_type = stream_type  # type: str
        self.query_type = query_type  # type: str
        self.order_by = order_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        return self


class DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo(TeaModel):
    def __init__(self, edge_node_addr=None, publish_url=None, stream_name=None, domain_name=None, stop_time=None,
                 transcode_id=None, publish_domain=None, app_name=None, publish_time=None, publish_type=None, transcoded=None,
                 client_addr=None, stream_url=None):
        self.edge_node_addr = edge_node_addr  # type: str
        self.publish_url = publish_url  # type: str
        self.stream_name = stream_name  # type: str
        self.domain_name = domain_name  # type: str
        self.stop_time = stop_time  # type: str
        self.transcode_id = transcode_id  # type: str
        self.publish_domain = publish_domain  # type: str
        self.app_name = app_name  # type: str
        self.publish_time = publish_time  # type: str
        self.publish_type = publish_type  # type: str
        self.transcoded = transcoded  # type: str
        self.client_addr = client_addr  # type: str
        self.stream_url = stream_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_node_addr is not None:
            result['EdgeNodeAddr'] = self.edge_node_addr
        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id
        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EdgeNodeAddr') is not None:
            self.edge_node_addr = m.get('EdgeNodeAddr')
        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')
        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')
        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')
        return self


class DescribeVsStreamsPublishListResponseBodyPublishInfo(TeaModel):
    def __init__(self, live_stream_publish_info=None):
        self.live_stream_publish_info = live_stream_publish_info  # type: list[DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo]

    def validate(self):
        if self.live_stream_publish_info:
            for k in self.live_stream_publish_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListResponseBodyPublishInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveStreamPublishInfo'] = []
        if self.live_stream_publish_info is not None:
            for k in self.live_stream_publish_info:
                result['LiveStreamPublishInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_stream_publish_info = []
        if m.get('LiveStreamPublishInfo') is not None:
            for k in m.get('LiveStreamPublishInfo'):
                temp_model = DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo()
                self.live_stream_publish_info.append(temp_model.from_map(k))
        return self


class DescribeVsStreamsPublishListResponseBody(TeaModel):
    def __init__(self, total_page=None, page_num=None, page_size=None, request_id=None, total_num=None,
                 publish_info=None):
        self.total_page = total_page  # type: int
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int
        self.publish_info = publish_info  # type: DescribeVsStreamsPublishListResponseBodyPublishInfo

    def validate(self):
        if self.publish_info:
            self.publish_info.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.publish_info is not None:
            result['PublishInfo'] = self.publish_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('PublishInfo') is not None:
            temp_model = DescribeVsStreamsPublishListResponseBodyPublishInfo()
            self.publish_info = temp_model.from_map(m['PublishInfo'])
        return self


class DescribeVsStreamsPublishListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsStreamsPublishListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListResponse, self).to_map()
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
            temp_model = DescribeVsStreamsPublishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsTopDomainsByFlowRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None, limit=None):
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(self, max_bps=None, rank=None, total_access=None, traffic_percent=None, domain_name=None,
                 total_traffic=None, max_bps_time=None):
        self.max_bps = max_bps  # type: long
        self.rank = rank  # type: long
        self.total_access = total_access  # type: long
        self.traffic_percent = traffic_percent  # type: str
        self.domain_name = domain_name  # type: str
        self.total_traffic = total_traffic  # type: str
        self.max_bps_time = max_bps_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        return self


class DescribeVsTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(self, top_domain=None):
        self.top_domain = top_domain  # type: list[DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain]

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowResponseBodyTopDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k in self.top_domain:
                result['TopDomain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.top_domain = []
        if m.get('TopDomain') is not None:
            for k in m.get('TopDomain'):
                temp_model = DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeVsTopDomainsByFlowResponseBody(TeaModel):
    def __init__(self, domain_online_count=None, end_time=None, start_time=None, request_id=None, domain_count=None,
                 top_domains=None):
        self.domain_online_count = domain_online_count  # type: long
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.domain_count = domain_count  # type: long
        self.top_domains = top_domains  # type: DescribeVsTopDomainsByFlowResponseBodyTopDomains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('TopDomains') is not None:
            temp_model = DescribeVsTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        return self


class DescribeVsTopDomainsByFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsTopDomainsByFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowResponse, self).to_map()
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
            temp_model = DescribeVsTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsUpPeakPublishStreamDataRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None, domain_switch=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.domain_switch = domain_switch  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain_switch is not None:
            result['DomainSwitch'] = self.domain_switch
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DomainSwitch') is not None:
            self.domain_switch = m.get('DomainSwitch')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData(TeaModel):
    def __init__(self, query_time=None, band_width=None, stat_name=None, peak_time=None, publish_stream_num=None):
        self.query_time = query_time  # type: str
        self.band_width = band_width  # type: str
        self.stat_name = stat_name  # type: str
        self.peak_time = peak_time  # type: str
        self.publish_stream_num = publish_stream_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.stat_name is not None:
            result['StatName'] = self.stat_name
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time
        if self.publish_stream_num is not None:
            result['PublishStreamNum'] = self.publish_stream_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('StatName') is not None:
            self.stat_name = m.get('StatName')
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')
        if m.get('PublishStreamNum') is not None:
            self.publish_stream_num = m.get('PublishStreamNum')
        return self


class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas(TeaModel):
    def __init__(self, describe_vs_up_peak_publish_stream_data=None):
        self.describe_vs_up_peak_publish_stream_data = describe_vs_up_peak_publish_stream_data  # type: list[DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData]

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_data:
            for k in self.describe_vs_up_peak_publish_stream_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DescribeVsUpPeakPublishStreamData'] = []
        if self.describe_vs_up_peak_publish_stream_data is not None:
            for k in self.describe_vs_up_peak_publish_stream_data:
                result['DescribeVsUpPeakPublishStreamData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.describe_vs_up_peak_publish_stream_data = []
        if m.get('DescribeVsUpPeakPublishStreamData') is not None:
            for k in m.get('DescribeVsUpPeakPublishStreamData'):
                temp_model = DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData()
                self.describe_vs_up_peak_publish_stream_data.append(temp_model.from_map(k))
        return self


class DescribeVsUpPeakPublishStreamDataResponseBody(TeaModel):
    def __init__(self, request_id=None, describe_vs_up_peak_publish_stream_datas=None):
        self.request_id = request_id  # type: str
        self.describe_vs_up_peak_publish_stream_datas = describe_vs_up_peak_publish_stream_datas  # type: DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_datas:
            self.describe_vs_up_peak_publish_stream_datas.validate()

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.describe_vs_up_peak_publish_stream_datas is not None:
            result['DescribeVsUpPeakPublishStreamDatas'] = self.describe_vs_up_peak_publish_stream_datas.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DescribeVsUpPeakPublishStreamDatas') is not None:
            temp_model = DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas()
            self.describe_vs_up_peak_publish_stream_datas = temp_model.from_map(m['DescribeVsUpPeakPublishStreamDatas'])
        return self


class DescribeVsUpPeakPublishStreamDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsUpPeakPublishStreamDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataResponse, self).to_map()
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
            temp_model = DescribeVsUpPeakPublishStreamDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsUserResourcePackageRequest(TeaModel):
    def __init__(self, security_token=None, owner_id=None):
        self.security_token = security_token  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(self, display_name=None, status=None, commodity_code=None, curr_capacity=None, init_capacity=None,
                 instance_id=None):
        self.display_name = display_name  # type: str
        self.status = status  # type: str
        self.commodity_code = commodity_code  # type: str
        self.curr_capacity = curr_capacity  # type: str
        self.init_capacity = init_capacity  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.status is not None:
            result['Status'] = self.status
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeVsUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(self, resource_package_info=None):
        self.resource_package_info = resource_package_info  # type: list[DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo]

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageResponseBodyResourcePackageInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourcePackageInfo'] = []
        if self.resource_package_info is not None:
            for k in self.resource_package_info:
                result['ResourcePackageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_package_info = []
        if m.get('ResourcePackageInfo') is not None:
            for k in m.get('ResourcePackageInfo'):
                temp_model = DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeVsUserResourcePackageResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_package_infos=None):
        self.request_id = request_id  # type: str
        self.resource_package_infos = resource_package_infos  # type: DescribeVsUserResourcePackageResponseBodyResourcePackageInfos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_package_infos is not None:
            result['ResourcePackageInfos'] = self.resource_package_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourcePackageInfos') is not None:
            temp_model = DescribeVsUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeVsUserResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsUserResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageResponse, self).to_map()
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
            temp_model = DescribeVsUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForbidVsStreamRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None, live_stream_type=None,
                 oneshot=None, control_stream_action=None, resume_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.oneshot = oneshot  # type: str
        self.control_stream_action = control_stream_action  # type: str
        self.resume_time = resume_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForbidVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')
        return self


class ForbidVsStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForbidVsStreamResponseBody, self).to_map()
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


class ForbidVsStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ForbidVsStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ForbidVsStreamResponse, self).to_map()
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
            temp_model = ForbidVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketInfoRequest(TeaModel):
    def __init__(self, owner_id=None, bucket_name=None):
        self.owner_id = owner_id  # type: long
        self.bucket_name = bucket_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBucketInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class GetBucketInfoResponseBodyBucketInfo(TeaModel):
    def __init__(self, storage_class=None, data_redundancy_type=None, resource_type=None, comment=None,
                 dispatcher_type=None, create_time=None, endpoint=None, bucket_acl=None, bucket_name=None, modify_time=None):
        self.storage_class = storage_class  # type: str
        self.data_redundancy_type = data_redundancy_type  # type: str
        self.resource_type = resource_type  # type: str
        self.comment = comment  # type: str
        self.dispatcher_type = dispatcher_type  # type: str
        self.create_time = create_time  # type: str
        self.endpoint = endpoint  # type: str
        self.bucket_acl = bucket_acl  # type: str
        self.bucket_name = bucket_name  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBucketInfoResponseBodyBucketInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetBucketInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, bucket_info=None):
        self.request_id = request_id  # type: str
        self.bucket_info = bucket_info  # type: GetBucketInfoResponseBodyBucketInfo

    def validate(self):
        if self.bucket_info:
            self.bucket_info.validate()

    def to_map(self):
        _map = super(GetBucketInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bucket_info is not None:
            result['BucketInfo'] = self.bucket_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BucketInfo') is not None:
            temp_model = GetBucketInfoResponseBodyBucketInfo()
            self.bucket_info = temp_model.from_map(m['BucketInfo'])
        return self


class GetBucketInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBucketInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBucketInfoResponse, self).to_map()
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
            temp_model = GetBucketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GotoPresetRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, preset_id=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.preset_id = preset_id  # type: str
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GotoPresetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class GotoPresetResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GotoPresetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GotoPresetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GotoPresetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GotoPresetResponse, self).to_map()
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
            temp_model = GotoPresetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBucketsRequest(TeaModel):
    def __init__(self, owner_id=None, prefix=None, keyword=None, marker=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.prefix = prefix  # type: str
        self.keyword = keyword  # type: str
        self.marker = marker  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBucketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBucketsResponseBodyBucketInfos(TeaModel):
    def __init__(self, storage_class=None, data_redundancy_type=None, resource_type=None, comment=None,
                 dispatcher_type=None, create_time=None, endpoint=None, bucket_acl=None, bucket_name=None, modify_time=None):
        self.storage_class = storage_class  # type: str
        self.data_redundancy_type = data_redundancy_type  # type: str
        self.resource_type = resource_type  # type: str
        self.comment = comment  # type: str
        self.dispatcher_type = dispatcher_type  # type: str
        self.create_time = create_time  # type: str
        self.endpoint = endpoint  # type: str
        self.bucket_acl = bucket_acl  # type: str
        self.bucket_name = bucket_name  # type: str
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBucketsResponseBodyBucketInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListBucketsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, bucket_infos=None):
        self.total_count = total_count  # type: long
        self.request_id = request_id  # type: str
        self.bucket_infos = bucket_infos  # type: list[ListBucketsResponseBodyBucketInfos]

    def validate(self):
        if self.bucket_infos:
            for k in self.bucket_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBucketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BucketInfos'] = []
        if self.bucket_infos is not None:
            for k in self.bucket_infos:
                result['BucketInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bucket_infos = []
        if m.get('BucketInfos') is not None:
            for k in m.get('BucketInfos'):
                temp_model = ListBucketsResponseBodyBucketInfos()
                self.bucket_infos.append(temp_model.from_map(k))
        return self


class ListBucketsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBucketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBucketsResponse, self).to_map()
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
            temp_model = ListBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceChannelsRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None, page_size=None, page_num=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class ListDeviceChannelsResponseBodyChannels(TeaModel):
    def __init__(self, channel_id=None, params=None, device_status=None, name=None, device_id=None):
        self.channel_id = channel_id  # type: long
        self.params = params  # type: str
        self.device_status = device_status  # type: str
        self.name = name  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceChannelsResponseBodyChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.params is not None:
            result['Params'] = self.params
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.name is not None:
            result['Name'] = self.name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class ListDeviceChannelsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 channels=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.channels = channels  # type: list[ListDeviceChannelsResponseBodyChannels]

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceChannelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = ListDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        return self


class ListDeviceChannelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDeviceChannelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceChannelsResponse, self).to_map()
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
            temp_model = ListDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceRecordsRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None, stream_id=None, search_criteria=None, page_size=None,
                 page_num=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str
        self.stream_id = stream_id  # type: str
        self.search_criteria = search_criteria  # type: str
        self.page_size = page_size  # type: long
        self.page_num = page_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.search_criteria is not None:
            result['SearchCriteria'] = self.search_criteria
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('SearchCriteria') is not None:
            self.search_criteria = m.get('SearchCriteria')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class ListDeviceRecordsResponseBodyRecords(TeaModel):
    def __init__(self, end_time=None, start_time=None, record_type=None, filename=None, file_size=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.record_type = record_type  # type: str
        self.filename = filename  # type: str
        self.file_size = file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceRecordsResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class ListDeviceRecordsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, page_count=None,
                 records=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.page_count = page_count  # type: long
        self.records = records  # type: list[ListDeviceRecordsResponseBodyRecords]

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListDeviceRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class ListDeviceRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDeviceRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceRecordsResponse, self).to_map()
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
            temp_model = ListDeviceRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListObjectsRequest(TeaModel):
    def __init__(self, owner_id=None, bucket_name=None, delimiter=None, encoding_type=None, marker=None,
                 max_keys=None, prefix=None, continuation_token=None, start_after=None):
        self.owner_id = owner_id  # type: long
        self.bucket_name = bucket_name  # type: str
        self.delimiter = delimiter  # type: str
        self.encoding_type = encoding_type  # type: str
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int
        self.prefix = prefix  # type: str
        self.continuation_token = continuation_token  # type: str
        self.start_after = start_after  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListObjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.start_after is not None:
            result['StartAfter'] = self.start_after
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('StartAfter') is not None:
            self.start_after = m.get('StartAfter')
        return self


class ListObjectsResponseBodyContents(TeaModel):
    def __init__(self, storage_class=None, last_modified=None, key=None, etag=None, size=None):
        self.storage_class = storage_class  # type: str
        self.last_modified = last_modified  # type: str
        self.key = key  # type: str
        self.etag = etag  # type: str
        self.size = size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListObjectsResponseBodyContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.key is not None:
            result['Key'] = self.key
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListObjectsResponseBody(TeaModel):
    def __init__(self, marker=None, max_keys=None, prefix=None, continuation_token=None,
                 next_continuation_token=None, encoding_type=None, next_marker=None, delimiter=None, request_id=None, bucket_name=None,
                 is_truncated=None, key_count=None, common_prefixes=None, contents=None):
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int
        self.prefix = prefix  # type: str
        self.continuation_token = continuation_token  # type: str
        self.next_continuation_token = next_continuation_token  # type: str
        self.encoding_type = encoding_type  # type: str
        self.next_marker = next_marker  # type: str
        self.delimiter = delimiter  # type: str
        self.request_id = request_id  # type: str
        self.bucket_name = bucket_name  # type: str
        self.is_truncated = is_truncated  # type: bool
        self.key_count = key_count  # type: int
        self.common_prefixes = common_prefixes  # type: list[str]
        self.contents = contents  # type: list[ListObjectsResponseBodyContents]

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListObjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key_count is not None:
            result['KeyCount'] = self.key_count
        if self.common_prefixes is not None:
            result['CommonPrefixes'] = self.common_prefixes
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('KeyCount') is not None:
            self.key_count = m.get('KeyCount')
        if m.get('CommonPrefixes') is not None:
            self.common_prefixes = m.get('CommonPrefixes')
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = ListObjectsResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        return self


class ListObjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListObjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListObjectsResponse, self).to_map()
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
            temp_model = ListObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, description=None, group_id=None, parent_id=None,
                 directory_id=None, type=None, auto_start=None, gb_id=None, ip=None, port=None, url=None, username=None,
                 password=None, vendor=None, longitude=None, latitude=None, auto_pos=None, pos_interval=None,
                 alarm_method=None, params=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.parent_id = parent_id  # type: str
        self.directory_id = directory_id  # type: str
        self.type = type  # type: str
        self.auto_start = auto_start  # type: bool
        self.gb_id = gb_id  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: long
        self.url = url  # type: str
        self.username = username  # type: str
        self.password = password  # type: str
        self.vendor = vendor  # type: str
        self.longitude = longitude  # type: str
        self.latitude = latitude  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.pos_interval = pos_interval  # type: long
        self.alarm_method = alarm_method  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.type is not None:
            result['Type'] = self.type
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class ModifyDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeviceResponse, self).to_map()
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
            temp_model = ModifyDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceAlarmRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, channel_id=None, alarm_id=None, status=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.channel_id = channel_id  # type: int
        self.alarm_id = alarm_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyDeviceAlarmResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceAlarmResponseBody, self).to_map()
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


class ModifyDeviceAlarmResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDeviceAlarmResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeviceAlarmResponse, self).to_map()
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
            temp_model = ModifyDeviceAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceCaptureRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, image=None, video=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.image = image  # type: int
        self.video = video  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceCaptureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class ModifyDeviceCaptureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceCaptureResponseBody, self).to_map()
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


class ModifyDeviceCaptureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDeviceCaptureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeviceCaptureResponse, self).to_map()
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
            temp_model = ModifyDeviceCaptureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceChannelsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, dsn=None, device_status=None, channels=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.dsn = dsn  # type: str
        self.device_status = device_status  # type: str
        self.channels = channels  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.channels is not None:
            result['Channels'] = self.channels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        return self


class ModifyDeviceChannelsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceChannelsResponseBody, self).to_map()
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


class ModifyDeviceChannelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDeviceChannelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDeviceChannelsResponse, self).to_map()
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
            temp_model = ModifyDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDirectoryRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, description=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyDirectoryResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDirectoryResponse, self).to_map()
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
            temp_model = ModifyDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGroupRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, description=None, region=None, in_protocol=None,
                 out_protocol=None, enabled=None, push_domain=None, play_domain=None, lazy_pull=None, callback=None,
                 capture_interval=None, capture_image=None, capture_video=None, capture_oss_bucket=None, capture_oss_path=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.region = region  # type: str
        self.in_protocol = in_protocol  # type: str
        self.out_protocol = out_protocol  # type: str
        self.enabled = enabled  # type: bool
        self.push_domain = push_domain  # type: str
        self.play_domain = play_domain  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.callback = callback  # type: str
        self.capture_interval = capture_interval  # type: int
        self.capture_image = capture_image  # type: int
        self.capture_video = capture_video  # type: int
        self.capture_oss_bucket = capture_oss_bucket  # type: str
        self.capture_oss_path = capture_oss_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.region is not None:
            result['Region'] = self.region
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.capture_image is not None:
            result['CaptureImage'] = self.capture_image
        if self.capture_video is not None:
            result['CaptureVideo'] = self.capture_video
        if self.capture_oss_bucket is not None:
            result['CaptureOssBucket'] = self.capture_oss_bucket
        if self.capture_oss_path is not None:
            result['CaptureOssPath'] = self.capture_oss_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('CaptureImage') is not None:
            self.capture_image = m.get('CaptureImage')
        if m.get('CaptureVideo') is not None:
            self.capture_video = m.get('CaptureVideo')
        if m.get('CaptureOssBucket') is not None:
            self.capture_oss_bucket = m.get('CaptureOssBucket')
        if m.get('CaptureOssPath') is not None:
            self.capture_oss_path = m.get('CaptureOssPath')
        return self


class ModifyGroupResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyGroupResponse, self).to_map()
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
            temp_model = ModifyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParentPlatformRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, description=None, gb_id=None, ip=None, port=None,
                 client_auth=None, client_username=None, client_password=None, auto_start=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.gb_id = gb_id  # type: str
        self.ip = ip  # type: str
        self.port = port  # type: long
        self.client_auth = client_auth  # type: bool
        self.client_username = client_username  # type: str
        self.client_password = client_password  # type: str
        self.auto_start = auto_start  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        return self


class ModifyParentPlatformResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParentPlatformResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyParentPlatformResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyParentPlatformResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyParentPlatformResponse, self).to_map()
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
            temp_model = ModifyParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, description=None, region=None, oss_bucket=None,
                 oss_endpoint=None, oss_file_prefix=None, trigger=None, start_time=None, end_time=None, interval=None,
                 retention=None, file_format=None, jpg_overwrite=None, jpg_sequence=None, jpg_on_demand=None, mp_4=None,
                 flv=None, hls_m3u_8=None, hls_ts=None, callback=None, trans_configs_json=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.region = region  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.trigger = trigger  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: long
        self.retention = retention  # type: long
        self.file_format = file_format  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.mp_4 = mp_4  # type: str
        self.flv = flv  # type: str
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.hls_ts = hls_ts  # type: str
        self.callback = callback  # type: str
        self.trans_configs_json = trans_configs_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.region is not None:
            result['Region'] = self.region
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')
        return self


class ModifyTemplateResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTemplateResponse, self).to_map()
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
            temp_model = ModifyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenVsServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenVsServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenVsServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenVsServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenVsServiceResponse, self).to_map()
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
            temp_model = OpenVsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PrepareUploadRequest(TeaModel):
    def __init__(self, owner_id=None, bucket_name=None, client_ip=None):
        self.owner_id = owner_id  # type: long
        self.bucket_name = bucket_name  # type: str
        self.client_ip = client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PrepareUploadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        return self


class PrepareUploadResponseBody(TeaModel):
    def __init__(self, request_id=None, bucket_name=None, endpoint=None):
        self.request_id = request_id  # type: str
        self.bucket_name = bucket_name  # type: str
        self.endpoint = endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PrepareUploadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        return self


class PrepareUploadResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PrepareUploadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PrepareUploadResponse, self).to_map()
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
            temp_model = PrepareUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutBucketRequest(TeaModel):
    def __init__(self, owner_id=None, bucket_name=None, endpoint=None, comment=None, dispatcher_type=None,
                 bucket_acl=None, storage_class=None, resource_type=None, data_redundancy_type=None):
        self.owner_id = owner_id  # type: long
        self.bucket_name = bucket_name  # type: str
        self.endpoint = endpoint  # type: str
        self.comment = comment  # type: str
        self.dispatcher_type = dispatcher_type  # type: str
        self.bucket_acl = bucket_acl  # type: str
        self.storage_class = storage_class  # type: str
        self.resource_type = resource_type  # type: str
        self.data_redundancy_type = data_redundancy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        return self


class PutBucketResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutBucketResponseBody, self).to_map()
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


class PutBucketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PutBucketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutBucketResponse, self).to_map()
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
            temp_model = PutBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeVsStreamRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None, live_stream_type=None,
                 control_stream_action=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.control_stream_action = control_stream_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        return self


class ResumeVsStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeVsStreamResponseBody, self).to_map()
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


class ResumeVsStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeVsStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeVsStreamResponse, self).to_map()
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
            temp_model = ResumeVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPresetRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, preset_id=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.preset_id = preset_id  # type: str
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPresetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class SetPresetResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPresetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetPresetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetPresetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPresetResponse, self).to_map()
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
            temp_model = SetPresetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVsDomainCertificateRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, sslprotocol=None, cert_name=None, cert_type=None,
                 sslpub=None, sslpri=None, region=None, force_set=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.sslpub = sslpub  # type: str
        self.sslpri = sslpri  # type: str
        self.region = region  # type: str
        self.force_set = force_set  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVsDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.region is not None:
            result['Region'] = self.region
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        return self


class SetVsDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVsDomainCertificateResponseBody, self).to_map()
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


class SetVsDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetVsDomainCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetVsDomainCertificateResponse, self).to_map()
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
            temp_model = SetVsDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVsStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, notify_url=None, auth_type=None, auth_key=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url  # type: str
        self.auth_type = auth_type  # type: str
        self.auth_key = auth_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVsStreamsNotifyUrlConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class SetVsStreamsNotifyUrlConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVsStreamsNotifyUrlConfigResponseBody, self).to_map()
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


class SetVsStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetVsStreamsNotifyUrlConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetVsStreamsNotifyUrlConfigResponse, self).to_map()
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
            temp_model = SetVsStreamsNotifyUrlConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDeviceResponse, self).to_map()
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
            temp_model = StartDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartParentPlatformRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartParentPlatformResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartParentPlatformResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartParentPlatformResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartParentPlatformResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartParentPlatformResponse, self).to_map()
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
            temp_model = StartParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRecordStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, play_domain=None, app=None, name=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.play_domain = play_domain  # type: str
        self.app = app  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.app is not None:
            result['App'] = self.app
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class StartRecordStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordStreamResponseBody, self).to_map()
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


class StartRecordStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartRecordStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartRecordStreamResponse, self).to_map()
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
            temp_model = StartRecordStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class StartStreamResponseBody(TeaModel):
    def __init__(self, request_id=None, name=None, id=None):
        self.request_id = request_id  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class StartStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartStreamResponse, self).to_map()
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
            temp_model = StartStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTransferStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, url=None, transcode=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.url = url  # type: str
        self.transcode = transcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTransferStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.url is not None:
            result['Url'] = self.url
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        return self


class StartTransferStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTransferStreamResponseBody, self).to_map()
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


class StartTransferStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartTransferStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartTransferStreamResponse, self).to_map()
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
            temp_model = StartTransferStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAdjustRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, iris=None, focus=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.iris = iris  # type: bool
        self.focus = focus  # type: bool
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAdjustRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.iris is not None:
            result['Iris'] = self.iris
        if self.focus is not None:
            result['Focus'] = self.focus
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Iris') is not None:
            self.iris = m.get('Iris')
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class StopAdjustResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAdjustResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAdjustResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopAdjustResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAdjustResponse, self).to_map()
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
            temp_model = StopAdjustResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, start_time=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StopDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDeviceResponse, self).to_map()
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
            temp_model = StopDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMoveRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, pan=None, tilt=None, zoom=None, sub_protocol=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.pan = pan  # type: bool
        self.tilt = tilt  # type: bool
        self.zoom = zoom  # type: bool
        self.sub_protocol = sub_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMoveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.pan is not None:
            result['Pan'] = self.pan
        if self.tilt is not None:
            result['Tilt'] = self.tilt
        if self.zoom is not None:
            result['Zoom'] = self.zoom
        if self.sub_protocol is not None:
            result['SubProtocol'] = self.sub_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Pan') is not None:
            self.pan = m.get('Pan')
        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')
        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')
        if m.get('SubProtocol') is not None:
            self.sub_protocol = m.get('SubProtocol')
        return self


class StopMoveResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMoveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopMoveResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopMoveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopMoveResponse, self).to_map()
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
            temp_model = StopMoveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, play_domain=None, app=None, name=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.play_domain = play_domain  # type: str
        self.app = app  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.app is not None:
            result['App'] = self.app
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class StopRecordStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordStreamResponseBody, self).to_map()
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


class StopRecordStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopRecordStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopRecordStreamResponse, self).to_map()
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
            temp_model = StopRecordStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, name=None, start_time=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StopStreamResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopStreamResponse, self).to_map()
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
            temp_model = StopStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTransferStreamRequest(TeaModel):
    def __init__(self, owner_id=None, id=None, transcode=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str
        self.transcode = transcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTransferStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        return self


class StopTransferStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTransferStreamResponseBody, self).to_map()
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


class StopTransferStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopTransferStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopTransferStreamResponse, self).to_map()
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
            temp_model = StopTransferStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncCatalogsRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncCatalogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SyncCatalogsResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncCatalogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncCatalogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncCatalogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncCatalogsResponse, self).to_map()
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
            temp_model = SyncCatalogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDeviceChannelsRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class SyncDeviceChannelsResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDeviceChannelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncDeviceChannelsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncDeviceChannelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncDeviceChannelsResponse, self).to_map()
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
            temp_model = SyncDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDirectoryRequest(TeaModel):
    def __init__(self, owner_id=None, directory_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.directory_id = directory_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UnbindDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDirectoryResponseBody, self).to_map()
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


class UnbindDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindDirectoryResponse, self).to_map()
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
            temp_model = UnbindDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindParentPlatformDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, parent_platform_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindParentPlatformDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UnbindParentPlatformDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindParentPlatformDeviceResponseBody, self).to_map()
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


class UnbindParentPlatformDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindParentPlatformDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindParentPlatformDeviceResponse, self).to_map()
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
            temp_model = UnbindParentPlatformDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPurchasedDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindPurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UnbindPurchasedDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindPurchasedDeviceResponseBody, self).to_map()
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


class UnbindPurchasedDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindPurchasedDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindPurchasedDeviceResponse, self).to_map()
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
            temp_model = UnbindPurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindTemplateRequest(TeaModel):
    def __init__(self, owner_id=None, template_id=None, template_type=None, instance_id=None, instance_type=None):
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class UnbindTemplateResponseBody(TeaModel):
    def __init__(self, template_type=None, instance_id=None, request_id=None, instance_type=None, template_id=None):
        self.template_type = template_type  # type: str
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UnbindTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindTemplateResponse, self).to_map()
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
            temp_model = UnbindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockDeviceRequest(TeaModel):
    def __init__(self, owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UnlockDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnlockDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnlockDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockDeviceResponse, self).to_map()
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
            temp_model = UnlockDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBucketInfoRequest(TeaModel):
    def __init__(self, owner_id=None, bucket_name=None, comment=None):
        self.owner_id = owner_id  # type: long
        self.bucket_name = bucket_name  # type: str
        self.comment = comment  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBucketInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class UpdateBucketInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBucketInfoResponseBody, self).to_map()
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


class UpdateBucketInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateBucketInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateBucketInfoResponse, self).to_map()
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
            temp_model = UpdateBucketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, app_name=None, stream_name=None, source_url=None,
                 start_time=None, end_time=None, always=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = domain_name  # type: str
        self.app_name = app_name  # type: str
        self.stream_name = stream_name  # type: str
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.always = always  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.always is not None:
            result['Always'] = self.always
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Always') is not None:
            self.always = m.get('Always')
        return self


class UpdateVsPullStreamInfoConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVsPullStreamInfoConfigResponseBody, self).to_map()
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


class UpdateVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateVsPullStreamInfoConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVsPullStreamInfoConfigResponse, self).to_map()
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
            temp_model = UpdateVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDeviceRecordRequest(TeaModel):
    def __init__(self, owner_id=None, device_id=None, stream_id=None, search_criteria=None, upload_type=None,
                 upload_id=None, upload_mode=None, upload_params=None):
        self.owner_id = owner_id  # type: long
        self.device_id = device_id  # type: str
        self.stream_id = stream_id  # type: str
        self.search_criteria = search_criteria  # type: str
        self.upload_type = upload_type  # type: str
        self.upload_id = upload_id  # type: str
        self.upload_mode = upload_mode  # type: str
        self.upload_params = upload_params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDeviceRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.search_criteria is not None:
            result['SearchCriteria'] = self.search_criteria
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        if self.upload_mode is not None:
            result['UploadMode'] = self.upload_mode
        if self.upload_params is not None:
            result['UploadParams'] = self.upload_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('SearchCriteria') is not None:
            self.search_criteria = m.get('SearchCriteria')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')
        if m.get('UploadParams') is not None:
            self.upload_params = m.get('UploadParams')
        return self


class UploadDeviceRecordResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDeviceRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadDeviceRecordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadDeviceRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadDeviceRecordResponse, self).to_map()
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
            temp_model = UploadDeviceRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


