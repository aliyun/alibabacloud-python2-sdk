# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BindInstance2VpcRequest(TeaModel):
    def __init__(self, instance_name=None, instance_vpc_name=None, network=None, region_no=None,
                 resource_owner_id=None, virtual_switch_id=None, vpc_id=None):
        self.instance_name = instance_name  # type: str
        self.instance_vpc_name = instance_vpc_name  # type: str
        self.network = network  # type: str
        self.region_no = region_no  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.virtual_switch_id = virtual_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindInstance2VpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.network is not None:
            result['Network'] = self.network
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.virtual_switch_id is not None:
            result['VirtualSwitchId'] = self.virtual_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VirtualSwitchId') is not None:
            self.virtual_switch_id = m.get('VirtualSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class BindInstance2VpcResponseBody(TeaModel):
    def __init__(self, domain=None, endpoint=None, request_id=None):
        self.domain = domain  # type: str
        self.endpoint = endpoint  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindInstance2VpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindInstance2VpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindInstance2VpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindInstance2VpcResponse, self).to_map()
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
            temp_model = BindInstance2VpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, resource_owner_id=None):
        self.instance_name = instance_name  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagsRequestTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagsRequestTagInfo, self).to_map()
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


class DeleteTagsRequest(TeaModel):
    def __init__(self, instance_name=None, resource_owner_id=None, tag_info=None):
        self.instance_name = instance_name  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_info = tag_info  # type: list[DeleteTagsRequestTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = DeleteTagsRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class DeleteTagsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagsResponseBody, self).to_map()
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


class DeleteTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagsResponse, self).to_map()
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
            temp_model = DeleteTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, resource_owner_id=None):
        self.instance_name = instance_name  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetInstanceResponseBodyInstanceInfoQuota(TeaModel):
    def __init__(self, entity_quota=None):
        self.entity_quota = entity_quota  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceInfoQuota, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_quota is not None:
            result['EntityQuota'] = self.entity_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityQuota') is not None:
            self.entity_quota = m.get('EntityQuota')
        return self


class GetInstanceResponseBodyInstanceInfoTagInfosTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceInfoTagInfosTagInfo, self).to_map()
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


class GetInstanceResponseBodyInstanceInfoTagInfos(TeaModel):
    def __init__(self, tag_info=None):
        self.tag_info = tag_info  # type: list[GetInstanceResponseBodyInstanceInfoTagInfosTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceInfoTagInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = GetInstanceResponseBodyInstanceInfoTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class GetInstanceResponseBodyInstanceInfo(TeaModel):
    def __init__(self, cluster_type=None, create_time=None, description=None, instance_name=None, network=None,
                 quota=None, read_capacity=None, status=None, tag_infos=None, user_id=None, write_capacity=None):
        self.cluster_type = cluster_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.instance_name = instance_name  # type: str
        self.network = network  # type: str
        self.quota = quota  # type: GetInstanceResponseBodyInstanceInfoQuota
        self.read_capacity = read_capacity  # type: int
        self.status = status  # type: int
        self.tag_infos = tag_infos  # type: GetInstanceResponseBodyInstanceInfoTagInfos
        self.user_id = user_id  # type: str
        self.write_capacity = write_capacity  # type: int

    def validate(self):
        if self.quota:
            self.quota.validate()
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBodyInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.network is not None:
            result['Network'] = self.network
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.read_capacity is not None:
            result['ReadCapacity'] = self.read_capacity
        if self.status is not None:
            result['Status'] = self.status
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.write_capacity is not None:
            result['WriteCapacity'] = self.write_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Quota') is not None:
            temp_model = GetInstanceResponseBodyInstanceInfoQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('ReadCapacity') is not None:
            self.read_capacity = m.get('ReadCapacity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TagInfos') is not None:
            temp_model = GetInstanceResponseBodyInstanceInfoTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WriteCapacity') is not None:
            self.write_capacity = m.get('WriteCapacity')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(self, instance_info=None, request_id=None):
        self.instance_info = instance_info  # type: GetInstanceResponseBodyInstanceInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super(GetInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceInfo') is not None:
            temp_model = GetInstanceResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceResponse, self).to_map()
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOtsServiceStatusRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOtsServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetOtsServiceStatusResponseBody(TeaModel):
    def __init__(self, data=None, dynamic_code=None, dynamic_message=None, err_code=None, http_status_code=None,
                 message=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.dynamic_code = dynamic_code  # type: str
        self.dynamic_message = dynamic_message  # type: str
        self.err_code = err_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOtsServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOtsServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOtsServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOtsServiceStatusResponse, self).to_map()
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
            temp_model = GetOtsServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertInstanceRequestTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInstanceRequestTagInfo, self).to_map()
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


