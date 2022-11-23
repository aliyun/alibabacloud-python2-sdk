# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachEaiRequest(TeaModel):
    def __init__(self, client_instance_id=None, elastic_accelerated_instance_id=None, region_id=None):
        self.client_instance_id = client_instance_id  # type: str
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachEaiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachEaiResponseBody(TeaModel):
    def __init__(self, client_instance_id=None, elastic_accelerated_instance_id=None, request_id=None):
        self.client_instance_id = client_instance_id  # type: str
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachEaiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachEaiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachEaiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachEaiResponse, self).to_map()
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
            temp_model = AttachEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEaiRequest(TeaModel):
    def __init__(self, client_token=None, instance_name=None, instance_type=None, region_id=None,
                 security_group_id=None, v_switch_id=None):
        self.client_token = client_token  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateEaiResponseBody(TeaModel):
    def __init__(self, elastic_accelerated_instance_id=None, request_id=None):
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEaiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEaiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEaiResponse, self).to_map()
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
            temp_model = CreateEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEaiAllRequest(TeaModel):
    def __init__(self, client_image_id=None, client_instance_name=None, client_instance_type=None,
                 client_internet_max_bandwidth_in=None, client_internet_max_bandwidth_out=None, client_password=None,
                 client_security_group_id=None, client_system_disk_category=None, client_system_disk_size=None, client_token=None,
                 client_vswitch_id=None, client_zone_id=None, eai_instance_type=None, instance_name=None, region_id=None):
        self.client_image_id = client_image_id  # type: str
        self.client_instance_name = client_instance_name  # type: str
        self.client_instance_type = client_instance_type  # type: str
        self.client_internet_max_bandwidth_in = client_internet_max_bandwidth_in  # type: int
        self.client_internet_max_bandwidth_out = client_internet_max_bandwidth_out  # type: int
        self.client_password = client_password  # type: str
        self.client_security_group_id = client_security_group_id  # type: str
        self.client_system_disk_category = client_system_disk_category  # type: str
        self.client_system_disk_size = client_system_disk_size  # type: int
        self.client_token = client_token  # type: str
        self.client_vswitch_id = client_vswitch_id  # type: str
        self.client_zone_id = client_zone_id  # type: str
        self.eai_instance_type = eai_instance_type  # type: str
        self.instance_name = instance_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiAllRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_image_id is not None:
            result['ClientImageId'] = self.client_image_id
        if self.client_instance_name is not None:
            result['ClientInstanceName'] = self.client_instance_name
        if self.client_instance_type is not None:
            result['ClientInstanceType'] = self.client_instance_type
        if self.client_internet_max_bandwidth_in is not None:
            result['ClientInternetMaxBandwidthIn'] = self.client_internet_max_bandwidth_in
        if self.client_internet_max_bandwidth_out is not None:
            result['ClientInternetMaxBandwidthOut'] = self.client_internet_max_bandwidth_out
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_security_group_id is not None:
            result['ClientSecurityGroupId'] = self.client_security_group_id
        if self.client_system_disk_category is not None:
            result['ClientSystemDiskCategory'] = self.client_system_disk_category
        if self.client_system_disk_size is not None:
            result['ClientSystemDiskSize'] = self.client_system_disk_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_vswitch_id is not None:
            result['ClientVSwitchId'] = self.client_vswitch_id
        if self.client_zone_id is not None:
            result['ClientZoneId'] = self.client_zone_id
        if self.eai_instance_type is not None:
            result['EaiInstanceType'] = self.eai_instance_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientImageId') is not None:
            self.client_image_id = m.get('ClientImageId')
        if m.get('ClientInstanceName') is not None:
            self.client_instance_name = m.get('ClientInstanceName')
        if m.get('ClientInstanceType') is not None:
            self.client_instance_type = m.get('ClientInstanceType')
        if m.get('ClientInternetMaxBandwidthIn') is not None:
            self.client_internet_max_bandwidth_in = m.get('ClientInternetMaxBandwidthIn')
        if m.get('ClientInternetMaxBandwidthOut') is not None:
            self.client_internet_max_bandwidth_out = m.get('ClientInternetMaxBandwidthOut')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientSecurityGroupId') is not None:
            self.client_security_group_id = m.get('ClientSecurityGroupId')
        if m.get('ClientSystemDiskCategory') is not None:
            self.client_system_disk_category = m.get('ClientSystemDiskCategory')
        if m.get('ClientSystemDiskSize') is not None:
            self.client_system_disk_size = m.get('ClientSystemDiskSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientVSwitchId') is not None:
            self.client_vswitch_id = m.get('ClientVSwitchId')
        if m.get('ClientZoneId') is not None:
            self.client_zone_id = m.get('ClientZoneId')
        if m.get('EaiInstanceType') is not None:
            self.eai_instance_type = m.get('EaiInstanceType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEaiAllResponseBody(TeaModel):
    def __init__(self, client_instance_id=None, elastic_accelerated_instance_id=None, request_id=None):
        self.client_instance_id = client_instance_id  # type: str
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiAllResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEaiAllResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEaiAllResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEaiAllResponse, self).to_map()
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
            temp_model = CreateEaiAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEaiJupyterRequestEnvironmentVar(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiJupyterRequestEnvironmentVar, self).to_map()
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


