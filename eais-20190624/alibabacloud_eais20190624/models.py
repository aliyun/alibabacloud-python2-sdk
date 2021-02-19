# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AttachEaiRequest(TeaModel):
    def __init__(self, region_id=None, elastic_accelerated_instance_id=None, client_instance_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode
        self.client_instance_id = TeaConverter.to_unicode(client_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        return self


class AttachEaiResponseBody(TeaModel):
    def __init__(self, request_id=None, client_instance_id=None, elastic_accelerated_instance_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.client_instance_id = TeaConverter.to_unicode(client_instance_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        return self


class AttachEaiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachEaiResponseBody

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
            temp_model = AttachEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEaiRequest(TeaModel):
    def __init__(self, region_id=None, instance_type=None, client_token=None, instance_name=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class CreateEaiResponseBody(TeaModel):
    def __init__(self, request_id=None, elastic_accelerated_instance_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        return self


class CreateEaiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateEaiResponseBody

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
            temp_model = CreateEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEaiAllRequest(TeaModel):
    def __init__(self, region_id=None, eai_instance_type=None, client_vswitch_id=None,
                 client_security_group_id=None, client_image_id=None, client_instance_type=None, client_zone_id=None,
                 client_instance_name=None, client_password=None, client_internet_max_bandwidth_in=None,
                 client_internet_max_bandwidth_out=None, client_system_disk_category=None, client_system_disk_size=None, client_token=None,
                 instance_name=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.eai_instance_type = TeaConverter.to_unicode(eai_instance_type)  # type: unicode
        self.client_vswitch_id = TeaConverter.to_unicode(client_vswitch_id)  # type: unicode
        self.client_security_group_id = TeaConverter.to_unicode(client_security_group_id)  # type: unicode
        self.client_image_id = TeaConverter.to_unicode(client_image_id)  # type: unicode
        self.client_instance_type = TeaConverter.to_unicode(client_instance_type)  # type: unicode
        self.client_zone_id = TeaConverter.to_unicode(client_zone_id)  # type: unicode
        self.client_instance_name = TeaConverter.to_unicode(client_instance_name)  # type: unicode
        self.client_password = TeaConverter.to_unicode(client_password)  # type: unicode
        self.client_internet_max_bandwidth_in = client_internet_max_bandwidth_in  # type: int
        self.client_internet_max_bandwidth_out = client_internet_max_bandwidth_out  # type: int
        self.client_system_disk_category = TeaConverter.to_unicode(client_system_disk_category)  # type: unicode
        self.client_system_disk_size = client_system_disk_size  # type: int
        self.client_token = TeaConverter.to_unicode(client_token)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.eai_instance_type is not None:
            result['EaiInstanceType'] = self.eai_instance_type
        if self.client_vswitch_id is not None:
            result['ClientVSwitchId'] = self.client_vswitch_id
        if self.client_security_group_id is not None:
            result['ClientSecurityGroupId'] = self.client_security_group_id
        if self.client_image_id is not None:
            result['ClientImageId'] = self.client_image_id
        if self.client_instance_type is not None:
            result['ClientInstanceType'] = self.client_instance_type
        if self.client_zone_id is not None:
            result['ClientZoneId'] = self.client_zone_id
        if self.client_instance_name is not None:
            result['ClientInstanceName'] = self.client_instance_name
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_internet_max_bandwidth_in is not None:
            result['ClientInternetMaxBandwidthIn'] = self.client_internet_max_bandwidth_in
        if self.client_internet_max_bandwidth_out is not None:
            result['ClientInternetMaxBandwidthOut'] = self.client_internet_max_bandwidth_out
        if self.client_system_disk_category is not None:
            result['ClientSystemDiskCategory'] = self.client_system_disk_category
        if self.client_system_disk_size is not None:
            result['ClientSystemDiskSize'] = self.client_system_disk_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EaiInstanceType') is not None:
            self.eai_instance_type = m.get('EaiInstanceType')
        if m.get('ClientVSwitchId') is not None:
            self.client_vswitch_id = m.get('ClientVSwitchId')
        if m.get('ClientSecurityGroupId') is not None:
            self.client_security_group_id = m.get('ClientSecurityGroupId')
        if m.get('ClientImageId') is not None:
            self.client_image_id = m.get('ClientImageId')
        if m.get('ClientInstanceType') is not None:
            self.client_instance_type = m.get('ClientInstanceType')
        if m.get('ClientZoneId') is not None:
            self.client_zone_id = m.get('ClientZoneId')
        if m.get('ClientInstanceName') is not None:
            self.client_instance_name = m.get('ClientInstanceName')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientInternetMaxBandwidthIn') is not None:
            self.client_internet_max_bandwidth_in = m.get('ClientInternetMaxBandwidthIn')
        if m.get('ClientInternetMaxBandwidthOut') is not None:
            self.client_internet_max_bandwidth_out = m.get('ClientInternetMaxBandwidthOut')
        if m.get('ClientSystemDiskCategory') is not None:
            self.client_system_disk_category = m.get('ClientSystemDiskCategory')
        if m.get('ClientSystemDiskSize') is not None:
            self.client_system_disk_size = m.get('ClientSystemDiskSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class CreateEaiAllResponseBody(TeaModel):
    def __init__(self, request_id=None, client_instance_id=None, elastic_accelerated_instance_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.client_instance_id = TeaConverter.to_unicode(client_instance_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        return self


class CreateEaiAllResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateEaiAllResponseBody

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
            temp_model = CreateEaiAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEaiRequest(TeaModel):
    def __init__(self, region_id=None, elastic_accelerated_instance_id=None, force=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteEaiResponseBody(TeaModel):
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


class DeleteEaiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteEaiResponseBody

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
            temp_model = DeleteEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEaiAllRequest(TeaModel):
    def __init__(self, region_id=None, elastic_accelerated_instance_id=None, client_instance_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode
        self.client_instance_id = TeaConverter.to_unicode(client_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        return self


class DeleteEaiAllResponseBody(TeaModel):
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


class DeleteEaiAllResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteEaiAllResponseBody

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
            temp_model = DeleteEaiAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEaisRequest(TeaModel):
    def __init__(self, region_id=None, elastic_accelerated_instance_ids=None, instance_name=None, status=None,
                 instance_type=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.elastic_accelerated_instance_ids = TeaConverter.to_unicode(elastic_accelerated_instance_ids)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.elastic_accelerated_instance_ids is not None:
            result['ElasticAcceleratedInstanceIds'] = self.elastic_accelerated_instance_ids
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ElasticAcceleratedInstanceIds') is not None:
            self.elastic_accelerated_instance_ids = m.get('ElasticAcceleratedInstanceIds')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeEaisResponseBodyInstancesInstanceTagsTag(TeaModel):
    def __init__(self, tag_value=None, tag_key=None):
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
    def __init__(self, status=None, creation_time=None, client_instance_type=None, client_instance_id=None,
                 tags=None, instance_type=None, region_id=None, client_instance_name=None, description=None,
                 elastic_accelerated_instance_id=None, instance_name=None, zone_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.client_instance_type = TeaConverter.to_unicode(client_instance_type)  # type: unicode
        self.client_instance_id = TeaConverter.to_unicode(client_instance_id)  # type: unicode
        self.tags = tags  # type: DescribeEaisResponseBodyInstancesInstanceTags
        self.instance_type = TeaConverter.to_unicode(instance_type)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.client_instance_name = TeaConverter.to_unicode(client_instance_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode
        self.instance_name = TeaConverter.to_unicode(instance_name)  # type: unicode
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.client_instance_type is not None:
            result['ClientInstanceType'] = self.client_instance_type
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_instance_name is not None:
            result['ClientInstanceName'] = self.client_instance_name
        if self.description is not None:
            result['Description'] = self.description
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ClientInstanceType') is not None:
            self.client_instance_type = m.get('ClientInstanceType')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        if m.get('Tags') is not None:
            temp_model = DescribeEaisResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInstanceName') is not None:
            self.client_instance_name = m.get('ClientInstanceName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
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
    def __init__(self, instances=None, total_count=None, request_id=None, page_size=None, page_number=None):
        self.instances = instances  # type: DescribeEaisResponseBodyInstances
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeEaisResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeEaisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeEaisResponseBody

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
            temp_model = DescribeEaisResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class DetachEaiRequest(TeaModel):
    def __init__(self, region_id=None, elastic_accelerated_instance_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.elastic_accelerated_instance_id = TeaConverter.to_unicode(elastic_accelerated_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.elastic_accelerated_instance_id is not None:
            result['ElasticAcceleratedInstanceId'] = self.elastic_accelerated_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ElasticAcceleratedInstanceId') is not None:
            self.elastic_accelerated_instance_id = m.get('ElasticAcceleratedInstanceId')
        return self


class DetachEaiResponseBody(TeaModel):
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


class DetachEaiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachEaiResponseBody

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
            temp_model = DetachEaiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrivateIpRequest(TeaModel):
    def __init__(self, region_id=None, client_instance_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.client_instance_id = TeaConverter.to_unicode(client_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_instance_id is not None:
            result['ClientInstanceId'] = self.client_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientInstanceId') is not None:
            self.client_instance_id = m.get('ClientInstanceId')
        return self


class GetPrivateIpResponseBody(TeaModel):
    def __init__(self, request_id=None, private_ip=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.private_ip = TeaConverter.to_unicode(private_ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        return self


class GetPrivateIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetPrivateIpResponseBody

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
            temp_model = GetPrivateIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