class InsertInstanceRequest(TeaModel):
    def __init__(self, cluster_type=None, description=None, instance_name=None, network=None,
                 resource_owner_id=None, tag_info=None):
        self.cluster_type = cluster_type  # type: str
        self.description = description  # type: str
        self.instance_name = instance_name  # type: str
        self.network = network  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_info = tag_info  # type: list[InsertInstanceRequestTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InsertInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.network is not None:
            result['Network'] = self.network
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = InsertInstanceRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class InsertInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInstanceResponseBody, self).to_map()
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


class InsertInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertInstanceResponse, self).to_map()
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
            temp_model = InsertInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTagsRequestTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTagsRequestTagInfo, self).to_map()
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


class InsertTagsRequest(TeaModel):
    def __init__(self, instance_name=None, resource_owner_id=None, tag_info=None):
        self.instance_name = instance_name  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_info = tag_info  # type: list[InsertTagsRequestTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InsertTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = InsertTagsRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class InsertTagsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTagsResponseBody, self).to_map()
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


class InsertTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertTagsResponse, self).to_map()
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
            temp_model = InsertTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterTypeRequest(TeaModel):
    def __init__(self, resource_owner_id=None):
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail(TeaModel):
    def __init__(self, cluster_type=None, is_multi_az=None):
        self.cluster_type = cluster_type  # type: str
        self.is_multi_az = is_multi_az  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.is_multi_az is not None:
            result['IsMultiAZ'] = self.is_multi_az
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('IsMultiAZ') is not None:
            self.is_multi_az = m.get('IsMultiAZ')
        return self


