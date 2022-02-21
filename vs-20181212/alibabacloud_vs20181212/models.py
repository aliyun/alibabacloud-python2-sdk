# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDeviceRequest(TeaModel):
    def __init__(self, config=None, group_id=None, owner_id=None, protocol=None):
        self.config = config  # type: str
        self.group_id = group_id  # type: str
        self.owner_id = owner_id  # type: long
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
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


class AddRegisteredDeviceRequest(TeaModel):
    def __init__(self, dsn=None, owner_id=None, register_code=None, secret_key=None, vendor=None):
        self.dsn = dsn  # type: str
        self.owner_id = owner_id  # type: long
        self.register_code = register_code  # type: str
        self.secret_key = secret_key  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRegisteredDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddRegisteredDeviceResponseBody(TeaModel):
    def __init__(self, dsn=None, id=None, register_code=None, request_id=None, secret_key=None, vendor=None):
        self.dsn = dsn  # type: str
        self.id = id  # type: str
        self.register_code = register_code  # type: str
        self.request_id = request_id  # type: str
        self.secret_key = secret_key  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRegisteredDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.id is not None:
            result['Id'] = self.id
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddRegisteredDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddRegisteredDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRegisteredDeviceResponse, self).to_map()
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
            temp_model = AddRegisteredDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRegisteredVendorRequest(TeaModel):
    def __init__(self, description=None, name=None, owner_id=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRegisteredVendorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class AddRegisteredVendorResponseBody(TeaModel):
    def __init__(self, description=None, name=None, request_id=None, vendor=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRegisteredVendorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddRegisteredVendorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddRegisteredVendorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRegisteredVendorResponse, self).to_map()
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
            temp_model = AddRegisteredVendorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRenderingDeviceInternetPortsRequest(TeaModel):
    def __init__(self, isp=None, instance_ids=None, internal_port=None, ip_protocol=None, owner_id=None):
        self.isp = isp  # type: str
        self.instance_ids = instance_ids  # type: str
        self.internal_port = internal_port  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRenderingDeviceInternetPortsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class AddRenderingDeviceInternetPortsResponseBody(TeaModel):
    def __init__(self, instance_ids=None, request_id=None):
        self.instance_ids = instance_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRenderingDeviceInternetPortsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddRenderingDeviceInternetPortsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddRenderingDeviceInternetPortsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRenderingDeviceInternetPortsResponse, self).to_map()
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
            temp_model = AddRenderingDeviceInternetPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, always=None, app_name=None, domain_name=None, end_time=None, owner_id=None, source_url=None,
                 start_time=None, stream_name=None):
        self.always = always  # type: str
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always is not None:
            result['Always'] = self.always
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Always') is not None:
            self.always = m.get('Always')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
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
    def __init__(self, device_id=None, directory_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.directory_id = directory_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchBindDirectoriesResponseBodyResults(TeaModel):
    def __init__(self, device_id=None, directory_id=None, error=None):
        self.device_id = device_id  # type: str
        self.directory_id = directory_id  # type: str
        self.error = error  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindDirectoriesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
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
    def __init__(self, device_id=None, owner_id=None, parent_platform_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindParentPlatformDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BatchBindParentPlatformDevicesResponseBodyResults(TeaModel):
    def __init__(self, device_id=None, error=None, parent_platform_id=None):
        self.device_id = device_id  # type: str
        self.error = error  # type: str
        self.parent_platform_id = parent_platform_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindParentPlatformDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
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
    def __init__(self, device_id=None, group_id=None, owner_id=None, region=None):
        self.device_id = device_id  # type: str
        self.group_id = group_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindPurchasedDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class BatchBindPurchasedDevicesResponseBodyResults(TeaModel):
    def __init__(self, device_id=None, error=None, group_id=None, region=None):
        self.device_id = device_id  # type: str
        self.error = error  # type: str
        self.group_id = group_id  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindPurchasedDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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
    def __init__(self, apply_all=None, instance_id=None, instance_type=None, owner_id=None, replace=None,
                 template_id=None):
        self.apply_all = apply_all  # type: bool
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.replace = replace  # type: bool
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
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
    def __init__(self, bindings=None, request_id=None):
        self.bindings = bindings  # type: list[BatchBindTemplateResponseBodyBindings]
        self.request_id = request_id  # type: str

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
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = BatchBindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, apply_all=None, instance_id=None, instance_type=None, owner_id=None, replace=None,
                 template_id=None, template_type=None):
        self.apply_all = apply_all  # type: bool
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.replace = replace  # type: bool
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchBindTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, domain_names=None, function_names=None, owner_id=None):
        self.domain_names = domain_names  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteVsDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, channel=None, control_stream_action=None, domain_name=None, live_stream_type=None,
                 oneshot=None, owner_id=None, resume_time=None):
        self.channel = channel  # type: str
        self.control_stream_action = control_stream_action  # type: str
        self.domain_name = domain_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.oneshot = oneshot  # type: str
        self.owner_id = owner_id  # type: long
        self.resume_time = resume_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchForbidVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, channels=None, count=None, detail=None, result=None):
        self.channels = channels  # type: BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels
        self.count = count  # type: int
        self.detail = detail  # type: str
        self.result = result  # type: str

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super(BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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
    def __init__(self, forbid_result=None, request_id=None):
        self.forbid_result = forbid_result  # type: BatchForbidVsStreamResponseBodyForbidResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.forbid_result:
            self.forbid_result.validate()

    def to_map(self):
        _map = super(BatchForbidVsStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forbid_result is not None:
            result['ForbidResult'] = self.forbid_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForbidResult') is not None:
            temp_model = BatchForbidVsStreamResponseBodyForbidResult()
            self.forbid_result = temp_model.from_map(m['ForbidResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, channel=None, control_stream_action=None, domain_name=None, live_stream_type=None,
                 owner_id=None):
        self.channel = channel  # type: str
        self.control_stream_action = control_stream_action  # type: str
        self.domain_name = domain_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchResumeVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, channels=None, count=None, detail=None, result=None):
        self.channels = channels  # type: BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels
        self.count = count  # type: int
        self.detail = detail  # type: str
        self.result = result  # type: str

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super(BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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
    def __init__(self, domain_names=None, functions=None, owner_id=None):
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetVsDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchStartDevicesResponseBodyResultsStreams(TeaModel):
    def __init__(self, error=None, id=None, name=None):
        self.error = error  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartDevicesResponseBodyResultsStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchStartStreamsResponseBodyResults(TeaModel):
    def __init__(self, error=None, id=None, name=None):
        self.error = error  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartStreamsResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, id=None, owner_id=None, start_time=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class BatchStopDevicesResponseBodyResultsStreams(TeaModel):
    def __init__(self, error=None, id=None, name=None):
        self.error = error  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopDevicesResponseBodyResultsStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, id=None, owner_id=None, start_time=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class BatchStopStreamsResponseBodyResults(TeaModel):
    def __init__(self, error=None, id=None, name=None):
        self.error = error  # type: str
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopStreamsResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, device_id=None, directory_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.directory_id = directory_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchUnbindDirectoriesResponseBodyResults(TeaModel):
    def __init__(self, device_id=None, directory_id=None, error=None):
        self.device_id = device_id  # type: str
        self.directory_id = directory_id  # type: str
        self.error = error  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindDirectoriesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
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
    def __init__(self, device_id=None, owner_id=None, parent_platform_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindParentPlatformDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BatchUnbindParentPlatformDevicesResponseBodyResults(TeaModel):
    def __init__(self, device_id=None, error=None, parent_platform_id=None):
        self.device_id = device_id  # type: str
        self.error = error  # type: str
        self.parent_platform_id = parent_platform_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindParentPlatformDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
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
    def __init__(self, device_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindPurchasedDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchUnbindPurchasedDevicesResponseBodyResults(TeaModel):
    def __init__(self, device_id=None, error=None):
        self.device_id = device_id  # type: str
        self.error = error  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindPurchasedDevicesResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
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
    def __init__(self, instance_id=None, instance_type=None, owner_id=None, template_id=None, template_type=None):
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
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
    def __init__(self, bindings=None, request_id=None):
        self.bindings = bindings  # type: list[BatchUnbindTemplateResponseBodyBindings]
        self.request_id = request_id  # type: str

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
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = BatchUnbindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, instance_id=None, instance_type=None, owner_id=None, template_id=None, template_type=None):
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BatchUnbindTemplatesResponseBodyResults(TeaModel):
    def __init__(self, error=None, instance_id=None, instance_type=None, template_id=None, template_type=None):
        self.error = error  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUnbindTemplatesResponseBodyResults, self).to_map()
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
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
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
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
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
    def __init__(self, device_id=None, directory_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.directory_id = directory_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, device_id=None, owner_id=None, parent_platform_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindParentPlatformDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
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
    def __init__(self, device_id=None, group_id=None, owner_id=None, region=None):
        self.device_id = device_id  # type: str
        self.group_id = group_id  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindPurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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
    def __init__(self, apply_all=None, instance_id=None, instance_type=None, owner_id=None, replace=None,
                 template_id=None, template_type=None):
        self.apply_all = apply_all  # type: bool
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.replace = replace  # type: bool
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BindTemplateResponseBody(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, request_id=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class CaptureDeviceSnapshotRequest(TeaModel):
    def __init__(self, device_id=None, mode=None, owner_id=None, snapshot_config=None, stream_id=None):
        self.device_id = device_id  # type: str
        self.mode = mode  # type: str
        self.owner_id = owner_id  # type: long
        self.snapshot_config = snapshot_config  # type: str
        self.stream_id = stream_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CaptureDeviceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SnapshotConfig') is not None:
            self.snapshot_config = m.get('SnapshotConfig')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class CaptureDeviceSnapshotResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CaptureDeviceSnapshotResponseBody, self).to_map()
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


class CaptureDeviceSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CaptureDeviceSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CaptureDeviceSnapshotResponse, self).to_map()
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
            temp_model = CaptureDeviceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinuousAdjustRequest(TeaModel):
    def __init__(self, focus=None, id=None, iris=None, owner_id=None):
        self.focus = focus  # type: str
        self.id = id  # type: str
        self.iris = iris  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinuousAdjustRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.focus is not None:
            result['Focus'] = self.focus
        if self.id is not None:
            result['Id'] = self.id
        if self.iris is not None:
            result['Iris'] = self.iris
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Iris') is not None:
            self.iris = m.get('Iris')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None, pan=None, tilt=None, zoom=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.pan = pan  # type: str
        self.tilt = tilt  # type: str
        self.zoom = zoom  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ContinuousMoveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pan is not None:
            result['Pan'] = self.pan
        if self.tilt is not None:
            result['Tilt'] = self.tilt
        if self.zoom is not None:
            result['Zoom'] = self.zoom
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Pan') is not None:
            self.pan = m.get('Pan')
        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')
        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')
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


class CreateAIConfigRequest(TeaModel):
    def __init__(self, capture_interval=None, configs=None, description=None, end_time=None, features=None,
                 instance_id=None, instance_type=None, owner_id=None, start_time=None, status=None):
        self.capture_interval = capture_interval  # type: int
        self.configs = configs  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.features = features  # type: str
        self.instance_id = instance_id  # type: long
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAIConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAIConfigResponseBody(TeaModel):
    def __init__(self, config_id=None, request_id=None):
        self.config_id = config_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAIConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAIConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAIConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAIConfigResponse, self).to_map()
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
            temp_model = CreateAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, description=None, internal_ports=None, maintain_time=None, name=None, owner_id=None,
                 security_group_id=None):
        self.description = description  # type: str
        self.internal_ports = internal_ports  # type: str
        self.maintain_time = maintain_time  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.internal_ports is not None:
            result['InternalPorts'] = self.internal_ports
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InternalPorts') is not None:
            self.internal_ports = m.get('InternalPorts')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(self, alarm_method=None, auto_pos=None, auto_start=None, description=None, directory_id=None,
                 dsn=None, gb_id=None, group_id=None, ip=None, latitude=None, longitude=None, name=None, owner_id=None,
                 params=None, parent_id=None, password=None, port=None, pos_interval=None, type=None, url=None,
                 username=None, vendor=None):
        self.alarm_method = alarm_method  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.auto_start = auto_start  # type: bool
        self.description = description  # type: str
        self.directory_id = directory_id  # type: str
        self.dsn = dsn  # type: str
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.ip = ip  # type: str
        self.latitude = latitude  # type: str
        self.longitude = longitude  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.params = params  # type: str
        self.parent_id = parent_id  # type: str
        self.password = password  # type: str
        self.port = port  # type: long
        self.pos_interval = pos_interval  # type: long
        self.type = type  # type: str
        self.url = url  # type: str
        self.username = username  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
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
    def __init__(self, alarm=None, channel_id=None, end_time=None, expire=None, id=None, object_type=None,
                 owner_id=None, start_time=None, sub_alarm=None):
        self.alarm = alarm  # type: int
        self.channel_id = channel_id  # type: int
        self.end_time = end_time  # type: long
        self.expire = expire  # type: long
        self.id = id  # type: str
        self.object_type = object_type  # type: int
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long
        self.sub_alarm = sub_alarm  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm is not None:
            result['Alarm'] = self.alarm
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_alarm is not None:
            result['SubAlarm'] = self.sub_alarm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alarm') is not None:
            self.alarm = m.get('Alarm')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubAlarm') is not None:
            self.sub_alarm = m.get('SubAlarm')
        return self


class CreateDeviceAlarmResponseBody(TeaModel):
    def __init__(self, alarm_delay=None, alarm_id=None, expire=None, request_id=None, url=None):
        self.alarm_delay = alarm_delay  # type: long
        self.alarm_id = alarm_id  # type: str
        self.expire = expire  # type: long
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceAlarmResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_delay is not None:
            result['AlarmDelay'] = self.alarm_delay
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmDelay') is not None:
            self.alarm_delay = m.get('AlarmDelay')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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
    def __init__(self, device_id=None, mode=None, owner_id=None, snapshot_config=None, stream_id=None):
        self.device_id = device_id  # type: str
        self.mode = mode  # type: str
        self.owner_id = owner_id  # type: long
        self.snapshot_config = snapshot_config  # type: str
        self.stream_id = stream_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDeviceSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SnapshotConfig') is not None:
            self.snapshot_config = m.get('SnapshotConfig')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
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
    def __init__(self, description=None, group_id=None, name=None, owner_id=None, parent_id=None):
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, app=None, callback=None, description=None, in_protocol=None, lazy_pull=None, name=None,
                 out_protocol=None, owner_id=None, play_domain=None, push_domain=None, region=None):
        self.app = app  # type: str
        self.callback = callback  # type: str
        self.description = description  # type: str
        self.in_protocol = in_protocol  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.name = name  # type: str
        self.out_protocol = out_protocol  # type: str
        self.owner_id = owner_id  # type: long
        self.play_domain = play_domain  # type: str
        self.push_domain = push_domain  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(self, gb_id=None, gb_ip=None, gb_port=None, id=None, request_id=None):
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.gb_port = gb_port  # type: long
        self.id = id  # type: str
        self.request_id = request_id  # type: str

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
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, auto_start=None, client_auth=None, client_password=None, client_username=None,
                 description=None, gb_id=None, ip=None, name=None, owner_id=None, port=None, protocol=None):
        self.auto_start = auto_start  # type: bool
        self.client_auth = client_auth  # type: bool
        self.client_password = client_password  # type: str
        self.client_username = client_username  # type: str
        self.description = description  # type: str
        self.gb_id = gb_id  # type: str
        self.ip = ip  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.port = port  # type: long
        self.protocol = protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
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


class CreateRenderingDeviceRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, cluster_id=None, count=None, description=None,
                 edge_node_name=None, isp=None, image_id=None, instance_charge_type=None, instance_name=None, owner_id=None,
                 password=None, period=None, period_unit=None, security_group_id=None, specification=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.cluster_id = cluster_id  # type: str
        self.count = count  # type: int
        self.description = description  # type: str
        self.edge_node_name = edge_node_name  # type: str
        self.isp = isp  # type: str
        self.image_id = image_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.instance_name = instance_name  # type: str
        self.owner_id = owner_id  # type: long
        self.password = password  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.security_group_id = security_group_id  # type: str
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRenderingDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.count is not None:
            result['Count'] = self.count
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class CreateRenderingDeviceResponseBody(TeaModel):
    def __init__(self, instance_ids=None, request_id=None):
        self.instance_ids = instance_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRenderingDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRenderingDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRenderingDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRenderingDeviceResponse, self).to_map()
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
            temp_model = CreateRenderingDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamSnapshotRequest(TeaModel):
    def __init__(self, id=None, location=None, owner_id=None):
        self.id = id  # type: str
        self.location = location  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateStreamSnapshotResponseBody(TeaModel):
    def __init__(self, format=None, height=None, id=None, oss_bucket=None, oss_endpoint=None, oss_object=None,
                 request_id=None, timestamp=None, url=None, width=None):
        self.format = format  # type: str
        self.height = height  # type: long
        self.id = id  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object  # type: str
        self.request_id = request_id  # type: str
        self.timestamp = timestamp  # type: long
        self.url = url  # type: str
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
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
    def __init__(self, callback=None, description=None, file_format=None, flv=None, hls_m3u_8=None, hls_ts=None,
                 interval=None, jpg_on_demand=None, jpg_overwrite=None, jpg_sequence=None, mp_4=None, name=None,
                 oss_bucket=None, oss_endpoint=None, oss_file_prefix=None, owner_id=None, region=None, retention=None,
                 trans_configs_json=None, trigger=None, type=None):
        self.callback = callback  # type: str
        self.description = description  # type: str
        self.file_format = file_format  # type: str
        self.flv = flv  # type: str
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.hls_ts = hls_ts  # type: str
        self.interval = interval  # type: long
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.mp_4 = mp_4  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.retention = retention  # type: long
        self.trans_configs_json = trans_configs_json  # type: str
        self.trigger = trigger  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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


class DeleteAIConfigRequest(TeaModel):
    def __init__(self, config_id=None, owner_id=None):
        self.config_id = config_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAIConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteAIConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAIConfigResponseBody, self).to_map()
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


class DeleteAIConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAIConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAIConfigResponse, self).to_map()
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
            temp_model = DeleteAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBucketRequest(TeaModel):
    def __init__(self, bucket_name=None, owner_id=None):
        self.bucket_name = bucket_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, owner_id=None):
        self.cluster_id = cluster_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
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


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterResponse, self).to_map()
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None, preset_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.preset_id = preset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePresetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
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


class DeletePurchasedDeviceRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeletePurchasedDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePurchasedDeviceResponseBody, self).to_map()
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


class DeletePurchasedDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePurchasedDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePurchasedDeviceResponse, self).to_map()
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
            temp_model = DeletePurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRenderingDeviceInternetPortsRequest(TeaModel):
    def __init__(self, isp=None, instance_ids=None, internal_port=None, ip_protocol=None, owner_id=None):
        self.isp = isp  # type: str
        self.instance_ids = instance_ids  # type: str
        self.internal_port = internal_port  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRenderingDeviceInternetPortsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_ids=None):
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        return self


class DeleteRenderingDeviceInternetPortsResponseBody(TeaModel):
    def __init__(self, instance_ids=None, request_id=None):
        self.instance_ids = instance_ids  # type: DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(DeleteRenderingDeviceInternetPortsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRenderingDeviceInternetPortsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRenderingDeviceInternetPortsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRenderingDeviceInternetPortsResponse, self).to_map()
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
            temp_model = DeleteRenderingDeviceInternetPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRenderingDevicesRequest(TeaModel):
    def __init__(self, instance_ids=None, owner_id=None):
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRenderingDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRenderingDevicesResponseBody(TeaModel):
    def __init__(self, failed_ids=None, request_id=None):
        self.failed_ids = failed_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRenderingDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRenderingDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRenderingDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRenderingDevicesResponse, self).to_map()
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
            temp_model = DeleteRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, app_name=None, domain_name=None, owner_id=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVsStreamsNotifyUrlConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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


