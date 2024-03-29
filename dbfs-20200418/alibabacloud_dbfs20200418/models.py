# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddTagsBatchRequest(TeaModel):
    def __init__(self, client_token=None, dbfs_list=None, region_id=None, tags=None):
        self.client_token = client_token  # type: str
        self.dbfs_list = dbfs_list  # type: str
        self.region_id = region_id  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTagsBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AddTagsBatchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTagsBatchResponseBody, self).to_map()
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


class AddTagsBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTagsBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTagsBatchResponse, self).to_map()
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
            temp_model = AddTagsBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, dbfs_ids=None, policy_id=None, region_id=None):
        self.dbfs_ids = dbfs_ids  # type: list[str]
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_ids is not None:
            result['DbfsIds'] = self.dbfs_ids
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbfsIds') is not None:
            self.dbfs_ids = m.get('DbfsIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ApplyAutoSnapshotPolicyShrinkRequest(TeaModel):
    def __init__(self, dbfs_ids_shrink=None, policy_id=None, region_id=None):
        self.dbfs_ids_shrink = dbfs_ids_shrink  # type: str
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyAutoSnapshotPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_ids_shrink is not None:
            result['DbfsIds'] = self.dbfs_ids_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbfsIds') is not None:
            self.dbfs_ids_shrink = m.get('DbfsIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ApplyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyAutoSnapshotPolicyResponseBody, self).to_map()
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


class ApplyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyAutoSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyAutoSnapshotPolicyResponse, self).to_map()
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
            temp_model = ApplyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDbfsRequest(TeaModel):
    def __init__(self, attach_mode=None, attach_point=None, ecsinstance_id=None, fs_id=None, region_id=None,
                 server_url=None):
        self.attach_mode = attach_mode  # type: str
        self.attach_point = attach_point  # type: str
        self.ecsinstance_id = ecsinstance_id  # type: str
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str
        self.server_url = server_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_mode is not None:
            result['AttachMode'] = self.attach_mode
        if self.attach_point is not None:
            result['AttachPoint'] = self.attach_point
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_url is not None:
            result['ServerUrl'] = self.server_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachMode') is not None:
            self.attach_mode = m.get('AttachMode')
        if m.get('AttachPoint') is not None:
            self.attach_point = m.get('AttachPoint')
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')
        return self


class AttachDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachDbfsResponseBody, self).to_map()
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


class AttachDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachDbfsResponse, self).to_map()
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
            temp_model = AttachDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, dbfs_ids=None, policy_id=None, region_id=None):
        self.dbfs_ids = dbfs_ids  # type: list[str]
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_ids is not None:
            result['DbfsIds'] = self.dbfs_ids
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbfsIds') is not None:
            self.dbfs_ids = m.get('DbfsIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CancelAutoSnapshotPolicyShrinkRequest(TeaModel):
    def __init__(self, dbfs_ids_shrink=None, policy_id=None, region_id=None):
        self.dbfs_ids_shrink = dbfs_ids_shrink  # type: str
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAutoSnapshotPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_ids_shrink is not None:
            result['DbfsIds'] = self.dbfs_ids_shrink
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbfsIds') is not None:
            self.dbfs_ids_shrink = m.get('DbfsIds')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CancelAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAutoSnapshotPolicyResponseBody, self).to_map()
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


class CancelAutoSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelAutoSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelAutoSnapshotPolicyResponse, self).to_map()
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
            temp_model = CancelAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, policy_name=None, region_id=None, repeat_weekdays=None, retention_days=None,
                 time_points=None):
        self.policy_name = policy_name  # type: str
        self.region_id = region_id  # type: str
        self.repeat_weekdays = repeat_weekdays  # type: list[str]
        self.retention_days = retention_days  # type: int
        self.time_points = time_points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class CreateAutoSnapshotPolicyShrinkRequest(TeaModel):
    def __init__(self, policy_name=None, region_id=None, repeat_weekdays_shrink=None, retention_days=None,
                 time_points_shrink=None):
        self.policy_name = policy_name  # type: str
        self.region_id = region_id  # type: str
        self.repeat_weekdays_shrink = repeat_weekdays_shrink  # type: str
        self.retention_days = retention_days  # type: int
        self.time_points_shrink = time_points_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoSnapshotPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays_shrink is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays_shrink
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points_shrink is not None:
            result['TimePoints'] = self.time_points_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays_shrink = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points_shrink = m.get('TimePoints')
        return self


class CreateAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, policy_id=None, request_id=None):
        self.policy_id = policy_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoSnapshotPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAutoSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAutoSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAutoSnapshotPolicyResponse, self).to_map()
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
            temp_model = CreateAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDbfsRequest(TeaModel):
    def __init__(self, advanced_features=None, category=None, client_token=None, delete_snapshot=None,
                 enable_raid=None, encryption=None, fs_name=None, instance_type=None, kmskey_id=None, performance_level=None,
                 raid_stripe_unit_number=None, region_id=None, size_g=None, snapshot_id=None, used_scene=None, zone_id=None):
        self.advanced_features = advanced_features  # type: str
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.delete_snapshot = delete_snapshot  # type: bool
        self.enable_raid = enable_raid  # type: bool
        self.encryption = encryption  # type: bool
        self.fs_name = fs_name  # type: str
        self.instance_type = instance_type  # type: str
        self.kmskey_id = kmskey_id  # type: str
        self.performance_level = performance_level  # type: str
        self.raid_stripe_unit_number = raid_stripe_unit_number  # type: int
        self.region_id = region_id  # type: str
        self.size_g = size_g  # type: int
        self.snapshot_id = snapshot_id  # type: str
        self.used_scene = used_scene  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_features is not None:
            result['AdvancedFeatures'] = self.advanced_features
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.delete_snapshot is not None:
            result['DeleteSnapshot'] = self.delete_snapshot
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.raid_stripe_unit_number is not None:
            result['RaidStripeUnitNumber'] = self.raid_stripe_unit_number
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedFeatures') is not None:
            self.advanced_features = m.get('AdvancedFeatures')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeleteSnapshot') is not None:
            self.delete_snapshot = m.get('DeleteSnapshot')
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RaidStripeUnitNumber') is not None:
            self.raid_stripe_unit_number = m.get('RaidStripeUnitNumber')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDbfsResponseBody(TeaModel):
    def __init__(self, fs_id=None, request_id=None):
        self.fs_id = fs_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDbfsResponse, self).to_map()
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
            temp_model = CreateDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBody, self).to_map()
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


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponse, self).to_map()
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
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, client_token=None, description=None, fs_id=None, region_id=None, retention_days=None,
                 snapshot_name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str
        self.retention_days = retention_days  # type: int
        self.snapshot_name = snapshot_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None, snapshot_id=None):
        self.request_id = request_id  # type: str
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSnapshotResponse, self).to_map()
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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, policy_id=None, region_id=None):
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoSnapshotPolicyResponseBody, self).to_map()
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


class DeleteAutoSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAutoSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAutoSnapshotPolicyResponse, self).to_map()
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
            temp_model = DeleteAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDbfsRequest(TeaModel):
    def __init__(self, force=None, fs_id=None, region_id=None):
        self.force = force  # type: bool
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDbfsResponseBody, self).to_map()
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


class DeleteDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDbfsResponse, self).to_map()
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
            temp_model = DeleteDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(self, force=None, region_id=None, snapshot_id=None):
        self.force = force  # type: bool
        self.region_id = region_id  # type: str
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotResponseBody, self).to_map()
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSnapshotResponse, self).to_map()
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
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagsBatchRequest(TeaModel):
    def __init__(self, dbfs_list=None, region_id=None, tags=None):
        self.dbfs_list = dbfs_list  # type: str
        self.region_id = region_id  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagsBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_list is not None:
            result['DbfsList'] = self.dbfs_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbfsList') is not None:
            self.dbfs_list = m.get('DbfsList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DeleteTagsBatchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagsBatchResponseBody, self).to_map()
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


class DeleteTagsBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagsBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagsBatchResponse, self).to_map()
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
            temp_model = DeleteTagsBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbfsSpecificationsRequest(TeaModel):
    def __init__(self, category=None, ecs_instance_type=None, region_id=None):
        self.category = category  # type: str
        self.ecs_instance_type = ecs_instance_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDbfsSpecificationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDbfsSpecificationsResponseBody(TeaModel):
    def __init__(self, max_dbfs_number_per_ecs=None, request_id=None, supported_ecs_instance_type_family=None):
        self.max_dbfs_number_per_ecs = max_dbfs_number_per_ecs  # type: dict[str, any]
        self.request_id = request_id  # type: str
        self.supported_ecs_instance_type_family = supported_ecs_instance_type_family  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDbfsSpecificationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_dbfs_number_per_ecs is not None:
            result['MaxDbfsNumberPerEcs'] = self.max_dbfs_number_per_ecs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supported_ecs_instance_type_family is not None:
            result['SupportedEcsInstanceTypeFamily'] = self.supported_ecs_instance_type_family
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxDbfsNumberPerEcs') is not None:
            self.max_dbfs_number_per_ecs = m.get('MaxDbfsNumberPerEcs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupportedEcsInstanceTypeFamily') is not None:
            self.supported_ecs_instance_type_family = m.get('SupportedEcsInstanceTypeFamily')
        return self


class DescribeDbfsSpecificationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDbfsSpecificationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDbfsSpecificationsResponse, self).to_map()
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
            temp_model = DescribeDbfsSpecificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTypesRequest, self).to_map()
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


class DescribeInstanceTypesResponseBodyInstanceTypes(TeaModel):
    def __init__(self, cpu_core_count=None, instance_type_description=None, instance_type_id=None,
                 memory_size=None):
        self.cpu_core_count = cpu_core_count  # type: float
        self.instance_type_description = instance_type_description  # type: str
        self.instance_type_id = instance_type_id  # type: str
        self.memory_size = memory_size  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceTypesResponseBodyInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.instance_type_description is not None:
            result['InstanceTypeDescription'] = self.instance_type_description
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('InstanceTypeDescription') is not None:
            self.instance_type_description = m.get('InstanceTypeDescription')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeInstanceTypesResponseBody(TeaModel):
    def __init__(self, instance_types=None, request_id=None):
        self.instance_types = instance_types  # type: list[DescribeInstanceTypesResponseBodyInstanceTypes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_types:
            for k in self.instance_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k in self.instance_types:
                result['InstanceTypes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k in m.get('InstanceTypes'):
                temp_model = DescribeInstanceTypesResponseBodyInstanceTypes()
                self.instance_types.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceTypesResponse, self).to_map()
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
            temp_model = DescribeInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDbfsRequest(TeaModel):
    def __init__(self, ecsinstance_id=None, fs_id=None, region_id=None):
        self.ecsinstance_id = ecsinstance_id  # type: str
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecsinstance_id is not None:
            result['ECSInstanceId'] = self.ecsinstance_id
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ECSInstanceId') is not None:
            self.ecsinstance_id = m.get('ECSInstanceId')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachDbfsResponseBody, self).to_map()
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


class DetachDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachDbfsResponse, self).to_map()
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
            temp_model = DetachDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, policy_id=None, region_id=None):
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAutoSnapshotPolicyResponseBodyData(TeaModel):
    def __init__(self, account_id=None, applied_dbfs_number=None, created_time=None, last_modified=None,
                 policy_id=None, policy_name=None, region_id=None, repeat_weekdays=None, retention_days=None, status=None,
                 status_detail=None, time_points=None):
        self.account_id = account_id  # type: str
        self.applied_dbfs_number = applied_dbfs_number  # type: int
        self.created_time = created_time  # type: str
        self.last_modified = last_modified  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.region_id = region_id  # type: str
        self.repeat_weekdays = repeat_weekdays  # type: list[str]
        self.retention_days = retention_days  # type: int
        self.status = status  # type: str
        self.status_detail = status_detail  # type: str
        self.time_points = time_points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoSnapshotPolicyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.applied_dbfs_number is not None:
            result['AppliedDbfsNumber'] = self.applied_dbfs_number
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppliedDbfsNumber') is not None:
            self.applied_dbfs_number = m.get('AppliedDbfsNumber')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class GetAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetAutoSnapshotPolicyResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAutoSnapshotPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetAutoSnapshotPolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAutoSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAutoSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAutoSnapshotPolicyResponse, self).to_map()
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
            temp_model = GetAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDbfsRequest(TeaModel):
    def __init__(self, fs_id=None, region_id=None):
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDbfsResponseBodyDBFSInfoEbsList(TeaModel):
    def __init__(self, ebs_id=None, size_g=None):
        self.ebs_id = ebs_id  # type: str
        self.size_g = size_g  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfoEbsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ebs_id is not None:
            result['EbsId'] = self.ebs_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EbsId') is not None:
            self.ebs_id = m.get('EbsId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        return self


class GetDbfsResponseBodyDBFSInfoEcsList(TeaModel):
    def __init__(self, ecs_id=None):
        self.ecs_id = ecs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfoEcsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class GetDbfsResponseBodyDBFSInfoSnapshotInfo(TeaModel):
    def __init__(self, link_id=None, policy_id=None, snapshot_count=None, total_size=None):
        self.link_id = link_id  # type: str
        self.policy_id = policy_id  # type: str
        self.snapshot_count = snapshot_count  # type: int
        self.total_size = total_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfoSnapshotInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link_id is not None:
            result['LinkId'] = self.link_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class GetDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(self, id=None, tag_key=None, tag_value=None):
        self.id = id  # type: int
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(self, attach_node_number=None, category=None, created_time=None, dbfscluster_id=None,
                 description=None, ebs_list=None, ecs_list=None, enable_raid=None, encryption=None, fs_id=None, fs_name=None,
                 instance_type=None, kmskey_id=None, last_failed=None, last_mount_time=None, last_umount_time=None, pay_type=None,
                 performance_level=None, raid_strip=None, region_id=None, size_g=None, snapshot_info=None, status=None, tags=None,
                 used_scene=None, zone_id=None):
        self.attach_node_number = attach_node_number  # type: int
        self.category = category  # type: str
        self.created_time = created_time  # type: str
        self.dbfscluster_id = dbfscluster_id  # type: str
        self.description = description  # type: str
        self.ebs_list = ebs_list  # type: list[GetDbfsResponseBodyDBFSInfoEbsList]
        self.ecs_list = ecs_list  # type: list[GetDbfsResponseBodyDBFSInfoEcsList]
        self.enable_raid = enable_raid  # type: bool
        self.encryption = encryption  # type: bool
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.instance_type = instance_type  # type: str
        self.kmskey_id = kmskey_id  # type: str
        self.last_failed = last_failed  # type: str
        self.last_mount_time = last_mount_time  # type: str
        self.last_umount_time = last_umount_time  # type: str
        self.pay_type = pay_type  # type: str
        self.performance_level = performance_level  # type: str
        self.raid_strip = raid_strip  # type: int
        self.region_id = region_id  # type: str
        self.size_g = size_g  # type: int
        self.snapshot_info = snapshot_info  # type: GetDbfsResponseBodyDBFSInfoSnapshotInfo
        self.status = status  # type: str
        self.tags = tags  # type: list[GetDbfsResponseBodyDBFSInfoTags]
        self.used_scene = used_scene  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()
        if self.snapshot_info:
            self.snapshot_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDbfsResponseBodyDBFSInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        if self.description is not None:
            result['Description'] = self.description
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.last_failed is not None:
            result['LastFailed'] = self.last_failed
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.snapshot_info is not None:
            result['SnapshotInfo'] = self.snapshot_info.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = GetDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('LastFailed') is not None:
            self.last_failed = m.get('LastFailed')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('SnapshotInfo') is not None:
            temp_model = GetDbfsResponseBodyDBFSInfoSnapshotInfo()
            self.snapshot_info = temp_model.from_map(m['SnapshotInfo'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetDbfsResponseBody(TeaModel):
    def __init__(self, dbfsinfo=None, request_id=None):
        self.dbfsinfo = dbfsinfo  # type: GetDbfsResponseBodyDBFSInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dbfsinfo:
            self.dbfsinfo.validate()

    def to_map(self):
        _map = super(GetDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfsinfo is not None:
            result['DBFSInfo'] = self.dbfsinfo.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DBFSInfo') is not None:
            temp_model = GetDbfsResponseBodyDBFSInfo()
            self.dbfsinfo = temp_model.from_map(m['DBFSInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDbfsResponse, self).to_map()
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
            temp_model = GetDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceLinkedRoleRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceLinkedRoleRequest, self).to_map()
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


class GetServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, account_id=None, dbfs_linked_role=None, region_id=None, request_id=None):
        self.account_id = account_id  # type: str
        self.dbfs_linked_role = dbfs_linked_role  # type: bool
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbfs_linked_role is not None:
            result['DbfsLinkedRole'] = self.dbfs_linked_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbfsLinkedRole') is not None:
            self.dbfs_linked_role = m.get('DbfsLinkedRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceLinkedRoleResponse, self).to_map()
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
            temp_model = GetServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSnapshotLinkRequest(TeaModel):
    def __init__(self, link_id=None, region_id=None):
        self.link_id = link_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link_id is not None:
            result['LinkId'] = self.link_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetSnapshotLinkResponseBodyDataEcsList(TeaModel):
    def __init__(self, ecs_id=None):
        self.ecs_id = ecs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotLinkResponseBodyDataEcsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class GetSnapshotLinkResponseBodyData(TeaModel):
    def __init__(self, category=None, ecs_list=None, fs_id=None, fs_name=None, link_id=None, snapshot_count=None,
                 source_size=None, status=None, total_size=None):
        self.category = category  # type: str
        self.ecs_list = ecs_list  # type: list[GetSnapshotLinkResponseBodyDataEcsList]
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.link_id = link_id  # type: str
        self.snapshot_count = snapshot_count  # type: int
        self.source_size = source_size  # type: int
        self.status = status  # type: str
        self.total_size = total_size  # type: long

    def validate(self):
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSnapshotLinkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.link_id is not None:
            result['LinkId'] = self.link_id
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.source_size is not None:
            result['SourceSize'] = self.source_size
        if self.status is not None:
            result['Status'] = self.status
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = GetSnapshotLinkResponseBodyDataEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('SourceSize') is not None:
            self.source_size = m.get('SourceSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class GetSnapshotLinkResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetSnapshotLinkResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSnapshotLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetSnapshotLinkResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSnapshotLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSnapshotLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSnapshotLinkResponse, self).to_map()
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
            temp_model = GetSnapshotLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoSnapshotPoliciesRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, page_number=None, page_size=None, region_id=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutoSnapshotPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAutoSnapshotPoliciesResponseBodySnapshotPolicies(TeaModel):
    def __init__(self, account_id=None, applied_dbfs_number=None, created_time=None, last_modified=None,
                 policy_id=None, policy_name=None, region_id=None, repeat_weekdays=None, retention_days=None, status=None,
                 status_detail=None, time_points=None):
        self.account_id = account_id  # type: str
        self.applied_dbfs_number = applied_dbfs_number  # type: int
        self.created_time = created_time  # type: str
        self.last_modified = last_modified  # type: str
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.region_id = region_id  # type: str
        self.repeat_weekdays = repeat_weekdays  # type: list[str]
        self.retention_days = retention_days  # type: int
        self.status = status  # type: str
        self.status_detail = status_detail  # type: str
        self.time_points = time_points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutoSnapshotPoliciesResponseBodySnapshotPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.applied_dbfs_number is not None:
            result['AppliedDbfsNumber'] = self.applied_dbfs_number
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AppliedDbfsNumber') is not None:
            self.applied_dbfs_number = m.get('AppliedDbfsNumber')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class ListAutoSnapshotPoliciesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, snapshot_policies=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.snapshot_policies = snapshot_policies  # type: list[ListAutoSnapshotPoliciesResponseBodySnapshotPolicies]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.snapshot_policies:
            for k in self.snapshot_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAutoSnapshotPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SnapshotPolicies'] = []
        if self.snapshot_policies is not None:
            for k in self.snapshot_policies:
                result['SnapshotPolicies'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshot_policies = []
        if m.get('SnapshotPolicies') is not None:
            for k in m.get('SnapshotPolicies'):
                temp_model = ListAutoSnapshotPoliciesResponseBodySnapshotPolicies()
                self.snapshot_policies.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAutoSnapshotPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAutoSnapshotPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAutoSnapshotPoliciesResponse, self).to_map()
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
            temp_model = ListAutoSnapshotPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoSnapshotPolicyAppliedDbfsRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, page_number=None, page_size=None, policy_id=None,
                 region_id=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyAppliedDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAutoSnapshotPolicyAppliedDbfsResponseBodyDbfsList(TeaModel):
    def __init__(self, fs_id=None, fs_name=None, region_id=None, size_g=None, snapshot_count=None, status=None,
                 total_size=None):
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.region_id = region_id  # type: str
        self.size_g = size_g  # type: long
        self.snapshot_count = snapshot_count  # type: int
        self.status = status  # type: str
        self.total_size = total_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyAppliedDbfsResponseBodyDbfsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.status is not None:
            result['Status'] = self.status
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAutoSnapshotPolicyAppliedDbfsResponseBody(TeaModel):
    def __init__(self, dbfs_list=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.dbfs_list = dbfs_list  # type: list[ListAutoSnapshotPolicyAppliedDbfsResponseBodyDbfsList]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dbfs_list:
            for k in self.dbfs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyAppliedDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbfsList'] = []
        if self.dbfs_list is not None:
            for k in self.dbfs_list:
                result['DbfsList'].append(k.to_map() if k else None)
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
        self.dbfs_list = []
        if m.get('DbfsList') is not None:
            for k in m.get('DbfsList'):
                temp_model = ListAutoSnapshotPolicyAppliedDbfsResponseBodyDbfsList()
                self.dbfs_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAutoSnapshotPolicyAppliedDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAutoSnapshotPolicyAppliedDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyAppliedDbfsResponse, self).to_map()
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
            temp_model = ListAutoSnapshotPolicyAppliedDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAutoSnapshotPolicyUnappliedDbfsRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, page_number=None, page_size=None, region_id=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyUnappliedDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAutoSnapshotPolicyUnappliedDbfsResponseBodyDbfsList(TeaModel):
    def __init__(self, fs_id=None, fs_name=None, region_id=None, size_g=None, snapshot_count=None, status=None,
                 total_size=None):
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.region_id = region_id  # type: str
        self.size_g = size_g  # type: long
        self.snapshot_count = snapshot_count  # type: int
        self.status = status  # type: str
        self.total_size = total_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyUnappliedDbfsResponseBodyDbfsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.status is not None:
            result['Status'] = self.status
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAutoSnapshotPolicyUnappliedDbfsResponseBody(TeaModel):
    def __init__(self, dbfs_list=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.dbfs_list = dbfs_list  # type: list[ListAutoSnapshotPolicyUnappliedDbfsResponseBodyDbfsList]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dbfs_list:
            for k in self.dbfs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyUnappliedDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbfsList'] = []
        if self.dbfs_list is not None:
            for k in self.dbfs_list:
                result['DbfsList'].append(k.to_map() if k else None)
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
        self.dbfs_list = []
        if m.get('DbfsList') is not None:
            for k in m.get('DbfsList'):
                temp_model = ListAutoSnapshotPolicyUnappliedDbfsResponseBodyDbfsList()
                self.dbfs_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAutoSnapshotPolicyUnappliedDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAutoSnapshotPolicyUnappliedDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAutoSnapshotPolicyUnappliedDbfsResponse, self).to_map()
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
            temp_model = ListAutoSnapshotPolicyUnappliedDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, page_number=None, page_size=None, region_id=None,
                 sort_key=None, sort_type=None, tags=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.sort_key = sort_key  # type: str
        self.sort_type = sort_type  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListDbfsResponseBodyDBFSInfoEbsList(TeaModel):
    def __init__(self, ebs_id=None, size_g=None):
        self.ebs_id = ebs_id  # type: str
        self.size_g = size_g  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfoEbsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ebs_id is not None:
            result['EbsId'] = self.ebs_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EbsId') is not None:
            self.ebs_id = m.get('EbsId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        return self


class ListDbfsResponseBodyDBFSInfoEcsList(TeaModel):
    def __init__(self, ecs_id=None):
        self.ecs_id = ecs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfoEcsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class ListDbfsResponseBodyDBFSInfoSnapshotInfo(TeaModel):
    def __init__(self, link_id=None, policy_id=None, snapshot_count=None, total_size=None):
        self.link_id = link_id  # type: str
        self.policy_id = policy_id  # type: str
        self.snapshot_count = snapshot_count  # type: int
        self.total_size = total_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfoSnapshotInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link_id is not None:
            result['LinkId'] = self.link_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListDbfsResponseBodyDBFSInfoTags(TeaModel):
    def __init__(self, id=None, tag_key=None, tag_value=None):
        self.id = id  # type: long
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListDbfsResponseBodyDBFSInfo(TeaModel):
    def __init__(self, attach_node_number=None, category=None, created_time=None, dbfscluster_id=None,
                 ebs_list=None, ecs_list=None, enable_raid=None, encryption=None, fs_id=None, fs_name=None,
                 instance_type=None, kmskey_id=None, last_failed=None, last_mount_time=None, last_umount_time=None, pay_type=None,
                 performance_level=None, raid_strip=None, region_id=None, size_g=None, snapshot_info=None, status=None, tags=None,
                 used_scene=None, zone_id=None):
        self.attach_node_number = attach_node_number  # type: int
        self.category = category  # type: str
        self.created_time = created_time  # type: str
        self.dbfscluster_id = dbfscluster_id  # type: str
        self.ebs_list = ebs_list  # type: list[ListDbfsResponseBodyDBFSInfoEbsList]
        self.ecs_list = ecs_list  # type: list[ListDbfsResponseBodyDBFSInfoEcsList]
        self.enable_raid = enable_raid  # type: bool
        self.encryption = encryption  # type: bool
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.instance_type = instance_type  # type: str
        self.kmskey_id = kmskey_id  # type: str
        self.last_failed = last_failed  # type: str
        self.last_mount_time = last_mount_time  # type: str
        self.last_umount_time = last_umount_time  # type: str
        self.pay_type = pay_type  # type: str
        self.performance_level = performance_level  # type: str
        self.raid_strip = raid_strip  # type: int
        self.region_id = region_id  # type: str
        self.size_g = size_g  # type: int
        self.snapshot_info = snapshot_info  # type: ListDbfsResponseBodyDBFSInfoSnapshotInfo
        self.status = status  # type: str
        self.tags = tags  # type: list[ListDbfsResponseBodyDBFSInfoTags]
        self.used_scene = used_scene  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.ebs_list:
            for k in self.ebs_list:
                if k:
                    k.validate()
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()
        if self.snapshot_info:
            self.snapshot_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDbfsResponseBodyDBFSInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_node_number is not None:
            result['AttachNodeNumber'] = self.attach_node_number
        if self.category is not None:
            result['Category'] = self.category
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dbfscluster_id is not None:
            result['DBFSClusterId'] = self.dbfscluster_id
        result['EbsList'] = []
        if self.ebs_list is not None:
            for k in self.ebs_list:
                result['EbsList'].append(k.to_map() if k else None)
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.enable_raid is not None:
            result['EnableRaid'] = self.enable_raid
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.last_failed is not None:
            result['LastFailed'] = self.last_failed
        if self.last_mount_time is not None:
            result['LastMountTime'] = self.last_mount_time
        if self.last_umount_time is not None:
            result['LastUmountTime'] = self.last_umount_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.raid_strip is not None:
            result['RaidStrip'] = self.raid_strip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size_g is not None:
            result['SizeG'] = self.size_g
        if self.snapshot_info is not None:
            result['SnapshotInfo'] = self.snapshot_info.to_map()
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachNodeNumber') is not None:
            self.attach_node_number = m.get('AttachNodeNumber')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DBFSClusterId') is not None:
            self.dbfscluster_id = m.get('DBFSClusterId')
        self.ebs_list = []
        if m.get('EbsList') is not None:
            for k in m.get('EbsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEbsList()
                self.ebs_list.append(temp_model.from_map(k))
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = ListDbfsResponseBodyDBFSInfoEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('EnableRaid') is not None:
            self.enable_raid = m.get('EnableRaid')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('LastFailed') is not None:
            self.last_failed = m.get('LastFailed')
        if m.get('LastMountTime') is not None:
            self.last_mount_time = m.get('LastMountTime')
        if m.get('LastUmountTime') is not None:
            self.last_umount_time = m.get('LastUmountTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RaidStrip') is not None:
            self.raid_strip = m.get('RaidStrip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SizeG') is not None:
            self.size_g = m.get('SizeG')
        if m.get('SnapshotInfo') is not None:
            temp_model = ListDbfsResponseBodyDBFSInfoSnapshotInfo()
            self.snapshot_info = temp_model.from_map(m['SnapshotInfo'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListDbfsResponseBodyDBFSInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListDbfsResponseBody(TeaModel):
    def __init__(self, dbfsinfo=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.dbfsinfo = dbfsinfo  # type: list[ListDbfsResponseBodyDBFSInfo]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dbfsinfo:
            for k in self.dbfsinfo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDbfsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBFSInfo'] = []
        if self.dbfsinfo is not None:
            for k in self.dbfsinfo:
                result['DBFSInfo'].append(k.to_map() if k else None)
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
        self.dbfsinfo = []
        if m.get('DBFSInfo') is not None:
            for k in m.get('DBFSInfo'):
                temp_model = ListDbfsResponseBodyDBFSInfo()
                self.dbfsinfo.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDbfsResponse, self).to_map()
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
            temp_model = ListDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsAttachableEcsInstancesRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, page_number=None, page_size=None, region_id=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsAttachableEcsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo(TeaModel):
    def __init__(self, image_id=None, instance_type_family=None, osname=None, status=None, zone_id=None, label=None,
                 value=None):
        self.image_id = image_id  # type: str
        self.instance_type_family = instance_type_family  # type: str
        self.osname = osname  # type: str
        self.status = status  # type: str
        self.zone_id = zone_id  # type: str
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.status is not None:
            result['Status'] = self.status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListDbfsAttachableEcsInstancesResponseBody(TeaModel):
    def __init__(self, ecs_label_info=None, request_id=None, total_count=None):
        self.ecs_label_info = ecs_label_info  # type: list[ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.ecs_label_info:
            for k in self.ecs_label_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDbfsAttachableEcsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsLabelInfo'] = []
        if self.ecs_label_info is not None:
            for k in self.ecs_label_info:
                result['EcsLabelInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ecs_label_info = []
        if m.get('EcsLabelInfo') is not None:
            for k in m.get('EcsLabelInfo'):
                temp_model = ListDbfsAttachableEcsInstancesResponseBodyEcsLabelInfo()
                self.ecs_label_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDbfsAttachableEcsInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDbfsAttachableEcsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDbfsAttachableEcsInstancesResponse, self).to_map()
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
            temp_model = ListDbfsAttachableEcsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDbfsAttachedEcsInstancesRequest(TeaModel):
    def __init__(self, fs_id=None, region_id=None):
        self.fs_id = fs_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsAttachedEcsInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo(TeaModel):
    def __init__(self, instance_type_family=None, mount_point=None, mounted_time=None, osname=None, label=None,
                 value=None):
        self.instance_type_family = instance_type_family  # type: str
        self.mount_point = mount_point  # type: str
        self.mounted_time = mounted_time  # type: str
        self.osname = osname  # type: str
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point
        if self.mounted_time is not None:
            result['MountedTime'] = self.mounted_time
        if self.osname is not None:
            result['OSName'] = self.osname
        if self.label is not None:
            result['label'] = self.label
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('MountPoint') is not None:
            self.mount_point = m.get('MountPoint')
        if m.get('MountedTime') is not None:
            self.mounted_time = m.get('MountedTime')
        if m.get('OSName') is not None:
            self.osname = m.get('OSName')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListDbfsAttachedEcsInstancesResponseBody(TeaModel):
    def __init__(self, ecs_label_info=None, request_id=None):
        self.ecs_label_info = ecs_label_info  # type: list[ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ecs_label_info:
            for k in self.ecs_label_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDbfsAttachedEcsInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsLabelInfo'] = []
        if self.ecs_label_info is not None:
            for k in self.ecs_label_info:
                result['EcsLabelInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ecs_label_info = []
        if m.get('EcsLabelInfo') is not None:
            for k in m.get('EcsLabelInfo'):
                temp_model = ListDbfsAttachedEcsInstancesResponseBodyEcsLabelInfo()
                self.ecs_label_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDbfsAttachedEcsInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDbfsAttachedEcsInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDbfsAttachedEcsInstancesResponse, self).to_map()
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
            temp_model = ListDbfsAttachedEcsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, fs_id=None, page_number=None, page_size=None,
                 region_id=None, snapshot_ids=None, snapshot_name=None, snapshot_type=None, sort_key=None, sort_type=None,
                 status=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.fs_id = fs_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.snapshot_ids = snapshot_ids  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.sort_key = sort_key  # type: str
        self.sort_type = sort_type  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSnapshotResponseBodySnapshots(TeaModel):
    def __init__(self, category=None, creation_time=None, description=None, last_modified_time=None, progress=None,
                 remain_time=None, retention_days=None, snapshot_id=None, snapshot_name=None, snapshot_type=None,
                 source_fs_id=None, source_fs_size=None, source_fs_stripe_width=None, status=None):
        self.category = category  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.last_modified_time = last_modified_time  # type: str
        self.progress = progress  # type: str
        self.remain_time = remain_time  # type: int
        self.retention_days = retention_days  # type: int
        self.snapshot_id = snapshot_id  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.source_fs_id = source_fs_id  # type: str
        self.source_fs_size = source_fs_size  # type: int
        self.source_fs_stripe_width = source_fs_stripe_width  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_fs_id is not None:
            result['SourceFsId'] = self.source_fs_id
        if self.source_fs_size is not None:
            result['SourceFsSize'] = self.source_fs_size
        if self.source_fs_stripe_width is not None:
            result['SourceFsStripeWidth'] = self.source_fs_stripe_width
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceFsId') is not None:
            self.source_fs_id = m.get('SourceFsId')
        if m.get('SourceFsSize') is not None:
            self.source_fs_size = m.get('SourceFsSize')
        if m.get('SourceFsStripeWidth') is not None:
            self.source_fs_stripe_width = m.get('SourceFsStripeWidth')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSnapshotResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, snapshots=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.snapshots = snapshots  # type: list[ListSnapshotResponseBodySnapshots]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListSnapshotResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSnapshotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSnapshotResponse, self).to_map()
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
            temp_model = ListSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotLinksRequest(TeaModel):
    def __init__(self, filter_key=None, filter_value=None, fs_ids=None, link_ids=None, page_number=None,
                 page_size=None, region_id=None):
        self.filter_key = filter_key  # type: str
        self.filter_value = filter_value  # type: str
        self.fs_ids = fs_ids  # type: str
        self.link_ids = link_ids  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotLinksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.fs_ids is not None:
            result['FsIds'] = self.fs_ids
        if self.link_ids is not None:
            result['LinkIds'] = self.link_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('FsIds') is not None:
            self.fs_ids = m.get('FsIds')
        if m.get('LinkIds') is not None:
            self.link_ids = m.get('LinkIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSnapshotLinksResponseBodySnapshotLinksEcsList(TeaModel):
    def __init__(self, ecs_id=None):
        self.ecs_id = ecs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotLinksResponseBodySnapshotLinksEcsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class ListSnapshotLinksResponseBodySnapshotLinks(TeaModel):
    def __init__(self, ecs_list=None, fs_id=None, fs_name=None, link_id=None, snapshot_count=None, source_size=None,
                 status=None, total_size=None):
        self.ecs_list = ecs_list  # type: list[ListSnapshotLinksResponseBodySnapshotLinksEcsList]
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.link_id = link_id  # type: str
        self.snapshot_count = snapshot_count  # type: int
        self.source_size = source_size  # type: int
        self.status = status  # type: str
        self.total_size = total_size  # type: long

    def validate(self):
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSnapshotLinksResponseBodySnapshotLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.link_id is not None:
            result['LinkId'] = self.link_id
        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count
        if self.source_size is not None:
            result['SourceSize'] = self.source_size
        if self.status is not None:
            result['Status'] = self.status
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = ListSnapshotLinksResponseBodySnapshotLinksEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')
        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')
        if m.get('SourceSize') is not None:
            self.source_size = m.get('SourceSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListSnapshotLinksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, snapshot_links=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.snapshot_links = snapshot_links  # type: list[ListSnapshotLinksResponseBodySnapshotLinks]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.snapshot_links:
            for k in self.snapshot_links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSnapshotLinksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SnapshotLinks'] = []
        if self.snapshot_links is not None:
            for k in self.snapshot_links:
                result['SnapshotLinks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshot_links = []
        if m.get('SnapshotLinks') is not None:
            for k in m.get('SnapshotLinks'):
                temp_model = ListSnapshotLinksResponseBodySnapshotLinks()
                self.snapshot_links.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSnapshotLinksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSnapshotLinksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSnapshotLinksResponse, self).to_map()
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
            temp_model = ListSnapshotLinksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
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


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_keys=None):
        self.request_id = request_id  # type: str
        self.tag_keys = tag_keys  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagKeysResponse, self).to_map()
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(self, region_id=None, tag_key=None):
        self.region_id = region_id  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_values=None):
        self.request_id = request_id  # type: str
        self.tag_values = tag_values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagValuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagValuesResponse, self).to_map()
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, policy_id=None, policy_name=None, region_id=None, repeat_weekdays=None, retention_days=None,
                 time_points=None):
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.region_id = region_id  # type: str
        self.repeat_weekdays = repeat_weekdays  # type: list[str]
        self.retention_days = retention_days  # type: int
        self.time_points = time_points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class ModifyAutoSnapshotPolicyShrinkRequest(TeaModel):
    def __init__(self, policy_id=None, policy_name=None, region_id=None, repeat_weekdays_shrink=None,
                 retention_days=None, time_points_shrink=None):
        self.policy_id = policy_id  # type: str
        self.policy_name = policy_name  # type: str
        self.region_id = region_id  # type: str
        self.repeat_weekdays_shrink = repeat_weekdays_shrink  # type: str
        self.retention_days = retention_days  # type: int
        self.time_points_shrink = time_points_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAutoSnapshotPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays_shrink is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays_shrink
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points_shrink is not None:
            result['TimePoints'] = self.time_points_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays_shrink = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points_shrink = m.get('TimePoints')
        return self


class ModifyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAutoSnapshotPolicyResponseBody, self).to_map()
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


class ModifyAutoSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAutoSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAutoSnapshotPolicyResponse, self).to_map()
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
            temp_model = ModifyAutoSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySnapshotAttributeRequest(TeaModel):
    def __init__(self, description=None, region_id=None, snapshot_id=None, snapshot_name=None):
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.snapshot_name = snapshot_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySnapshotAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class ModifySnapshotAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySnapshotAttributeResponseBody, self).to_map()
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


class ModifySnapshotAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySnapshotAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySnapshotAttributeResponse, self).to_map()
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
            temp_model = ModifySnapshotAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDbfsRequest(TeaModel):
    def __init__(self, fs_id=None, fs_name=None, region_id=None):
        self.fs_id = fs_id  # type: str
        self.fs_name = fs_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenameDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.fs_name is not None:
            result['FsName'] = self.fs_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('FsName') is not None:
            self.fs_name = m.get('FsName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenameDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenameDbfsResponseBody, self).to_map()
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


class RenameDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenameDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenameDbfsResponse, self).to_map()
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
            temp_model = RenameDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDbfsRequest(TeaModel):
    def __init__(self, fs_id=None, new_size_g=None, region_id=None):
        self.fs_id = fs_id  # type: str
        self.new_size_g = new_size_g  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.new_size_g is not None:
            result['NewSizeG'] = self.new_size_g
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('NewSizeG') is not None:
            self.new_size_g = m.get('NewSizeG')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResizeDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResizeDbfsResponseBody, self).to_map()
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


class ResizeDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResizeDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResizeDbfsResponse, self).to_map()
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
            temp_model = ResizeDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagDbfsRequest(TeaModel):
    def __init__(self, dbfs_id=None, region_id=None, tags=None):
        self.dbfs_id = dbfs_id  # type: str
        self.region_id = region_id  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbfs_id is not None:
            result['DbfsId'] = self.dbfs_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbfsId') is not None:
            self.dbfs_id = m.get('DbfsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagDbfsResponseBody, self).to_map()
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


class TagDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagDbfsResponse, self).to_map()
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
            temp_model = TagDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDbfsRequest(TeaModel):
    def __init__(self, advanced_features=None, fs_id=None, instance_type=None, region_id=None, used_scene=None):
        self.advanced_features = advanced_features  # type: str
        self.fs_id = fs_id  # type: str
        self.instance_type = instance_type  # type: str
        self.region_id = region_id  # type: str
        self.used_scene = used_scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDbfsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_features is not None:
            result['AdvancedFeatures'] = self.advanced_features
        if self.fs_id is not None:
            result['FsId'] = self.fs_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.used_scene is not None:
            result['UsedScene'] = self.used_scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdvancedFeatures') is not None:
            self.advanced_features = m.get('AdvancedFeatures')
        if m.get('FsId') is not None:
            self.fs_id = m.get('FsId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UsedScene') is not None:
            self.used_scene = m.get('UsedScene')
        return self


class UpdateDbfsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDbfsResponseBody, self).to_map()
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


class UpdateDbfsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateDbfsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDbfsResponse, self).to_map()
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
            temp_model = UpdateDbfsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