class ListClusterTypeResponseBodyClusterTypeDetailList(TeaModel):
    def __init__(self, cluster_type_detail=None):
        self.cluster_type_detail = cluster_type_detail  # type: list[ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail]

    def validate(self):
        if self.cluster_type_detail:
            for k in self.cluster_type_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterTypeResponseBodyClusterTypeDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterTypeDetail'] = []
        if self.cluster_type_detail is not None:
            for k in self.cluster_type_detail:
                result['ClusterTypeDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_type_detail = []
        if m.get('ClusterTypeDetail') is not None:
            for k in m.get('ClusterTypeDetail'):
                temp_model = ListClusterTypeResponseBodyClusterTypeDetailListClusterTypeDetail()
                self.cluster_type_detail.append(temp_model.from_map(k))
        return self


class ListClusterTypeResponseBodyClusterTypeInfos(TeaModel):
    def __init__(self, cluster_type=None):
        self.cluster_type = cluster_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterTypeResponseBodyClusterTypeInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListClusterTypeResponseBody(TeaModel):
    def __init__(self, cluster_type_detail_list=None, cluster_type_infos=None, request_id=None):
        self.cluster_type_detail_list = cluster_type_detail_list  # type: ListClusterTypeResponseBodyClusterTypeDetailList
        self.cluster_type_infos = cluster_type_infos  # type: ListClusterTypeResponseBodyClusterTypeInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster_type_detail_list:
            self.cluster_type_detail_list.validate()
        if self.cluster_type_infos:
            self.cluster_type_infos.validate()

    def to_map(self):
        _map = super(ListClusterTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type_detail_list is not None:
            result['ClusterTypeDetailList'] = self.cluster_type_detail_list.to_map()
        if self.cluster_type_infos is not None:
            result['ClusterTypeInfos'] = self.cluster_type_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterTypeDetailList') is not None:
            temp_model = ListClusterTypeResponseBodyClusterTypeDetailList()
            self.cluster_type_detail_list = temp_model.from_map(m['ClusterTypeDetailList'])
        if m.get('ClusterTypeInfos') is not None:
            temp_model = ListClusterTypeResponseBodyClusterTypeInfos()
            self.cluster_type_infos = temp_model.from_map(m['ClusterTypeInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterTypeResponse, self).to_map()
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
            temp_model = ListClusterTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequestTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceRequestTagInfo, self).to_map()
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


class ListInstanceRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, resource_owner_id=None, tag_info=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_info = tag_info  # type: list[ListInstanceRequestTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListInstanceRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListInstanceResponseBodyInstanceInfosInstanceInfo(TeaModel):
    def __init__(self, instance_name=None, timestamp=None):
        self.instance_name = instance_name  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstanceResponseBodyInstanceInfosInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListInstanceResponseBodyInstanceInfos(TeaModel):
    def __init__(self, instance_info=None):
        self.instance_info = instance_info  # type: list[ListInstanceResponseBodyInstanceInfosInstanceInfo]

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBodyInstanceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = ListInstanceResponseBodyInstanceInfosInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(self, instance_infos=None, page_num=None, page_size=None, request_id=None, total_count=None):
        self.instance_infos = instance_infos  # type: ListInstanceResponseBodyInstanceInfos
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instance_infos:
            self.instance_infos.validate()

    def to_map(self):
        _map = super(ListInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos.to_map()
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
        if m.get('InstanceInfos') is not None:
            temp_model = ListInstanceResponseBodyInstanceInfos()
            self.instance_infos = temp_model.from_map(m['InstanceInfos'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstanceResponse, self).to_map()
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequestTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsRequestTagInfo, self).to_map()
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


class ListTagsRequest(TeaModel):
    def __init__(self, instance_name=None, page_num=None, page_size=None, resource_owner_id=None, tag_info=None):
        self.instance_name = instance_name  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_info = tag_info  # type: list[ListTagsRequestTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListTagsRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListTagsResponseBodyTagInfosTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsResponseBodyTagInfosTagInfo, self).to_map()
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


class ListTagsResponseBodyTagInfos(TeaModel):
    def __init__(self, tag_info=None):
        self.tag_info = tag_info  # type: list[ListTagsResponseBodyTagInfosTagInfo]

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsResponseBodyTagInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListTagsResponseBodyTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, tag_infos=None, total_count=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.tag_infos = tag_infos  # type: ListTagsResponseBodyTagInfos
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        _map = super(ListTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagInfos') is not None:
            temp_model = ListTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagsResponse, self).to_map()
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcInfoByInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, page_num=None, page_size=None, resource_owner_id=None):
        self.instance_name = instance_name  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcInfoByInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo(TeaModel):
    def __init__(self, domain=None, endpoint=None, instance_vpc_name=None, region_no=None, vpc_id=None):
        self.domain = domain  # type: str
        self.endpoint = endpoint  # type: str
        self.instance_vpc_name = instance_vpc_name  # type: str
        self.region_no = region_no  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcInfoByInstanceResponseBodyVpcInfos(TeaModel):
    def __init__(self, vpc_info=None):
        self.vpc_info = vpc_info  # type: list[ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo]

    def validate(self):
        if self.vpc_info:
            for k in self.vpc_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcInfoByInstanceResponseBodyVpcInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcInfo'] = []
        if self.vpc_info is not None:
            for k in self.vpc_info:
                result['VpcInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpc_info = []
        if m.get('VpcInfo') is not None:
            for k in m.get('VpcInfo'):
                temp_model = ListVpcInfoByInstanceResponseBodyVpcInfosVpcInfo()
                self.vpc_info.append(temp_model.from_map(k))
        return self


class ListVpcInfoByInstanceResponseBody(TeaModel):
    def __init__(self, instance_name=None, page_num=None, page_size=None, request_id=None, total_count=None,
                 vpc_infos=None):
        self.instance_name = instance_name  # type: str
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.vpc_infos = vpc_infos  # type: ListVpcInfoByInstanceResponseBodyVpcInfos

    def validate(self):
        if self.vpc_infos:
            self.vpc_infos.validate()

    def to_map(self):
        _map = super(ListVpcInfoByInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpc_infos is not None:
            result['VpcInfos'] = self.vpc_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VpcInfos') is not None:
            temp_model = ListVpcInfoByInstanceResponseBodyVpcInfos()
            self.vpc_infos = temp_model.from_map(m['VpcInfos'])
        return self


class ListVpcInfoByInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcInfoByInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcInfoByInstanceResponse, self).to_map()
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
            temp_model = ListVpcInfoByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcInfoByVpcRequestTagInfo(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcInfoByVpcRequestTagInfo, self).to_map()
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


class ListVpcInfoByVpcRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, resource_owner_id=None, tag_info=None, vpc_id=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_id = resource_owner_id  # type: long
        self.tag_info = tag_info  # type: list[ListVpcInfoByVpcRequestTagInfo]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcInfoByVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListVpcInfoByVpcRequestTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo(TeaModel):
    def __init__(self, domain=None, endpoint=None, instance_name=None, instance_vpc_name=None, region_no=None):
        self.domain = domain  # type: str
        self.endpoint = endpoint  # type: str
        self.instance_name = instance_name  # type: str
        self.instance_vpc_name = instance_vpc_name  # type: str
        self.region_no = region_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class ListVpcInfoByVpcResponseBodyVpcInfos(TeaModel):
    def __init__(self, vpc_info=None):
        self.vpc_info = vpc_info  # type: list[ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo]

    def validate(self):
        if self.vpc_info:
            for k in self.vpc_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcInfoByVpcResponseBodyVpcInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcInfo'] = []
        if self.vpc_info is not None:
            for k in self.vpc_info:
                result['VpcInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpc_info = []
        if m.get('VpcInfo') is not None:
            for k in m.get('VpcInfo'):
                temp_model = ListVpcInfoByVpcResponseBodyVpcInfosVpcInfo()
                self.vpc_info.append(temp_model.from_map(k))
        return self


class ListVpcInfoByVpcResponseBody(TeaModel):
    def __init__(self, page_num=None, page_size=None, request_id=None, total_count=None, vpc_id=None, vpc_infos=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.vpc_id = vpc_id  # type: str
        self.vpc_infos = vpc_infos  # type: ListVpcInfoByVpcResponseBodyVpcInfos

    def validate(self):
        if self.vpc_infos:
            self.vpc_infos.validate()

    def to_map(self):
        _map = super(ListVpcInfoByVpcResponseBody, self).to_map()
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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_infos is not None:
            result['VpcInfos'] = self.vpc_infos.to_map()
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
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInfos') is not None:
            temp_model = ListVpcInfoByVpcResponseBodyVpcInfos()
            self.vpc_infos = temp_model.from_map(m['VpcInfos'])
        return self


class ListVpcInfoByVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcInfoByVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcInfoByVpcResponse, self).to_map()
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
            temp_model = ListVpcInfoByVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenOtsServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenOtsServiceResponseBody, self).to_map()
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


class OpenOtsServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenOtsServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenOtsServiceResponse, self).to_map()
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
            temp_model = OpenOtsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindInstance2VpcRequest(TeaModel):
    def __init__(self, instance_name=None, instance_vpc_name=None, region_no=None, resource_owner_id=None):
        self.instance_name = instance_name  # type: str
        self.instance_vpc_name = instance_vpc_name  # type: str
        self.region_no = region_no  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindInstance2VpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UnbindInstance2VpcResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindInstance2VpcResponseBody, self).to_map()
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


class UnbindInstance2VpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindInstance2VpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindInstance2VpcResponse, self).to_map()
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
            temp_model = UnbindInstance2VpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, instance_name=None, network=None, resource_owner_id=None):
        self.instance_name = instance_name  # type: str
        self.network = network  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.network is not None:
            result['Network'] = self.network
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
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


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