class DescribeAIConfigRequest(TeaModel):
    def __init__(self, config_id=None, owner_id=None):
        self.config_id = config_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAIConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAIConfigResponseBodyAIConfig(TeaModel):
    def __init__(self, capture_interval=None, configs=None, description=None, end_time=None, features=None,
                 instance_id=None, instance_type=None, start_time=None, status=None):
        self.capture_interval = capture_interval  # type: int
        self.configs = configs  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.features = features  # type: str
        self.instance_id = instance_id  # type: long
        self.instance_type = instance_type  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAIConfigResponseBodyAIConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAIConfigResponseBody(TeaModel):
    def __init__(self, aiconfig=None, request_id=None):
        self.aiconfig = aiconfig  # type: DescribeAIConfigResponseBodyAIConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aiconfig:
            self.aiconfig.validate()

    def to_map(self):
        _map = super(DescribeAIConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiconfig is not None:
            result['AIConfig'] = self.aiconfig.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIConfig') is not None:
            temp_model = DescribeAIConfigResponseBodyAIConfig()
            self.aiconfig = temp_model.from_map(m['AIConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAIConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAIConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAIConfigResponse, self).to_map()
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
            temp_model = DescribeAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAIConfigListRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAIConfigListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAIConfigListResponseBodyAIConfigListAIConfigList(TeaModel):
    def __init__(self, capture_interval=None, config_id=None, configs=None, description=None, end_time=None,
                 features=None, instance_id=None, instance_type=None, start_time=None, status=None):
        self.capture_interval = capture_interval  # type: int
        self.config_id = config_id  # type: str
        self.configs = configs  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.features = features  # type: str
        self.instance_id = instance_id  # type: long
        self.instance_type = instance_type  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAIConfigListResponseBodyAIConfigListAIConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAIConfigListResponseBodyAIConfigList(TeaModel):
    def __init__(self, aiconfig_list=None):
        self.aiconfig_list = aiconfig_list  # type: list[DescribeAIConfigListResponseBodyAIConfigListAIConfigList]

    def validate(self):
        if self.aiconfig_list:
            for k in self.aiconfig_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAIConfigListResponseBodyAIConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AIConfigList'] = []
        if self.aiconfig_list is not None:
            for k in self.aiconfig_list:
                result['AIConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aiconfig_list = []
        if m.get('AIConfigList') is not None:
            for k in m.get('AIConfigList'):
                temp_model = DescribeAIConfigListResponseBodyAIConfigListAIConfigList()
                self.aiconfig_list.append(temp_model.from_map(k))
        return self


class DescribeAIConfigListResponseBody(TeaModel):
    def __init__(self, aiconfig_list=None, request_id=None):
        self.aiconfig_list = aiconfig_list  # type: DescribeAIConfigListResponseBodyAIConfigList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aiconfig_list:
            self.aiconfig_list.validate()

    def to_map(self):
        _map = super(DescribeAIConfigListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiconfig_list is not None:
            result['AIConfigList'] = self.aiconfig_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIConfigList') is not None:
            temp_model = DescribeAIConfigListResponseBodyAIConfigList()
            self.aiconfig_list = temp_model.from_map(m['AIConfigList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAIConfigListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAIConfigListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAIConfigListResponse, self).to_map()
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
            temp_model = DescribeAIConfigListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAIEventListRequest(TeaModel):
    def __init__(self, end_time=None, feature=None, instance_id=None, instance_type=None, owner_id=None,
                 start_time=None, triggered=None):
        self.end_time = end_time  # type: long
        self.feature = feature  # type: str
        self.instance_id = instance_id  # type: long
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long
        self.triggered = triggered  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAIEventListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.triggered is not None:
            result['Triggered'] = self.triggered
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Triggered') is not None:
            self.triggered = m.get('Triggered')
        return self


class DescribeAIEventListResponseBody(TeaModel):
    def __init__(self, aievent_list=None, request_id=None):
        self.aievent_list = aievent_list  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAIEventListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aievent_list is not None:
            result['AIEventList'] = self.aievent_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIEventList') is not None:
            self.aievent_list = m.get('AIEventList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAIEventListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAIEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAIEventListResponse, self).to_map()
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
            temp_model = DescribeAIEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountStatRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAccountStatResponseBody(TeaModel):
    def __init__(self, group_limit=None, group_num=None, id=None, request_id=None, template_limit=None,
                 template_num=None):
        self.group_limit = group_limit  # type: long
        self.group_num = group_num  # type: long
        self.id = id  # type: str
        self.request_id = request_id  # type: str
        self.template_limit = template_limit  # type: long
        self.template_num = template_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_limit is not None:
            result['GroupLimit'] = self.group_limit
        if self.group_num is not None:
            result['GroupNum'] = self.group_num
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_limit is not None:
            result['TemplateLimit'] = self.template_limit
        if self.template_num is not None:
            result['TemplateNum'] = self.template_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupLimit') is not None:
            self.group_limit = m.get('GroupLimit')
        if m.get('GroupNum') is not None:
            self.group_num = m.get('GroupNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateLimit') is not None:
            self.template_limit = m.get('TemplateLimit')
        if m.get('TemplateNum') is not None:
            self.template_num = m.get('TemplateNum')
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


class DescribeClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, owner_id=None):
        self.cluster_id = cluster_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeClusterResponseBodyInternalPorts(TeaModel):
    def __init__(self, ip_protocol=None, platform=None, port=None):
        self.ip_protocol = ip_protocol  # type: str
        self.platform = platform  # type: str
        self.port = port  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyInternalPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, description=None, internal_ports=None, maintain_time=None, name=None,
                 request_id=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.internal_ports = internal_ports  # type: list[DescribeClusterResponseBodyInternalPorts]
        self.maintain_time = maintain_time  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.internal_ports:
            for k in self.internal_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        result['InternalPorts'] = []
        if self.internal_ports is not None:
            for k in self.internal_ports:
                result['InternalPorts'].append(k.to_map() if k else None)
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.internal_ports = []
        if m.get('InternalPorts') is not None:
            for k in m.get('InternalPorts'):
                temp_model = DescribeClusterResponseBodyInternalPorts()
                self.internal_ports.append(temp_model.from_map(k))
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterResponse, self).to_map()
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
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterDevicesRequest(TeaModel):
    def __init__(self, cluster_id=None, description=None, edge_node_name=None, owner_id=None, page_no=None,
                 page_size=None, platform=None, specification=None):
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.edge_node_name = edge_node_name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.platform = platform  # type: str
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class DescribeClusterDevicesResponseBodyDevicesIpInfos(TeaModel):
    def __init__(self, external_ip=None, external_port=None, isp=None, internal_ip=None, internal_port=None,
                 ip_protocol=None, nat_type=None):
        self.external_ip = external_ip  # type: str
        self.external_port = external_port  # type: str
        self.isp = isp  # type: str
        self.internal_ip = internal_ip  # type: str
        self.internal_port = internal_port  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.nat_type = nat_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDevicesResponseBodyDevicesIpInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        return self


class DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork(TeaModel):
    def __init__(self, container_ports=None, external_ip=None, external_ports=None):
        self.container_ports = container_ports  # type: str
        self.external_ip = external_ip  # type: str
        self.external_ports = external_ports  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_ports is not None:
            result['ContainerPorts'] = self.container_ports
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_ports is not None:
            result['ExternalPorts'] = self.external_ports
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerPorts') is not None:
            self.container_ports = m.get('ContainerPorts')
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPorts') is not None:
            self.external_ports = m.get('ExternalPorts')
        return self


class DescribeClusterDevicesResponseBodyDevicesPodInfos(TeaModel):
    def __init__(self, network=None, pod_id=None, status=None):
        self.network = network  # type: list[DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork]
        self.pod_id = pod_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDevicesResponseBodyDevicesPodInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Network'] = []
        if self.network is not None:
            for k in self.network:
                result['Network'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network = []
        if m.get('Network') is not None:
            for k in m.get('Network'):
                temp_model = DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork()
                self.network.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterDevicesResponseBodyDevices(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, description=None, edge_node_name=None,
                 image_id=None, instance_charge_type=None, instance_id=None, instance_name=None, ip_infos=None,
                 mac_address=None, period=None, period_unit=None, platform_type=None, pod_infos=None, server=None, status=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.description = description  # type: str
        self.edge_node_name = edge_node_name  # type: str
        self.image_id = image_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.ip_infos = ip_infos  # type: list[DescribeClusterDevicesResponseBodyDevicesIpInfos]
        self.mac_address = mac_address  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.platform_type = platform_type  # type: str
        self.pod_infos = pod_infos  # type: list[DescribeClusterDevicesResponseBodyDevicesPodInfos]
        self.server = server  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.ip_infos:
            for k in self.ip_infos:
                if k:
                    k.validate()
        if self.pod_infos:
            for k in self.pod_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['IpInfos'] = []
        if self.ip_infos is not None:
            for k in self.ip_infos:
                result['IpInfos'].append(k.to_map() if k else None)
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        result['PodInfos'] = []
        if self.pod_infos is not None:
            for k in self.pod_infos:
                result['PodInfos'].append(k.to_map() if k else None)
        if self.server is not None:
            result['Server'] = self.server
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.ip_infos = []
        if m.get('IpInfos') is not None:
            for k in m.get('IpInfos'):
                temp_model = DescribeClusterDevicesResponseBodyDevicesIpInfos()
                self.ip_infos.append(temp_model.from_map(k))
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        self.pod_infos = []
        if m.get('PodInfos') is not None:
            for k in m.get('PodInfos'):
                temp_model = DescribeClusterDevicesResponseBodyDevicesPodInfos()
                self.pod_infos.append(temp_model.from_map(k))
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterDevicesResponseBody(TeaModel):
    def __init__(self, devices=None, request_id=None, total=None):
        self.devices = devices  # type: list[DescribeClusterDevicesResponseBodyDevices]
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeClusterDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeClusterDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterDevicesResponse, self).to_map()
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
            temp_model = DescribeClusterDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeClustersResponseBodyClustersInternalPorts(TeaModel):
    def __init__(self, ip_protocol=None, platform=None, port=None):
        self.ip_protocol = ip_protocol  # type: str
        self.platform = platform  # type: str
        self.port = port  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersResponseBodyClustersInternalPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster_id=None, description=None, internal_ports=None, maintain_time=None, name=None,
                 status=None):
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.internal_ports = internal_ports  # type: list[DescribeClustersResponseBodyClustersInternalPorts]
        self.maintain_time = maintain_time  # type: str
        self.name = name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.internal_ports:
            for k in self.internal_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        result['InternalPorts'] = []
        if self.internal_ports is not None:
            for k in self.internal_ports:
                result['InternalPorts'].append(k.to_map() if k else None)
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.internal_ports = []
        if m.get('InternalPorts') is not None:
            for k in m.get('InternalPorts'):
                temp_model = DescribeClustersResponseBodyClustersInternalPorts()
                self.internal_ports.append(temp_model.from_map(k))
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None, total=None):
        self.clusters = clusters  # type: list[DescribeClustersResponseBodyClusters]
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClustersResponse, self).to_map()
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
            temp_model = DescribeClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerInstanceIdRequest(TeaModel):
    def __init__(self, node_name=None, owner_id=None, pod_index=None):
        self.node_name = node_name  # type: str
        self.owner_id = owner_id  # type: long
        self.pod_index = pod_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerInstanceIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pod_index is not None:
            result['PodIndex'] = self.pod_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PodIndex') is not None:
            self.pod_index = m.get('PodIndex')
        return self


class DescribeContainerInstanceIdResponseBodyInstanceDetail(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerInstanceIdResponseBodyInstanceDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeContainerInstanceIdResponseBody(TeaModel):
    def __init__(self, instance_detail=None, request_id=None):
        self.instance_detail = instance_detail  # type: DescribeContainerInstanceIdResponseBodyInstanceDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_detail:
            self.instance_detail.validate()

    def to_map(self):
        _map = super(DescribeContainerInstanceIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_detail is not None:
            result['InstanceDetail'] = self.instance_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceDetail') is not None:
            temp_model = DescribeContainerInstanceIdResponseBodyInstanceDetail()
            self.instance_detail = temp_model.from_map(m['InstanceDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerInstanceIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeContainerInstanceIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerInstanceIdResponse, self).to_map()
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
            temp_model = DescribeContainerInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceRequest(TeaModel):
    def __init__(self, id=None, include_directory=None, include_stats=None, owner_id=None):
        self.id = id  # type: str
        self.include_directory = include_directory  # type: bool
        self.include_stats = include_stats  # type: bool
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDeviceResponseBodyDirectory(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, id=None, name=None, parent_id=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceResponseBodyDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeDeviceResponseBodyStats(TeaModel):
    def __init__(self, channel_num=None, failed_num=None, offline_num=None, online_num=None, stream_num=None):
        self.channel_num = channel_num  # type: long
        self.failed_num = failed_num  # type: long
        self.offline_num = offline_num  # type: long
        self.online_num = online_num  # type: long
        self.stream_num = stream_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceResponseBodyStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        return self


class DescribeDeviceResponseBody(TeaModel):
    def __init__(self, alarm_method=None, auto_pos=None, auto_start=None, channel_sync_time=None, created_time=None,
                 description=None, directory=None, directory_id=None, dsn=None, enabled=None, gb_id=None, group_id=None, id=None,
                 ip=None, latitude=None, longitude=None, name=None, params=None, parent_id=None, password=None,
                 port=None, pos_interval=None, protocol=None, registered_time=None, request_id=None, stats=None,
                 status=None, type=None, url=None, username=None, vendor=None):
        self.alarm_method = alarm_method  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.auto_start = auto_start  # type: bool
        self.channel_sync_time = channel_sync_time  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.directory = directory  # type: DescribeDeviceResponseBodyDirectory
        self.directory_id = directory_id  # type: str
        self.dsn = dsn  # type: str
        self.enabled = enabled  # type: bool
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.ip = ip  # type: str
        self.latitude = latitude  # type: str
        self.longitude = longitude  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.parent_id = parent_id  # type: str
        self.password = password  # type: str
        self.port = port  # type: long
        self.pos_interval = pos_interval  # type: long
        self.protocol = protocol  # type: str
        self.registered_time = registered_time  # type: str
        self.request_id = request_id  # type: str
        self.stats = stats  # type: DescribeDeviceResponseBodyStats
        self.status = status  # type: str
        self.type = type  # type: str
        self.url = url  # type: str
        self.username = username  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super(DescribeDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = DescribeDeviceResponseBodyDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stats') is not None:
            temp_model = DescribeDeviceResponseBodyStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
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
    def __init__(self, id=None, owner_id=None, page_num=None, page_size=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDeviceChannelsResponseBodyChannels(TeaModel):
    def __init__(self, channel_id=None, device_id=None, device_status=None, gb_id=None, name=None, params=None,
                 stream_id=None, stream_status=None):
        self.channel_id = channel_id  # type: long
        self.device_id = device_id  # type: str
        self.device_status = device_status  # type: str
        self.gb_id = gb_id  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.stream_id = stream_id  # type: str
        self.stream_status = stream_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceChannelsResponseBodyChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class DescribeDeviceChannelsResponseBody(TeaModel):
    def __init__(self, channels=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.channels = channels  # type: list[DescribeDeviceChannelsResponseBodyChannels]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = DescribeDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, client_ip=None, expire=None, id=None, owner_id=None):
        self.client_ip = client_ip  # type: str
        self.expire = expire  # type: long
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceGatewayRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDeviceGatewayResponseBody(TeaModel):
    def __init__(self, host=None, port=None, protocol=None, request_id=None, token=None):
        self.host = host  # type: str
        self.port = port  # type: long
        self.protocol = protocol  # type: str
        self.request_id = request_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceGatewayResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
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


class DescribeDeviceURLRequest(TeaModel):
    def __init__(self, auth=None, expire=None, id=None, mode=None, out_protocol=None, owner_id=None, stream=None,
                 type=None):
        self.auth = auth  # type: bool
        self.expire = expire  # type: long
        self.id = id  # type: str
        self.mode = mode  # type: str
        self.out_protocol = out_protocol  # type: str
        self.owner_id = owner_id  # type: long
        self.stream = stream  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDeviceURLResponseBody(TeaModel):
    def __init__(self, expire_time=None, request_id=None, url=None):
        self.expire_time = expire_time  # type: long
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeviceURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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


class DescribeDevicesRequest(TeaModel):
    def __init__(self, directory_id=None, dsn=None, gb_id=None, group_id=None, id=None, include_directory=None,
                 include_stats=None, name=None, owner_id=None, page_num=None, page_size=None, parent_id=None, sort_by=None,
                 sort_direction=None, status=None, type=None, vendor=None):
        self.directory_id = directory_id  # type: str
        self.dsn = dsn  # type: str
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.include_directory = include_directory  # type: bool
        self.include_stats = include_stats  # type: bool
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.parent_id = parent_id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.status = status  # type: str
        self.type = type  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeDevicesResponseBodyDevicesDirectory(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, id=None, name=None, parent_id=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyDevicesDirectory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeDevicesResponseBodyDevicesStats(TeaModel):
    def __init__(self, channel_num=None, failed_num=None, offline_num=None, online_num=None, stream_num=None):
        self.channel_num = channel_num  # type: long
        self.failed_num = failed_num  # type: long
        self.offline_num = offline_num  # type: long
        self.online_num = online_num  # type: long
        self.stream_num = stream_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyDevicesStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        return self


class DescribeDevicesResponseBodyDevices(TeaModel):
    def __init__(self, alarm_method=None, auto_directory=None, auto_pos=None, auto_start=None,
                 channel_sync_time=None, created_time=None, description=None, directory=None, directory_id=None, dsn=None,
                 enabled=None, gb_id=None, group_id=None, id=None, ip=None, latitude=None, longitude=None, name=None,
                 params=None, parent_id=None, password=None, port=None, pos_interval=None, protocol=None,
                 registered_time=None, stats=None, status=None, type=None, url=None, username=None, vendor=None):
        self.alarm_method = alarm_method  # type: str
        self.auto_directory = auto_directory  # type: bool
        self.auto_pos = auto_pos  # type: bool
        self.auto_start = auto_start  # type: bool
        self.channel_sync_time = channel_sync_time  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.directory = directory  # type: DescribeDevicesResponseBodyDevicesDirectory
        self.directory_id = directory_id  # type: str
        self.dsn = dsn  # type: str
        self.enabled = enabled  # type: bool
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.ip = ip  # type: str
        self.latitude = latitude  # type: str
        self.longitude = longitude  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.parent_id = parent_id  # type: str
        self.password = password  # type: str
        self.port = port  # type: long
        self.pos_interval = pos_interval  # type: long
        self.protocol = protocol  # type: str
        self.registered_time = registered_time  # type: str
        self.stats = stats  # type: DescribeDevicesResponseBodyDevicesStats
        self.status = status  # type: str
        self.type = type  # type: str
        self.url = url  # type: str
        self.username = username  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        if self.directory:
            self.directory.validate()
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super(DescribeDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_directory is not None:
            result['AutoDirectory'] = self.auto_directory
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoDirectory') is not None:
            self.auto_directory = m.get('AutoDirectory')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = DescribeDevicesResponseBodyDevicesDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')
        if m.get('Stats') is not None:
            temp_model = DescribeDevicesResponseBodyDevicesStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeDevicesResponseBody(TeaModel):
    def __init__(self, devices=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.devices = devices  # type: list[DescribeDevicesResponseBodyDevices]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, group_id=None, no_pagination=None, owner_id=None, page_num=None, page_size=None,
                 parent_id=None, sort_by=None, sort_direction=None):
        self.group_id = group_id  # type: str
        self.no_pagination = no_pagination  # type: bool
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.parent_id = parent_id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.no_pagination is not None:
            result['NoPagination'] = self.no_pagination
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NoPagination') is not None:
            self.no_pagination = m.get('NoPagination')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, id=None, name=None, parent_id=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBodyDirectories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(self, directories=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.directories = directories  # type: list[DescribeDirectoriesResponseBodyDirectories]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDirectoryResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, id=None, name=None, parent_id=None,
                 request_id=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeExternalStreamURLRequest(TeaModel):
    def __init__(self, kind=None, owner_id=None, profile=None, tx_id=None, url=None):
        self.kind = kind  # type: str
        self.owner_id = owner_id  # type: long
        self.profile = profile  # type: str
        self.tx_id = tx_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExternalStreamURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeExternalStreamURLResponseBody(TeaModel):
    def __init__(self, ip=None, out_protocol=None, port=None, profile=None, request_id=None, tx_id=None, url=None):
        self.ip = ip  # type: str
        self.out_protocol = out_protocol  # type: str
        self.port = port  # type: long
        self.profile = profile  # type: str
        self.request_id = request_id  # type: str
        self.tx_id = tx_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExternalStreamURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.port is not None:
            result['Port'] = self.port
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeExternalStreamURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeExternalStreamURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExternalStreamURLResponse, self).to_map()
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
            temp_model = DescribeExternalStreamURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupRequest(TeaModel):
    def __init__(self, id=None, include_stats=None, owner_id=None):
        self.id = id  # type: str
        self.include_stats = include_stats  # type: bool
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeGroupResponseBodyStats(TeaModel):
    def __init__(self, device_num=None, ied_num=None, ipc_num=None, platform_num=None):
        self.device_num = device_num  # type: long
        self.ied_num = ied_num  # type: long
        self.ipc_num = ipc_num  # type: long
        self.platform_num = platform_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupResponseBodyStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.ied_num is not None:
            result['IedNum'] = self.ied_num
        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num
        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')
        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')
        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')
        return self


class DescribeGroupResponseBody(TeaModel):
    def __init__(self, alias_id=None, app=None, callback=None, created_time=None, description=None, enabled=None,
                 gb_id=None, gb_ip=None, gb_port=None, gb_tcp_ports=None, gb_udp_ports=None, id=None, in_protocol=None,
                 lazy_pull=None, name=None, out_protocol=None, play_domain=None, push_domain=None, region=None,
                 request_id=None, stats=None, status=None):
        self.alias_id = alias_id  # type: str
        self.app = app  # type: str
        self.callback = callback  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.enabled = enabled  # type: bool
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.gb_port = gb_port  # type: long
        self.gb_tcp_ports = gb_tcp_ports  # type: list[str]
        self.gb_udp_ports = gb_udp_ports  # type: list[str]
        self.id = id  # type: str
        self.in_protocol = in_protocol  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.name = name  # type: str
        self.out_protocol = out_protocol  # type: str
        self.play_domain = play_domain  # type: str
        self.push_domain = push_domain  # type: str
        self.region = region  # type: str
        self.request_id = request_id  # type: str
        self.stats = stats  # type: DescribeGroupResponseBodyStats
        self.status = status  # type: str

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super(DescribeGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id
        if self.app is not None:
            result['App'] = self.app
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports
        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')
        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stats') is not None:
            temp_model = DescribeGroupResponseBodyStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, id=None, in_protocol=None, include_stats=None, name=None, owner_id=None, page_num=None,
                 page_size=None, region=None, sort_by=None, sort_direction=None, status=None):
        self.id = id  # type: str
        self.in_protocol = in_protocol  # type: str
        self.include_stats = include_stats  # type: bool
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.region = region  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGroupsResponseBodyGroupsStats(TeaModel):
    def __init__(self, device_num=None, ied_num=None, ipc_num=None, platform_num=None):
        self.device_num = device_num  # type: long
        self.ied_num = ied_num  # type: long
        self.ipc_num = ipc_num  # type: long
        self.platform_num = platform_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupsResponseBodyGroupsStats, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.ied_num is not None:
            result['IedNum'] = self.ied_num
        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num
        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')
        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')
        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')
        return self


class DescribeGroupsResponseBodyGroups(TeaModel):
    def __init__(self, alias_id=None, app=None, callback=None, created_time=None, description=None, enabled=None,
                 gb_id=None, gb_ip=None, gb_port=None, gb_tcp_ports=None, gb_udp_ports=None, id=None, in_protocol=None,
                 lazy_pull=None, name=None, out_protocol=None, play_domain=None, push_domain=None, region=None, stats=None,
                 status=None):
        self.alias_id = alias_id  # type: str
        self.app = app  # type: str
        self.callback = callback  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.enabled = enabled  # type: bool
        self.gb_id = gb_id  # type: str
        self.gb_ip = gb_ip  # type: str
        self.gb_port = gb_port  # type: long
        self.gb_tcp_ports = gb_tcp_ports  # type: list[str]
        self.gb_udp_ports = gb_udp_ports  # type: list[str]
        self.id = id  # type: str
        self.in_protocol = in_protocol  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.name = name  # type: str
        self.out_protocol = out_protocol  # type: str
        self.play_domain = play_domain  # type: str
        self.push_domain = push_domain  # type: str
        self.region = region  # type: str
        self.stats = stats  # type: DescribeGroupsResponseBodyGroupsStats
        self.status = status  # type: str

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super(DescribeGroupsResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id
        if self.app is not None:
            result['App'] = self.app
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports
        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')
        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Stats') is not None:
            temp_model = DescribeGroupsResponseBodyGroupsStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGroupsResponseBody(TeaModel):
    def __init__(self, groups=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.groups = groups  # type: list[DescribeGroupsResponseBodyGroups]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class DescribeNodeDevicesInfoRequest(TeaModel):
    def __init__(self, node_name=None, owner_id=None):
        self.node_name = node_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeDevicesInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos(TeaModel):
    def __init__(self, ip=None, instance_id=None, name=None, server=None):
        self.ip = ip  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.server = server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class DescribeNodeDevicesInfoResponseBodyNodeDevices(TeaModel):
    def __init__(self, device_infos=None, node_name=None):
        self.device_infos = device_infos  # type: list[DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos]
        self.node_name = node_name  # type: str

    def validate(self):
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNodeDevicesInfoResponseBodyNodeDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class DescribeNodeDevicesInfoResponseBody(TeaModel):
    def __init__(self, node_devices=None, request_id=None):
        self.node_devices = node_devices  # type: list[DescribeNodeDevicesInfoResponseBodyNodeDevices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.node_devices:
            for k in self.node_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNodeDevicesInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeDevices'] = []
        if self.node_devices is not None:
            for k in self.node_devices:
                result['NodeDevices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_devices = []
        if m.get('NodeDevices') is not None:
            for k in m.get('NodeDevices'):
                temp_model = DescribeNodeDevicesInfoResponseBodyNodeDevices()
                self.node_devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeDevicesInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeNodeDevicesInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeDevicesInfoResponse, self).to_map()
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
            temp_model = DescribeNodeDevicesInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeParentPlatformResponseBody(TeaModel):
    def __init__(self, auto_start=None, client_auth=None, client_gb_id=None, client_ip=None, client_password=None,
                 client_port=None, client_username=None, created_time=None, description=None, gb_id=None, id=None, ip=None,
                 name=None, port=None, protocol=None, request_id=None, status=None):
        self.auto_start = auto_start  # type: bool
        self.client_auth = client_auth  # type: bool
        self.client_gb_id = client_gb_id  # type: str
        self.client_ip = client_ip  # type: str
        self.client_password = client_password  # type: str
        self.client_port = client_port  # type: long
        self.client_username = client_username  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.gb_id = gb_id  # type: str
        self.id = id  # type: str
        self.ip = ip  # type: str
        self.name = name  # type: str
        self.port = port  # type: long
        self.protocol = protocol  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, id=None, owner_id=None, page_num=None, page_size=None, sort_by=None, sort_direction=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        return self


class DescribeParentPlatformDevicesResponseBodyDevices(TeaModel):
    def __init__(self, gb_id=None, group_id=None, id=None, name=None, parent_id=None):
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeParentPlatformDevicesResponseBody(TeaModel):
    def __init__(self, devices=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.devices = devices  # type: list[DescribeParentPlatformDevicesResponseBodyDevices]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeParentPlatformDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, gb_id=None, owner_id=None, page_num=None, page_size=None, sort_by=None, sort_direction=None,
                 status=None):
        self.gb_id = gb_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeParentPlatformsResponseBodyPlatforms(TeaModel):
    def __init__(self, auto_start=None, client_auth=None, client_gb_id=None, client_ip=None, client_password=None,
                 client_port=None, client_username=None, created_time=None, description=None, gb_id=None, id=None, ip=None,
                 name=None, port=None, protocol=None, status=None):
        self.auto_start = auto_start  # type: bool
        self.client_auth = client_auth  # type: bool
        self.client_gb_id = client_gb_id  # type: str
        self.client_ip = client_ip  # type: str
        self.client_password = client_password  # type: str
        self.client_port = client_port  # type: long
        self.client_username = client_username  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.gb_id = gb_id  # type: str
        self.id = id  # type: str
        self.ip = ip  # type: str
        self.name = name  # type: str
        self.port = port  # type: long
        self.protocol = protocol  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParentPlatformsResponseBodyPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeParentPlatformsResponseBody(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, platforms=None, request_id=None,
                 total_count=None):
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.platforms = platforms  # type: list[DescribeParentPlatformsResponseBodyPlatforms]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['Platforms'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.platforms = []
        if m.get('Platforms') is not None:
            for k in m.get('Platforms'):
                temp_model = DescribeParentPlatformsResponseBodyPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePresetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribePresetsResponseBodyPresets(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePresetsResponseBodyPresets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePresetsResponseBody(TeaModel):
    def __init__(self, id=None, presets=None, request_id=None):
        self.id = id  # type: str
        self.presets = presets  # type: list[DescribePresetsResponseBodyPresets]
        self.request_id = request_id  # type: str

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
        result['Presets'] = []
        if self.presets is not None:
            for k in self.presets:
                result['Presets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.presets = []
        if m.get('Presets') is not None:
            for k in m.get('Presets'):
                temp_model = DescribePresetsResponseBodyPresets()
                self.presets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribePurchasedDeviceResponseBody(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, group_name=None, id=None, name=None,
                 order_id=None, region=None, register_code=None, request_id=None, sub_type=None, type=None, vendor=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: str
        self.region = region  # type: str
        self.register_code = register_code  # type: str
        self.request_id = request_id  # type: str
        self.sub_type = sub_type  # type: str
        self.type = type  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region is not None:
            result['Region'] = self.region
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
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
    def __init__(self, group_id=None, id=None, name=None, owner_id=None, page_num=None, page_size=None, sort_by=None,
                 sort_direction=None, sub_type=None, type=None, vendor=None):
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.sub_type = sub_type  # type: str
        self.type = type  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribePurchasedDevicesResponseBodyDevices(TeaModel):
    def __init__(self, created_time=None, description=None, group_id=None, group_name=None, id=None, name=None,
                 order_id=None, region=None, register_code=None, sub_type=None, type=None, vendor=None):
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: str
        self.region = region  # type: str
        self.register_code = register_code  # type: str
        self.sub_type = sub_type  # type: str
        self.type = type  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePurchasedDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region is not None:
            result['Region'] = self.region
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribePurchasedDevicesResponseBody(TeaModel):
    def __init__(self, devices=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.devices = devices  # type: list[DescribePurchasedDevicesResponseBodyDevices]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribePurchasedDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, end_time=None, owner_id=None, page_num=None, page_size=None, private_bucket=None,
                 sort_by=None, sort_direction=None, start_time=None, stream_id=None, type=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.private_bucket = private_bucket  # type: bool
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.start_time = start_time  # type: str
        self.stream_id = stream_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_bucket is not None:
            result['PrivateBucket'] = self.private_bucket
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateBucket') is not None:
            self.private_bucket = m.get('PrivateBucket')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeRecordsResponseBodyRecords(TeaModel):
    def __init__(self, end_time=None, file_format=None, height=None, id=None, oss_bucket=None, oss_endpoint=None,
                 oss_object=None, start_time=None, stream_id=None, template_id=None, type=None, url=None, width=None):
        self.end_time = end_time  # type: str
        self.file_format = file_format  # type: str
        self.height = height  # type: long
        self.id = id  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object  # type: str
        self.start_time = start_time  # type: str
        self.stream_id = stream_id  # type: str
        self.template_id = template_id  # type: str
        self.type = type  # type: str
        self.url = url  # type: str
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordsResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeRecordsResponseBody(TeaModel):
    def __init__(self, next_start_time=None, page_count=None, page_num=None, page_size=None, records=None,
                 request_id=None, total_count=None):
        self.next_start_time = next_start_time  # type: str
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.records = records  # type: list[DescribeRecordsResponseBodyRecords]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class DescribeRenderingDevicesRequest(TeaModel):
    def __init__(self, instance_ids=None, owner_id=None):
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenderingDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRenderingDevicesResponseBodyDevicesIpInfos(TeaModel):
    def __init__(self, external_ip=None, external_port=None, isp=None, internal_ip=None, internal_port=None,
                 ip_protocol=None, nat_type=None):
        self.external_ip = external_ip  # type: str
        self.external_port = external_port  # type: str
        self.isp = isp  # type: str
        self.internal_ip = internal_ip  # type: str
        self.internal_port = internal_port  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.nat_type = nat_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenderingDevicesResponseBodyDevicesIpInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        return self


class DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork(TeaModel):
    def __init__(self, container_ports=None, external_ip=None, external_ports=None):
        self.container_ports = container_ports  # type: str
        self.external_ip = external_ip  # type: str
        self.external_ports = external_ports  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_ports is not None:
            result['ContainerPorts'] = self.container_ports
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_ports is not None:
            result['ExternalPorts'] = self.external_ports
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerPorts') is not None:
            self.container_ports = m.get('ContainerPorts')
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPorts') is not None:
            self.external_ports = m.get('ExternalPorts')
        return self


class DescribeRenderingDevicesResponseBodyDevicesPodInfos(TeaModel):
    def __init__(self, network=None, pod_id=None, status=None):
        self.network = network  # type: list[DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork]
        self.pod_id = pod_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenderingDevicesResponseBodyDevicesPodInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Network'] = []
        if self.network is not None:
            for k in self.network:
                result['Network'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network = []
        if m.get('Network') is not None:
            for k in m.get('Network'):
                temp_model = DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork()
                self.network.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRenderingDevicesResponseBodyDevices(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, cluster_id=None, description=None,
                 edge_node_name=None, image_id=None, instance_charge_type=None, instance_id=None, instance_name=None,
                 ip_infos=None, mac_address=None, period=None, period_unit=None, platform_type=None, pod_infos=None,
                 server_name=None, specification=None, status=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.edge_node_name = edge_node_name  # type: str
        self.image_id = image_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.ip_infos = ip_infos  # type: list[DescribeRenderingDevicesResponseBodyDevicesIpInfos]
        self.mac_address = mac_address  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.platform_type = platform_type  # type: str
        self.pod_infos = pod_infos  # type: list[DescribeRenderingDevicesResponseBodyDevicesPodInfos]
        self.server_name = server_name  # type: str
        self.specification = specification  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.ip_infos:
            for k in self.ip_infos:
                if k:
                    k.validate()
        if self.pod_infos:
            for k in self.pod_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenderingDevicesResponseBodyDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['IpInfos'] = []
        if self.ip_infos is not None:
            for k in self.ip_infos:
                result['IpInfos'].append(k.to_map() if k else None)
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        result['PodInfos'] = []
        if self.pod_infos is not None:
            for k in self.pod_infos:
                result['PodInfos'].append(k.to_map() if k else None)
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.ip_infos = []
        if m.get('IpInfos') is not None:
            for k in m.get('IpInfos'):
                temp_model = DescribeRenderingDevicesResponseBodyDevicesIpInfos()
                self.ip_infos.append(temp_model.from_map(k))
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        self.pod_infos = []
        if m.get('PodInfos') is not None:
            for k in m.get('PodInfos'):
                temp_model = DescribeRenderingDevicesResponseBodyDevicesPodInfos()
                self.pod_infos.append(temp_model.from_map(k))
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRenderingDevicesResponseBody(TeaModel):
    def __init__(self, devices=None, request_id=None, total=None):
        self.devices = devices  # type: list[DescribeRenderingDevicesResponseBodyDevices]
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRenderingDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeRenderingDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRenderingDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRenderingDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRenderingDevicesResponse, self).to_map()
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
            temp_model = DescribeRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeStreamResponseBody(TeaModel):
    def __init__(self, app=None, created_time=None, device_id=None, enabled=None, group_id=None, height=None, id=None,
                 name=None, play_domain=None, protocol=None, push_domain=None, request_id=None, status=None, width=None):
        self.app = app  # type: str
        self.created_time = created_time  # type: str
        self.device_id = device_id  # type: str
        self.enabled = enabled  # type: bool
        self.group_id = group_id  # type: str
        self.height = height  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.play_domain = play_domain  # type: str
        self.protocol = protocol  # type: str
        self.push_domain = push_domain  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Width') is not None:
            self.width = m.get('Width')
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


class DescribeStreamURLRequest(TeaModel):
    def __init__(self, auth=None, auth_key=None, end_time=None, expire=None, id=None, out_protocol=None,
                 owner_id=None, start_time=None, transcode=None, type=None):
        self.auth = auth  # type: bool
        self.auth_key = auth_key  # type: str
        self.end_time = end_time  # type: long
        self.expire = expire  # type: long
        self.id = id  # type: str
        self.out_protocol = out_protocol  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long
        self.transcode = transcode  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeStreamURLResponseBody(TeaModel):
    def __init__(self, expire_time=None, request_id=None, url=None):
        self.expire_time = expire_time  # type: long
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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
    def __init__(self, end_time=None, id=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: long
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamVodListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, records=None, request_id=None):
        self.records = records  # type: list[DescribeStreamVodListResponseBodyRecords]
        self.request_id = request_id  # type: str

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
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeStreamVodListResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeStreamsRequest(TeaModel):
    def __init__(self, app=None, device_id=None, domain=None, group_id=None, id=None, name=None, owner_id=None,
                 page_num=None, page_size=None, parent_id=None, sort_by=None, sort_direction=None):
        self.app = app  # type: str
        self.device_id = device_id  # type: str
        self.domain = domain  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.parent_id = parent_id  # type: str
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        return self


class DescribeStreamsResponseBodyStreams(TeaModel):
    def __init__(self, app=None, created_time=None, device_id=None, enabled=None, group_id=None, height=None, id=None,
                 name=None, play_domain=None, protocol=None, push_domain=None, status=None, width=None):
        self.app = app  # type: str
        self.created_time = created_time  # type: str
        self.device_id = device_id  # type: str
        self.enabled = enabled  # type: bool
        self.group_id = group_id  # type: str
        self.height = height  # type: int
        self.id = id  # type: str
        self.name = name  # type: str
        self.play_domain = play_domain  # type: str
        self.protocol = protocol  # type: str
        self.push_domain = push_domain  # type: str
        self.status = status  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStreamsResponseBodyStreams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.status is not None:
            result['Status'] = self.status
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeStreamsResponseBody(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, request_id=None, streams=None,
                 total_count=None):
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.streams = streams  # type: list[DescribeStreamsResponseBodyStreams]
        self.total_count = total_count  # type: long

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
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = DescribeStreamsResponseBodyStreams()
                self.streams.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class DescribeTemplateRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeTemplateResponseBodyTransConfigs(TeaModel):
    def __init__(self, fps=None, gop=None, height=None, id=None, name=None, video_bitrate=None, video_codec=None,
                 width=None):
        self.fps = fps  # type: long
        self.gop = gop  # type: long
        self.height = height  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.video_bitrate = video_bitrate  # type: long
        self.video_codec = video_codec  # type: str
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateResponseBodyTransConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.gop is not None:
            result['Gop'] = self.gop
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Gop') is not None:
            self.gop = m.get('Gop')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeTemplateResponseBody(TeaModel):
    def __init__(self, callback=None, created_time=None, description=None, file_format=None, flv=None,
                 hls_m3u_8=None, hls_ts=None, id=None, interval=None, jpg_on_demand=None, jpg_overwrite=None,
                 jpg_sequence=None, mp_4=None, name=None, oss_bucket=None, oss_endpoint=None, oss_file_prefix=None, region=None,
                 request_id=None, retention=None, trans_configs=None, trigger=None, type=None):
        self.callback = callback  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.file_format = file_format  # type: str
        self.flv = flv  # type: str
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.hls_ts = hls_ts  # type: str
        self.id = id  # type: str
        self.interval = interval  # type: long
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.mp_4 = mp_4  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.region = region  # type: str
        self.request_id = request_id  # type: str
        self.retention = retention  # type: long
        self.trans_configs = trans_configs  # type: list[DescribeTemplateResponseBodyTransConfigs]
        self.trigger = trigger  # type: str
        self.type = type  # type: str

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
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k in self.trans_configs:
                result['TransConfigs'].append(k.to_map() if k else None)
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k in m.get('TransConfigs'):
                temp_model = DescribeTemplateResponseBodyTransConfigs()
                self.trans_configs.append(temp_model.from_map(k))
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
    def __init__(self, id=None, instance_id=None, owner_id=None, page_num=None, page_size=None, sort_by=None,
                 sort_direction=None, type=None):
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.sort_direction = sort_direction  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTemplatesResponseBodyTemplatesTransConfigs(TeaModel):
    def __init__(self, fps=None, gop=None, height=None, name=None, video_bitrate=None, video_codec=None, width=None,
                 id=None):
        self.fps = fps  # type: long
        self.gop = gop  # type: long
        self.height = height  # type: long
        self.name = name  # type: str
        self.video_bitrate = video_bitrate  # type: long
        self.video_codec = video_codec  # type: str
        self.width = width  # type: long
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplatesResponseBodyTemplatesTransConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.gop is not None:
            result['Gop'] = self.gop
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.width is not None:
            result['Width'] = self.width
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Gop') is not None:
            self.gop = m.get('Gop')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, callback=None, created_time=None, description=None, file_format=None, flv=None,
                 hls_m3u_8=None, hls_ts=None, id=None, interval=None, jpg_on_demand=None, jpg_overwrite=None,
                 jpg_sequence=None, mp_4=None, name=None, oss_bucket=None, oss_endpoint=None, oss_file_prefix=None, region=None,
                 retention=None, trans_configs=None, trigger=None, type=None):
        self.callback = callback  # type: str
        self.created_time = created_time  # type: str
        self.description = description  # type: str
        self.file_format = file_format  # type: str
        self.flv = flv  # type: str
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.hls_ts = hls_ts  # type: str
        self.id = id  # type: str
        self.interval = interval  # type: long
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.mp_4 = mp_4  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.region = region  # type: str
        self.retention = retention  # type: long
        self.trans_configs = trans_configs  # type: list[DescribeTemplatesResponseBodyTemplatesTransConfigs]
        self.trigger = trigger  # type: str
        self.type = type  # type: str

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
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k in self.trans_configs:
                result['TransConfigs'].append(k.to_map() if k else None)
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k in m.get('TransConfigs'):
                temp_model = DescribeTemplatesResponseBodyTemplatesTransConfigs()
                self.trans_configs.append(temp_model.from_map(k))
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, request_id=None, templates=None,
                 total_count=None):
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.templates = templates  # type: list[DescribeTemplatesResponseBodyTemplates]
        self.total_count = total_count  # type: long

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
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, owner_id=None, tx_id=None, url=None):
        self.owner_id = owner_id  # type: long
        self.tx_id = tx_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodStreamURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeVodStreamURLResponseBody(TeaModel):
    def __init__(self, out_protocol=None, port=None, request_id=None, tx_id=None, url=None):
        self.out_protocol = out_protocol  # type: str
        self.port = port  # type: long
        self.request_id = request_id  # type: str
        self.tx_id = tx_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodStreamURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.port is not None:
            result['Port'] = self.port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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
    def __init__(self, cert_name=None, owner_id=None):
        self.cert_name = cert_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsCertificateDetailResponseBody(TeaModel):
    def __init__(self, cert=None, cert_id=None, cert_name=None, key=None, request_id=None):
        self.cert = cert  # type: str
        self.cert_id = cert_id  # type: long
        self.cert_name = cert_name  # type: str
        self.key = key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
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
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, cert_id=None, cert_name=None, common=None, fingerprint=None, issuer=None, last_time=None):
        self.cert_id = cert_id  # type: long
        self.cert_name = cert_name  # type: str
        self.common = common  # type: str
        self.fingerprint = fingerprint  # type: str
        self.issuer = issuer  # type: str
        self.last_time = last_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsCertificateListResponseBodyCertificateListModelCertList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        return self


class DescribeVsCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, cert_list=None, count=None):
        self.cert_list = cert_list  # type: list[DescribeVsCertificateListResponseBodyCertificateListModelCertList]
        self.count = count  # type: int

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
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = DescribeVsCertificateListResponseBodyCertificateListModelCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeVsCertificateListResponseBody(TeaModel):
    def __init__(self, certificate_list_model=None, request_id=None):
        self.certificate_list_model = certificate_list_model  # type: DescribeVsCertificateListResponseBodyCertificateListModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeVsCertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeVsCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeVsDevicesDataRequest(TeaModel):
    def __init__(self, end_time=None, group_id=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.group_id = group_id  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDevicesDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule(TeaModel):
    def __init__(self, devices_data_value=None, time_stamp=None):
        self.devices_data_value = devices_data_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.devices_data_value is not None:
            result['DevicesDataValue'] = self.devices_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DevicesDataValue') is not None:
            self.devices_data_value = m.get('DevicesDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDevicesDataResponseBodyDevicesDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDevicesDataResponseBodyDevicesDataPerInterval, self).to_map()
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
                temp_model = DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDevicesDataResponseBody(TeaModel):
    def __init__(self, devices_data_per_interval=None, request_id=None):
        self.devices_data_per_interval = devices_data_per_interval  # type: DescribeVsDevicesDataResponseBodyDevicesDataPerInterval
        self.request_id = request_id  # type: str

    def validate(self):
        if self.devices_data_per_interval:
            self.devices_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDevicesDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.devices_data_per_interval is not None:
            result['DevicesDataPerInterval'] = self.devices_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DevicesDataPerInterval') is not None:
            temp_model = DescribeVsDevicesDataResponseBodyDevicesDataPerInterval()
            self.devices_data_per_interval = temp_model.from_map(m['DevicesDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsDevicesDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDevicesDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDevicesDataResponse, self).to_map()
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
            temp_model = DescribeVsDevicesDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 request_id=None, start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_domain_name=None, cert_expire_time=None, cert_life=None, cert_name=None, cert_org=None,
                 cert_type=None, domain_name=None, sslpub=None, server_certificate_status=None, status=None):
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_life = cert_life  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.sslpub = sslpub  # type: str
        self.server_certificate_status = server_certificate_status  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeVsDomainCertificateInfoResponseBodyCertInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeVsDomainCertificateInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeVsDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, domain_name=None, function_names=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: list[DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs]
        self.function_name = function_name  # type: str
        self.status = status  # type: str

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
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeVsDomainConfigsResponseBody(TeaModel):
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: list[DescribeVsDomainConfigsResponseBodyDomainConfigs]
        self.request_id = request_id  # type: str

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
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeVsDomainConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsDomainDetailResponseBodyDomainConfig(TeaModel):
    def __init__(self, cname=None, description=None, domain_name=None, domain_status=None, domain_type=None,
                 gmt_created=None, gmt_modified=None, region=None, sslprotocol=None, scope=None):
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.domain_type = domain_type  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.region = region  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.scope = scope  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainDetailResponseBodyDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.region is not None:
            result['Region'] = self.region
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class DescribeVsDomainDetailResponseBody(TeaModel):
    def __init__(self, domain_config=None, request_id=None):
        self.domain_config = domain_config  # type: DescribeVsDomainDetailResponseBodyDomainConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        _map = super(DescribeVsDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainConfig') is not None:
            temp_model = DescribeVsDomainDetailResponseBodyDomainConfig()
            self.domain_config = temp_model.from_map(m['DomainConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeVsDomainOnlineUserNumRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, query_time=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.query_time = query_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo(TeaModel):
    def __init__(self, transcode_template=None, user_number=None):
        self.transcode_template = transcode_template  # type: str
        self.user_number = user_number  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transcode_template is not None:
            result['TranscodeTemplate'] = self.transcode_template
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TranscodeTemplate') is not None:
            self.transcode_template = m.get('TranscodeTemplate')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos(TeaModel):
    def __init__(self, info=None):
        self.info = info  # type: list[DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo]

    def validate(self):
        if self.info:
            for k in self.info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Info'] = []
        if self.info is not None:
            for k in self.info:
                result['Info'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.info = []
        if m.get('Info') is not None:
            for k in m.get('Info'):
                temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo()
                self.info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo(TeaModel):
    def __init__(self, infos=None, stream_name=None):
        self.infos = infos  # type: DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos
        self.stream_name = stream_name  # type: str

    def validate(self):
        if self.infos:
            self.infos.validate()

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.infos is not None:
            result['Infos'] = self.infos.to_map()
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Infos') is not None:
            temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos()
            self.infos = temp_model.from_map(m['Infos'])
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo(TeaModel):
    def __init__(self, live_stream_online_user_num_info=None):
        self.live_stream_online_user_num_info = live_stream_online_user_num_info  # type: list[DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo]

    def validate(self):
        if self.live_stream_online_user_num_info:
            for k in self.live_stream_online_user_num_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveStreamOnlineUserNumInfo'] = []
        if self.live_stream_online_user_num_info is not None:
            for k in self.live_stream_online_user_num_info:
                result['LiveStreamOnlineUserNumInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_stream_online_user_num_info = []
        if m.get('LiveStreamOnlineUserNumInfo') is not None:
            for k in m.get('LiveStreamOnlineUserNumInfo'):
                temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo()
                self.live_stream_online_user_num_info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainOnlineUserNumResponseBody(TeaModel):
    def __init__(self, online_user_info=None, request_id=None, stream_count=None, user_count=None):
        self.online_user_info = online_user_info  # type: DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo
        self.request_id = request_id  # type: str
        self.stream_count = stream_count  # type: int
        self.user_count = user_count  # type: int

    def validate(self):
        if self.online_user_info:
            self.online_user_info.validate()

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_user_info is not None:
            result['OnlineUserInfo'] = self.online_user_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnlineUserInfo') is not None:
            temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo()
            self.online_user_info = temp_model.from_map(m['OnlineUserInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        return self


class DescribeVsDomainOnlineUserNumResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsDomainOnlineUserNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsDomainOnlineUserNumResponse, self).to_map()
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
            temp_model = DescribeVsDomainOnlineUserNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainPvDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, pv_data_interval=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.pv_data_interval = pv_data_interval  # type: DescribeVsDomainPvDataResponseBodyPvDataInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeVsDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, pv_uv_data_infos=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.pv_uv_data_infos = pv_uv_data_infos  # type: DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.pv_uv_data_infos:
            self.pv_uv_data_infos.validate()

    def to_map(self):
        _map = super(DescribeVsDomainPvUvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pv_uv_data_infos is not None:
            result['PvUvDataInfos'] = self.pv_uv_data_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PvUvDataInfos') is not None:
            temp_model = DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos()
            self.pv_uv_data_infos = temp_model.from_map(m['PvUvDataInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, end_time=None, owner_id=None, region=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule(TeaModel):
    def __init__(self, record_value=None, stream_count_value=None, time_stamp=None):
        self.record_value = record_value  # type: str
        self.stream_count_value = stream_count_value  # type: str
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
        if self.stream_count_value is not None:
            result['StreamCountValue'] = self.stream_count_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')
        if m.get('StreamCountValue') is not None:
            self.stream_count_value = m.get('StreamCountValue')
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
    def __init__(self, record_data_per_interval=None, request_id=None):
        self.record_data_per_interval = record_data_per_interval  # type: DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval
        self.request_id = request_id  # type: str

    def validate(self):
        if self.record_data_per_interval:
            self.record_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRecordDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_data_per_interval is not None:
            result['RecordDataPerInterval'] = self.record_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecordDataPerInterval') is not None:
            temp_model = DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval()
            self.record_data_per_interval = temp_model.from_map(m['RecordDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(self, avg_object_size=None, avg_response_rate=None, avg_response_time=None, bps=None,
                 bytes_proportion=None, proportion=None, qps=None, region=None, region_ename=None, req_err_rate=None,
                 total_bytes=None, total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.region = region  # type: str
        self.region_ename = region_ename  # type: str
        self.req_err_rate = req_err_rate  # type: str
        self.total_bytes = total_bytes  # type: str
        self.total_query = total_query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataResponseBodyValueRegionProportionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 value=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.value = value  # type: DescribeVsDomainRegionDataResponseBodyValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeVsDomainRegionDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, req_bps_value=None, time_stamp=None):
        self.req_bps_value = req_bps_value  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_bps_value is not None:
            result['ReqBpsValue'] = self.req_bps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReqBpsValue') is not None:
            self.req_bps_value = m.get('ReqBpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, req_bps_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.req_bps_data_per_interval = req_bps_data_per_interval  # type: DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.req_bps_data_per_interval:
            self.req_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.req_bps_data_per_interval is not None:
            result['ReqBpsDataPerInterval'] = self.req_bps_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReqBpsDataPerInterval') is not None:
            temp_model = DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval()
            self.req_bps_data_per_interval = temp_model.from_map(m['ReqBpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, req_traffic_data_per_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.req_traffic_data_per_interval = req_traffic_data_per_interval  # type: DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.req_traffic_data_per_interval:
            self.req_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainReqTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.req_traffic_data_per_interval is not None:
            result['ReqTrafficDataPerInterval'] = self.req_traffic_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReqTrafficDataPerInterval') is not None:
            temp_model = DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval()
            self.req_traffic_data_per_interval = temp_model.from_map(m['ReqTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, request_id=None, snapshot_data_per_interval=None):
        self.request_id = request_id  # type: str
        self.snapshot_data_per_interval = snapshot_data_per_interval  # type: DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval

    def validate(self):
        if self.snapshot_data_per_interval:
            self.snapshot_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainSnapshotDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_data_per_interval is not None:
            result['SnapshotDataPerInterval'] = self.snapshot_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, traffic_value=None):
        self.time_stamp = time_stamp  # type: str
        self.traffic_value = traffic_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 traffic_data_per_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainUvDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 uv_data_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.uv_data_interval = uv_data_interval  # type: DescribeVsDomainUvDataResponseBodyUvDataInterval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeVsDomainUvDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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


class DescribeVsPullStreamConfigRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsPullStreamConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(self, app_name=None, domain_name=None, end_time=None, source_url=None, start_time=None,
                 stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DescribeVsPullStreamConfigResponseBodyLiveAppRecordList(TeaModel):
    def __init__(self, live_app_record=None):
        self.live_app_record = live_app_record  # type: list[DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord]

    def validate(self):
        if self.live_app_record:
            for k in self.live_app_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamConfigResponseBodyLiveAppRecordList, self).to_map()
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
                temp_model = DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k))
        return self


class DescribeVsPullStreamConfigResponseBody(TeaModel):
    def __init__(self, live_app_record_list=None, request_id=None):
        self.live_app_record_list = live_app_record_list  # type: DescribeVsPullStreamConfigResponseBodyLiveAppRecordList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveAppRecordList') is not None:
            temp_model = DescribeVsPullStreamConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m['LiveAppRecordList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsPullStreamConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsPullStreamConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamConfigResponse, self).to_map()
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
            temp_model = DescribeVsPullStreamConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(self, app_name=None, domain_name=None, end_time=None, source_url=None, start_time=None,
                 stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
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
    def __init__(self, live_app_record_list=None, request_id=None):
        self.live_app_record_list = live_app_record_list  # type: DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        _map = super(DescribeVsPullStreamInfoConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveAppRecordList') is not None:
            temp_model = DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m['LiveAppRecordList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeVsStorageTrafficUsageDataRequest(TeaModel):
    def __init__(self, bucket=None, end_time=None, interval=None, owner_id=None, split_by=None, start_time=None):
        self.bucket = bucket  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.split_by = split_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStorageTrafficUsageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.split_by is not None:
            result['SplitBy'] = self.split_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule(TeaModel):
    def __init__(self, bucket=None, lan_bandwidth_in_data_value=None, lan_bandwidth_out_data_value=None,
                 lan_traffic_in_data_value=None, lan_traffic_out_data_value=None, time_stamp=None, wan_bandwidth_in_data_value=None,
                 wan_bandwidth_out_data_value=None, wan_traffic_in_data_value=None, wan_traffic_out_data_value=None):
        self.bucket = bucket  # type: str
        self.lan_bandwidth_in_data_value = lan_bandwidth_in_data_value  # type: float
        self.lan_bandwidth_out_data_value = lan_bandwidth_out_data_value  # type: float
        self.lan_traffic_in_data_value = lan_traffic_in_data_value  # type: long
        self.lan_traffic_out_data_value = lan_traffic_out_data_value  # type: long
        self.time_stamp = time_stamp  # type: str
        self.wan_bandwidth_in_data_value = wan_bandwidth_in_data_value  # type: float
        self.wan_bandwidth_out_data_value = wan_bandwidth_out_data_value  # type: float
        self.wan_traffic_in_data_value = wan_traffic_in_data_value  # type: long
        self.wan_traffic_out_data_value = wan_traffic_out_data_value  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.lan_bandwidth_in_data_value is not None:
            result['LanBandwidthInDataValue'] = self.lan_bandwidth_in_data_value
        if self.lan_bandwidth_out_data_value is not None:
            result['LanBandwidthOutDataValue'] = self.lan_bandwidth_out_data_value
        if self.lan_traffic_in_data_value is not None:
            result['LanTrafficInDataValue'] = self.lan_traffic_in_data_value
        if self.lan_traffic_out_data_value is not None:
            result['LanTrafficOutDataValue'] = self.lan_traffic_out_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.wan_bandwidth_in_data_value is not None:
            result['WanBandwidthInDataValue'] = self.wan_bandwidth_in_data_value
        if self.wan_bandwidth_out_data_value is not None:
            result['WanBandwidthOutDataValue'] = self.wan_bandwidth_out_data_value
        if self.wan_traffic_in_data_value is not None:
            result['WanTrafficInDataValue'] = self.wan_traffic_in_data_value
        if self.wan_traffic_out_data_value is not None:
            result['WanTrafficOutDataValue'] = self.wan_traffic_out_data_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('LanBandwidthInDataValue') is not None:
            self.lan_bandwidth_in_data_value = m.get('LanBandwidthInDataValue')
        if m.get('LanBandwidthOutDataValue') is not None:
            self.lan_bandwidth_out_data_value = m.get('LanBandwidthOutDataValue')
        if m.get('LanTrafficInDataValue') is not None:
            self.lan_traffic_in_data_value = m.get('LanTrafficInDataValue')
        if m.get('LanTrafficOutDataValue') is not None:
            self.lan_traffic_out_data_value = m.get('LanTrafficOutDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WanBandwidthInDataValue') is not None:
            self.wan_bandwidth_in_data_value = m.get('WanBandwidthInDataValue')
        if m.get('WanBandwidthOutDataValue') is not None:
            self.wan_bandwidth_out_data_value = m.get('WanBandwidthOutDataValue')
        if m.get('WanTrafficInDataValue') is not None:
            self.wan_traffic_in_data_value = m.get('WanTrafficInDataValue')
        if m.get('WanTrafficOutDataValue') is not None:
            self.wan_traffic_out_data_value = m.get('WanTrafficOutDataValue')
        return self


class DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage(TeaModel):
    def __init__(self, traffic_usage_data_module=None):
        self.traffic_usage_data_module = traffic_usage_data_module  # type: list[DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule]

    def validate(self):
        if self.traffic_usage_data_module:
            for k in self.traffic_usage_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficUsageDataModule'] = []
        if self.traffic_usage_data_module is not None:
            for k in self.traffic_usage_data_module:
                result['TrafficUsageDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.traffic_usage_data_module = []
        if m.get('TrafficUsageDataModule') is not None:
            for k in m.get('TrafficUsageDataModule'):
                temp_model = DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule()
                self.traffic_usage_data_module.append(temp_model.from_map(k))
        return self


class DescribeVsStorageTrafficUsageDataResponseBody(TeaModel):
    def __init__(self, request_id=None, traffic_usage=None):
        self.request_id = request_id  # type: str
        self.traffic_usage = traffic_usage  # type: DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage

    def validate(self):
        if self.traffic_usage:
            self.traffic_usage.validate()

    def to_map(self):
        _map = super(DescribeVsStorageTrafficUsageDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_usage is not None:
            result['TrafficUsage'] = self.traffic_usage.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficUsage') is not None:
            temp_model = DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage()
            self.traffic_usage = temp_model.from_map(m['TrafficUsage'])
        return self


class DescribeVsStorageTrafficUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVsStorageTrafficUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVsStorageTrafficUsageDataResponse, self).to_map()
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
            temp_model = DescribeVsStorageTrafficUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStorageUsageDataRequest(TeaModel):
    def __init__(self, bucket=None, end_time=None, interval=None, owner_id=None, split_by=None, start_time=None):
        self.bucket = bucket  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.split_by = split_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.split_by is not None:
            result['SplitBy'] = self.split_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule(TeaModel):
    def __init__(self, bucket=None, storage_data_value=None, time_stamp=None):
        self.bucket = bucket  # type: str
        self.storage_data_value = storage_data_value  # type: int
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.storage_data_value is not None:
            result['StorageDataValue'] = self.storage_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('StorageDataValue') is not None:
            self.storage_data_value = m.get('StorageDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig(TeaModel):
    def __init__(self, auth_key=None, auth_type=None, domain_name=None, notify_url=None):
        self.auth_key = auth_key  # type: str
        self.auth_type = auth_type  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        return self


class DescribeVsStreamsNotifyUrlConfigResponseBody(TeaModel):
    def __init__(self, live_streams_notify_config=None, request_id=None):
        self.live_streams_notify_config = live_streams_notify_config  # type: DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig
        self.request_id = request_id  # type: str

    def validate(self):
        if self.live_streams_notify_config:
            self.live_streams_notify_config.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsNotifyUrlConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_streams_notify_config is not None:
            result['LiveStreamsNotifyConfig'] = self.live_streams_notify_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveStreamsNotifyConfig') is not None:
            temp_model = DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig()
            self.live_streams_notify_config = temp_model.from_map(m['LiveStreamsNotifyConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, app_name=None, domain_name=None, end_time=None, order_by=None, owner_id=None, page_num=None,
                 page_size=None, query_type=None, start_time=None, stream_name=None, stream_type=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.order_by = order_by  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.query_type = query_type  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str
        self.stream_type = stream_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo(TeaModel):
    def __init__(self, app_name=None, domain_name=None, publish_domain=None, publish_time=None, publish_type=None,
                 publish_url=None, stream_name=None, transcode_id=None, transcoded=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.publish_domain = publish_domain  # type: str
        self.publish_time = publish_time  # type: str
        self.publish_type = publish_type  # type: str
        self.publish_url = publish_url  # type: str
        self.stream_name = stream_name  # type: str
        self.transcode_id = transcode_id  # type: str
        self.transcoded = transcoded  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id
        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')
        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')
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
    def __init__(self, online_info=None, page_num=None, page_size=None, request_id=None, total_num=None,
                 total_page=None):
        self.online_info = online_info  # type: DescribeVsStreamsOnlineListResponseBodyOnlineInfo
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.online_info:
            self.online_info.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsOnlineListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_info is not None:
            result['OnlineInfo'] = self.online_info.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnlineInfo') is not None:
            temp_model = DescribeVsStreamsOnlineListResponseBodyOnlineInfo()
            self.online_info = temp_model.from_map(m['OnlineInfo'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
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
    def __init__(self, app_name=None, domain_name=None, end_time=None, order_by=None, owner_id=None,
                 page_number=None, page_size=None, query_type=None, start_time=None, stream_name=None, stream_type=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.order_by = order_by  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_type = query_type  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str
        self.stream_type = stream_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo(TeaModel):
    def __init__(self, app_name=None, client_addr=None, domain_name=None, edge_node_addr=None, publish_domain=None,
                 publish_time=None, publish_type=None, publish_url=None, stop_time=None, stream_name=None, stream_url=None,
                 transcode_id=None, transcoded=None):
        self.app_name = app_name  # type: str
        self.client_addr = client_addr  # type: str
        self.domain_name = domain_name  # type: str
        self.edge_node_addr = edge_node_addr  # type: str
        self.publish_domain = publish_domain  # type: str
        self.publish_time = publish_time  # type: str
        self.publish_type = publish_type  # type: str
        self.publish_url = publish_url  # type: str
        self.stop_time = stop_time  # type: str
        self.stream_name = stream_name  # type: str
        self.stream_url = stream_url  # type: str
        self.transcode_id = transcode_id  # type: str
        self.transcoded = transcoded  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.edge_node_addr is not None:
            result['EdgeNodeAddr'] = self.edge_node_addr
        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url
        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id
        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EdgeNodeAddr') is not None:
            self.edge_node_addr = m.get('EdgeNodeAddr')
        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')
        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')
        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')
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
    def __init__(self, page_num=None, page_size=None, publish_info=None, request_id=None, total_num=None,
                 total_page=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.publish_info = publish_info  # type: DescribeVsStreamsPublishListResponseBodyPublishInfo
        self.request_id = request_id  # type: str
        self.total_num = total_num  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.publish_info:
            self.publish_info.validate()

    def to_map(self):
        _map = super(DescribeVsStreamsPublishListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.publish_info is not None:
            result['PublishInfo'] = self.publish_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublishInfo') is not None:
            temp_model = DescribeVsStreamsPublishListResponseBodyPublishInfo()
            self.publish_info = temp_model.from_map(m['PublishInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
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
    def __init__(self, end_time=None, limit=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.limit = limit  # type: long
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(self, domain_name=None, max_bps=None, max_bps_time=None, rank=None, total_access=None,
                 total_traffic=None, traffic_percent=None):
        self.domain_name = domain_name  # type: str
        self.max_bps = max_bps  # type: long
        self.max_bps_time = max_bps_time  # type: str
        self.rank = rank  # type: long
        self.total_access = total_access  # type: long
        self.total_traffic = total_traffic  # type: str
        self.traffic_percent = traffic_percent  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
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
    def __init__(self, domain_count=None, domain_online_count=None, end_time=None, request_id=None, start_time=None,
                 top_domains=None):
        self.domain_count = domain_count  # type: long
        self.domain_online_count = domain_online_count  # type: long
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.top_domains = top_domains  # type: DescribeVsTopDomainsByFlowResponseBodyTopDomains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super(DescribeVsTopDomainsByFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
    def __init__(self, domain_name=None, domain_switch=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.domain_switch = domain_switch  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_switch is not None:
            result['DomainSwitch'] = self.domain_switch
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainSwitch') is not None:
            self.domain_switch = m.get('DomainSwitch')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData(TeaModel):
    def __init__(self, band_width=None, peak_time=None, publish_stream_num=None, query_time=None, stat_name=None):
        self.band_width = band_width  # type: str
        self.peak_time = peak_time  # type: str
        self.publish_stream_num = publish_stream_num  # type: int
        self.query_time = query_time  # type: str
        self.stat_name = stat_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time
        if self.publish_stream_num is not None:
            result['PublishStreamNum'] = self.publish_stream_num
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.stat_name is not None:
            result['StatName'] = self.stat_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')
        if m.get('PublishStreamNum') is not None:
            self.publish_stream_num = m.get('PublishStreamNum')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('StatName') is not None:
            self.stat_name = m.get('StatName')
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
    def __init__(self, describe_vs_up_peak_publish_stream_datas=None, request_id=None):
        self.describe_vs_up_peak_publish_stream_datas = describe_vs_up_peak_publish_stream_datas  # type: DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas
        self.request_id = request_id  # type: str

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_datas:
            self.describe_vs_up_peak_publish_stream_datas.validate()

    def to_map(self):
        _map = super(DescribeVsUpPeakPublishStreamDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.describe_vs_up_peak_publish_stream_datas is not None:
            result['DescribeVsUpPeakPublishStreamDatas'] = self.describe_vs_up_peak_publish_stream_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DescribeVsUpPeakPublishStreamDatas') is not None:
            temp_model = DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas()
            self.describe_vs_up_peak_publish_stream_datas = temp_model.from_map(m['DescribeVsUpPeakPublishStreamDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(self, commodity_code=None, curr_capacity=None, display_name=None, init_capacity=None,
                 instance_id=None, status=None):
        self.commodity_code = commodity_code  # type: str
        self.curr_capacity = curr_capacity  # type: str
        self.display_name = display_name  # type: str
        self.init_capacity = init_capacity  # type: str
        self.instance_id = instance_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
    def __init__(self, app_name=None, control_stream_action=None, domain_name=None, live_stream_type=None,
                 oneshot=None, owner_id=None, resume_time=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.control_stream_action = control_stream_action  # type: str
        self.domain_name = domain_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.oneshot = oneshot  # type: str
        self.owner_id = owner_id  # type: long
        self.resume_time = resume_time  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ForbidVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
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
    def __init__(self, bucket_name=None, owner_id=None):
        self.bucket_name = bucket_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBucketInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetBucketInfoResponseBodyBucketInfo(TeaModel):
    def __init__(self, bucket_acl=None, bucket_name=None, comment=None, create_time=None, data_redundancy_type=None,
                 dispatcher_type=None, endpoint=None, modify_time=None, resource_type=None, storage_class=None):
        self.bucket_acl = bucket_acl  # type: str
        self.bucket_name = bucket_name  # type: str
        self.comment = comment  # type: str
        self.create_time = create_time  # type: str
        self.data_redundancy_type = data_redundancy_type  # type: str
        self.dispatcher_type = dispatcher_type  # type: str
        self.endpoint = endpoint  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_type = resource_type  # type: str
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBucketInfoResponseBodyBucketInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class GetBucketInfoResponseBody(TeaModel):
    def __init__(self, bucket_info=None, request_id=None):
        self.bucket_info = bucket_info  # type: GetBucketInfoResponseBodyBucketInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bucket_info:
            self.bucket_info.validate()

    def to_map(self):
        _map = super(GetBucketInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_info is not None:
            result['BucketInfo'] = self.bucket_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketInfo') is not None:
            temp_model = GetBucketInfoResponseBodyBucketInfo()
            self.bucket_info = temp_model.from_map(m['BucketInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetObjectTotalRequest(TeaModel):
    def __init__(self, bucket_name=None, owner_id=None):
        self.bucket_name = bucket_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetObjectTotalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetObjectTotalResponseBody(TeaModel):
    def __init__(self, object_count=None, request_id=None):
        self.object_count = object_count  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetObjectTotalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_count is not None:
            result['ObjectCount'] = self.object_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetObjectTotalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetObjectTotalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetObjectTotalResponse, self).to_map()
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
            temp_model = GetObjectTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GotoPresetRequest(TeaModel):
    def __init__(self, id=None, owner_id=None, preset_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.preset_id = preset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GotoPresetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
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
    def __init__(self, keyword=None, marker=None, owner_id=None, page_number=None, page_size=None, prefix=None):
        self.keyword = keyword  # type: str
        self.marker = marker  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBucketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListBucketsResponseBodyBucketInfos(TeaModel):
    def __init__(self, bucket_acl=None, bucket_name=None, comment=None, create_time=None, data_redundancy_type=None,
                 dispatcher_type=None, endpoint=None, modify_time=None, resource_type=None, storage_class=None):
        self.bucket_acl = bucket_acl  # type: str
        self.bucket_name = bucket_name  # type: str
        self.comment = comment  # type: str
        self.create_time = create_time  # type: str
        self.data_redundancy_type = data_redundancy_type  # type: str
        self.dispatcher_type = dispatcher_type  # type: str
        self.endpoint = endpoint  # type: str
        self.modify_time = modify_time  # type: str
        self.resource_type = resource_type  # type: str
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBucketsResponseBodyBucketInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class ListBucketsResponseBody(TeaModel):
    def __init__(self, bucket_infos=None, request_id=None, total_count=None):
        self.bucket_infos = bucket_infos  # type: list[ListBucketsResponseBodyBucketInfos]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['BucketInfos'] = []
        if self.bucket_infos is not None:
            for k in self.bucket_infos:
                result['BucketInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bucket_infos = []
        if m.get('BucketInfos') is not None:
            for k in m.get('BucketInfos'):
                temp_model = ListBucketsResponseBodyBucketInfos()
                self.bucket_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, device_id=None, owner_id=None, page_num=None, page_size=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceChannelsResponseBodyChannels(TeaModel):
    def __init__(self, channel_id=None, device_id=None, device_status=None, name=None, params=None):
        self.channel_id = channel_id  # type: long
        self.device_id = device_id  # type: str
        self.device_status = device_status  # type: str
        self.name = name  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceChannelsResponseBodyChannels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class ListDeviceChannelsResponseBody(TeaModel):
    def __init__(self, channels=None, page_count=None, page_num=None, page_size=None, request_id=None,
                 total_count=None):
        self.channels = channels  # type: list[ListDeviceChannelsResponseBodyChannels]
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = ListDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, device_id=None, owner_id=None, page_num=None, page_size=None, search_criteria=None,
                 stream_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.search_criteria = search_criteria  # type: str
        self.stream_id = stream_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_criteria is not None:
            result['SearchCriteria'] = self.search_criteria
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchCriteria') is not None:
            self.search_criteria = m.get('SearchCriteria')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class ListDeviceRecordsResponseBodyRecords(TeaModel):
    def __init__(self, end_time=None, file_size=None, filename=None, record_type=None, start_time=None):
        self.end_time = end_time  # type: str
        self.file_size = file_size  # type: long
        self.filename = filename  # type: str
        self.record_type = record_type  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceRecordsResponseBodyRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDeviceRecordsResponseBody(TeaModel):
    def __init__(self, page_count=None, page_num=None, page_size=None, records=None, request_id=None,
                 total_count=None):
        self.page_count = page_count  # type: long
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.records = records  # type: list[ListDeviceRecordsResponseBodyRecords]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

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
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListDeviceRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
    def __init__(self, bucket_name=None, continuation_token=None, delimiter=None, encoding_type=None, marker=None,
                 max_keys=None, owner_id=None, prefix=None, start_after=None):
        self.bucket_name = bucket_name  # type: str
        self.continuation_token = continuation_token  # type: str
        self.delimiter = delimiter  # type: str
        self.encoding_type = encoding_type  # type: str
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int
        self.owner_id = owner_id  # type: long
        self.prefix = prefix  # type: str
        self.start_after = start_after  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListObjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.start_after is not None:
            result['StartAfter'] = self.start_after
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('StartAfter') is not None:
            self.start_after = m.get('StartAfter')
        return self


class ListObjectsResponseBodyContents(TeaModel):
    def __init__(self, etag=None, key=None, last_modified=None, size=None, storage_class=None):
        self.etag = etag  # type: str
        self.key = key  # type: str
        self.last_modified = last_modified  # type: str
        self.size = size  # type: long
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListObjectsResponseBodyContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.key is not None:
            result['Key'] = self.key
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class ListObjectsResponseBody(TeaModel):
    def __init__(self, bucket_name=None, common_prefixes=None, contents=None, continuation_token=None,
                 delimiter=None, encoding_type=None, is_truncated=None, key_count=None, marker=None, max_keys=None,
                 next_continuation_token=None, next_marker=None, prefix=None, request_id=None):
        self.bucket_name = bucket_name  # type: str
        self.common_prefixes = common_prefixes  # type: list[str]
        self.contents = contents  # type: list[ListObjectsResponseBodyContents]
        self.continuation_token = continuation_token  # type: str
        self.delimiter = delimiter  # type: str
        self.encoding_type = encoding_type  # type: str
        self.is_truncated = is_truncated  # type: bool
        self.key_count = key_count  # type: int
        self.marker = marker  # type: str
        self.max_keys = max_keys  # type: int
        self.next_continuation_token = next_continuation_token  # type: str
        self.next_marker = next_marker  # type: str
        self.prefix = prefix  # type: str
        self.request_id = request_id  # type: str

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
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.common_prefixes is not None:
            result['CommonPrefixes'] = self.common_prefixes
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key_count is not None:
            result['KeyCount'] = self.key_count
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CommonPrefixes') is not None:
            self.common_prefixes = m.get('CommonPrefixes')
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = ListObjectsResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('KeyCount') is not None:
            self.key_count = m.get('KeyCount')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, alarm_method=None, auto_pos=None, auto_start=None, description=None, directory_id=None,
                 gb_id=None, group_id=None, id=None, ip=None, latitude=None, longitude=None, name=None, owner_id=None,
                 params=None, parent_id=None, password=None, port=None, pos_interval=None, type=None, url=None,
                 username=None, vendor=None):
        self.alarm_method = alarm_method  # type: str
        self.auto_pos = auto_pos  # type: bool
        self.auto_start = auto_start  # type: bool
        self.description = description  # type: str
        self.directory_id = directory_id  # type: str
        self.gb_id = gb_id  # type: str
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.ip = ip  # type: str
        self.latitude = latitude  # type: str
        self.longitude = longitude  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.params = params  # type: str
        self.parent_id = parent_id  # type: str
        self.password = password  # type: str
        self.port = port  # type: long
        self.pos_interval = pos_interval  # type: long
        self.type = type  # type: str
        self.url = url  # type: str
        self.username = username  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
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
    def __init__(self, alarm_id=None, channel_id=None, id=None, owner_id=None, status=None):
        self.alarm_id = alarm_id  # type: str
        self.channel_id = channel_id  # type: int
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceAlarmRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, image=None, owner_id=None, video=None):
        self.id = id  # type: str
        self.image = image  # type: int
        self.owner_id = owner_id  # type: long
        self.video = video  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceCaptureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, channels=None, device_status=None, dsn=None, id=None, owner_id=None):
        self.channels = channels  # type: str
        self.device_status = device_status  # type: str
        self.dsn = dsn  # type: str
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, description=None, id=None, name=None, owner_id=None):
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, callback=None, description=None, enabled=None, id=None, in_protocol=None, lazy_pull=None,
                 name=None, out_protocol=None, owner_id=None, play_domain=None, push_domain=None, region=None):
        self.callback = callback  # type: str
        self.description = description  # type: str
        self.enabled = enabled  # type: bool
        self.id = id  # type: str
        self.in_protocol = in_protocol  # type: str
        self.lazy_pull = lazy_pull  # type: bool
        self.name = name  # type: str
        self.out_protocol = out_protocol  # type: str
        self.owner_id = owner_id  # type: long
        self.play_domain = play_domain  # type: str
        self.push_domain = push_domain  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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
    def __init__(self, auto_start=None, client_auth=None, client_password=None, client_username=None,
                 description=None, gb_id=None, id=None, ip=None, name=None, owner_id=None, port=None):
        self.auto_start = auto_start  # type: bool
        self.client_auth = client_auth  # type: bool
        self.client_password = client_password  # type: str
        self.client_username = client_username  # type: str
        self.description = description  # type: str
        self.gb_id = gb_id  # type: str
        self.id = id  # type: str
        self.ip = ip  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.port = port  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
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


class ModifyPurchasedDeviceRequest(TeaModel):
    def __init__(self, description=None, id=None, name=None, order_id=None, owner_id=None, register_code=None,
                 sub_type=None, vendor=None):
        self.description = description  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: str
        self.owner_id = owner_id  # type: long
        self.register_code = register_code  # type: str
        self.sub_type = sub_type  # type: str
        self.vendor = vendor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ModifyPurchasedDeviceResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPurchasedDeviceResponseBody, self).to_map()
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


class ModifyPurchasedDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPurchasedDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPurchasedDeviceResponse, self).to_map()
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
            temp_model = ModifyPurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateRequest(TeaModel):
    def __init__(self, callback=None, description=None, file_format=None, flv=None, hls_m3u_8=None, hls_ts=None,
                 id=None, interval=None, jpg_on_demand=None, jpg_overwrite=None, jpg_sequence=None, mp_4=None,
                 name=None, oss_bucket=None, oss_endpoint=None, oss_file_prefix=None, owner_id=None, region=None,
                 retention=None, trans_configs_json=None, trigger=None):
        self.callback = callback  # type: str
        self.description = description  # type: str
        self.file_format = file_format  # type: str
        self.flv = flv  # type: str
        self.hls_m3u_8 = hls_m3u_8  # type: str
        self.hls_ts = hls_ts  # type: str
        self.id = id  # type: str
        self.interval = interval  # type: long
        self.jpg_on_demand = jpg_on_demand  # type: str
        self.jpg_overwrite = jpg_overwrite  # type: str
        self.jpg_sequence = jpg_sequence  # type: str
        self.mp_4 = mp_4  # type: str
        self.name = name  # type: str
        self.oss_bucket = oss_bucket  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_file_prefix = oss_file_prefix  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.retention = retention  # type: long
        self.trans_configs_json = trans_configs_json  # type: str
        self.trigger = trigger  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
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


class OperateRenderingDevicesRequest(TeaModel):
    def __init__(self, instance_ids=None, operation=None, owner_id=None, pod_id=None):
        self.instance_ids = instance_ids  # type: str
        self.operation = operation  # type: str
        self.owner_id = owner_id  # type: long
        self.pod_id = pod_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateRenderingDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class OperateRenderingDevicesResponseBody(TeaModel):
    def __init__(self, failed_ids=None, request_id=None):
        self.failed_ids = failed_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateRenderingDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateRenderingDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OperateRenderingDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateRenderingDevicesResponse, self).to_map()
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
            temp_model = OperateRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PrepareUploadRequest(TeaModel):
    def __init__(self, bucket_name=None, client_ip=None, owner_id=None):
        self.bucket_name = bucket_name  # type: str
        self.client_ip = client_ip  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PrepareUploadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class PrepareUploadResponseBody(TeaModel):
    def __init__(self, bucket_name=None, endpoint=None, request_id=None):
        self.bucket_name = bucket_name  # type: str
        self.endpoint = endpoint  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PrepareUploadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, bucket_acl=None, bucket_name=None, comment=None, data_redundancy_type=None,
                 dispatcher_type=None, endpoint=None, owner_id=None, resource_type=None, storage_class=None):
        self.bucket_acl = bucket_acl  # type: str
        self.bucket_name = bucket_name  # type: str
        self.comment = comment  # type: str
        self.data_redundancy_type = data_redundancy_type  # type: str
        self.dispatcher_type = dispatcher_type  # type: str
        self.endpoint = endpoint  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_type = resource_type  # type: str
        self.storage_class = storage_class  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutBucketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
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


class ResetRenderingDevicesRequest(TeaModel):
    def __init__(self, image_id=None, instance_ids=None, owner_id=None, pod_id=None):
        self.image_id = image_id  # type: str
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long
        self.pod_id = pod_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetRenderingDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class ResetRenderingDevicesResponseBody(TeaModel):
    def __init__(self, failed_ids=None, request_id=None):
        self.failed_ids = failed_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetRenderingDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetRenderingDevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetRenderingDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetRenderingDevicesResponse, self).to_map()
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
            temp_model = ResetRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeVsStreamRequest(TeaModel):
    def __init__(self, app_name=None, control_stream_action=None, domain_name=None, live_stream_type=None,
                 owner_id=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.control_stream_action = control_stream_action  # type: str
        self.domain_name = domain_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.owner_id = owner_id  # type: long
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeVsStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
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
    def __init__(self, id=None, owner_id=None, preset_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.preset_id = preset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPresetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
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
    def __init__(self, cert_name=None, cert_type=None, domain_name=None, force_set=None, owner_id=None, region=None,
                 sslpri=None, sslprotocol=None, sslpub=None):
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.force_set = force_set  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.sslpri = sslpri  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVsDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
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
    def __init__(self, auth_key=None, auth_type=None, domain_name=None, notify_url=None, owner_id=None):
        self.auth_key = auth_key  # type: str
        self.auth_type = auth_type  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVsStreamsNotifyUrlConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, app=None, id=None, name=None, owner_id=None, play_domain=None):
        self.app = app  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.play_domain = play_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRecordStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
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
    def __init__(self, end_time=None, id=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: long
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StartStreamResponseBody(TeaModel):
    def __init__(self, id=None, name=None, request_id=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartStreamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, id=None, owner_id=None, transcode=None, url=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.transcode = transcode  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTransferStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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
    def __init__(self, focus=None, id=None, iris=None, owner_id=None):
        self.focus = focus  # type: bool
        self.id = id  # type: str
        self.iris = iris  # type: bool
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAdjustRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.focus is not None:
            result['Focus'] = self.focus
        if self.id is not None:
            result['Id'] = self.id
        if self.iris is not None:
            result['Iris'] = self.iris
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Iris') is not None:
            self.iris = m.get('Iris')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None, start_time=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None, pan=None, tilt=None, zoom=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.pan = pan  # type: bool
        self.tilt = tilt  # type: bool
        self.zoom = zoom  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopMoveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pan is not None:
            result['Pan'] = self.pan
        if self.tilt is not None:
            result['Tilt'] = self.tilt
        if self.zoom is not None:
            result['Zoom'] = self.zoom
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Pan') is not None:
            self.pan = m.get('Pan')
        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')
        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')
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


class StopParentPlatformRequest(TeaModel):
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopParentPlatformRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StopParentPlatformResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopParentPlatformResponseBody, self).to_map()
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


class StopParentPlatformResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopParentPlatformResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopParentPlatformResponse, self).to_map()
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
            temp_model = StopParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordStreamRequest(TeaModel):
    def __init__(self, app=None, id=None, name=None, owner_id=None, play_domain=None):
        self.app = app  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.play_domain = play_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRecordStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
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
    def __init__(self, id=None, name=None, owner_id=None, start_time=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None, transcode=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.transcode = transcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTransferStreamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncCatalogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, device_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncDeviceChannelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, device_id=None, directory_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.directory_id = directory_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, device_id=None, owner_id=None, parent_platform_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.parent_platform_id = parent_platform_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindParentPlatformDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
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
    def __init__(self, device_id=None, owner_id=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindPurchasedDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
    def __init__(self, instance_id=None, instance_type=None, owner_id=None, template_id=None, template_type=None):
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.owner_id = owner_id  # type: long
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class UnbindTemplateResponseBody(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, request_id=None, template_id=None, template_type=None):
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
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
    def __init__(self, id=None, owner_id=None):
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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


class UpdateAIConfigRequest(TeaModel):
    def __init__(self, capture_interval=None, config_id=None, configs=None, description=None, end_time=None,
                 features=None, owner_id=None, start_time=None, status=None):
        self.capture_interval = capture_interval  # type: int
        self.config_id = config_id  # type: str
        self.configs = configs  # type: str
        self.description = description  # type: str
        self.end_time = end_time  # type: long
        self.features = features  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAIConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAIConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAIConfigResponseBody, self).to_map()
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


class UpdateAIConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAIConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAIConfigResponse, self).to_map()
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
            temp_model = UpdateAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBucketInfoRequest(TeaModel):
    def __init__(self, bucket_name=None, comment=None, owner_id=None):
        self.bucket_name = bucket_name  # type: str
        self.comment = comment  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateBucketInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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


class UpdateClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, description=None, effective_time=None, internal_ports=None,
                 maintain_time=None, name=None, owner_id=None, security_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.effective_time = effective_time  # type: str
        self.internal_ports = internal_ports  # type: str
        self.maintain_time = maintain_time  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.internal_ports is not None:
            result['InternalPorts'] = self.internal_ports
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InternalPorts') is not None:
            self.internal_ports = m.get('InternalPorts')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class UpdateClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterResponseBody, self).to_map()
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


class UpdateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClusterResponse, self).to_map()
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
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRenderingDeviceSpecRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, description=None, effective_time=None,
                 instance_ids=None, owner_id=None, period=None, period_unit=None, specification=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: long
        self.description = description  # type: str
        self.effective_time = effective_time  # type: bool
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRenderingDeviceSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.description is not None:
            result['Description'] = self.description
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class UpdateRenderingDeviceSpecResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRenderingDeviceSpecResponseBody, self).to_map()
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


class UpdateRenderingDeviceSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateRenderingDeviceSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRenderingDeviceSpecResponse, self).to_map()
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
            temp_model = UpdateRenderingDeviceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, always=None, app_name=None, domain_name=None, end_time=None, owner_id=None, source_url=None,
                 start_time=None, stream_name=None):
        self.always = always  # type: str
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.source_url = source_url  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVsPullStreamInfoConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always is not None:
            result['Always'] = self.always
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Always') is not None:
            self.always = m.get('Always')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
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


class UpgradeRenderingDevicesHostOSRequest(TeaModel):
    def __init__(self, instance_ids=None, owner_id=None, rom_name=None, rom_path=None, rom_version=None):
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long
        self.rom_name = rom_name  # type: str
        self.rom_path = rom_path  # type: str
        self.rom_version = rom_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeRenderingDevicesHostOSRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rom_name is not None:
            result['RomName'] = self.rom_name
        if self.rom_path is not None:
            result['RomPath'] = self.rom_path
        if self.rom_version is not None:
            result['RomVersion'] = self.rom_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RomName') is not None:
            self.rom_name = m.get('RomName')
        if m.get('RomPath') is not None:
            self.rom_path = m.get('RomPath')
        if m.get('RomVersion') is not None:
            self.rom_version = m.get('RomVersion')
        return self


class UpgradeRenderingDevicesHostOSResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeRenderingDevicesHostOSResponseBody, self).to_map()
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


class UpgradeRenderingDevicesHostOSResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeRenderingDevicesHostOSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeRenderingDevicesHostOSResponse, self).to_map()
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
            temp_model = UpgradeRenderingDevicesHostOSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeRenderingDevicesImageRequest(TeaModel):
    def __init__(self, image_id=None, instance_ids=None, owner_id=None):
        self.image_id = image_id  # type: str
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeRenderingDevicesImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpgradeRenderingDevicesImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeRenderingDevicesImageResponseBody, self).to_map()
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


class UpgradeRenderingDevicesImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeRenderingDevicesImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeRenderingDevicesImageResponse, self).to_map()
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
            temp_model = UpgradeRenderingDevicesImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDeviceRecordRequest(TeaModel):
    def __init__(self, device_id=None, owner_id=None, search_criteria=None, stream_id=None, upload_id=None,
                 upload_mode=None, upload_params=None, upload_type=None):
        self.device_id = device_id  # type: str
        self.owner_id = owner_id  # type: long
        self.search_criteria = search_criteria  # type: str
        self.stream_id = stream_id  # type: str
        self.upload_id = upload_id  # type: str
        self.upload_mode = upload_mode  # type: str
        self.upload_params = upload_params  # type: str
        self.upload_type = upload_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadDeviceRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.search_criteria is not None:
            result['SearchCriteria'] = self.search_criteria
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        if self.upload_mode is not None:
            result['UploadMode'] = self.upload_mode
        if self.upload_params is not None:
            result['UploadParams'] = self.upload_params
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SearchCriteria') is not None:
            self.search_criteria = m.get('SearchCriteria')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')
        if m.get('UploadParams') is not None:
            self.upload_params = m.get('UploadParams')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
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