class CreateEaiJupyterRequest(TeaModel):
    def __init__(self, client_token=None, eais_type=None, environment_var=None, region_id=None,
                 security_group_id=None, v_switch_id=None):
        self.client_token = client_token  # type: str
        self.eais_type = eais_type  # type: str
        self.environment_var = environment_var  # type: list[CreateEaiJupyterRequestEnvironmentVar]
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        if self.environment_var:
            for k in self.environment_var:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEaiJupyterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.eais_type is not None:
            result['EaisType'] = self.eais_type
        result['EnvironmentVar'] = []
        if self.environment_var is not None:
            for k in self.environment_var:
                result['EnvironmentVar'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EaisType') is not None:
            self.eais_type = m.get('EaisType')
        self.environment_var = []
        if m.get('EnvironmentVar') is not None:
            for k in m.get('EnvironmentVar'):
                temp_model = CreateEaiJupyterRequestEnvironmentVar()
                self.environment_var.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateEaiJupyterShrinkRequest(TeaModel):
    def __init__(self, client_token=None, eais_type=None, environment_var_shrink=None, region_id=None,
                 security_group_id=None, v_switch_id=None):
        self.client_token = client_token  # type: str
        self.eais_type = eais_type  # type: str
        self.environment_var_shrink = environment_var_shrink  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiJupyterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.eais_type is not None:
            result['EaisType'] = self.eais_type
        if self.environment_var_shrink is not None:
            result['EnvironmentVar'] = self.environment_var_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EaisType') is not None:
            self.eais_type = m.get('EaisType')
        if m.get('EnvironmentVar') is not None:
            self.environment_var_shrink = m.get('EnvironmentVar')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateEaiJupyterResponseBody(TeaModel):
    def __init__(self, elastic_accelerated_instance_id=None, request_id=None):
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEaiJupyterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEaiJupyterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEaiJupyterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEaiJupyterResponse, self).to_map()
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
            temp_model = CreateEaiJupyterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEaiRequest(TeaModel):
    def __init__(self, elastic_accelerated_instance_id=None, force=None, region_id=None):
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.force = force  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEaiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.force is not None:
            result['Force'] = self.force
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteEaiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEaiResponseBody, self).to_map()
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


class DeleteEaiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEaiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEaiResponse, self).to_map()
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
            temp_model = DeleteEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEaiAllRequest(TeaModel):
    def __init__(self, client_instance_id=None, elastic_accelerated_instance_id=None, region_id=None):
        self.client_instance_id = client_instance_id  # type: str
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEaiAllRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteEaiAllResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEaiAllResponseBody, self).to_map()
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


class DeleteEaiAllResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEaiAllResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEaiAllResponse, self).to_map()
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
            temp_model = DeleteEaiAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEaisRequest(TeaModel):
    def __init__(self, elastic_accelerated_instance_ids=None, instance_name=None, instance_type=None,
                 page_number=None, page_size=None, region_id=None, status=None):
        self.elastic_accelerated_instance_ids = elastic_accelerated_instance_ids  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEaisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_accelerated_instance_ids is not None:
            result['ElasticAcceleratedInstanceIds'] = self.elastic_accelerated_instance_ids
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticAcceleratedInstanceIds') is not None:
            self.elastic_accelerated_instance_ids = m.get('ElasticAcceleratedInstanceIds')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEaisResponseBodyInstancesInstanceTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEaisResponseBodyInstancesInstanceTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeEaisResponseBodyInstancesInstanceTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeEaisResponseBodyInstancesInstanceTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEaisResponseBodyInstancesInstanceTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeEaisResponseBodyInstancesInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeEaisResponseBodyInstancesInstance(TeaModel):
    def __init__(self, category=None, client_instance_id=None, client_instance_name=None,
                 client_instance_type=None, creation_time=None, description=None, elastic_accelerated_instance_id=None,
                 instance_name=None, instance_type=None, jupyter_url=None, region_id=None, security_group_id=None,
                 start_time=None, status=None, tags=None, v_switch_id=None, zone_id=None):
        self.category = category  # type: str
        self.client_instance_id = client_instance_id  # type: str
        self.client_instance_name = client_instance_name  # type: str
        self.client_instance_type = client_instance_type  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_type = instance_type  # type: str
        self.jupyter_url = jupyter_url  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeEaisResponseBodyInstancesInstanceTags
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeEaisResponseBodyInstancesInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.client_instance_name is not None:
            result['ClientInstanceName'] = self.client_instance_name
        if self.client_instance_type is not None:
            result['ClientInstanceType'] = self.client_instance_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.jupyter_url is not None:
            result['JupyterUrl'] = self.jupyter_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ClientInstanceName') is not None:
            self.client_instance_name = m.get('ClientInstanceName')
        if m.get('ClientInstanceType') is not None:
            self.client_instance_type = m.get('ClientInstanceType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('JupyterUrl') is not None:
            self.jupyter_url = m.get('JupyterUrl')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeEaisResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeEaisResponseBodyInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[DescribeEaisResponseBodyInstancesInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEaisResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeEaisResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeEaisResponseBody(TeaModel):
    def __init__(self, instances=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.instances = instances  # type: DescribeEaisResponseBodyInstances
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(DescribeEaisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeEaisResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEaisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEaisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEaisResponse, self).to_map()
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
            temp_model = DescribeEaisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachEaiRequest(TeaModel):
    def __init__(self, elastic_accelerated_instance_id=None, region_id=None):
        self.elastic_accelerated_instance_id = elastic_accelerated_instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachEaiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachEaiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachEaiResponseBody, self).to_map()
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


class DetachEaiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachEaiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachEaiResponse, self).to_map()
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
            temp_model = DetachEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


