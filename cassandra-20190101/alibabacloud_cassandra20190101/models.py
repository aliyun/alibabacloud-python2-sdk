# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocatePublicContactPointsRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None, data_center_id=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePublicContactPointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class AllocatePublicContactPointsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AllocatePublicContactPointsResponseBody, self).to_map()
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


class AllocatePublicContactPointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AllocatePublicContactPointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AllocatePublicContactPointsResponse, self).to_map()
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
            temp_model = AllocatePublicContactPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(self, active=None, backup_period=None, backup_time=None, client_token=None, cluster_id=None,
                 data_center_id=None, retention_period=None):
        self.active = active  # type: bool
        self.backup_period = backup_period  # type: str
        self.backup_time = backup_time  # type: str
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.retention_period = retention_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        return self


class CreateBackupPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBackupPlanResponseBody, self).to_map()
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


class CreateBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateBackupPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBackupPlanResponse, self).to_map()
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
            temp_model = CreateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, client_token=None, cluster_name=None,
                 data_center_name=None, disk_size=None, disk_type=None, instance_type=None, major_version=None, node_count=None,
                 password=None, pay_type=None, period=None, period_unit=None, region_id=None, resource_group_id=None,
                 vpc_id=None, vswitch_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.cluster_name = cluster_name  # type: str
        self.data_center_name = data_center_name  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str
        self.instance_type = instance_type  # type: str
        self.major_version = major_version  # type: str
        self.node_count = node_count  # type: int
        self.password = password  # type: str
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.password is not None:
            result['Password'] = self.password
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCenterRequest(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, client_token=None, cluster_id=None,
                 data_center_name=None, disk_size=None, disk_type=None, instance_type=None, node_count=None, pay_type=None,
                 period=None, period_unit=None, region_id=None, vpc_id=None, vswitch_id=None, zone_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.auto_renew_period = auto_renew_period  # type: int
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_name = data_center_name  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str
        self.instance_type = instance_type  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCenterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDataCenterResponseBody(TeaModel):
    def __init__(self, data_center_id=None, request_id=None):
        self.data_center_id = data_center_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataCenterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataCenterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDataCenterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataCenterResponse, self).to_map()
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
            temp_model = CreateDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupPlanRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DeleteBackupPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBackupPlanResponseBody, self).to_map()
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


class DeleteBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBackupPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBackupPlanResponse, self).to_map()
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
            temp_model = DeleteBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataCenterRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataCenterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DeleteDataCenterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataCenterResponseBody, self).to_map()
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


class DeleteDataCenterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataCenterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataCenterResponse, self).to_map()
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
            temp_model = DeleteDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodeToolExecutionHistoryRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None, job_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodeToolExecutionHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteNodeToolExecutionHistoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodeToolExecutionHistoryResponseBody, self).to_map()
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


class DeleteNodeToolExecutionHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNodeToolExecutionHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNodeToolExecutionHistoryResponse, self).to_map()
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
            temp_model = DeleteNodeToolExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccountsAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account  # type: list[DescribeAccountsResponseBodyAccountsAccount]

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBodyAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = DescribeAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(self, accounts=None, request_id=None):
        self.accounts = accounts  # type: DescribeAccountsResponseBodyAccounts
        self.request_id = request_id  # type: str

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccountsResponse, self).to_map()
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupRequest(TeaModel):
    def __init__(self, backup_id=None, backup_type=None, cluster_id=None, data_center_id=None):
        self.backup_id = backup_id  # type: str
        self.backup_type = backup_type  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeBackupResponseBodyBackup(TeaModel):
    def __init__(self, backup_id=None, backup_type=None, cluster_id=None, data_center_id=None, details=None,
                 end_time=None, size=None, start_time=None, status=None):
        self.backup_id = backup_id  # type: str
        self.backup_type = backup_type  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.details = details  # type: str
        self.end_time = end_time  # type: str
        self.size = size  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupResponseBodyBackup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.details is not None:
            result['Details'] = self.details
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupResponseBody(TeaModel):
    def __init__(self, backup=None, request_id=None):
        self.backup = backup  # type: DescribeBackupResponseBodyBackup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.backup:
            self.backup.validate()

    def to_map(self):
        _map = super(DescribeBackupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup is not None:
            result['Backup'] = self.backup.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backup') is not None:
            temp_model = DescribeBackupResponseBodyBackup()
            self.backup = temp_model.from_map(m['Backup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupResponse, self).to_map()
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
            temp_model = DescribeBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeBackupPlanResponseBodyBackupPlan(TeaModel):
    def __init__(self, active=None, backup_period=None, backup_time=None, cluster_id=None, created_time=None,
                 data_center_id=None, retention_period=None):
        self.active = active  # type: bool
        self.backup_period = backup_period  # type: str
        self.backup_time = backup_time  # type: str
        self.cluster_id = cluster_id  # type: str
        self.created_time = created_time  # type: str
        self.data_center_id = data_center_id  # type: str
        self.retention_period = retention_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlanResponseBodyBackupPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        return self


class DescribeBackupPlanResponseBody(TeaModel):
    def __init__(self, backup_plan=None, request_id=None):
        self.backup_plan = backup_plan  # type: DescribeBackupPlanResponseBodyBackupPlan
        self.request_id = request_id  # type: str

    def validate(self):
        if self.backup_plan:
            self.backup_plan.validate()

    def to_map(self):
        _map = super(DescribeBackupPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan is not None:
            result['BackupPlan'] = self.backup_plan.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPlan') is not None:
            temp_model = DescribeBackupPlanResponseBodyBackupPlan()
            self.backup_plan = temp_model.from_map(m['BackupPlan'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupPlanResponse, self).to_map()
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
            temp_model = DescribeBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlansRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupPlansResponseBodyBackupPlansBackupPlan(TeaModel):
    def __init__(self, active=None, backup_period=None, backup_time=None, cluster_id=None, created_time=None,
                 data_center_id=None, retention_period=None):
        self.active = active  # type: bool
        self.backup_period = backup_period  # type: str
        self.backup_time = backup_time  # type: str
        self.cluster_id = cluster_id  # type: str
        self.created_time = created_time  # type: str
        self.data_center_id = data_center_id  # type: str
        self.retention_period = retention_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlansBackupPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        return self


class DescribeBackupPlansResponseBodyBackupPlans(TeaModel):
    def __init__(self, backup_plan=None):
        self.backup_plan = backup_plan  # type: list[DescribeBackupPlansResponseBodyBackupPlansBackupPlan]

    def validate(self):
        if self.backup_plan:
            for k in self.backup_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBodyBackupPlans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupPlan'] = []
        if self.backup_plan is not None:
            for k in self.backup_plan:
                result['BackupPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup_plan = []
        if m.get('BackupPlan') is not None:
            for k in m.get('BackupPlan'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlan()
                self.backup_plan.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBody(TeaModel):
    def __init__(self, backup_plans=None, request_id=None):
        self.backup_plans = backup_plans  # type: DescribeBackupPlansResponseBodyBackupPlans
        self.request_id = request_id  # type: str

    def validate(self):
        if self.backup_plans:
            self.backup_plans.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plans is not None:
            result['BackupPlans'] = self.backup_plans.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupPlans') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlans()
            self.backup_plans = temp_model.from_map(m['BackupPlans'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupPlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupPlansResponse, self).to_map()
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
            temp_model = DescribeBackupPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, backup_type=None, cluster_id=None, data_center_id=None):
        self.backup_type = backup_type  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(self, backup_id=None, backup_type=None, cluster_id=None, data_center_id=None, end_time=None,
                 size=None, start_time=None, status=None):
        self.backup_id = backup_id  # type: str
        self.backup_type = backup_type  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.end_time = end_time  # type: str
        self.size = size  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyBackupsBackup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupsResponseBodyBackups(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup  # type: list[DescribeBackupsResponseBodyBackupsBackup]

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBodyBackups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyBackupsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(self, backups=None, request_id=None):
        self.backups = backups  # type: DescribeBackupsResponseBodyBackups
        self.request_id = request_id  # type: str

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backups') is not None:
            temp_model = DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m['Backups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackupsResponse, self).to_map()
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterResponseBodyClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterTagsTag, self).to_map()
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


class DescribeClusterResponseBodyClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeClusterResponseBodyClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterTags, self).to_map()
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
                temp_model = DescribeClusterResponseBodyClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyCluster(TeaModel):
    def __init__(self, auto_renew_period=None, auto_renewal=None, cluster_id=None, cluster_name=None,
                 confirm_product_offline=None, created_time=None, data_center_count=None, expire_time=None, is_latest_version=None,
                 lock_mode=None, maintain_end_time=None, maintain_start_time=None, major_version=None, minor_version=None,
                 pay_type=None, resource_group_id=None, status=None, tags=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.auto_renewal = auto_renewal  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.confirm_product_offline = confirm_product_offline  # type: bool
        self.created_time = created_time  # type: str
        self.data_center_count = data_center_count  # type: int
        self.expire_time = expire_time  # type: str
        self.is_latest_version = is_latest_version  # type: bool
        self.lock_mode = lock_mode  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str
        self.major_version = major_version  # type: str
        self.minor_version = minor_version  # type: str
        self.pay_type = pay_type  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeClusterResponseBodyClusterTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.confirm_product_offline is not None:
            result['ConfirmProductOffline'] = self.confirm_product_offline
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_count is not None:
            result['DataCenterCount'] = self.data_center_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ConfirmProductOffline') is not None:
            self.confirm_product_offline = m.get('ConfirmProductOffline')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterCount') is not None:
            self.data_center_count = m.get('DataCenterCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeClusterResponseBodyClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(self, cluster=None, request_id=None):
        self.cluster = cluster  # type: DescribeClusterResponseBodyCluster
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribeClusterResponseBodyCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterDashboardRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDashboardRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode(TeaModel):
    def __init__(self, address=None, load=None, status=None):
        self.address = address  # type: str
        self.load = load  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.load is not None:
            result['Load'] = self.load
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes(TeaModel):
    def __init__(self, node=None):
        self.node = node  # type: list[DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode]

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode()
                self.node.append(temp_model.from_map(k))
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter(TeaModel):
    def __init__(self, data_center_id=None, nodes=None):
        self.data_center_id = data_center_id  # type: str
        self.nodes = nodes  # type: DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('Nodes') is not None:
            temp_model = DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCenters(TeaModel):
    def __init__(self, data_center=None):
        self.data_center = data_center  # type: list[DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter]

    def validate(self):
        if self.data_center:
            for k in self.data_center:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterDashboardResponseBodyDashboardDataCenters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataCenter'] = []
        if self.data_center is not None:
            for k in self.data_center:
                result['DataCenter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_center = []
        if m.get('DataCenter') is not None:
            for k in m.get('DataCenter'):
                temp_model = DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter()
                self.data_center.append(temp_model.from_map(k))
        return self


class DescribeClusterDashboardResponseBodyDashboard(TeaModel):
    def __init__(self, cluster_id=None, data_centers=None):
        self.cluster_id = cluster_id  # type: str
        self.data_centers = data_centers  # type: DescribeClusterDashboardResponseBodyDashboardDataCenters

    def validate(self):
        if self.data_centers:
            self.data_centers.validate()

    def to_map(self):
        _map = super(DescribeClusterDashboardResponseBodyDashboard, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_centers is not None:
            result['DataCenters'] = self.data_centers.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenters') is not None:
            temp_model = DescribeClusterDashboardResponseBodyDashboardDataCenters()
            self.data_centers = temp_model.from_map(m['DataCenters'])
        return self


class DescribeClusterDashboardResponseBody(TeaModel):
    def __init__(self, dashboard=None, request_id=None):
        self.dashboard = dashboard  # type: DescribeClusterDashboardResponseBodyDashboard
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dashboard:
            self.dashboard.validate()

    def to_map(self):
        _map = super(DescribeClusterDashboardResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard is not None:
            result['Dashboard'] = self.dashboard.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dashboard') is not None:
            temp_model = DescribeClusterDashboardResponseBodyDashboard()
            self.dashboard = temp_model.from_map(m['Dashboard'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterDashboardResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterDashboardResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterDashboardResponse, self).to_map()
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
            temp_model = DescribeClusterDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterStatusRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterStatusResponseBody(TeaModel):
    def __init__(self, created_time=None, request_id=None, status=None):
        self.created_time = created_time  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterStatusResponse, self).to_map()
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
            temp_model = DescribeClusterStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersRequestTag, self).to_map()
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


class DescribeClustersRequest(TeaModel):
    def __init__(self, cluster_name=None, page_number=None, page_size=None, region_id=None, resource_group_id=None,
                 tag=None):
        self.cluster_name = cluster_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[DescribeClustersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeClustersResponseBodyClustersClusterTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersResponseBodyClustersClusterTagsTag, self).to_map()
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


class DescribeClustersResponseBodyClustersClusterTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeClustersResponseBodyClustersClusterTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBodyClustersClusterTags, self).to_map()
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
                temp_model = DescribeClustersResponseBodyClustersClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeClustersResponseBodyClustersCluster(TeaModel):
    def __init__(self, auto_renew_period=None, auto_renewal=None, cluster_id=None, cluster_name=None,
                 created_time=None, data_center_count=None, expire_time=None, lock_mode=None, major_version=None,
                 minor_version=None, pay_type=None, resource_group_id=None, status=None, tags=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.auto_renewal = auto_renewal  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.created_time = created_time  # type: str
        self.data_center_count = data_center_count  # type: int
        self.expire_time = expire_time  # type: str
        self.lock_mode = lock_mode  # type: str
        self.major_version = major_version  # type: str
        self.minor_version = minor_version  # type: str
        self.pay_type = pay_type  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.tags = tags  # type: DescribeClustersResponseBodyClustersClusterTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBodyClustersCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_count is not None:
            result['DataCenterCount'] = self.data_center_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterCount') is not None:
            self.data_center_count = m.get('DataCenterCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeClustersResponseBodyClustersClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster=None):
        self.cluster = cluster  # type: list[DescribeClustersResponseBodyClustersCluster]

    def validate(self):
        if self.cluster:
            for k in self.cluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cluster'] = []
        if self.cluster is not None:
            for k in self.cluster:
                result['Cluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k in m.get('Cluster'):
                temp_model = DescribeClustersResponseBodyClustersCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.clusters = clusters  # type: DescribeClustersResponseBodyClusters
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(DescribeClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = DescribeClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactPointsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactPointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses(TeaModel):
    def __init__(self, private_address=None):
        self.private_address = private_address  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_address is not None:
            result['PrivateAddress'] = self.private_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrivateAddress') is not None:
            self.private_address = m.get('PrivateAddress')
        return self


class DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses(TeaModel):
    def __init__(self, public_address=None):
        self.public_address = public_address  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_address is not None:
            result['PublicAddress'] = self.public_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PublicAddress') is not None:
            self.public_address = m.get('PublicAddress')
        return self


class DescribeContactPointsResponseBodyContactPointsContactPoint(TeaModel):
    def __init__(self, data_center_id=None, port=None, private_addresses=None, public_addresses=None):
        self.data_center_id = data_center_id  # type: str
        self.port = port  # type: int
        self.private_addresses = private_addresses  # type: DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses
        self.public_addresses = public_addresses  # type: DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses

    def validate(self):
        if self.private_addresses:
            self.private_addresses.validate()
        if self.public_addresses:
            self.public_addresses.validate()

    def to_map(self):
        _map = super(DescribeContactPointsResponseBodyContactPointsContactPoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.port is not None:
            result['Port'] = self.port
        if self.private_addresses is not None:
            result['PrivateAddresses'] = self.private_addresses.to_map()
        if self.public_addresses is not None:
            result['PublicAddresses'] = self.public_addresses.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateAddresses') is not None:
            temp_model = DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses()
            self.private_addresses = temp_model.from_map(m['PrivateAddresses'])
        if m.get('PublicAddresses') is not None:
            temp_model = DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses()
            self.public_addresses = temp_model.from_map(m['PublicAddresses'])
        return self


class DescribeContactPointsResponseBodyContactPoints(TeaModel):
    def __init__(self, contact_point=None):
        self.contact_point = contact_point  # type: list[DescribeContactPointsResponseBodyContactPointsContactPoint]

    def validate(self):
        if self.contact_point:
            for k in self.contact_point:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeContactPointsResponseBodyContactPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactPoint'] = []
        if self.contact_point is not None:
            for k in self.contact_point:
                result['ContactPoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contact_point = []
        if m.get('ContactPoint') is not None:
            for k in m.get('ContactPoint'):
                temp_model = DescribeContactPointsResponseBodyContactPointsContactPoint()
                self.contact_point.append(temp_model.from_map(k))
        return self


class DescribeContactPointsResponseBody(TeaModel):
    def __init__(self, contact_points=None, request_id=None):
        self.contact_points = contact_points  # type: DescribeContactPointsResponseBodyContactPoints
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contact_points:
            self.contact_points.validate()

    def to_map(self):
        _map = super(DescribeContactPointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_points is not None:
            result['ContactPoints'] = self.contact_points.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContactPoints') is not None:
            temp_model = DescribeContactPointsResponseBodyContactPoints()
            self.contact_points = temp_model.from_map(m['ContactPoints'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContactPointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeContactPointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContactPointsResponse, self).to_map()
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
            temp_model = DescribeContactPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCenterRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCenterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeDataCenterResponseBody(TeaModel):
    def __init__(self, auto_renew_period=None, auto_renewal=None, cluster_id=None, commodity_instance=None,
                 created_time=None, data_center_id=None, data_center_name=None, disk_size=None, disk_type=None, expire_time=None,
                 instance_type=None, lock_mode=None, node_count=None, pay_type=None, region_id=None, request_id=None, status=None,
                 vpc_id=None, vswitch_id=None, zone_id=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.auto_renewal = auto_renewal  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.commodity_instance = commodity_instance  # type: str
        self.created_time = created_time  # type: str
        self.data_center_id = data_center_id  # type: str
        self.data_center_name = data_center_name  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str
        self.expire_time = expire_time  # type: str
        self.instance_type = instance_type  # type: str
        self.lock_mode = lock_mode  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCenterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.commodity_instance is not None:
            result['CommodityInstance'] = self.commodity_instance
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommodityInstance') is not None:
            self.commodity_instance = m.get('CommodityInstance')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDataCenterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataCenterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataCenterResponse, self).to_map()
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
            temp_model = DescribeDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCentersRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCentersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDataCentersResponseBodyDataCentersDataCenter(TeaModel):
    def __init__(self, auto_renew_period=None, auto_renewal=None, cluster_id=None, commodity_instance=None,
                 created_time=None, data_center_id=None, data_center_name=None, disk_size=None, disk_type=None, expire_time=None,
                 instance_type=None, lock_mode=None, node_count=None, pay_type=None, region_id=None, status=None, vpc_id=None,
                 vswitch_id=None, zone_id=None):
        self.auto_renew_period = auto_renew_period  # type: int
        self.auto_renewal = auto_renewal  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.commodity_instance = commodity_instance  # type: str
        self.created_time = created_time  # type: str
        self.data_center_id = data_center_id  # type: str
        self.data_center_name = data_center_name  # type: str
        self.disk_size = disk_size  # type: int
        self.disk_type = disk_type  # type: str
        self.expire_time = expire_time  # type: str
        self.instance_type = instance_type  # type: str
        self.lock_mode = lock_mode  # type: str
        self.node_count = node_count  # type: int
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataCentersResponseBodyDataCentersDataCenter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.commodity_instance is not None:
            result['CommodityInstance'] = self.commodity_instance
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommodityInstance') is not None:
            self.commodity_instance = m.get('CommodityInstance')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDataCentersResponseBodyDataCenters(TeaModel):
    def __init__(self, data_center=None):
        self.data_center = data_center  # type: list[DescribeDataCentersResponseBodyDataCentersDataCenter]

    def validate(self):
        if self.data_center:
            for k in self.data_center:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataCentersResponseBodyDataCenters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataCenter'] = []
        if self.data_center is not None:
            for k in self.data_center:
                result['DataCenter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_center = []
        if m.get('DataCenter') is not None:
            for k in m.get('DataCenter'):
                temp_model = DescribeDataCentersResponseBodyDataCentersDataCenter()
                self.data_center.append(temp_model.from_map(k))
        return self


class DescribeDataCentersResponseBody(TeaModel):
    def __init__(self, data_centers=None, request_id=None):
        self.data_centers = data_centers  # type: DescribeDataCentersResponseBodyDataCenters
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_centers:
            self.data_centers.validate()

    def to_map(self):
        _map = super(DescribeDataCentersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_centers is not None:
            result['DataCenters'] = self.data_centers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataCenters') is not None:
            temp_model = DescribeDataCentersResponseBodyDataCenters()
            self.data_centers = temp_model.from_map(m['DataCenters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataCentersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataCentersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataCentersResponse, self).to_map()
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
            temp_model = DescribeDataCentersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeletedClustersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeletedClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDeletedClustersResponseBodyClustersCluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, created_time=None, data_center_count=None,
                 expire_time=None, major_version=None, minor_version=None, pay_type=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.created_time = created_time  # type: str
        self.data_center_count = data_center_count  # type: int
        self.expire_time = expire_time  # type: str
        self.major_version = major_version  # type: str
        self.minor_version = minor_version  # type: str
        self.pay_type = pay_type  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDeletedClustersResponseBodyClustersCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.data_center_count is not None:
            result['DataCenterCount'] = self.data_center_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DataCenterCount') is not None:
            self.data_center_count = m.get('DataCenterCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDeletedClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster=None):
        self.cluster = cluster  # type: list[DescribeDeletedClustersResponseBodyClustersCluster]

    def validate(self):
        if self.cluster:
            for k in self.cluster:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDeletedClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cluster'] = []
        if self.cluster is not None:
            for k in self.cluster:
                result['Cluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k in m.get('Cluster'):
                temp_model = DescribeDeletedClustersResponseBodyClustersCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class DescribeDeletedClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.clusters = clusters  # type: DescribeDeletedClustersResponseBodyClusters
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(DescribeDeletedClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = DescribeDeletedClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeletedClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDeletedClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDeletedClustersResponse, self).to_map()
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
            temp_model = DescribeDeletedClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypeRequest(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTypeRequest, self).to_map()
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


class DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec(TeaModel):
    def __init__(self, cpu_size=None, instance_type=None, mem_size=None):
        self.cpu_size = cpu_size  # type: long
        self.instance_type = instance_type  # type: str
        self.mem_size = mem_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_size is not None:
            result['CpuSize'] = self.cpu_size
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuSize') is not None:
            self.cpu_size = m.get('CpuSize')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        return self


class DescribeInstanceTypeResponseBodyInstanceTypeSpecList(TeaModel):
    def __init__(self, instance_type_spec=None):
        self.instance_type_spec = instance_type_spec  # type: list[DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec]

    def validate(self):
        if self.instance_type_spec:
            for k in self.instance_type_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypeResponseBodyInstanceTypeSpecList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypeSpec'] = []
        if self.instance_type_spec is not None:
            for k in self.instance_type_spec:
                result['InstanceTypeSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_type_spec = []
        if m.get('InstanceTypeSpec') is not None:
            for k in m.get('InstanceTypeSpec'):
                temp_model = DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec()
                self.instance_type_spec.append(temp_model.from_map(k))
        return self


class DescribeInstanceTypeResponseBody(TeaModel):
    def __init__(self, instance_type_spec_list=None, request_id=None):
        self.instance_type_spec_list = instance_type_spec_list  # type: DescribeInstanceTypeResponseBodyInstanceTypeSpecList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_type_spec_list:
            self.instance_type_spec_list.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_spec_list is not None:
            result['InstanceTypeSpecList'] = self.instance_type_spec_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTypeSpecList') is not None:
            temp_model = DescribeInstanceTypeResponseBodyInstanceTypeSpecList()
            self.instance_type_spec_list = temp_model.from_map(m['InstanceTypeSpecList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypeResponse, self).to_map()
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
            temp_model = DescribeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpWhitelistRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeIpWhitelistResponseBodyIpList(TeaModel):
    def __init__(self, ip=None):
        self.ip = ip  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpWhitelistResponseBodyIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeIpWhitelistResponseBody(TeaModel):
    def __init__(self, ip_list=None, request_id=None):
        self.ip_list = ip_list  # type: DescribeIpWhitelistResponseBodyIpList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ip_list:
            self.ip_list.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['IpList'] = self.ip_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpList') is not None:
            temp_model = DescribeIpWhitelistResponseBodyIpList()
            self.ip_list = temp_model.from_map(m['IpList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistResponse, self).to_map()
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
            temp_model = DescribeIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpWhitelistGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpWhitelistGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList(TeaModel):
    def __init__(self, ip=None):
        self.ip = ip  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeIpWhitelistGroupsResponseBodyGroupsGroup(TeaModel):
    def __init__(self, group_name=None, ip_list=None, ip_version=None):
        self.group_name = group_name  # type: str
        self.ip_list = ip_list  # type: DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList
        self.ip_version = ip_version  # type: int

    def validate(self):
        if self.ip_list:
            self.ip_list.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistGroupsResponseBodyGroupsGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list.to_map()
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpList') is not None:
            temp_model = DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList()
            self.ip_list = temp_model.from_map(m['IpList'])
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class DescribeIpWhitelistGroupsResponseBodyGroups(TeaModel):
    def __init__(self, group=None):
        self.group = group  # type: list[DescribeIpWhitelistGroupsResponseBodyGroupsGroup]

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistGroupsResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = DescribeIpWhitelistGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class DescribeIpWhitelistGroupsResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None):
        self.groups = groups  # type: DescribeIpWhitelistGroupsResponseBodyGroups
        self.request_id = request_id  # type: str

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = DescribeIpWhitelistGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpWhitelistGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIpWhitelistGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpWhitelistGroupsResponse, self).to_map()
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
            temp_model = DescribeIpWhitelistGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeToolExecutionHistoriesRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory(TeaModel):
    def __init__(self, arguments=None, command=None, create_time=None, data_center_id=None, error_message=None,
                 is_ended=None, job_id=None, modify_time=None, nodes=None, region_id=None):
        self.arguments = arguments  # type: str
        self.command = command  # type: str
        self.create_time = create_time  # type: long
        self.data_center_id = data_center_id  # type: str
        self.error_message = error_message  # type: str
        self.is_ended = is_ended  # type: bool
        self.job_id = job_id  # type: str
        self.modify_time = modify_time  # type: long
        self.nodes = nodes  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.command is not None:
            result['Command'] = self.command
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_ended is not None:
            result['IsEnded'] = self.is_ended
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsEnded') is not None:
            self.is_ended = m.get('IsEnded')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNodeToolExecutionHistoriesResponseBodyHistories(TeaModel):
    def __init__(self, history=None):
        self.history = history  # type: list[DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory]

    def validate(self):
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoriesResponseBodyHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.history = []
        if m.get('History') is not None:
            for k in m.get('History'):
                temp_model = DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory()
                self.history.append(temp_model.from_map(k))
        return self


class DescribeNodeToolExecutionHistoriesResponseBody(TeaModel):
    def __init__(self, histories=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.histories = histories  # type: DescribeNodeToolExecutionHistoriesResponseBodyHistories
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.histories:
            self.histories.validate()

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.histories is not None:
            result['Histories'] = self.histories.to_map()
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
        if m.get('Histories') is not None:
            temp_model = DescribeNodeToolExecutionHistoriesResponseBodyHistories()
            self.histories = temp_model.from_map(m['Histories'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNodeToolExecutionHistoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNodeToolExecutionHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoriesResponse, self).to_map()
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
            temp_model = DescribeNodeToolExecutionHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeToolExecutionHistoryRequest(TeaModel):
    def __init__(self, cluster_id=None, dc_id=None, job_id=None):
        self.cluster_id = cluster_id  # type: str
        self.dc_id = dc_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dc_id is not None:
            result['DcId'] = self.dc_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DcId') is not None:
            self.dc_id = m.get('DcId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeNodeToolExecutionHistoryResponseBody(TeaModel):
    def __init__(self, arguments=None, command=None, create_time=None, data_center_id=None, error_message=None,
                 is_ended=None, job_id=None, modify_time=None, nodes=None, region_id=None, request_id=None, result=None):
        self.arguments = arguments  # type: str
        self.command = command  # type: str
        self.create_time = create_time  # type: long
        self.data_center_id = data_center_id  # type: str
        self.error_message = error_message  # type: str
        self.is_ended = is_ended  # type: bool
        self.job_id = job_id  # type: str
        self.modify_time = modify_time  # type: long
        self.nodes = nodes  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.command is not None:
            result['Command'] = self.command
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_ended is not None:
            result['IsEnded'] = self.is_ended
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsEnded') is not None:
            self.is_ended = m.get('IsEnded')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeNodeToolExecutionHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNodeToolExecutionHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeToolExecutionHistoryResponse, self).to_map()
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
            temp_model = DescribeNodeToolExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterModificationHistoriesRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterModificationHistoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeParameterModificationHistoriesResponseBodyHistoriesHistory(TeaModel):
    def __init__(self, name=None, new_value=None, old_value=None, time=None):
        self.name = name  # type: str
        self.new_value = new_value  # type: str
        self.old_value = old_value  # type: str
        self.time = time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParameterModificationHistoriesResponseBodyHistoriesHistory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeParameterModificationHistoriesResponseBodyHistories(TeaModel):
    def __init__(self, history=None):
        self.history = history  # type: list[DescribeParameterModificationHistoriesResponseBodyHistoriesHistory]

    def validate(self):
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParameterModificationHistoriesResponseBodyHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.history = []
        if m.get('History') is not None:
            for k in m.get('History'):
                temp_model = DescribeParameterModificationHistoriesResponseBodyHistoriesHistory()
                self.history.append(temp_model.from_map(k))
        return self


class DescribeParameterModificationHistoriesResponseBody(TeaModel):
    def __init__(self, histories=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.histories = histories  # type: DescribeParameterModificationHistoriesResponseBodyHistories
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.histories:
            self.histories.validate()

    def to_map(self):
        _map = super(DescribeParameterModificationHistoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.histories is not None:
            result['Histories'] = self.histories.to_map()
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
        if m.get('Histories') is not None:
            temp_model = DescribeParameterModificationHistoriesResponseBodyHistories()
            self.histories = temp_model.from_map(m['Histories'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParameterModificationHistoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParameterModificationHistoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParameterModificationHistoriesResponse, self).to_map()
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
            temp_model = DescribeParameterModificationHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeParametersResponseBodyParametersParameter(TeaModel):
    def __init__(self, allowed_values=None, data_type=None, default_value=None, description=None, name=None,
                 value=None):
        self.allowed_values = allowed_values  # type: str
        self.data_type = data_type  # type: str
        self.default_value = default_value  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeParametersResponseBodyParametersParameter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(self, parameter=None):
        self.parameter = parameter  # type: list[DescribeParametersResponseBodyParametersParameter]

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBodyParameters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = DescribeParametersResponseBodyParametersParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, parameters=None, request_id=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.parameters = parameters  # type: DescribeParametersResponseBodyParameters
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super(DescribeParametersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Parameters') is not None:
            temp_model = DescribeParametersResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeParametersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeParametersResponse, self).to_map()
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
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZonesZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeRegionsResponseBodyRegionsRegionZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None, zones=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.zones = zones  # type: DescribeRegionsResponseBodyRegionsRegionZones

    def validate(self):
        if self.zones:
            self.zones.validate()

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
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
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


class DescribeSecurityGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroupIds(TeaModel):
    def __init__(self, security_group_id=None):
        self.security_group_id = security_group_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityGroupsResponseBodySecurityGroupIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_group_ids=None):
        self.request_id = request_id  # type: str
        self.security_group_ids = security_group_ids  # type: DescribeSecurityGroupsResponseBodySecurityGroupIds

    def validate(self):
        if self.security_group_ids:
            self.security_group_ids.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupIds') is not None:
            temp_model = DescribeSecurityGroupsResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m['SecurityGroupIds'])
        return self


class DescribeSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityGroupsResponse, self).to_map()
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
            temp_model = DescribeSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteNodeToolRequest(TeaModel):
    def __init__(self, arguments=None, cluster_id=None, command=None, data_center_id=None, execute_nodes=None):
        self.arguments = arguments  # type: str
        self.cluster_id = cluster_id  # type: str
        self.command = command  # type: str
        self.data_center_id = data_center_id  # type: str
        self.execute_nodes = execute_nodes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteNodeToolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command is not None:
            result['Command'] = self.command
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.execute_nodes is not None:
            result['ExecuteNodes'] = self.execute_nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('ExecuteNodes') is not None:
            self.execute_nodes = m.get('ExecuteNodes')
        return self


class ExecuteNodeToolResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteNodeToolResponseBody, self).to_map()
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


class ExecuteNodeToolResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecuteNodeToolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteNodeToolResponse, self).to_map()
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
            temp_model = ExecuteNodeToolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCmsUrlRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCmsUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetCmsUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, url=None):
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCmsUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetCmsUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCmsUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCmsUrlResponse, self).to_map()
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
            temp_model = GetCmsUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
    def __init__(self, next_token=None, region_id=None, resource_id=None, tag=None):
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListTagsResponseBodyTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsResponseBodyTagsTag, self).to_map()
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


class ListTagsResponseBodyTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListTagsResponseBodyTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsResponseBodyTags, self).to_map()
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
                temp_model = ListTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: ListTagsResponseBodyTags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            temp_model = ListTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
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


class ModifyAccountPasswordRequest(TeaModel):
    def __init__(self, account=None, cluster_id=None, password=None):
        self.account = account  # type: str
        self.cluster_id = cluster_id  # type: str
        self.password = password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class ModifyAccountPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccountPasswordResponseBody, self).to_map()
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


class ModifyAccountPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccountPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccountPasswordResponse, self).to_map()
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
            temp_model = ModifyAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPlanRequest(TeaModel):
    def __init__(self, active=None, backup_period=None, backup_time=None, cluster_id=None, data_center_id=None,
                 retention_period=None):
        self.active = active  # type: bool
        self.backup_period = backup_period  # type: str
        self.backup_time = backup_time  # type: str
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.retention_period = retention_period  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        return self


class ModifyBackupPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBackupPlanResponseBody, self).to_map()
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


class ModifyBackupPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBackupPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBackupPlanResponse, self).to_map()
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
            temp_model = ModifyBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, confirm_product_offline=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.confirm_product_offline = confirm_product_offline  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.confirm_product_offline is not None:
            result['ConfirmProductOffline'] = self.confirm_product_offline
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ConfirmProductOffline') is not None:
            self.confirm_product_offline = m.get('ConfirmProductOffline')
        return self


class ModifyClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterResponseBody, self).to_map()
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


class ModifyClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterResponse, self).to_map()
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
            temp_model = ModifyClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataCenterRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None, data_center_name=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.data_center_name = data_center_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataCenterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        return self


class ModifyDataCenterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataCenterResponseBody, self).to_map()
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


class ModifyDataCenterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataCenterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataCenterResponse, self).to_map()
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
            temp_model = ModifyDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, cluster_id=None, maintain_end_time=None, maintain_start_time=None):
        self.cluster_id = cluster_id  # type: str
        self.maintain_end_time = maintain_end_time  # type: str
        self.maintain_start_time = maintain_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        return self


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponseBody, self).to_map()
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


class ModifyInstanceMaintainTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceMaintainTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceMaintainTimeResponse, self).to_map()
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
            temp_model = ModifyInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTypeRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None, instance_type=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ModifyInstanceTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTypeResponseBody, self).to_map()
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


class ModifyInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceTypeResponse, self).to_map()
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
            temp_model = ModifyInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpWhitelistRequest(TeaModel):
    def __init__(self, cluster_id=None, ip_list=None):
        self.cluster_id = cluster_id  # type: str
        self.ip_list = ip_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class ModifyIpWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpWhitelistResponseBody, self).to_map()
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


class ModifyIpWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIpWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIpWhitelistResponse, self).to_map()
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
            temp_model = ModifyIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpWhitelistGroupRequest(TeaModel):
    def __init__(self, cluster_id=None, group_name=None, ip_list=None, ip_version=None):
        self.cluster_id = cluster_id  # type: str
        self.group_name = group_name  # type: str
        self.ip_list = ip_list  # type: str
        self.ip_version = ip_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpWhitelistGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class ModifyIpWhitelistGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyIpWhitelistGroupResponseBody, self).to_map()
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


class ModifyIpWhitelistGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyIpWhitelistGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyIpWhitelistGroupResponse, self).to_map()
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
            temp_model = ModifyIpWhitelistGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParameterRequest(TeaModel):
    def __init__(self, cluster_id=None, name=None, value=None):
        self.cluster_id = cluster_id  # type: str
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParameterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyParameterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyParameterResponseBody, self).to_map()
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


class ModifyParameterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyParameterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyParameterResponse, self).to_map()
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
            temp_model = ModifyParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None, security_group_ids=None):
        self.cluster_id = cluster_id  # type: str
        self.security_group_ids = security_group_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ModifySecurityGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySecurityGroupsResponseBody, self).to_map()
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


class ModifySecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySecurityGroupsResponse, self).to_map()
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
            temp_model = ModifySecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, cluster_id=None, new_resource_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.new_resource_group_id = new_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponse, self).to_map()
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurgeClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurgeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class PurgeClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurgeClusterResponseBody, self).to_map()
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


class PurgeClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PurgeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PurgeClusterResponse, self).to_map()
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
            temp_model = PurgeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class RebootClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootClusterResponseBody, self).to_map()
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


class RebootClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebootClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebootClusterResponse, self).to_map()
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
            temp_model = RebootClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicContactPointsRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleasePublicContactPointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class ReleasePublicContactPointsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleasePublicContactPointsResponseBody, self).to_map()
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


class ReleasePublicContactPointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleasePublicContactPointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleasePublicContactPointsResponse, self).to_map()
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
            temp_model = ReleasePublicContactPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDiskSizeRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None, disk_size=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.disk_size = disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDiskSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        return self


class ResizeDiskSizeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDiskSizeResponseBody, self).to_map()
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


class ResizeDiskSizeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResizeDiskSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeDiskSizeResponse, self).to_map()
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
            temp_model = ResizeDiskSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeNodeCountRequest(TeaModel):
    def __init__(self, cluster_id=None, data_center_id=None, node_count=None):
        self.cluster_id = cluster_id  # type: str
        self.data_center_id = data_center_id  # type: str
        self.node_count = node_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeNodeCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        return self


class ResizeNodeCountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeNodeCountResponseBody, self).to_map()
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


class ResizeNodeCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResizeNodeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeNodeCountResponse, self).to_map()
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
            temp_model = ResizeNodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, tag_key=None):
        self.all = all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesResponseBody, self).to_map()
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


class UnTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnTagResourcesResponse, self).to_map()
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
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterVersionRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UpgradeClusterVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClusterVersionResponseBody, self).to_map()
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


class UpgradeClusterVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeClusterVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeClusterVersionResponse, self).to_map()
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
            temp_model = UpgradeClusterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


