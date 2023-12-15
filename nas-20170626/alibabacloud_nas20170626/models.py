# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddClientToBlackListRequest(TeaModel):
    def __init__(self, client_ip=None, client_token=None, file_system_id=None, region_id=None):
        # The IP address of the client to add.
        self.client_ip = client_ip  # type: str
        # This parameter ensures the idempotency of each request. A ClientToken is generated for each client. Make sure that each ClientToken is unique between different requests. The parameter can be a maximum of 64 characters in length and contain ASCII characters.
        # 
        # For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/doc-detail/25693.htm).
        self.client_token = client_token  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the region where the file system resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClientToBlackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddClientToBlackListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClientToBlackListResponseBody, self).to_map()
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


class AddClientToBlackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddClientToBlackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddClientToBlackListResponse, self).to_map()
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
            temp_model = AddClientToBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTagsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of each tag. The tag includes a TagKey and TagValue. You can add a maximum of 10 tags at a time. You must specify a TagKey. You can leave a TagValue empty.
        self.key = key  # type: str
        # The value of each tag. The tag includes a TagKey and TagValue. You can add a maximum of 10 tags at a time. You must specify a TagKey. You can leave a TagValue empty.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTagsRequestTag, self).to_map()
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


class AddTagsRequest(TeaModel):
    def __init__(self, file_system_id=None, tag=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        self.tag = tag  # type: list[AddTagsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = AddTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class AddTagsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTagsResponseBody, self).to_map()
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


class AddTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTagsResponse, self).to_map()
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
            temp_model = AddTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, file_system_ids=None):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # The IDs of advanced Extreme NAS file systems.
        # 
        # You can specify a maximum of 100 file system IDs at a time. If you want to apply an automatic snapshot policy to multiple file systems, separate the file system IDs with commas (,).
        self.file_system_ids = file_system_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        return self


class ApplyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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


class ApplyDataFlowAutoRefreshRequestAutoRefreshs(TeaModel):
    def __init__(self, refresh_path=None):
        # The automatic update directory. CPFS automatically checks whether the source data only in the directory is updated and imports the updated data.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # 
        # >  The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        self.refresh_path = refresh_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyDataFlowAutoRefreshRequestAutoRefreshs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class ApplyDataFlowAutoRefreshRequest(TeaModel):
    def __init__(self, auto_refresh_interval=None, auto_refresh_policy=None, auto_refreshs=None, client_token=None,
                 data_flow_id=None, dry_run=None, file_system_id=None):
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval  # type: long
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy. Valid values:
        # 
        # *   None (default): Updated data in the source storage is not automatically imported into the CPFS file system. You can run a dataflow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        self.auto_refresh_policy = auto_refresh_policy  # type: str
        # The automatic update configurations.
        self.auto_refreshs = auto_refreshs  # type: list[ApplyDataFlowAutoRefreshRequestAutoRefreshs]
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        if self.auto_refreshs:
            for k in self.auto_refreshs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyDataFlowAutoRefreshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        result['AutoRefreshs'] = []
        if self.auto_refreshs is not None:
            for k in self.auto_refreshs:
                result['AutoRefreshs'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')
        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')
        self.auto_refreshs = []
        if m.get('AutoRefreshs') is not None:
            for k in m.get('AutoRefreshs'):
                temp_model = ApplyDataFlowAutoRefreshRequestAutoRefreshs()
                self.auto_refreshs.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ApplyDataFlowAutoRefreshResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyDataFlowAutoRefreshResponseBody, self).to_map()
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


class ApplyDataFlowAutoRefreshResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyDataFlowAutoRefreshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyDataFlowAutoRefreshResponse, self).to_map()
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
            temp_model = ApplyDataFlowAutoRefreshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, file_system_ids=None):
        # The IDs of file systems.
        # 
        # You can specify a maximum of 100 file system IDs. If you want to remove automatic snapshot policies from multiple file systems, separate the file system IDs with commas (,).
        self.file_system_ids = file_system_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        return self


class CancelAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
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


class CancelDataFlowAutoRefreshRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, dry_run=None, file_system_id=None, refresh_path=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the DataFlowld parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The directory for which you want to cancel AutoRefresh configurations.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # 
        # >  The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        self.refresh_path = refresh_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDataFlowAutoRefreshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class CancelDataFlowAutoRefreshResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDataFlowAutoRefreshResponseBody, self).to_map()
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


class CancelDataFlowAutoRefreshResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelDataFlowAutoRefreshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelDataFlowAutoRefreshResponse, self).to_map()
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
            temp_model = CancelDataFlowAutoRefreshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDataFlowTaskRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, dry_run=None, file_system_id=None, task_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. The dry run does not cancel the specified dataflow task or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, service limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified dataflow task is canceled.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the dataflow task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDataFlowTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelDataFlowTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDataFlowTaskResponseBody, self).to_map()
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


class CancelDataFlowTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelDataFlowTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelDataFlowTaskResponse, self).to_map()
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
            temp_model = CancelDataFlowTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDirQuotaRequest(TeaModel):
    def __init__(self, file_system_id=None, path=None, user_id=None, user_type=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The absolute path of a directory.
        self.path = path  # type: str
        # The UID or GID of a user for whom you want to cancel the directory quota.
        # 
        # This parameter is required and valid only if the UserType parameter is set to Uid or Gid.
        # 
        # Examples:
        # 
        # *   If you want to cancel a quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500.
        # *   If you want to cancel a quota for a group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100.
        self.user_id = user_id  # type: str
        # The type of the user.
        # 
        # Valid values:
        # 
        # *   Uid: user ID
        # *   Gid: user group ID
        # *   AllUsers: all users
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDirQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CancelDirQuotaResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelDirQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelDirQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelDirQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelDirQuotaResponse, self).to_map()
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
            temp_model = CancelDirQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelLifecycleRetrieveJobRequest(TeaModel):
    def __init__(self, job_id=None):
        # The ID of the data retrieval task.
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelLifecycleRetrieveJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelLifecycleRetrieveJobResponseBody, self).to_map()
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


class CancelLifecycleRetrieveJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelLifecycleRetrieveJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelLifecycleRetrieveJobResponse, self).to_map()
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
            temp_model = CancelLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRecycleBinJobRequest(TeaModel):
    def __init__(self, job_id=None):
        # The job ID.
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRecycleBinJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CancelRecycleBinJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRecycleBinJobResponseBody, self).to_map()
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


class CancelRecycleBinJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelRecycleBinJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelRecycleBinJobResponse, self).to_map()
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
            temp_model = CancelRecycleBinJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessGroupRequest(TeaModel):
    def __init__(self, access_group_name=None, access_group_type=None, description=None, file_system_type=None):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (\_), and hyphens (-).
        # *   The name must be different from the name of the default permission group.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        self.access_group_name = access_group_name  # type: str
        # The network type of the permission group. Valid value: **Vpc**.
        self.access_group_type = access_group_type  # type: str
        # The description of the permission group.
        # 
        # Limits:
        # 
        # *   By default, the description of a permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length.
        # *   The name must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class CreateAccessGroupResponseBody(TeaModel):
    def __init__(self, access_group_name=None, request_id=None):
        # The name of the permission group.
        self.access_group_name = access_group_name  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessGroupResponse, self).to_map()
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
            temp_model = CreateAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessRuleRequest(TeaModel):
    def __init__(self, access_group_name=None, file_system_type=None, ipv_6source_cidr_ip=None, priority=None,
                 rwaccess_type=None, source_cidr_ip=None, user_access_type=None):
        # The name of the permission group.
        self.access_group_name = access_group_name  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str
        # The IPv6 address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IPv6 address or CIDR block.
        # 
        # > *   Only Extreme NAS file systems that reside in the Chinese mainland support IPv6. If you specify this parameter, you must enable IPv6 for the file system.
        # >*   Only permission groups that reside in virtual private clouds (VPCs) support IPv6.
        # >*   You cannot specify an IPv4 address and an IPv6 address at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip  # type: str
        # The priority of the rule.
        # 
        # The rule with the highest priority takes effect if multiple rules are attached to the authorized object.
        # 
        # Valid values: 1 to 100. The value 1 indicates the highest priority.
        self.priority = priority  # type: int
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess_type = rwaccess_type  # type: str
        # The IP address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IP address or CIDR block.
        # 
        # > If the permission group resides in the classic network, you must set this parameter to an IP address.
        self.source_cidr_ip = source_cidr_ip  # type: str
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash (default): grants root users the permissions to access the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
        self.user_access_type = user_access_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')
        return self


class CreateAccessRuleResponseBody(TeaModel):
    def __init__(self, access_rule_id=None, request_id=None):
        # The rule ID.
        self.access_rule_id = access_rule_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessRuleResponse, self).to_map()
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
            temp_model = CreateAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, auto_snapshot_policy_name=None, file_system_type=None, repeat_weekdays=None,
                 retention_days=None, time_points=None):
        # The name of the automatic snapshot policy.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter.
        # *   The name can contain digits, colons (:), underscores (\_), and hyphens (-). It cannot start with `http://` or `https://`.
        # *   This parameter is empty by default.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name  # type: str
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        self.file_system_type = file_system_type  # type: str
        # The days of a week on which to create automatic snapshots.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7. The values from 1 to 7 indicate the seven days in a week from Monday to Sunday.
        # 
        # If you want to create multiple auto snapshots within a week, you can specify multiple days from Monday to Sunday and separate the days with commas (,). You can specify a maximum of seven days.
        self.repeat_weekdays = repeat_weekdays  # type: str
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \-1 (default). Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days  # type: int
        # The points in time at which auto snapshots were created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23. The values from 0 to 23 indicate a total of 24 hours from 00:00 to 23:00. For example, the value 1 indicates 01:00.
        # 
        # If you want to create multiple auto snapshots within a day, you can specify multiple points in time and separate the points in time with commas (,). You can specify a maximum of 24 points in time.
        self.time_points = time_points  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class CreateAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, request_id=None):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAutoSnapshotPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
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


class CreateDataFlowRequestAutoRefreshs(TeaModel):
    def __init__(self, refresh_path=None):
        # The automatic update directory. CPFS registers the data update event in the source storage, and automatically checks whether the source data in the directory is updated and imports the updated data.
        # 
        # This parameter is empty by default. Updated data in the source storage is not automatically imported into the CPFS file system. You must import the updated data by running a manual task.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        self.refresh_path = refresh_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataFlowRequestAutoRefreshs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class CreateDataFlowRequest(TeaModel):
    def __init__(self, auto_refresh_interval=None, auto_refresh_policy=None, auto_refreshs=None, client_token=None,
                 description=None, dry_run=None, file_system_id=None, fset_id=None, source_security_type=None,
                 source_storage=None, throughput=None):
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 5 to 525600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval  # type: long
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy.
        # 
        # *   None (default): Updated data in the source storage is not automatically imported into the CPFS file system. You can run a dataflow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        self.auto_refresh_policy = auto_refresh_policy  # type: str
        # The automatic update configurations.
        self.auto_refreshs = auto_refreshs  # type: list[CreateDataFlowRequestAutoRefreshs]
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The fileset ID.
        self.fset_id = fset_id  # type: str
        # The type of security mechanism for the source storage. This parameter must be specified if the source storage is accessed with a security mechanism. Valid values:
        # 
        # *   None (default): The source storage can be accessed without a security mechanism.
        # *   SSL: The source storage must be accessed with an SSL certificate.
        self.source_security_type = source_security_type  # type: str
        # The access path of the source storage. Format: `<storage type>://<path>`.
        # 
        # Parameters:
        # 
        # *   storage type: Only OSS is supported.
        # 
        # *   path: the name of the OSS bucket. Limits:
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name must be 8 to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        #     *   The name cannot start with `http://` or `https://`.
        # 
        # >  The OSS bucket must be an existing bucket in the region.
        self.source_storage = source_storage  # type: str
        # The maximum dataflow throughput. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1,200
        # *   1,500
        # 
        # >  The dataflow throughput must be less than the I/O throughput of the file system
        self.throughput = throughput  # type: long

    def validate(self):
        if self.auto_refreshs:
            for k in self.auto_refreshs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDataFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        result['AutoRefreshs'] = []
        if self.auto_refreshs is not None:
            for k in self.auto_refreshs:
                result['AutoRefreshs'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.source_security_type is not None:
            result['SourceSecurityType'] = self.source_security_type
        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')
        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')
        self.auto_refreshs = []
        if m.get('AutoRefreshs') is not None:
            for k in m.get('AutoRefreshs'):
                temp_model = CreateDataFlowRequestAutoRefreshs()
                self.auto_refreshs.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('SourceSecurityType') is not None:
            self.source_security_type = m.get('SourceSecurityType')
        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        return self


class CreateDataFlowResponseBody(TeaModel):
    def __init__(self, data_flow_id=None, request_id=None):
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDataFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataFlowResponse, self).to_map()
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
            temp_model = CreateDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataFlowTaskRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, data_type=None, directory=None, dry_run=None,
                 entry_list=None, file_system_id=None, src_task_id=None, task_action=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # The type of data on which operations are performed by the dataflow task.
        # 
        # Valid values:
        # 
        # *   Metadata: the metadata of a file, including the timestamp, ownership, and permission information of the file. If you select Metadata, only the metadata of the file is imported. You can only query the file. When you access the file data, the file is loaded from the source storage as required.
        # *   Data: the data blocks of a file.
        # *   MetaAndData: the metadata and data blocks of the file.
        self.data_type = data_type  # type: str
        # The directory in which the dataflow task is executed.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   Only one directory can be listed at a time.
        # *   The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        self.directory = directory  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The list of files that are executed by the dataflow task.
        # 
        # Limits:
        # 
        # *   The list must be encoded in UTF-8.
        # *   The file list is in JSON format.
        # *   If the source storage is Object Storage Service (OSS), the list name must comply with the naming conventions of OSS objects.
        self.entry_list = entry_list  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # If you specify SrcTaskId, the configurations of the TaskAction, DataType, and EntryList parameters are copied from the desired dataflow task. You do not need to specify them.
        self.src_task_id = src_task_id  # type: str
        # The type of the dataflow task.
        # 
        # Valid values:
        # 
        # *   Import: imports data stored in the source storage to a CPFS file system.
        # *   Export: exports specified data from a CPFS file system to the source storage.
        # *   Evict: releases the data blocks of a file in a CPFS file system. After the eviction, only the metadata of the file is retained in the CPFS file system. You can still query the file. However, the data blocks of the file are cleared and do not occupy the storage space in the CPFS file system. When you access the file data, the file is loaded from the source storage as required.
        # *   Inventory: obtains the inventory list managed by a dataflow from the CPFS file system, providing the cache status of inventories in the dataflow.
        self.task_action = task_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataFlowTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.entry_list is not None:
            result['EntryList'] = self.entry_list
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.src_task_id is not None:
            result['SrcTaskId'] = self.src_task_id
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EntryList') is not None:
            self.entry_list = m.get('EntryList')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SrcTaskId') is not None:
            self.src_task_id = m.get('SrcTaskId')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class CreateDataFlowTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the dataflow task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataFlowTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDataFlowTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDataFlowTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataFlowTaskResponse, self).to_map()
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
            temp_model = CreateDataFlowTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequest(TeaModel):
    def __init__(self, file_system_id=None, owner=None, owner_access_inheritable=None, path=None, type=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the portable account. The ID must be a 16-digit string. The string can contain digits and lowercase letters.
        self.owner = owner  # type: str
        # Specifies whether to share the directory. Valid values:
        # 
        # *   false (default): does not share the directory.
        # *   true: shares the directory.
        # 
        # > *   This parameter takes effect only if the Type parameter is set to Directory and the Owner parameter is not empty.
        # > *   The permissions on a directory can be inherited by the owner. The owner has read and write permissions on the subdirectories and subfiles created in the directory, even if they are created by others.
        self.owner_access_inheritable = owner_access_inheritable  # type: bool
        # The absolute path of the directory or file. The path must start and end with a forward slash (/) and must be 2 to 1024 characters in length.
        self.path = path  # type: str
        # The type of the object. Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_access_inheritable is not None:
            result['OwnerAccessInheritable'] = self.owner_access_inheritable
        if self.path is not None:
            result['Path'] = self.path
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerAccessInheritable') is not None:
            self.owner_access_inheritable = m.get('OwnerAccessInheritable')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileResponseBody, self).to_map()
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


class CreateFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileResponse, self).to_map()
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
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileSystemRequest(TeaModel):
    def __init__(self, bandwidth=None, capacity=None, charge_type=None, client_token=None, description=None,
                 dry_run=None, duration=None, encrypt_type=None, file_system_type=None, kms_key_id=None, protocol_type=None,
                 snapshot_id=None, storage_type=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # The maximum throughput of the file system.
        # 
        # Unit: MB/s.
        # 
        # Specify a value based on the specifications on the buy page.
        self.bandwidth = bandwidth  # type: long
        # The capacity of the file system. Unit: GiB.
        # 
        # This parameter is valid and required if the FileSystemType parameter is set to extreme.
        # 
        # Specify a value based on the specifications on the following buy page:
        # 
        # [Extreme NAS file system (Pay-as-you-go)](https://common-buy-intl.alibabacloud.com/?commodityCode=nas_extpost_public_intl#/buy)
        self.capacity = capacity  # type: long
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PayAsYouGo (default): pay-as-you-go
        # *   Subscription: subscription
        self.charge_type = charge_type  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the precheck, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The subscription duration.
        # 
        # This parameter is valid and required only if the ChargeType parameter is set to Subscription. Unit: months.
        # 
        # If you do not renew a subscription file system when the file system expires, the file system is automatically released.
        self.duration = duration  # type: int
        # Specifies whether to encrypt the data in the NAS file system.
        # 
        # You can use a key that is managed by Key Management Service (KMS) to encrypt the data that is stored in a file system. When you read and write the encrypted data, the data is automatically decrypted.
        # 
        # Valid values:
        # 
        # *   0: The data in the file system is not encrypted.
        # *   1: A NAS-managed key is used to encrypt the data in the file system. This value is valid only if the FileSystemType parameter is set to standard or extreme.
        # *   2: A KMS-managed key is used to encrypt the data in the file system. This value is valid only if the FileSystemType parameter is set to extreme.
        # 
        # > You can use KMS-managed keys only in the following regions: US (Silicon Valley), US (Virginia), UK (London), Australia (Sydney), Germany (Frankfurt), India (Mumbai), and Singapore.
        self.encrypt_type = encrypt_type  # type: int
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type  # type: str
        # The ID of the KMS-managed key.
        # 
        # This parameter is required only if the EncryptType parameter is set to 2.
        self.kms_key_id = kms_key_id  # type: str
        # The protocol type.
        # 
        # *   If the FileSystemType parameter is set to standard, you can set the ProtocolType parameter to NFS or SMB.
        # *   If the FileSystemType parameter is set to extreme, you can set the ProtocolType parameter to NFS.
        self.protocol_type = protocol_type  # type: str
        # The snapshot ID.
        # 
        # This parameter is available only for Extreme NAS file systems.
        # 
        # > You can create a file system from a snapshot. In this case, the version of the file system is the same as that of the source file system. For example, the source file system of the snapshot uses version 1. To create a file system of version 2, you can create File System A from the snapshot and create File System B of version 2. You can then copy the data and migrate your business from File System A to File System B.
        self.snapshot_id = snapshot_id  # type: str
        # The storage type.
        # 
        # *   If the FileSystemType parameter is set to standard, you can set the StorageType parameter to Performance or Capacity.
        # *   If the FileSystemType parameter is set to extreme, you can set the StorageType parameter to standard or advance.
        self.storage_type = storage_type  # type: str
        # The ID of the vSwitch.
        # 
        # This parameter is reserved and does not take effect. You do not need to configure this parameter.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is reserved and does not take effect. You do not need to configure this parameter.
        self.vpc_id = vpc_id  # type: str
        # The zone ID.
        # 
        # Each region has multiple isolated locations known as zones. Each zone has its own independent power supply and networks.
        # 
        # This parameter is not required if the FileSystemType parameter is set to standard. By default, a random zone is selected based on the protocol type and storage type.
        # 
        # This parameter is required if the FileSystemType parameter is set to extreme.
        # 
        # > *   An Elastic Compute Service (ECS) instance and a NAS file system that reside in different zones of the same region can access each other.
        # >*   We recommend that you select the zone where the ECS instance resides. This prevents cross-zone latency between the file system and the ECS instance.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFileSystemResponseBody(TeaModel):
    def __init__(self, file_system_id=None, request_id=None):
        # The ID of the file system that is created.
        self.file_system_id = file_system_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileSystemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileSystemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileSystemResponse, self).to_map()
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
            temp_model = CreateFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFilesetRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, file_system_id=None,
                 file_system_path=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the fileset.
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with http:// or https://.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FsetId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a fileset is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The absolute path of the fileset.
        # 
        # *   The parent directory of the path that you specify must be an existing directory in the file system.
        # *   The path must be 2 to 1,024 characters in length.
        # *   The path must start and end with a forward slash (/).
        self.file_system_path = file_system_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFilesetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        return self


class CreateFilesetResponseBody(TeaModel):
    def __init__(self, fset_id=None, request_id=None):
        # The fileset ID.
        self.fset_id = fset_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFilesetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFilesetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFilesetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFilesetResponse, self).to_map()
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
            temp_model = CreateFilesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLDAPConfigRequest(TeaModel):
    def __init__(self, bind_dn=None, file_system_id=None, search_base=None, uri=None):
        # An LDAP entry.
        self.bind_dn = bind_dn  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # An LDAP search base.
        self.search_base = search_base  # type: str
        # An LDAP URI.
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLDAPConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class CreateLDAPConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLDAPConfigResponseBody, self).to_map()
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


class CreateLDAPConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLDAPConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLDAPConfigResponse, self).to_map()
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
            temp_model = CreateLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecyclePolicyRequest(TeaModel):
    def __init__(self, file_system_id=None, lifecycle_policy_name=None, lifecycle_rule_name=None, path=None,
                 paths=None, storage_type=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The name of the lifecycle policy. The name must be 3 to 64 characters in length and can contain letters, digits, underscores (\_), and hyphens (-). The name must start with a letter.
        self.lifecycle_policy_name = lifecycle_policy_name  # type: str
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME\_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name  # type: str
        # The absolute path of the directory that is associated with the lifecycle policy.
        # 
        # If you specify this parameter, you can associate the lifecycle policy with only one directory. The path must start with a forward slash (/) and must be a path that exists in the mount target.
        # 
        # > We recommend that you specify the Paths.N parameter so that you can associate the lifecycle policy with multiple directories.
        self.path = path  # type: str
        # The absolute paths of the directories that are associated with the lifecycle policy.
        # 
        # If you specify this parameter, you can associate the lifecycle policy with multiple directories. Each path must start with a forward slash (/) and must be a path that exists in the mount target. Valid values of N: 1 to 10.
        self.paths = paths  # type: list[str]
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLifecyclePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.path is not None:
            result['Path'] = self.path
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class CreateLifecyclePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLifecyclePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLifecyclePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLifecyclePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLifecyclePolicyResponse, self).to_map()
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
            temp_model = CreateLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLifecycleRetrieveJobRequest(TeaModel):
    def __init__(self, file_system_id=None, paths=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The directories or files that you want to retrieve. You can specify a maximum of 10 paths.
        self.paths = paths  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLifecycleRetrieveJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.paths is not None:
            result['Paths'] = self.paths
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        return self


class CreateLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the data retrieval task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLifecycleRetrieveJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLifecycleRetrieveJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLifecycleRetrieveJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLifecycleRetrieveJobResponse, self).to_map()
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
            temp_model = CreateLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogAnalysisRequest(TeaModel):
    def __init__(self, file_system_id=None, region_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogAnalysisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateLogAnalysisResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogAnalysisResponseBody, self).to_map()
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


class CreateLogAnalysisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLogAnalysisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLogAnalysisResponse, self).to_map()
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
            temp_model = CreateLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMountTargetRequest(TeaModel):
    def __init__(self, access_group_name=None, dry_run=None, enable_ipv_6=None, file_system_id=None,
                 network_type=None, security_group_id=None, v_switch_id=None, vpc_id=None):
        # The name of the permission group.
        # 
        # This parameter is required if you create a mount target for a General-purpose NAS file system or an Extreme NAS file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        self.access_group_name = access_group_name  # type: str
        # Specifies whether to perform a dry run to check for existing mount targets. This parameter is valid only for CPFS file systems.
        # 
        # If you set this parameter to true, the system checks whether the request parameters are valid and whether the requested resources are available. In this case, no mount target is created and no fee is incurred.
        # 
        # *   true: performs a dry run but does not create a mount target. In the dry run, the system checks the request format, service limits, available CPFS resources, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code `200` is returned. No value is returned for the `MountTargetDomain` parameter.
        # *   false (default): sends the request. If the request passes the dry run, a mount target is created.
        self.dry_run = dry_run  # type: bool
        # Specifies whether to create an IPv6 domain name for the mount target.
        # 
        # Valid values:
        # 
        # *   true: An IPv6 domain name is created for the mount target.
        # *   false (default): No IPv6 domain name is created for the mount target.
        # 
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6. If you want to create an IPv6 domain name for the mount target, you must enable IPv6 for the file system.
        self.enable_ipv_6 = enable_ipv_6  # type: bool
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\*\*\*\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\*\*\*\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-125487\*\*\*\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str
        # The network type of the mount target. Valid value: **Vpc**.
        self.network_type = network_type  # type: str
        # The ID of the security group.
        self.security_group_id = security_group_id  # type: str
        # The ID of the vSwitch.
        # 
        # This parameter is valid and required if the mount target resides in a VPC. Example: If you set the NetworkType parameter to VPC, you must specify the VSwitchId parameter.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the VPC.
        # 
        # This parameter is valid and required if the mount target resides in a VPC. Example: If you set the NetworkType parameter to VPC, you must specify the VpcId parameter.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateMountTargetResponseBodyMountTargetExtra(TeaModel):
    def __init__(self, dual_stack_mount_target_domain=None):
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMountTargetResponseBodyMountTargetExtra, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        return self


class CreateMountTargetResponseBody(TeaModel):
    def __init__(self, mount_target_domain=None, mount_target_extra=None, request_id=None):
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str
        # The information about the mount target.
        self.mount_target_extra = mount_target_extra  # type: CreateMountTargetResponseBodyMountTargetExtra
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.mount_target_extra:
            self.mount_target_extra.validate()

    def to_map(self):
        _map = super(CreateMountTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.mount_target_extra is not None:
            result['MountTargetExtra'] = self.mount_target_extra.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('MountTargetExtra') is not None:
            temp_model = CreateMountTargetResponseBodyMountTargetExtra()
            self.mount_target_extra = temp_model.from_map(m['MountTargetExtra'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMountTargetResponse, self).to_map()
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
            temp_model = CreateMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtocolMountTargetRequest(TeaModel):
    def __init__(self, access_group_name=None, client_token=None, description=None, dry_run=None,
                 file_system_id=None, fset_id=None, path=None, protocol_service_id=None, v_switch_id=None, vpc_id=None):
        # The name of the permission group.
        # 
        # Default value: DEFAULT_VPC_GROUP_NAME.
        self.access_group_name = access_group_name  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the export directory for the protocol service. The **name of the export directory** appears in the console.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform a dry run. The dry run checks parameter validity and prerequisites. The dry run does not create an export directory or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the ExportId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, an export directory is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the fileset that you want to export.
        # 
        # Limits:
        # 
        # *   The fileset already exists.
        # *   You can create only one export directory for a fileset.
        # *   You can specify either a fileset or a path.
        self.fset_id = fset_id  # type: str
        # The path of the CPFS directory that you want to export.
        # 
        # Limits:
        # 
        # *   The directory already exists in the CPFS file system.
        # *   You can create only one export directory for a directory.
        # *   You can specify either a fileset or a path.
        # 
        # Format:
        # 
        # *   The path must be 1 to 1,024 characters in length.
        # *   The path must be encoded in UTF-8.
        # *   The path must start and end with a forward slash (/). The root directory is `/`.
        self.path = path  # type: str
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str
        # The vSwitch ID of the export directory for the protocol service.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC ID of the export directory for the protocol service.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProtocolMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.path is not None:
            result['Path'] = self.path
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateProtocolMountTargetResponseBody(TeaModel):
    def __init__(self, export_id=None, request_id=None):
        # The ID of the export directory for the protocol service.
        self.export_id = export_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProtocolMountTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProtocolMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProtocolMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProtocolMountTargetResponse, self).to_map()
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
            temp_model = CreateProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtocolServiceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, file_system_id=None, protocol_spec=None,
                 protocol_type=None, throughput=None, v_switch_id=None, vpc_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the protocol service. The name of the protocol service appears in the console.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform a dry run.
        # 
        # The dry run checks parameter validity and prerequisites. The dry run does not create a protocol service or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run and does not create the protocol service. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the ProtocolServiceId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a protocol service is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The specification of the protocol service.
        # 
        # Set the value to General (default).
        # 
        # Valid values:
        # 
        # *   CL2
        # *   General
        # *   CL1
        self.protocol_spec = protocol_spec  # type: str
        # The protocol type of the protocol service.
        # 
        # Valid value: NFS (default). Only NFSv3 is supported.
        self.protocol_type = protocol_type  # type: str
        # The throughput of the protocol service.
        # 
        # Unit: MB/s.
        self.throughput = throughput  # type: int
        # The vSwitch ID of the protocol service.
        self.v_switch_id = v_switch_id  # type: str
        # The virtual private cloud (VPC) ID of the protocol service. The VPC ID of the protocol service must be the same as the VPC ID of the file system.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProtocolServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_spec is not None:
            result['ProtocolSpec'] = self.protocol_spec
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolSpec') is not None:
            self.protocol_spec = m.get('ProtocolSpec')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateProtocolServiceResponseBody(TeaModel):
    def __init__(self, protocol_service_id=None, request_id=None):
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProtocolServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProtocolServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProtocolServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProtocolServiceResponse, self).to_map()
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
            temp_model = CreateProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecycleBinDeleteJobRequest(TeaModel):
    def __init__(self, client_token=None, file_id=None, file_system_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The ID of the file or directory that you want to permanently delete.
        # 
        # You can call the [ListRecycledDirectoriesAndFiles](~~264193~~) operation to query the value of the FileId parameter.
        self.file_id = file_id  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecycleBinDeleteJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class CreateRecycleBinDeleteJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The job ID.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecycleBinDeleteJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRecycleBinDeleteJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRecycleBinDeleteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRecycleBinDeleteJobResponse, self).to_map()
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
            temp_model = CreateRecycleBinDeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecycleBinRestoreJobRequest(TeaModel):
    def __init__(self, client_token=None, file_id=None, file_system_id=None, target_file_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The ID of the file or directory that you want to restore.
        # 
        # You can call the [ListRecycleBinJobs](~~264192~~) operation to query the value of the FileId parameter.
        self.file_id = file_id  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the directory to which the file is restored.
        self.target_file_id = target_file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecycleBinRestoreJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.target_file_id is not None:
            result['TargetFileId'] = self.target_file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('TargetFileId') is not None:
            self.target_file_id = m.get('TargetFileId')
        return self


class CreateRecycleBinRestoreJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The job ID.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecycleBinRestoreJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRecycleBinRestoreJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRecycleBinRestoreJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRecycleBinRestoreJobResponse, self).to_map()
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
            temp_model = CreateRecycleBinRestoreJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, retention_days=None, snapshot_name=None):
        # The description of the snapshot.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 256 characters in length.
        # *   The description cannot start with `http://` or `https://`.
        # *   This parameter is empty by default.
        self.description = description  # type: str
        # The ID of the advanced Extreme NAS file system. The value must start with `extreme-`, for example, `extreme-01dd****`.
        self.file_system_id = file_system_id  # type: str
        # The retention period of the snapshot.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \-1 (default). Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days  # type: int
        # The snapshot name.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`.
        # *   The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        # *   The name cannot start with auto because snapshots whose names start with auto are recognized as auto snapshots.
        self.snapshot_name = snapshot_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None, snapshot_id=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The snapshot ID.
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


class DeleteAccessGroupRequest(TeaModel):
    def __init__(self, access_group_name=None, file_system_type=None):
        # The name of the permission group to be deleted.
        self.access_group_name = access_group_name  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DeleteAccessGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessGroupResponseBody, self).to_map()
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


class DeleteAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessGroupResponse, self).to_map()
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
            temp_model = DeleteAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessRuleRequest(TeaModel):
    def __init__(self, access_group_name=None, access_rule_id=None, file_system_type=None):
        # The name of the permission group.
        self.access_group_name = access_group_name  # type: str
        # The rule ID.
        self.access_rule_id = access_rule_id  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class DeleteAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessRuleResponseBody, self).to_map()
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


class DeleteAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessRuleResponse, self).to_map()
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
            temp_model = DeleteAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None):
        # The ID of the automatic snapshot policy.
        # 
        # You can call the [DescribeAutoSnapshotPolicies](~~126583~~) operation to view available automatic snapshot policies.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        return self


class DeleteAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
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


class DeleteDataFlowRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, dry_run=None, file_system_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteDataFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataFlowResponseBody, self).to_map()
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


class DeleteDataFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDataFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataFlowResponse, self).to_map()
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
            temp_model = DeleteDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileSystemRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system that you want to delete.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\*\*\*\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\*\*\*\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-00cb6fa094ca\*\*\*\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteFileSystemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileSystemResponseBody, self).to_map()
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


class DeleteFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFileSystemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileSystemResponse, self).to_map()
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
            temp_model = DeleteFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilesetRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, file_system_id=None, fset_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is deleted.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a fileset is deleted.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The fileset ID.
        self.fset_id = fset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFilesetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        return self


class DeleteFilesetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFilesetResponseBody, self).to_map()
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


class DeleteFilesetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFilesetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFilesetResponse, self).to_map()
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
            temp_model = DeleteFilesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLDAPConfigRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLDAPConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteLDAPConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLDAPConfigResponseBody, self).to_map()
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


class DeleteLDAPConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLDAPConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLDAPConfigResponse, self).to_map()
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
            temp_model = DeleteLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLifecyclePolicyRequest(TeaModel):
    def __init__(self, file_system_id=None, lifecycle_policy_name=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The name of the lifecycle policy.
        self.lifecycle_policy_name = lifecycle_policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLifecyclePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        return self


class DeleteLifecyclePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: The request failed.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLifecyclePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLifecyclePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLifecyclePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLifecyclePolicyResponse, self).to_map()
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
            temp_model = DeleteLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogAnalysisRequest(TeaModel):
    def __init__(self, file_system_id=None, region_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLogAnalysisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteLogAnalysisResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLogAnalysisResponseBody, self).to_map()
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


class DeleteLogAnalysisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLogAnalysisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLogAnalysisResponse, self).to_map()
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
            temp_model = DeleteLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMountTargetRequest(TeaModel):
    def __init__(self, file_system_id=None, mount_target_domain=None):
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\*\*\*\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\*\*\*\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-125487\*\*\*\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        return self


class DeleteMountTargetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMountTargetResponseBody, self).to_map()
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


class DeleteMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMountTargetResponse, self).to_map()
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
            temp_model = DeleteMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProtocolMountTargetRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, export_id=None, file_system_id=None,
                 protocol_service_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not delete the specified export directory or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified export directory is deleted.
        self.dry_run = dry_run  # type: bool
        # The ID of the export directory.
        self.export_id = export_id  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProtocolMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class DeleteProtocolMountTargetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProtocolMountTargetResponseBody, self).to_map()
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


class DeleteProtocolMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProtocolMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProtocolMountTargetResponse, self).to_map()
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
            temp_model = DeleteProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProtocolServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, file_system_id=None, protocol_service_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not delete the specified protocol service.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified protocol service is deleted.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProtocolServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class DeleteProtocolServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProtocolServiceResponseBody, self).to_map()
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


class DeleteProtocolServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProtocolServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProtocolServiceResponse, self).to_map()
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
            temp_model = DeleteProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(self, snapshot_id=None):
        # The snapshot ID.
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
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


class DescribeAccessGroupsRequest(TeaModel):
    def __init__(self, access_group_name=None, file_system_type=None, page_number=None, page_size=None,
                 use_utcdate_time=None):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (\_), and hyphens (-).
        self.access_group_name = access_group_name  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # Specifies whether to display the creation time of the permission group in UTC.
        # 
        # Valid values:
        # 
        # *   true (default): The time is displayed in UTC.
        # *   false: The time is not displayed in UTC.
        self.use_utcdate_time = use_utcdate_time  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccessGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')
        return self


class DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup(TeaModel):
    def __init__(self, access_group_name=None, access_group_type=None, create_time=None, description=None,
                 mount_target_count=None, rule_count=None):
        # The name of the permission group.
        self.access_group_name = access_group_name  # type: str
        # The network type of the permission group. Valid value: **Vpc**.
        self.access_group_type = access_group_type  # type: str
        # The time when the permission group was created.
        self.create_time = create_time  # type: str
        # The description of the permission group.
        self.description = description  # type: str
        # The number of mount targets to which the permission group is attached.
        self.mount_target_count = mount_target_count  # type: int
        # The total number of rules in the permission group.
        self.rule_count = rule_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class DescribeAccessGroupsResponseBodyAccessGroups(TeaModel):
    def __init__(self, access_group=None):
        self.access_group = access_group  # type: list[DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup]

    def validate(self):
        if self.access_group:
            for k in self.access_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccessGroupsResponseBodyAccessGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessGroup'] = []
        if self.access_group is not None:
            for k in self.access_group:
                result['AccessGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.access_group = []
        if m.get('AccessGroup') is not None:
            for k in m.get('AccessGroup'):
                temp_model = DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup()
                self.access_group.append(temp_model.from_map(k))
        return self


class DescribeAccessGroupsResponseBody(TeaModel):
    def __init__(self, access_groups=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The queried permission groups.
        self.access_groups = access_groups  # type: DescribeAccessGroupsResponseBodyAccessGroups
        # The page number.
        self.page_number = page_number  # type: int
        # The number of permission groups returned per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of permission groups.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.access_groups:
            self.access_groups.validate()

    def to_map(self):
        _map = super(DescribeAccessGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_groups is not None:
            result['AccessGroups'] = self.access_groups.to_map()
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
        if m.get('AccessGroups') is not None:
            temp_model = DescribeAccessGroupsResponseBodyAccessGroups()
            self.access_groups = temp_model.from_map(m['AccessGroups'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccessGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAccessGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccessGroupsResponse, self).to_map()
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
            temp_model = DescribeAccessGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessRulesRequest(TeaModel):
    def __init__(self, access_group_name=None, access_rule_id=None, file_system_type=None, page_number=None,
                 page_size=None):
        # The name of the permission group.
        self.access_group_name = access_group_name  # type: str
        # The ID of the rule.
        self.access_rule_id = access_rule_id  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccessRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAccessRulesResponseBodyAccessRulesAccessRule(TeaModel):
    def __init__(self, access_rule_id=None, ipv_6source_cidr_ip=None, priority=None, rwaccess=None,
                 source_cidr_ip=None, user_access=None):
        # The ID of the rule.
        self.access_rule_id = access_rule_id  # type: str
        # The IPv6 address or CIDR block of the authorized object.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip  # type: str
        # The priority of the rule.
        # 
        # If multiple rules are attached to the authorized object, the rule with the highest priority takes effect.
        # 
        # Valid values: 1 to 100. The value 1 indicates the highest priority.
        self.priority = priority  # type: int
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess = rwaccess  # type: str
        # The IP address or CIDR block of the authorized object.
        self.source_cidr_ip = source_cidr_ip  # type: str
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash: allows access from root users to the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
        self.user_access = user_access  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAccessRulesResponseBodyAccessRulesAccessRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess is not None:
            result['RWAccess'] = self.rwaccess
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.user_access is not None:
            result['UserAccess'] = self.user_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccess') is not None:
            self.rwaccess = m.get('RWAccess')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('UserAccess') is not None:
            self.user_access = m.get('UserAccess')
        return self


class DescribeAccessRulesResponseBodyAccessRules(TeaModel):
    def __init__(self, access_rule=None):
        self.access_rule = access_rule  # type: list[DescribeAccessRulesResponseBodyAccessRulesAccessRule]

    def validate(self):
        if self.access_rule:
            for k in self.access_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAccessRulesResponseBodyAccessRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessRule'] = []
        if self.access_rule is not None:
            for k in self.access_rule:
                result['AccessRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.access_rule = []
        if m.get('AccessRule') is not None:
            for k in m.get('AccessRule'):
                temp_model = DescribeAccessRulesResponseBodyAccessRulesAccessRule()
                self.access_rule.append(temp_model.from_map(k))
        return self


class DescribeAccessRulesResponseBody(TeaModel):
    def __init__(self, access_rules=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The rules in the permission group.
        self.access_rules = access_rules  # type: DescribeAccessRulesResponseBodyAccessRules
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of rules.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.access_rules:
            self.access_rules.validate()

    def to_map(self):
        _map = super(DescribeAccessRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rules is not None:
            result['AccessRules'] = self.access_rules.to_map()
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
        if m.get('AccessRules') is not None:
            temp_model = DescribeAccessRulesResponseBodyAccessRules()
            self.access_rules = temp_model.from_map(m['AccessRules'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAccessRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAccessRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAccessRulesResponse, self).to_map()
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
            temp_model = DescribeAccessRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoSnapshotPoliciesRequest(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, file_system_type=None, page_number=None, page_size=None):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        self.file_system_type = file_system_type  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoSnapshotPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, auto_snapshot_policy_name=None, create_time=None,
                 file_system_nums=None, region_id=None, repeat_weekdays=None, retention_days=None, status=None, time_points=None):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # The name of the automatic snapshot policy.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name  # type: str
        # The time when the automatic snapshot policy was created.
        # 
        # The time follows the [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The number of file systems to which the automatic snapshot policy applies.
        self.file_system_nums = file_system_nums  # type: int
        # The region ID of the automatic snapshot policy.
        self.region_id = region_id  # type: str
        # The days of a week on which auto snapshots are created.
        # 
        # Auto snapshots are created on a weekly basis.
        # 
        # Valid values: 1 to 7. The values from 1 to 7 indicate 7 days in a week from Monday to Sunday.
        self.repeat_weekdays = repeat_weekdays  # type: str
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \-1: Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days  # type: int
        # The status of the automatic snapshot policy.
        # 
        # Valid values:
        # 
        # *   Creating: The automatic snapshot policy is being created.
        # *   Available: The automatic snapshot policy is available.
        self.status = status  # type: str
        # The points in time at which auto snapshots are created.
        # 
        # Unit: hours.
        # 
        # Valid values: `0 to 23`. The values from 0 to 23 indicate a total of 24 hours from `00:00 to 23:00`. For example, 1 indicates 01:00. A maximum of 24 points in time can be returned. Multiple points in time are separated with commas (,).
        self.time_points = time_points  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_system_nums is not None:
            result['FileSystemNums'] = self.file_system_nums
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.status is not None:
            result['Status'] = self.status
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileSystemNums') is not None:
            self.file_system_nums = m.get('FileSystemNums')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies(TeaModel):
    def __init__(self, auto_snapshot_policy=None):
        self.auto_snapshot_policy = auto_snapshot_policy  # type: list[DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy]

    def validate(self):
        if self.auto_snapshot_policy:
            for k in self.auto_snapshot_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoSnapshotPolicy'] = []
        if self.auto_snapshot_policy is not None:
            for k in self.auto_snapshot_policy:
                result['AutoSnapshotPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_snapshot_policy = []
        if m.get('AutoSnapshotPolicy') is not None:
            for k in m.get('AutoSnapshotPolicy'):
                temp_model = DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy()
                self.auto_snapshot_policy.append(temp_model.from_map(k))
        return self


class DescribeAutoSnapshotPoliciesResponseBody(TeaModel):
    def __init__(self, auto_snapshot_policies=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        # The queried automatic snapshot policies.
        self.auto_snapshot_policies = auto_snapshot_policies  # type: DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of automatic snapshot policies.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.auto_snapshot_policies:
            self.auto_snapshot_policies.validate()

    def to_map(self):
        _map = super(DescribeAutoSnapshotPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policies is not None:
            result['AutoSnapshotPolicies'] = self.auto_snapshot_policies.to_map()
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
        if m.get('AutoSnapshotPolicies') is not None:
            temp_model = DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies()
            self.auto_snapshot_policies = temp_model.from_map(m['AutoSnapshotPolicies'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAutoSnapshotPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutoSnapshotPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoSnapshotPoliciesResponse, self).to_map()
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
            temp_model = DescribeAutoSnapshotPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoSnapshotTasksRequest(TeaModel):
    def __init__(self, auto_snapshot_policy_ids=None, file_system_ids=None, file_system_type=None,
                 page_number=None, page_size=None):
        # The IDs of automatic snapshot policies.
        # 
        # You can specify a maximum of 100 policy IDs. If you want to query the tasks of multiple automatic snapshot policies, you must separate the policy IDs with commas (,).
        self.auto_snapshot_policy_ids = auto_snapshot_policy_ids  # type: str
        # The ID of the file system.
        # 
        # You can specify a maximum of 100 file system IDs. If you want to query the snapshots of multiple file systems, you must separate the file system IDs with commas (,).
        self.file_system_ids = file_system_ids  # type: str
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        self.file_system_type = file_system_type  # type: str
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_number = page_number  # type: int
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoSnapshotTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_ids is not None:
            result['AutoSnapshotPolicyIds'] = self.auto_snapshot_policy_ids
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyIds') is not None:
            self.auto_snapshot_policy_ids = m.get('AutoSnapshotPolicyIds')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, source_file_system_id=None):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # The ID of the file system.
        self.source_file_system_id = source_file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')
        return self


class DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks(TeaModel):
    def __init__(self, auto_snapshot_task=None):
        self.auto_snapshot_task = auto_snapshot_task  # type: list[DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask]

    def validate(self):
        if self.auto_snapshot_task:
            for k in self.auto_snapshot_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoSnapshotTask'] = []
        if self.auto_snapshot_task is not None:
            for k in self.auto_snapshot_task:
                result['AutoSnapshotTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_snapshot_task = []
        if m.get('AutoSnapshotTask') is not None:
            for k in m.get('AutoSnapshotTask'):
                temp_model = DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasksAutoSnapshotTask()
                self.auto_snapshot_task.append(temp_model.from_map(k))
        return self


class DescribeAutoSnapshotTasksResponseBody(TeaModel):
    def __init__(self, auto_snapshot_tasks=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        # The queried automatic snapshot tasks.
        self.auto_snapshot_tasks = auto_snapshot_tasks  # type: DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of automatic snapshot tasks.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.auto_snapshot_tasks:
            self.auto_snapshot_tasks.validate()

    def to_map(self):
        _map = super(DescribeAutoSnapshotTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_tasks is not None:
            result['AutoSnapshotTasks'] = self.auto_snapshot_tasks.to_map()
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
        if m.get('AutoSnapshotTasks') is not None:
            temp_model = DescribeAutoSnapshotTasksResponseBodyAutoSnapshotTasks()
            self.auto_snapshot_tasks = temp_model.from_map(m['AutoSnapshotTasks'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAutoSnapshotTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutoSnapshotTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoSnapshotTasksResponse, self).to_map()
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
            temp_model = DescribeAutoSnapshotTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackListClientsRequest(TeaModel):
    def __init__(self, client_ip=None, file_system_id=None, region_id=None):
        # The IP address of the client.
        self.client_ip = client_ip  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the region where the file system resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlackListClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBlackListClientsResponseBody(TeaModel):
    def __init__(self, clients=None, request_id=None):
        # The IDs of clients and the status of each client. This parameter contains a JSON object, for example, {"client1": "EVICTING","client2":"EVICTED"}.
        # 
        # Available client statuses include:
        # 
        # *   EVICTING indicates that a client is being removed
        # *   EVICTED indicates that a client is removed
        # *   ACCEPTING indicates that the write access to the file system is being granted to a client
        # *   ACCEPTABLE indicates that the write access to the file system is granted to a client
        self.clients = clients  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlackListClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clients') is not None:
            self.clients = m.get('Clients')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBlackListClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBlackListClientsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBlackListClientsResponse, self).to_map()
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
            temp_model = DescribeBlackListClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataFlowTasksRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        # *\
        self.key = key  # type: str
        # *   ````
        # *   ````
        # *\
        # *\
        # *\
        # *\
        # *   ``
        # *   ``
        # *   ``
        # *   ``
        # *   ``
        # *   ``
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataFlowTasksRequestFilters, self).to_map()
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


class DescribeDataFlowTasksRequest(TeaModel):
    def __init__(self, file_system_id=None, filters=None, max_results=None, next_token=None):
        self.file_system_id = file_system_id  # type: str
        self.filters = filters  # type: list[DescribeDataFlowTasksRequestFilters]
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataFlowTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeDataFlowTasksRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDataFlowTasksResponseBodyTaskInfoTask(TeaModel):
    def __init__(self, create_time=None, data_flow_id=None, data_type=None, end_time=None, file_system_path=None,
                 filesystem_id=None, fs_path=None, originator=None, progress=None, report_path=None, source_storage=None,
                 start_time=None, status=None, task_action=None, task_id=None):
        # The time when the task was created.
        self.create_time = create_time  # type: str
        self.data_flow_id = data_flow_id  # type: str
        # null Valid values:
        # 
        # *   null null
        # *   null
        # *   null
        self.data_type = data_type  # type: str
        # The time when the task ended.
        self.end_time = end_time  # type: str
        # *\
        # *\
        # *\
        # *   null
        self.file_system_path = file_system_path  # type: str
        self.filesystem_id = filesystem_id  # type: str
        # null
        self.fs_path = fs_path  # type: str
        # null Valid values:
        # 
        # *   null
        # *   null
        self.originator = originator  # type: str
        # null null
        self.progress = progress  # type: long
        # null
        # 
        # null``
        # 
        # Limits:
        # 
        # *   null
        # *   The name must be encoded in UTF-8.
        self.report_path = report_path  # type: str
        # ://\
        # 
        # *\
        # *   *\
        #     *\
        #     *\
        #     *   [](http://https://。)
        # 
        # **\
        # 
        # ****\
        self.source_storage = source_storage  # type: str
        # null
        self.start_time = start_time  # type: str
        # null Valid values:
        # 
        # *   null
        # *   null
        # *   null
        # *   null
        # *   null
        # *   null
        self.status = status  # type: str
        # null Valid values:
        # 
        # *   null
        # *   null
        # *   null null
        # *   null
        self.task_action = task_action  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataFlowTasksResponseBodyTaskInfoTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.filesystem_id is not None:
            result['FilesystemId'] = self.filesystem_id
        if self.fs_path is not None:
            result['FsPath'] = self.fs_path
        if self.originator is not None:
            result['Originator'] = self.originator
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.report_path is not None:
            result['ReportPath'] = self.report_path
        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FilesystemId') is not None:
            self.filesystem_id = m.get('FilesystemId')
        if m.get('FsPath') is not None:
            self.fs_path = m.get('FsPath')
        if m.get('Originator') is not None:
            self.originator = m.get('Originator')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ReportPath') is not None:
            self.report_path = m.get('ReportPath')
        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDataFlowTasksResponseBodyTaskInfo(TeaModel):
    def __init__(self, task=None):
        self.task = task  # type: list[DescribeDataFlowTasksResponseBodyTaskInfoTask]

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataFlowTasksResponseBodyTaskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeDataFlowTasksResponseBodyTaskInfoTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeDataFlowTasksResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, task_info=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.task_info = task_info  # type: DescribeDataFlowTasksResponseBodyTaskInfo

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super(DescribeDataFlowTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskInfo') is not None:
            temp_model = DescribeDataFlowTasksResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class DescribeDataFlowTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataFlowTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataFlowTasksResponse, self).to_map()
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
            temp_model = DescribeDataFlowTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataFlowsRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The filter name. Valid values:
        # 
        # *   DataFlowIds: filters dataflows by dataflow ID.
        # *   FsetIds: filters dataflows by fileset ID.
        # *   FileSystemPath: filters dataflows based on the path of a fileset in a CPFS file system.
        # *   SourceStorage: filters dataflows based on the access path of the source storage.
        # *   ThroughputList: filters dataflows based on dataflow throughput.
        # *   Description: filters dataflows based on the fileset description.
        # *   Status: filters dataflows based on dataflow status.
        self.key = key  # type: str
        # The value of the filter. This parameter does not support wildcards.
        # 
        # *   If Key is set to DataFlowIds, set Value to a data flow ID or a part of the data flow ID. You can specify a dataflow ID or a group of dataflow IDs. You can specify a maximum of 10 dataflow IDs. Example: `dfid-12345678` or `dfid-12345678,dfid-12345679`.
        # *   If Key is set to FsetIds, set Value to a fileset ID or a part of the fileset ID. You can specify a fileset ID or a group of fileset IDs. You can specify a maximum of 10 fileset IDs. Example: `fset-12345678` or `fset-12345678,fset-12345679`.
        # *   If Key set to FileSystemPath, set Value to the path or a part of the path of a fileset in a CPFS file system. The value must be 2 to 1,024 characters in length. The value must be encoded in UTF-8.
        # *   If Key is set to SourceStorage, set Value to the access path or a part of the access path of the source storage. The value must be 8 to 128 characters in length. The value must be encoded in UTF-8 and comply with the naming conventions of Object Storage Service (OSS) buckets.
        # *   If Key is set to ThroughputList, set Value to the dataflow throughput. Combined query is supported.
        # *   If Key is set to Description, set Value to a dataflow description or a part of the dataflow description.
        # *   If Key is set to Status, set Value to the dataflow status.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataFlowsRequestFilters, self).to_map()
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


class DescribeDataFlowsRequest(TeaModel):
    def __init__(self, file_system_id=None, filters=None, max_results=None, next_token=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The filter that is used to query dataflows.
        self.filters = filters  # type: list[DescribeDataFlowsRequestFilters]
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataFlowsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeDataFlowsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh(TeaModel):
    def __init__(self, refresh_path=None):
        # The automatic update directory. CPFS automatically checks whether the source data only in the directory is updated and imports the updated data.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # 
        # >  The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        self.refresh_path = refresh_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')
        return self


class DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh(TeaModel):
    def __init__(self, auto_refresh=None):
        self.auto_refresh = auto_refresh  # type: list[DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh]

    def validate(self):
        if self.auto_refresh:
            for k in self.auto_refresh:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoRefresh'] = []
        if self.auto_refresh is not None:
            for k in self.auto_refresh:
                result['AutoRefresh'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_refresh = []
        if m.get('AutoRefresh') is not None:
            for k in m.get('AutoRefresh'):
                temp_model = DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh()
                self.auto_refresh.append(temp_model.from_map(k))
        return self


class DescribeDataFlowsResponseBodyDataFlowInfoDataFlow(TeaModel):
    def __init__(self, auto_refresh=None, auto_refresh_interval=None, auto_refresh_policy=None, create_time=None,
                 data_flow_id=None, description=None, error_message=None, file_system_id=None, file_system_path=None,
                 fset_description=None, fset_id=None, source_security_type=None, source_storage=None, status=None, throughput=None,
                 update_time=None):
        # The details about automatic update policies.
        self.auto_refresh = auto_refresh  # type: DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
        self.auto_refresh_interval = auto_refresh_interval  # type: long
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy. Valid values:
        # 
        # *   None: Updated data in the source storage is not automatically imported to the CPFS file system. You can run a dataflow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported to the CPFS file system.
        self.auto_refresh_policy = auto_refresh_policy  # type: str
        # The time when the fileset was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The error message returned. Valid values:
        # 
        # *   None (default): The dataflow status is normal.
        # *   SourceStorageUnreachable: The access path of the source storage is not found.
        # *   ThroughputTooLow: The dataflow throughput is low.
        self.error_message = error_message  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The directory of the fileset in the CPFS file system.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be a fileset directory in the CPFS file system.
        self.file_system_path = file_system_path  # type: str
        # The description of the automatic update.
        self.fset_description = fset_description  # type: str
        # The fileset ID.
        self.fset_id = fset_id  # type: str
        # The type of security mechanism for the source storage. This parameter must be specified if the source storage is accessed with a security mechanism. Valid values:
        # 
        # *   None (default): The source storage can be accessed without a security mechanism.
        # *   SSL: The source storage must be accessed with an SSL certificate.
        self.source_security_type = source_security_type  # type: str
        # The access path of the source storage. Format:://.
        # 
        # Parameters:
        # 
        # *   storage type: Only OSS is supported.
        # 
        # *   path: the name of the OSS bucket.
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name must be 8 to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        #     *   The name cannot start with http:// or https://.
        # 
        # >  The OSS bucket must be an existing bucket in the region.
        self.source_storage = source_storage  # type: str
        # The dataflow status. Valid values:
        # 
        # *   Starting: The dataflow is being created or enabled.
        # *   Running: The dataflow has been created and is running properly.
        # *   Updating: The dataflow is being modified. For example, the dataflow throughput is increased and the automatic update interval is modified.
        # *   Deleting: The dataflow is being deleted.
        # *   Stopping: The dataflow is being disabled.
        # *   Stopped: The dataflow has been disabled.
        # *   Misconfigured: The dataflow configuration is abnormal. For example, the source storage is inaccessible, and the automatic update cannot be completed due to low dataflow throughput.
        self.status = status  # type: str
        # The maximum dataflow throughput. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1,200
        # *   1,500
        # 
        # >  The dataflow throughput must be less than the I/O throughput of the file system.
        self.throughput = throughput  # type: long
        # The time when the fileset was last updated.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.auto_refresh:
            self.auto_refresh.validate()

    def to_map(self):
        _map = super(DescribeDataFlowsResponseBodyDataFlowInfoDataFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh is not None:
            result['AutoRefresh'] = self.auto_refresh.to_map()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.description is not None:
            result['Description'] = self.description
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.fset_description is not None:
            result['FsetDescription'] = self.fset_description
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.source_security_type is not None:
            result['SourceSecurityType'] = self.source_security_type
        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage
        if self.status is not None:
            result['Status'] = self.status
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRefresh') is not None:
            temp_model = DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh()
            self.auto_refresh = temp_model.from_map(m['AutoRefresh'])
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')
        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FsetDescription') is not None:
            self.fset_description = m.get('FsetDescription')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('SourceSecurityType') is not None:
            self.source_security_type = m.get('SourceSecurityType')
        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDataFlowsResponseBodyDataFlowInfo(TeaModel):
    def __init__(self, data_flow=None):
        self.data_flow = data_flow  # type: list[DescribeDataFlowsResponseBodyDataFlowInfoDataFlow]

    def validate(self):
        if self.data_flow:
            for k in self.data_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDataFlowsResponseBodyDataFlowInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataFlow'] = []
        if self.data_flow is not None:
            for k in self.data_flow:
                result['DataFlow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_flow = []
        if m.get('DataFlow') is not None:
            for k in m.get('DataFlow'):
                temp_model = DescribeDataFlowsResponseBodyDataFlowInfoDataFlow()
                self.data_flow.append(temp_model.from_map(k))
        return self


class DescribeDataFlowsResponseBody(TeaModel):
    def __init__(self, data_flow_info=None, next_token=None, request_id=None):
        # The details about dataflows.
        self.data_flow_info = data_flow_info  # type: DescribeDataFlowsResponseBodyDataFlowInfo
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_flow_info:
            self.data_flow_info.validate()

    def to_map(self):
        _map = super(DescribeDataFlowsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_flow_info is not None:
            result['DataFlowInfo'] = self.data_flow_info.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataFlowInfo') is not None:
            temp_model = DescribeDataFlowsResponseBodyDataFlowInfo()
            self.data_flow_info = temp_model.from_map(m['DataFlowInfo'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataFlowsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDataFlowsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDataFlowsResponse, self).to_map()
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
            temp_model = DescribeDataFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirQuotasRequest(TeaModel):
    def __init__(self, file_system_id=None, page_number=None, page_size=None, path=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Default value: 10.
        # 
        # Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The absolute path of a directory.
        # 
        # If you do not specify this parameter, all directories for which quotas are created are returned.
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirQuotasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos(TeaModel):
    def __init__(self, file_count_limit=None, file_count_real=None, quota_type=None, size_limit=None,
                 size_real=None, user_id=None, user_type=None):
        # The maximum number of files that a user can create in the directory.
        self.file_count_limit = file_count_limit  # type: long
        # The total number of files that a user has created in the directory.
        self.file_count_real = file_count_real  # type: long
        # The type of the quota. Valid values: Accounting and Enforcement.
        self.quota_type = quota_type  # type: str
        # The maximum size of files that a user can create in the directory. Unit: GiB.
        self.size_limit = size_limit  # type: long
        # The total size of files that a user has created in the directory. Unit: GiB.
        self.size_real = size_real  # type: long
        # The ID of the user that you specify to create a quota for the directory. The value depends on the value of the UserType parameter. Valid values: Uid and Gid.
        self.user_id = user_id  # type: str
        # The type of the user ID. Valid values: Uid, Gid, and AllUsers.
        # 
        # *   If the parameter is set to Uid or Gid, the value of the UserId parameter is returned.
        # *   If the parameter is set to AllUsers, the value of the UserID parameter is empty.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.file_count_real is not None:
            result['FileCountReal'] = self.file_count_real
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        if self.size_real is not None:
            result['SizeReal'] = self.size_real
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('FileCountReal') is not None:
            self.file_count_real = m.get('FileCountReal')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        if m.get('SizeReal') is not None:
            self.size_real = m.get('SizeReal')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeDirQuotasResponseBodyDirQuotaInfos(TeaModel):
    def __init__(self, dir_inode=None, path=None, status=None, user_quota_infos=None):
        # The inode number of the directory.
        self.dir_inode = dir_inode  # type: str
        # The absolute path of a directory.
        self.path = path  # type: str
        # The status of the quota created for the directory. Valid values: Initializing and Normal. The Initializing state indicates that the quota is being created. The Normal state indicates that the quota is created.
        self.status = status  # type: str
        # The information about quotas for all users.
        self.user_quota_infos = user_quota_infos  # type: list[DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos]

    def validate(self):
        if self.user_quota_infos:
            for k in self.user_quota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDirQuotasResponseBodyDirQuotaInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dir_inode is not None:
            result['DirInode'] = self.dir_inode
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        result['UserQuotaInfos'] = []
        if self.user_quota_infos is not None:
            for k in self.user_quota_infos:
                result['UserQuotaInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirInode') is not None:
            self.dir_inode = m.get('DirInode')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.user_quota_infos = []
        if m.get('UserQuotaInfos') is not None:
            for k in m.get('UserQuotaInfos'):
                temp_model = DescribeDirQuotasResponseBodyDirQuotaInfosUserQuotaInfos()
                self.user_quota_infos.append(temp_model.from_map(k))
        return self


class DescribeDirQuotasResponseBody(TeaModel):
    def __init__(self, dir_quota_infos=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The queried directory quotas.
        self.dir_quota_infos = dir_quota_infos  # type: list[DescribeDirQuotasResponseBodyDirQuotaInfos]
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of directories.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dir_quota_infos:
            for k in self.dir_quota_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDirQuotasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DirQuotaInfos'] = []
        if self.dir_quota_infos is not None:
            for k in self.dir_quota_infos:
                result['DirQuotaInfos'].append(k.to_map() if k else None)
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
        self.dir_quota_infos = []
        if m.get('DirQuotaInfos') is not None:
            for k in m.get('DirQuotaInfos'):
                temp_model = DescribeDirQuotasResponseBodyDirQuotaInfos()
                self.dir_quota_infos.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDirQuotasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDirQuotasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDirQuotasResponse, self).to_map()
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
            temp_model = DescribeDirQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileSystemStatisticsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic(TeaModel):
    def __init__(self, expired_count=None, expiring_count=None, file_system_type=None, metered_size=None,
                 total_count=None):
        # The number of expired file systems.
        self.expired_count = expired_count  # type: int
        # The number of expiring file systems.
        # 
        # File systems whose expiration time is less than or equal to seven days away from the current time are counted.
        self.expiring_count = expiring_count  # type: int
        # The type of the file system.
        self.file_system_type = file_system_type  # type: str
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour.
        # 
        # Unit: bytes.
        self.metered_size = metered_size  # type: long
        # The number of file systems of the current type.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        if self.expiring_count is not None:
            result['ExpiringCount'] = self.expiring_count
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        if m.get('ExpiringCount') is not None:
            self.expiring_count = m.get('ExpiringCount')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemStatistics(TeaModel):
    def __init__(self, file_system_statistic=None):
        self.file_system_statistic = file_system_statistic  # type: list[DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic]

    def validate(self):
        if self.file_system_statistic:
            for k in self.file_system_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBodyFileSystemStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystemStatistic'] = []
        if self.file_system_statistic is not None:
            for k in self.file_system_statistic:
                result['FileSystemStatistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_system_statistic = []
        if m.get('FileSystemStatistic') is not None:
            for k in m.get('FileSystemStatistic'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemStatisticsFileSystemStatistic()
                self.file_system_statistic.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage(TeaModel):
    def __init__(self, expired_time=None, package_id=None, size=None, start_time=None):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time  # type: str
        # The ID of the storage plan.
        self.package_id = package_id  # type: str
        # The capacity of the storage plan.
        self.size = size  # type: long
        # The start time of the validity period for the storage plan.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages(TeaModel):
    def __init__(self, package=None):
        self.package = package  # type: list[DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage]

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem(TeaModel):
    def __init__(self, capacity=None, charge_type=None, create_time=None, description=None, expired_time=None,
                 file_system_id=None, file_system_type=None, metered_iasize=None, metered_size=None, packages=None,
                 protocol_type=None, region_id=None, status=None, storage_type=None, zone_id=None):
        # The capacity of the file system.
        # 
        # Unit: GiB.
        self.capacity = capacity  # type: long
        # The billing method.
        # 
        # Valid values:
        # 
        # *   Subscription: The subscription billing method is used.
        # *   PayAsYouGo: The pay-as-you-go billing method is used.
        # *   Package: A storage plan is attached to the file system.
        self.charge_type = charge_type  # type: str
        # The time when the NAS file system was created.
        self.create_time = create_time  # type: str
        # The description of the file system.
        self.description = description  # type: str
        # The time when the file system expires.
        self.expired_time = expired_time  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: CPFS file system
        self.file_system_type = file_system_type  # type: str
        # The storage usage of the Infrequent Access (IA) storage medium.
        # 
        # Unit: bytes.
        self.metered_iasize = metered_iasize  # type: long
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour. Unit: bytes.
        self.metered_size = metered_size  # type: long
        # The information about storage plans.
        self.packages = packages  # type: DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages
        # The protocol type of the file system.
        # 
        # Valid values:
        # 
        # *   NFS: Network File System (NFS)
        # *   SMB: Server Message Block (SMB)
        # *   cpfs: the protocol type supported by the CPFS file system
        self.protocol_type = protocol_type  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The status of the file system.
        # 
        # This parameter is returned for Extreme NAS file systems and Cloud Parallel File Storage (CPFS) file systems. Valid values:
        # 
        # *   Pending: The file system is being created or modified.
        # *   Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state.
        # *   Stopped: The file system is unavailable.
        # *   Extending: The file system is being scaled out.
        # *   Stopping: The file system is being disabled.
        # *   Deleting: The file system is being deleted.
        self.status = status  # type: str
        # The storage type.
        # 
        # Valid values:
        # 
        # *   Valid values for General-purpose NAS file systems: Capacity and Performance.
        # *   Valid values for Extreme NAS file systems: standard and advance.
        # *   Valid values for CPFS file systems: advance\_100 (100 MB/s/TiB baseline) and advance\_200 (200 MB/s/TiB baseline).
        self.storage_type = storage_type  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('Packages') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFileSystemStatisticsResponseBodyFileSystems(TeaModel):
    def __init__(self, file_system=None):
        self.file_system = file_system  # type: list[DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem]

    def validate(self):
        if self.file_system:
            for k in self.file_system:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBodyFileSystems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystem'] = []
        if self.file_system is not None:
            for k in self.file_system:
                result['FileSystem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k in m.get('FileSystem'):
                temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k))
        return self


class DescribeFileSystemStatisticsResponseBody(TeaModel):
    def __init__(self, file_system_statistics=None, file_systems=None, page_number=None, page_size=None,
                 request_id=None, total_count=None):
        # The statistics of file systems.
        self.file_system_statistics = file_system_statistics  # type: DescribeFileSystemStatisticsResponseBodyFileSystemStatistics
        # The queried file systems.
        self.file_systems = file_systems  # type: DescribeFileSystemStatisticsResponseBodyFileSystems
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of file system entries.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.file_system_statistics:
            self.file_system_statistics.validate()
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_statistics is not None:
            result['FileSystemStatistics'] = self.file_system_statistics.to_map()
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()
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
        if m.get('FileSystemStatistics') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystemStatistics()
            self.file_system_statistics = temp_model.from_map(m['FileSystemStatistics'])
        if m.get('FileSystems') is not None:
            temp_model = DescribeFileSystemStatisticsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m['FileSystems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFileSystemStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFileSystemStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFileSystemStatisticsResponse, self).to_map()
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
            temp_model = DescribeFileSystemStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileSystemsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the resource.
        # 
        # Limits:
        # 
        # *   Valid values of N: 1 to 20.
        # *   The tag key must be 1 to 128 characters in length.
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of tag N to add to the resource.
        # 
        # Limits:
        # 
        # *   Valid values of N: 1 to 20.
        # *   The tag value must be 1 to 128 characters in length.
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsRequestTag, self).to_map()
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


class DescribeFileSystemsRequest(TeaModel):
    def __init__(self, file_system_id=None, file_system_type=None, page_number=None, page_size=None, tag=None,
                 vpc_id=None):
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\*\*\*\*.
        # *   The IDs of Extreme NAS file systems must start with extreme-, for example, extreme-0015\*\*\*\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with cpfs-, for example, cpfs-125487\*\*\*\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   all (default): all types
        # *   standard: General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: CPFS file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The details about the tags.
        self.tag = tag  # type: list[DescribeFileSystemsRequestTag]
        # The ID of the virtual private cloud (VPC).
        # 
        # If you want to mount the file system on an Elastic Compute Service (ECS) instance, the file system and the ECS instance must reside in the same VPC.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFileSystemsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap(TeaModel):
    def __init__(self, bind_dn=None, search_base=None, uri=None):
        # An LDAP entry.
        self.bind_dn = bind_dn  # type: str
        # An LDAP search base.
        self.search_base = search_base  # type: str
        # An LDAP URI.
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode(TeaModel):
    def __init__(self, default_passwd=None, ecs_id=None, ecs_ip=None):
        # The default logon password of the ECS instance on the client management node.
        self.default_passwd = default_passwd  # type: str
        # The ID of the ECS instance on the client management node.
        self.ecs_id = ecs_id  # type: str
        # The IP address of the ECS instance on the client management node.
        self.ecs_ip = ecs_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes(TeaModel):
    def __init__(self, client_master_node=None):
        self.client_master_node = client_master_node  # type: list[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode]

    def validate(self):
        if self.client_master_node:
            for k in self.client_master_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k in self.client_master_node:
                result['ClientMasterNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k in m.get('ClientMasterNode'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag, self).to_map()
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


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags, self).to_map()
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
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget(TeaModel):
    def __init__(self, access_group_name=None, client_master_nodes=None, dual_stack_mount_target_domain=None,
                 mount_target_domain=None, network_type=None, status=None, tags=None, vpc_id=None, vsw_id=None):
        # The name of the permission group that is attached to the mount target.
        self.access_group_name = access_group_name  # type: str
        # The information about client management nodes.
        # 
        # This parameter is available only for CPFS file systems.
        self.client_master_nodes = client_master_nodes  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain  # type: str
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str
        # The network type. Valid value: vpc.
        self.network_type = network_type  # type: str
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # *   Pending: The mount target is being created or modified.
        # *   Deleting: The mount target is being deleted.
        # *   Hibernating: The mount target is being hibernated.
        # *   Hibernated: The mount target is hibernated.
        self.status = status  # type: str
        # The tags that are attached to the mount target.
        self.tags = tags  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch.
        self.vsw_id = vsw_id  # type: str

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('ClientMasterNodes') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m['ClientMasterNodes'])
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTargetTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets(TeaModel):
    def __init__(self, mount_target=None):
        self.mount_target = mount_target  # type: list[DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget]

    def validate(self):
        if self.mount_target:
            for k in self.mount_target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k in self.mount_target:
                result['MountTarget'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k in m.get('MountTarget'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage(TeaModel):
    def __init__(self, expired_time=None, package_id=None, package_type=None, size=None, start_time=None):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time  # type: str
        # The ID of the storage plan.
        self.package_id = package_id  # type: str
        # The type of the storage plan.
        # 
        # Valid values:
        # 
        # *   ssd: the storage plan for Performance NAS file systems
        # *   hybrid: the storage plan for Capacity NAS file systems
        self.package_type = package_type  # type: str
        # The capacity of the storage plan. Unit: bytes.
        self.size = size  # type: long
        # The start time of the validity period for the storage plan.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages(TeaModel):
    def __init__(self, package=None):
        self.package = package  # type: list[DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage]

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures(TeaModel):
    def __init__(self, supported_feature=None):
        self.supported_feature = supported_feature  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_feature is not None:
            result['SupportedFeature'] = self.supported_feature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportedFeature') is not None:
            self.supported_feature = m.get('SupportedFeature')
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag, self).to_map()
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


class DescribeFileSystemsResponseBodyFileSystemsFileSystemTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystemTags, self).to_map()
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
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBodyFileSystemsFileSystem(TeaModel):
    def __init__(self, access_point_count=None, bandwidth=None, capacity=None, charge_type=None, create_time=None,
                 description=None, encrypt_type=None, expired_time=None, file_system_id=None, file_system_type=None,
                 kmskey_id=None, ldap=None, metered_iasize=None, metered_size=None, mount_targets=None, packages=None,
                 protocol_type=None, region_id=None, status=None, storage_type=None, supported_features=None, tags=None,
                 version=None, zone_id=None):
        self.access_point_count = access_point_count  # type: str
        # The bandwidth of the file system.
        # 
        # Unit: MB/s. This parameter is unavailable for General-purpose NAS file systems.
        self.bandwidth = bandwidth  # type: long
        # The capacity of the file system.
        # 
        # Unit: GiB.
        self.capacity = capacity  # type: long
        # The billing method.
        # 
        # Valid values:
        # 
        # *   Subscription: The subscription billing method is used.
        # *   PayAsYouGo: The pay-as-you-go billing method is used.
        # *   Package: A storage plan is attached to the file system.
        self.charge_type = charge_type  # type: str
        # The time when the file system was created.
        self.create_time = create_time  # type: str
        # The description of the file system.
        self.description = description  # type: str
        # The encryption type.
        # 
        # Valid values:
        # 
        # *   0: The data in the file system is not encrypted.
        # *   1: A NAS-managed key is used to encrypt the data in the file system.
        # *   2: A KMS-managed key is used to encrypt the data in the file system.
        self.encrypt_type = encrypt_type  # type: int
        # The time when the file system expires.
        self.expired_time = expired_time  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: CPFS file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type  # type: str
        # The ID of the key that is managed by Key Management Service (KMS).
        self.kmskey_id = kmskey_id  # type: str
        # The Lightweight Directory Access Protocol (LDAP) configurations.
        # 
        # This parameter is available only for CPFS file systems.
        self.ldap = ldap  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap
        # The storage usage of the Infrequent Access (IA) storage medium.
        # 
        # Unit: bytes.
        self.metered_iasize = metered_iasize  # type: long
        # The storage usage of the file system.
        # 
        # The value of this parameter is the maximum storage usage of the file system over the last hour. Unit: bytes.
        self.metered_size = metered_size  # type: long
        # The information about mount targets.
        self.mount_targets = mount_targets  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets
        # The information about storage plans.
        self.packages = packages  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages
        # The protocol type of the file system.
        # 
        # Valid values:
        # 
        # *   NFS: Network File System (NFS)
        # *   SMB: Server Message Block (SMB)
        # *   cpfs: the protocol type supported by the CPFS file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.protocol_type = protocol_type  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The status of the file system. Valid values:
        # 
        # *   Pending: The file system is being created or modified.
        # *   Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state.
        # *   Stopped: The file system is unavailable.
        # *   Extending: The file system is being scaled up.
        # *   Stopping: The file system is being stopped.
        # *   Deleting: The file system is being deleted.
        self.status = status  # type: str
        # The storage type.
        # 
        # Valid values:
        # 
        # *   Valid values for General-purpose NAS file systems: Capacity and Performance.
        # *   Valid values for Extreme NAS file systems: standard and advance.
        # *   Valid values for CPFS file systems: advance\_100 (100 MB/s/TiB baseline) and advance\_200 (200 MB/s/TiB baseline).
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.storage_type = storage_type  # type: str
        # The features that are supported by the file system.
        self.supported_features = supported_features  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures
        # The tags that are attached to the file system.
        self.tags = tags  # type: DescribeFileSystemsResponseBodyFileSystemsFileSystemTags
        # The version number of the file system.
        # 
        # This parameter is available only for Extreme NAS file systems.
        self.version = version  # type: str
        # The ID of the zone where the file system resides.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.ldap:
            self.ldap.validate()
        if self.mount_targets:
            self.mount_targets.validate()
        if self.packages:
            self.packages.validate()
        if self.supported_features:
            self.supported_features.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystemsFileSystem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_point_count is not None:
            result['AccessPointCount'] = self.access_point_count
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.ldap is not None:
            result['Ldap'] = self.ldap.to_map()
        if self.metered_iasize is not None:
            result['MeteredIASize'] = self.metered_iasize
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.supported_features is not None:
            result['SupportedFeatures'] = self.supported_features.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPointCount') is not None:
            self.access_point_count = m.get('AccessPointCount')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('Ldap') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemLdap()
            self.ldap = temp_model.from_map(m['Ldap'])
        if m.get('MeteredIASize') is not None:
            self.metered_iasize = m.get('MeteredIASize')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('MountTargets') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemMountTargets()
            self.mount_targets = temp_model.from_map(m['MountTargets'])
        if m.get('Packages') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportedFeatures') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemSupportedFeatures()
            self.supported_features = temp_model.from_map(m['SupportedFeatures'])
        if m.get('Tags') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystemTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(self, file_system=None):
        self.file_system = file_system  # type: list[DescribeFileSystemsResponseBodyFileSystemsFileSystem]

    def validate(self):
        if self.file_system:
            for k in self.file_system:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBodyFileSystems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystem'] = []
        if self.file_system is not None:
            for k in self.file_system:
                result['FileSystem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_system = []
        if m.get('FileSystem') is not None:
            for k in m.get('FileSystem'):
                temp_model = DescribeFileSystemsResponseBodyFileSystemsFileSystem()
                self.file_system.append(temp_model.from_map(k))
        return self


class DescribeFileSystemsResponseBody(TeaModel):
    def __init__(self, file_systems=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The queried file systems.
        self.file_systems = file_systems  # type: DescribeFileSystemsResponseBodyFileSystems
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of file systems.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.file_systems:
            self.file_systems.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_systems is not None:
            result['FileSystems'] = self.file_systems.to_map()
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
        if m.get('FileSystems') is not None:
            temp_model = DescribeFileSystemsResponseBodyFileSystems()
            self.file_systems = temp_model.from_map(m['FileSystems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFileSystemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFileSystemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFileSystemsResponse, self).to_map()
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
            temp_model = DescribeFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFilesetsRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The filter name. Valid values:
        # 
        # *   FsetIds: filters filesets by fileset ID.
        # *   FileSystemPath: filters filesets based on the path of a fileset in a CPFS file system.
        # *   Description: filters filesets based on the fileset description.
        self.key = key  # type: str
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to FsetIds, set Value to a fileset ID or a part of the fileset ID. You can specify a fileset ID or a group of fileset IDs. You can specify a maximum of 10 fileset IDs. Example: `fset-12345678` or `fset-12345678,fset-12345679`.
        # *   If Key is set to FileSystemPath, set Value to the path or a part of the path of a fileset in a CPFS file system. The value must be 2 to 1,024 characters in length. The value must be encoded in UTF-8.
        # *   If Key is set to Description, set Value to a fileset description or a part of the fileset description.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFilesetsRequestFilters, self).to_map()
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


class DescribeFilesetsRequest(TeaModel):
    def __init__(self, file_system_id=None, filters=None, max_results=None, next_token=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The filter that is used to query filesets.
        self.filters = filters  # type: list[DescribeFilesetsRequestFilters]
        # The number of results for each query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFilesetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeFilesetsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeFilesetsResponseBodyEntriesEntrie(TeaModel):
    def __init__(self, create_time=None, description=None, file_system_path=None, fset_id=None, status=None,
                 update_time=None):
        # The time when the fileset was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time  # type: str
        # The fileset description.
        self.description = description  # type: str
        # The fileset path.
        self.file_system_path = file_system_path  # type: str
        # The fileset ID.
        self.fset_id = fset_id  # type: str
        # The fileset status. Valid values:
        # 
        # *   CREATING: The fileset is being created.
        # *   CREATED: The fileset has been created and is running properly.
        # *   RELEASING: The fileset is being released.
        # *   RELEASED: The fileset has been deleted.
        self.status = status  # type: str
        # The time when the fileset was last updated.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFilesetsResponseBodyEntriesEntrie, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeFilesetsResponseBodyEntries(TeaModel):
    def __init__(self, entrie=None):
        self.entrie = entrie  # type: list[DescribeFilesetsResponseBodyEntriesEntrie]

    def validate(self):
        if self.entrie:
            for k in self.entrie:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFilesetsResponseBodyEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entrie'] = []
        if self.entrie is not None:
            for k in self.entrie:
                result['Entrie'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entrie = []
        if m.get('Entrie') is not None:
            for k in m.get('Entrie'):
                temp_model = DescribeFilesetsResponseBodyEntriesEntrie()
                self.entrie.append(temp_model.from_map(k))
        return self


class DescribeFilesetsResponseBody(TeaModel):
    def __init__(self, entries=None, file_system_id=None, next_token=None, request_id=None):
        # The fileset information.
        self.entries = entries  # type: DescribeFilesetsResponseBodyEntries
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.entries:
            self.entries.validate()

    def to_map(self):
        _map = super(DescribeFilesetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entries is not None:
            result['Entries'] = self.entries.to_map()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entries') is not None:
            temp_model = DescribeFilesetsResponseBodyEntries()
            self.entries = temp_model.from_map(m['Entries'])
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFilesetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFilesetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFilesetsResponse, self).to_map()
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
            temp_model = DescribeFilesetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLifecyclePoliciesRequest(TeaModel):
    def __init__(self, file_system_id=None, lifecycle_policy_name=None, page_number=None, page_size=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The name of the lifecycle policy. The name must meet the following conventions:
        # 
        # The name must be 3 to 64 characters in length and must start with a letter. It can contain letters, digits, underscores (\_), and hyphens (-).
        self.lifecycle_policy_name = lifecycle_policy_name  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLifecyclePoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeLifecyclePoliciesResponseBodyLifecyclePolicies(TeaModel):
    def __init__(self, create_time=None, file_system_id=None, lifecycle_policy_name=None, lifecycle_rule_name=None,
                 path=None, paths=None, storage_type=None):
        # The time when the lifecycle policy was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The name of the lifecycle policy.
        self.lifecycle_policy_name = lifecycle_policy_name  # type: str
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME\_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name  # type: str
        # The absolute path of a directory with which the lifecycle policy is associated.
        self.path = path  # type: str
        self.paths = paths  # type: list[str]
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLifecyclePoliciesResponseBodyLifecyclePolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.path is not None:
            result['Path'] = self.path
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeLifecyclePoliciesResponseBody(TeaModel):
    def __init__(self, lifecycle_policies=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The queried lifecycle policies.
        self.lifecycle_policies = lifecycle_policies  # type: list[DescribeLifecyclePoliciesResponseBodyLifecyclePolicies]
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of lifecycle policies.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.lifecycle_policies:
            for k in self.lifecycle_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLifecyclePoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LifecyclePolicies'] = []
        if self.lifecycle_policies is not None:
            for k in self.lifecycle_policies:
                result['LifecyclePolicies'].append(k.to_map() if k else None)
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
        self.lifecycle_policies = []
        if m.get('LifecyclePolicies') is not None:
            for k in m.get('LifecyclePolicies'):
                temp_model = DescribeLifecyclePoliciesResponseBodyLifecyclePolicies()
                self.lifecycle_policies.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLifecyclePoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLifecyclePoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLifecyclePoliciesResponse, self).to_map()
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
            temp_model = DescribeLifecyclePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogAnalysisRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None):
        # The page number. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size  # type: int
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogAnalysisRequest, self).to_map()
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


class DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue(TeaModel):
    def __init__(self, logstore=None, project=None, region=None, role_arn=None):
        # The name of the dedicated Logstore that is used to store NAS operation logs.
        self.logstore = logstore  # type: str
        # The name of the project where the dedicated Logstore resides.
        self.project = project  # type: str
        # The region where the dedicated Logstore resides.
        self.region = region  # type: str
        # The role that is used by NAS to access Simple Log Service.
        self.role_arn = role_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class DescribeLogAnalysisResponseBodyAnalysesAnalysis(TeaModel):
    def __init__(self, meta_key=None, meta_value=None):
        # The ID of the file system.
        self.meta_key = meta_key  # type: str
        # The log dump information of the file system.
        self.meta_value = meta_value  # type: DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue

    def validate(self):
        if self.meta_value:
            self.meta_value.validate()

    def to_map(self):
        _map = super(DescribeLogAnalysisResponseBodyAnalysesAnalysis, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_key is not None:
            result['MetaKey'] = self.meta_key
        if self.meta_value is not None:
            result['MetaValue'] = self.meta_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetaKey') is not None:
            self.meta_key = m.get('MetaKey')
        if m.get('MetaValue') is not None:
            temp_model = DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue()
            self.meta_value = temp_model.from_map(m['MetaValue'])
        return self


class DescribeLogAnalysisResponseBodyAnalyses(TeaModel):
    def __init__(self, analysis=None):
        self.analysis = analysis  # type: list[DescribeLogAnalysisResponseBodyAnalysesAnalysis]

    def validate(self):
        if self.analysis:
            for k in self.analysis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogAnalysisResponseBodyAnalyses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Analysis'] = []
        if self.analysis is not None:
            for k in self.analysis:
                result['Analysis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.analysis = []
        if m.get('Analysis') is not None:
            for k in m.get('Analysis'):
                temp_model = DescribeLogAnalysisResponseBodyAnalysesAnalysis()
                self.analysis.append(temp_model.from_map(k))
        return self


class DescribeLogAnalysisResponseBody(TeaModel):
    def __init__(self, analyses=None, code=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The collection of log dump information.
        self.analyses = analyses  # type: DescribeLogAnalysisResponseBodyAnalyses
        # The HTTP status code.
        self.code = code  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of log dump entries returned per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of log dump entries in the region.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.analyses:
            self.analyses.validate()

    def to_map(self):
        _map = super(DescribeLogAnalysisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyses is not None:
            result['Analyses'] = self.analyses.to_map()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Analyses') is not None:
            temp_model = DescribeLogAnalysisResponseBodyAnalyses()
            self.analyses = temp_model.from_map(m['Analyses'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeLogAnalysisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogAnalysisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogAnalysisResponse, self).to_map()
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
            temp_model = DescribeLogAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMountTargetsRequest(TeaModel):
    def __init__(self, dual_stack_mount_target_domain=None, file_system_id=None, mount_target_domain=None,
                 page_number=None, page_size=None):
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # > Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain  # type: str
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: 31a8e4\*\*\*\*.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\*\*\*\*.
        # *   The IDs of Cloud Parallel File Storage (CPFS) file systems must start with `cpfs-`, for example, cpfs-125487\*\*\*\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMountTargetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode(TeaModel):
    def __init__(self, default_passwd=None, ecs_id=None, ecs_ip=None):
        # The default logon password of the ECS instance.
        self.default_passwd = default_passwd  # type: str
        # The ID of the ECS instance on the client management node.
        self.ecs_id = ecs_id  # type: str
        # The IP address of the ECS instance on the client management node.
        self.ecs_ip = ecs_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes(TeaModel):
    def __init__(self, client_master_node=None):
        self.client_master_node = client_master_node  # type: list[DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode]

    def validate(self):
        if self.client_master_node:
            for k in self.client_master_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k in self.client_master_node:
                result['ClientMasterNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k in m.get('ClientMasterNode'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBodyMountTargetsMountTarget(TeaModel):
    def __init__(self, access_group=None, client_master_nodes=None, dual_stack_mount_target_domain=None,
                 ipversion=None, mount_target_domain=None, network_type=None, status=None, vpc_id=None, vsw_id=None):
        # The name of the permission group that is attached to the mount target.
        self.access_group = access_group  # type: str
        # The information about client management nodes.
        self.client_master_nodes = client_master_nodes  # type: DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain  # type: str
        # The type of the mount target.
        # 
        # *   IPv4: an IPv4 mount target
        # *   DualStack: a dual-stack mount target
        self.ipversion = ipversion  # type: str
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str
        # The network type. Valid value: **Vpc**.
        self.network_type = network_type  # type: str
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # *   Pending: The mount target is being created or modified.
        # *   Deleting: The mount target is being deleted.
        # *   Hibernating: The mount target is being hibernated.
        # *   Hibernated: The mount target is hibernated.
        # 
        # > You can mount a file system only when the mount target of the file system is in the Active state.
        self.status = status  # type: str
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch.
        self.vsw_id = vsw_id  # type: str

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()

    def to_map(self):
        _map = super(DescribeMountTargetsResponseBodyMountTargetsMountTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.ipversion is not None:
            result['IPVersion'] = self.ipversion
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('ClientMasterNodes') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m['ClientMasterNodes'])
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('IPVersion') is not None:
            self.ipversion = m.get('IPVersion')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class DescribeMountTargetsResponseBodyMountTargets(TeaModel):
    def __init__(self, mount_target=None):
        self.mount_target = mount_target  # type: list[DescribeMountTargetsResponseBodyMountTargetsMountTarget]

    def validate(self):
        if self.mount_target:
            for k in self.mount_target:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMountTargetsResponseBodyMountTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k in self.mount_target:
                result['MountTarget'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k in m.get('MountTarget'):
                temp_model = DescribeMountTargetsResponseBodyMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k))
        return self


class DescribeMountTargetsResponseBody(TeaModel):
    def __init__(self, mount_targets=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The information about mount targets.
        self.mount_targets = mount_targets  # type: DescribeMountTargetsResponseBodyMountTargets
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of mount targets.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.mount_targets:
            self.mount_targets.validate()

    def to_map(self):
        _map = super(DescribeMountTargetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()
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
        if m.get('MountTargets') is not None:
            temp_model = DescribeMountTargetsResponseBodyMountTargets()
            self.mount_targets = temp_model.from_map(m['MountTargets'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMountTargetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMountTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMountTargetsResponse, self).to_map()
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
            temp_model = DescribeMountTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMountedClientsRequest(TeaModel):
    def __init__(self, client_ip=None, file_system_id=None, mount_target_domain=None, page_number=None,
                 page_size=None, region_id=None):
        # The IP address of the client.
        # 
        # *   If you specify an IP address, the operation checks whether the client list includes this IP address. If the client list includes the IP address, the operation returns the IP address. If the client list does not include the IP address, the operation returns an empty list.
        # *   If you do not specify an IP address, the operation returns the IP addresses of all clients that have accessed the specified NAS file system within the last minute.
        self.client_ip = client_ip  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of IP addresses to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMountedClientsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMountedClientsResponseBodyClientsClient(TeaModel):
    def __init__(self, client_ip=None):
        # The IP address of the client.
        self.client_ip = client_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMountedClientsResponseBodyClientsClient, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        return self


class DescribeMountedClientsResponseBodyClients(TeaModel):
    def __init__(self, client=None):
        self.client = client  # type: list[DescribeMountedClientsResponseBodyClientsClient]

    def validate(self):
        if self.client:
            for k in self.client:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMountedClientsResponseBodyClients, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Client'] = []
        if self.client is not None:
            for k in self.client:
                result['Client'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.client = []
        if m.get('Client') is not None:
            for k in m.get('Client'):
                temp_model = DescribeMountedClientsResponseBodyClientsClient()
                self.client.append(temp_model.from_map(k))
        return self


class DescribeMountedClientsResponseBody(TeaModel):
    def __init__(self, clients=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The queried clients.
        self.clients = clients  # type: DescribeMountedClientsResponseBodyClients
        # The page number.
        self.page_number = page_number  # type: int
        # The number of IP addresses returned per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of IP addresses.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.clients:
            self.clients.validate()

    def to_map(self):
        _map = super(DescribeMountedClientsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clients is not None:
            result['Clients'] = self.clients.to_map()
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
        if m.get('Clients') is not None:
            temp_model = DescribeMountedClientsResponseBodyClients()
            self.clients = temp_model.from_map(m['Clients'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMountedClientsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMountedClientsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMountedClientsResponse, self).to_map()
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
            temp_model = DescribeMountedClientsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNfsAclRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNfsAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeNfsAclResponseBodyAcl(TeaModel):
    def __init__(self, enabled=None):
        # Indicates whether the NFS ACL feature is enabled.
        # 
        # *   true: The NFS ACL feature is enabled.
        # *   false: The NFS ACL feature is disabled.
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNfsAclResponseBodyAcl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeNfsAclResponseBody(TeaModel):
    def __init__(self, acl=None, request_id=None):
        # The information about the ACL feature.
        self.acl = acl  # type: DescribeNfsAclResponseBodyAcl
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super(DescribeNfsAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = DescribeNfsAclResponseBodyAcl()
            self.acl = temp_model.from_map(m['Acl'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNfsAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNfsAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNfsAclResponse, self).to_map()
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
            temp_model = DescribeNfsAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtocolMountTargetRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The filter name.
        # 
        # *   ProtocolServiceIds: filters export directories by protocol service ID.
        # *   ExportIds: filters export directories by export directory ID.
        # *   VpcIds: filters export directories by virtual private cloud (VPC) ID.
        # *   VSwitchIds: filters export directories by vSwitch ID.
        # *   FsetIds: filters export directories by fileset ID.
        # *   Paths: filters export directories based on the path of the file system corresponding to the mount target.
        # *   AccessGroupNames: filters export directories by permission group name.
        self.key = key  # type: str
        # The filter value. This parameter does not support wildcards.
        # 
        # *   If Key is set to ProtocolServiceIds, set Value to a protocol service ID. You can specify a maximum of 10 protocol service IDs. Example: `ptc-12345678` or `ptc-12345678,ptc-12345679`.
        # *   If Key is set to ExportIds, set Value to an export directory ID. You can specify a maximum of 10 export directory IDs. For example, `exp-12345678` or `exp-12345678,exp-12345679`.
        # *   If Key is set to VpcIds, set Value to a VPC ID of the protocol service. You can specify a maximum of 10 VPC IDs. Example: `vpc-12345678` or `vpc-12345678,vpc-12345679`.
        # *   If Key is set to FsetIds, set Value to a fileset ID. You can specify a maximum of 10 fileset IDs. Example, `fset-12345678` or `fset-12345678,fset-12345679`.
        # *   If Key is set to Paths, set Value to a path of the file system corresponding to the mount target. You can specify a maximum of 10 paths. Example: `/cpfs/mnt_1/` or `/cpfs/mnt_1/,/cpfs/mnt_2/`.
        # *   If Key is set to AccessGroupNames, set Value to a permission group name for the protocol service. You can specify a maximum of 10 permission group names. Example: `ag-12345678` or `ag-12345678,ag-12345679`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtocolMountTargetRequestFilters, self).to_map()
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


class DescribeProtocolMountTargetRequest(TeaModel):
    def __init__(self, client_token=None, file_system_id=None, filters=None, max_results=None, next_token=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The filter that is used to query the export directories of the protocol service.
        self.filters = filters  # type: list[DescribeProtocolMountTargetRequestFilters]
        # The number of results for each query.
        # 
        # *   Value values: 10 to 100.
        # *   Default value: 20.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProtocolMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = DescribeProtocolMountTargetRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeProtocolMountTargetResponseBodyProtocolMountTargets(TeaModel):
    def __init__(self, access_group_name=None, create_time=None, description=None, export_id=None, fset_id=None,
                 path=None, protocol_mount_target_domain=None, protocol_service_id=None, protocol_type=None,
                 status=None, v_switch_id=None, vpc_id=None):
        # The permission group that is associated with the export directory of the protocol service.
        self.access_group_name = access_group_name  # type: str
        # The time when the export directory of the protocol service was created.
        self.create_time = create_time  # type: str
        # The description of the export directory for the protocol service.
        self.description = description  # type: str
        # The ID of the export directory for the protocol service.
        self.export_id = export_id  # type: str
        # The fileset ID of the export directory for the protocol service.
        self.fset_id = fset_id  # type: str
        # The export directory of the protocol service.
        self.path = path  # type: str
        # The domain name of the export directory for the protocol service.
        self.protocol_mount_target_domain = protocol_mount_target_domain  # type: str
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str
        # The protocol type supported by the protocol service.
        self.protocol_type = protocol_type  # type: str
        # The status of the mount target.
        self.status = status  # type: str
        # The vSwitch ID of the export directory for the protocol service.
        self.v_switch_id = v_switch_id  # type: str
        # The VPC ID of the export directory for the protocol service.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtocolMountTargetResponseBodyProtocolMountTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        if self.path is not None:
            result['Path'] = self.path
        if self.protocol_mount_target_domain is not None:
            result['ProtocolMountTargetDomain'] = self.protocol_mount_target_domain
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProtocolMountTargetDomain') is not None:
            self.protocol_mount_target_domain = m.get('ProtocolMountTargetDomain')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeProtocolMountTargetResponseBody(TeaModel):
    def __init__(self, next_token=None, protocol_mount_targets=None, request_id=None):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The export directories of the protocol service.
        self.protocol_mount_targets = protocol_mount_targets  # type: list[DescribeProtocolMountTargetResponseBodyProtocolMountTargets]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.protocol_mount_targets:
            for k in self.protocol_mount_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProtocolMountTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ProtocolMountTargets'] = []
        if self.protocol_mount_targets is not None:
            for k in self.protocol_mount_targets:
                result['ProtocolMountTargets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.protocol_mount_targets = []
        if m.get('ProtocolMountTargets') is not None:
            for k in m.get('ProtocolMountTargets'):
                temp_model = DescribeProtocolMountTargetResponseBodyProtocolMountTargets()
                self.protocol_mount_targets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtocolMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeProtocolMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProtocolMountTargetResponse, self).to_map()
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
            temp_model = DescribeProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtocolServiceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, file_system_id=None, max_results=None, next_token=None,
                 protocol_service_ids=None, status=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description or a part of the description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The number of results for each query.
        # 
        # *   Maximum value: 100.
        # *   Minimum value: 10.
        # *   Default value: 20.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. If not all dataflows are returned in a query, the return value of the NextToken parameter is not empty. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The ID of the protocol service.
        # 
        # *   Format: CSV.
        # *   Limit: You can specify a maximum of 10 protocol service IDs.
        self.protocol_service_ids = protocol_service_ids  # type: str
        # The status of the protocol service.
        # 
        # Format: CSV.
        # 
        # Valid values:
        # 
        # *   Creating: The protocol service is being created.
        # *   Starting: The protocol service is being started.
        # *   Running: The protocol service is running.
        # *   Updating: The protocol service is being updated.
        # *   Deleting: The protocol service is being deleted.
        # *   Stopping: The protocol service is being stopped.
        # *   Stopped: The protocol service is stopped.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtocolServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.protocol_service_ids is not None:
            result['ProtocolServiceIds'] = self.protocol_service_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProtocolServiceIds') is not None:
            self.protocol_service_ids = m.get('ProtocolServiceIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeProtocolServiceResponseBodyProtocolServices(TeaModel):
    def __init__(self, create_time=None, description=None, file_system_id=None, instance_base_throughput=None,
                 instance_burst_throughput=None, instance_ram=None, modify_time=None, mount_target_count=None, protocol_service_id=None,
                 protocol_spec=None, protocol_throughput=None, protocol_type=None, status=None):
        # The time when the protocol service was created. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The base throughput of the protocol service. Unit: MB/s.
        self.instance_base_throughput = instance_base_throughput  # type: int
        # The burst throughput of the protocol service. Unit: MB/s.
        self.instance_burst_throughput = instance_burst_throughput  # type: int
        # The memory cache size of the protocol service. Unit: GiB.
        self.instance_ram = instance_ram  # type: int
        # The time when the protocol service was modified. The time is displayed in UTC.
        self.modify_time = modify_time  # type: str
        # The total number of CPFS directories and filesets exported in the protocol service.
        self.mount_target_count = mount_target_count  # type: int
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str
        # The specification of the protocol service.
        # 
        # *   Valid value: General.
        # *   Default value: General.
        self.protocol_spec = protocol_spec  # type: str
        # The throughput of the protocol service. Unit: MB/s.
        self.protocol_throughput = protocol_throughput  # type: int
        # The protocol type supported by the protocol service.
        # 
        # Valid values:
        # 
        # *   NFS: The protocol service supports access over the Network File System (NFS) protocol.
        self.protocol_type = protocol_type  # type: str
        # The status of the protocol service.
        # 
        # Valid values:
        # 
        # *   Creating: The protocol service is being created.
        # *   Starting: The protocol service is being started.
        # *   Running: The protocol service is running.
        # *   Updating: The protocol service is being updated.
        # *   Deleting: The protocol service is being deleted.
        # *   Stopping: The protocol service is being stopped.
        # *   Stopped: The protocol service is stopped.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtocolServiceResponseBodyProtocolServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.instance_base_throughput is not None:
            result['InstanceBaseThroughput'] = self.instance_base_throughput
        if self.instance_burst_throughput is not None:
            result['InstanceBurstThroughput'] = self.instance_burst_throughput
        if self.instance_ram is not None:
            result['InstanceRAM'] = self.instance_ram
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        if self.protocol_spec is not None:
            result['ProtocolSpec'] = self.protocol_spec
        if self.protocol_throughput is not None:
            result['ProtocolThroughput'] = self.protocol_throughput
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InstanceBaseThroughput') is not None:
            self.instance_base_throughput = m.get('InstanceBaseThroughput')
        if m.get('InstanceBurstThroughput') is not None:
            self.instance_burst_throughput = m.get('InstanceBurstThroughput')
        if m.get('InstanceRAM') is not None:
            self.instance_ram = m.get('InstanceRAM')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        if m.get('ProtocolSpec') is not None:
            self.protocol_spec = m.get('ProtocolSpec')
        if m.get('ProtocolThroughput') is not None:
            self.protocol_throughput = m.get('ProtocolThroughput')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeProtocolServiceResponseBody(TeaModel):
    def __init__(self, next_token=None, protocol_services=None, request_id=None):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The information about protocol services.
        self.protocol_services = protocol_services  # type: list[DescribeProtocolServiceResponseBodyProtocolServices]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.protocol_services:
            for k in self.protocol_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProtocolServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ProtocolServices'] = []
        if self.protocol_services is not None:
            for k in self.protocol_services:
                result['ProtocolServices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.protocol_services = []
        if m.get('ProtocolServices') is not None:
            for k in m.get('ProtocolServices'):
                temp_model = DescribeProtocolServiceResponseBodyProtocolServices()
                self.protocol_services.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProtocolServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeProtocolServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProtocolServiceResponse, self).to_map()
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
            temp_model = DescribeProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, file_system_type=None, page_number=None, page_size=None):
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   all: all types of file systems
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The region name.
        self.local_name = local_name  # type: str
        # The endpoint for the region.
        self.region_endpoint = region_endpoint  # type: str
        # The region ID.
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
    def __init__(self, page_number=None, page_size=None, regions=None, request_id=None, total_count=None):
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The queried regions.
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
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
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class DescribeSmbAclRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSmbAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeSmbAclResponseBodyAcl(TeaModel):
    def __init__(self, enable_anonymous_access=None, enabled=None, encrypt_data=None, home_dir_path=None,
                 reject_unencrypted_access=None, super_admin_sid=None):
        # Indicates whether the file system allows anonymous access. Valid values:
        # 
        # *   true: The file system allows anonymous access.
        # *   false: The file system does not allow anonymous access.
        self.enable_anonymous_access = enable_anonymous_access  # type: bool
        # Indicates whether the ACL feature is enabled. Valid values:
        # 
        # *   true: The ACL feature is enabled.
        # *   false: The ACL feature is disabled.
        self.enabled = enabled  # type: bool
        # Indicates whether encryption in transit is enabled. Valid values:
        # 
        # *   true: Encryption in transit is enabled.
        # *   false: Encryption in transit is disabled.
        self.encrypt_data = encrypt_data  # type: bool
        # The home directory of each user.
        self.home_dir_path = home_dir_path  # type: str
        # Indicates whether the file system denies access from non-encrypted clients. Valid values:
        # 
        # *   true: The file system denies access from non-encrypted clients.
        # *   false: The file system allows access from non-encrypted clients.
        self.reject_unencrypted_access = reject_unencrypted_access  # type: bool
        # The ID of a super admin.
        self.super_admin_sid = super_admin_sid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSmbAclResponseBodyAcl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_anonymous_access is not None:
            result['EnableAnonymousAccess'] = self.enable_anonymous_access
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.encrypt_data is not None:
            result['EncryptData'] = self.encrypt_data
        if self.home_dir_path is not None:
            result['HomeDirPath'] = self.home_dir_path
        if self.reject_unencrypted_access is not None:
            result['RejectUnencryptedAccess'] = self.reject_unencrypted_access
        if self.super_admin_sid is not None:
            result['SuperAdminSid'] = self.super_admin_sid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableAnonymousAccess') is not None:
            self.enable_anonymous_access = m.get('EnableAnonymousAccess')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EncryptData') is not None:
            self.encrypt_data = m.get('EncryptData')
        if m.get('HomeDirPath') is not None:
            self.home_dir_path = m.get('HomeDirPath')
        if m.get('RejectUnencryptedAccess') is not None:
            self.reject_unencrypted_access = m.get('RejectUnencryptedAccess')
        if m.get('SuperAdminSid') is not None:
            self.super_admin_sid = m.get('SuperAdminSid')
        return self


class DescribeSmbAclResponseBody(TeaModel):
    def __init__(self, acl=None, request_id=None):
        # The information about the ACL feature.
        self.acl = acl  # type: DescribeSmbAclResponseBodyAcl
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super(DescribeSmbAclResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['Acl'] = self.acl.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acl') is not None:
            temp_model = DescribeSmbAclResponseBodyAcl()
            self.acl = temp_model.from_map(m['Acl'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSmbAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSmbAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSmbAclResponse, self).to_map()
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
            temp_model = DescribeSmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(self, file_system_id=None, file_system_type=None, page_number=None, page_size=None,
                 snapshot_ids=None, snapshot_name=None, snapshot_type=None, status=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The type of the file system.
        # 
        # Valid value: extreme, which indicates Extreme NAS file systems.
        self.file_system_type = file_system_type  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The snapshot IDs.
        # 
        # You can specify a maximum of 100 snapshot IDs. You must separate snapshot IDs with commas (,).
        self.snapshot_ids = snapshot_ids  # type: str
        # The snapshot name.
        self.snapshot_name = snapshot_name  # type: str
        # The type of the snapshot.
        # 
        # Valid values:
        # 
        # *   auto: auto snapshot
        # *   user: manual snapshot
        # *   all (default): all snapshot types
        self.snapshot_type = snapshot_type  # type: str
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        # *   all (default): all snapshot states.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnapshotsResponseBodySnapshotsSnapshot(TeaModel):
    def __init__(self, create_time=None, description=None, encrypt_type=None, progress=None, remain_time=None,
                 retention_days=None, snapshot_id=None, snapshot_name=None, source_file_system_id=None,
                 source_file_system_size=None, source_file_system_version=None, status=None):
        # The time when the snapshot was created.
        # 
        # The time follows the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in UTC. The time is displayed in the `yyyy-MM-ddThh:mmZ` format.
        self.create_time = create_time  # type: str
        # The description of the snapshot.
        self.description = description  # type: str
        # Indicates whether the snapshot is encrypted.
        # 
        # Valid values:
        # 
        # *   0: The snapshot is not encrypted.
        # *   1: The snapshot is encrypted.
        self.encrypt_type = encrypt_type  # type: int
        # The progress of the snapshot creation. The value of this parameter is expressed as a percentage.
        self.progress = progress  # type: str
        # The remaining time that is required to create the snapshot.
        # 
        # Unit: seconds.
        self.remain_time = remain_time  # type: int
        # The retention period of the auto snapshot.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \-1: Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days  # type: int
        # The snapshot ID.
        self.snapshot_id = snapshot_id  # type: str
        # The snapshot name.
        # 
        # If you specify a name to create a snapshot, the name of the snapshot is returned. Otherwise, no value is returned for this parameter.
        self.snapshot_name = snapshot_name  # type: str
        # The ID of the source file system.
        # 
        # This parameter is retained even if the source file system of the snapshot is deleted.
        self.source_file_system_id = source_file_system_id  # type: str
        # The capacity of the source file system.
        # 
        # Unit: GiB.
        self.source_file_system_size = source_file_system_size  # type: long
        # The version of the source file system.
        self.source_file_system_version = source_file_system_version  # type: str
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBodySnapshotsSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
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
        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id
        if self.source_file_system_size is not None:
            result['SourceFileSystemSize'] = self.source_file_system_size
        if self.source_file_system_version is not None:
            result['SourceFileSystemVersion'] = self.source_file_system_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
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
        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')
        if m.get('SourceFileSystemSize') is not None:
            self.source_file_system_size = m.get('SourceFileSystemSize')
        if m.get('SourceFileSystemVersion') is not None:
            self.source_file_system_version = m.get('SourceFileSystemVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[DescribeSnapshotsResponseBodySnapshotsSnapshot]

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k in self.snapshot:
                result['Snapshot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k in m.get('Snapshot'):
                temp_model = DescribeSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, snapshots=None, total_count=None):
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The details about snapshots.
        self.snapshots = snapshots  # type: DescribeSnapshotsResponseBodySnapshots
        # The total number of snapshots returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
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
        if m.get('Snapshots') is not None:
            temp_model = DescribeSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSnapshotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponse, self).to_map()
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
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoragePackagesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, use_utcdate_time=None):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of storage plans to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The region ID.
        self.region_id = region_id  # type: str
        # Specifies whether the time to return is in UTC.
        # 
        # Valid values:
        # 
        # *   true (default): returns UTC time.
        # *   false: returns UNIX timestamp.
        self.use_utcdate_time = use_utcdate_time  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStoragePackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.use_utcdate_time is not None:
            result['UseUTCDateTime'] = self.use_utcdate_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UseUTCDateTime') is not None:
            self.use_utcdate_time = m.get('UseUTCDateTime')
        return self


class DescribeStoragePackagesResponseBodyPackagesPackage(TeaModel):
    def __init__(self, expired_time=None, file_system_id=None, package_id=None, size=None, start_time=None,
                 status=None, storage_type=None):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time  # type: str
        # The ID of the file system that is bound to the storage plan.
        self.file_system_id = file_system_id  # type: str
        # The ID of the storage plan.
        self.package_id = package_id  # type: str
        # The capacity of the storage plan.
        # 
        # Unit: bytes.
        self.size = size  # type: long
        # The start time of the validity period for the storage plan.
        self.start_time = start_time  # type: str
        # The status of the storage plan.
        # 
        # Valid values:
        # 
        # *   free: The storage plan is not bound to a file system. You can bind the storage plan to a file system of the same storage type.
        # *   bound: The storage plan is bound to a file system.
        self.status = status  # type: str
        # The type of the storage plan.
        # 
        # Valid values:
        # 
        # *   Performance
        # *   Capacity
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStoragePackagesResponseBodyPackagesPackage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeStoragePackagesResponseBodyPackages(TeaModel):
    def __init__(self, package=None):
        self.package = package  # type: list[DescribeStoragePackagesResponseBodyPackagesPackage]

    def validate(self):
        if self.package:
            for k in self.package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeStoragePackagesResponseBodyPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Package'] = []
        if self.package is not None:
            for k in self.package:
                result['Package'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k in m.get('Package'):
                temp_model = DescribeStoragePackagesResponseBodyPackagesPackage()
                self.package.append(temp_model.from_map(k))
        return self


class DescribeStoragePackagesResponseBody(TeaModel):
    def __init__(self, packages=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The list of storage plans.
        self.packages = packages  # type: DescribeStoragePackagesResponseBodyPackages
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of storage plans returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of storage plans.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        _map = super(DescribeStoragePackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()
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
        if m.get('Packages') is not None:
            temp_model = DescribeStoragePackagesResponseBodyPackages()
            self.packages = temp_model.from_map(m['Packages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeStoragePackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeStoragePackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStoragePackagesResponse, self).to_map()
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
            temp_model = DescribeStoragePackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, file_system_type=None, region_id=None):
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        # *   cpfs: Cloud Parallel File Storage (CPFS) file system
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_type = file_system_type  # type: str
        # The ID of the region where you want to query zones.
        # 
        # You can call the DescribeRegions operation to query the latest region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZonesZoneCapacity(TeaModel):
    def __init__(self, protocol=None):
        self.protocol = protocol  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesZoneCapacity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType(TeaModel):
    def __init__(self, protocol_type=None, storage_type=None):
        # The protocol type.
        # 
        # *   If the FileSystemType parameter is set to standard, the protocol type is nfs or smb.
        # *   If the FileSystemType parameter is set to extreme, the protocol type is nfs.
        # *   If the FileSystemType parameter is set to cpfs, the protocol type is cpfs.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.protocol_type = protocol_type  # type: str
        # The storage type.
        # 
        # *   If the FileSystemType parameter is set to standard, the storage type is Performance or Capacity.
        # *   If the FileSystemType parameter is set to extreme, the storage type is standard or advance.
        # *   If the FileSystemType parameter is set to cpfs, the storage type is advance\_100 (100 MB/s/TiB baseline) or advance\_200 (200 MB/s/TiB baseline).
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeZonesResponseBodyZonesZoneInstanceTypes(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: list[DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType]

    def validate(self):
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesZoneInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k in m.get('InstanceType'):
                temp_model = DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBodyZonesZonePerformance(TeaModel):
    def __init__(self, protocol=None):
        self.protocol = protocol  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesZonePerformance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(self, capacity=None, instance_types=None, performance=None, zone_id=None):
        # This parameter is reserved. You can ignore this parameter.
        self.capacity = capacity  # type: DescribeZonesResponseBodyZonesZoneCapacity
        # The details about file system types.
        self.instance_types = instance_types  # type: DescribeZonesResponseBodyZonesZoneInstanceTypes
        # This parameter is reserved. You can ignore this parameter.
        self.performance = performance  # type: DescribeZonesResponseBodyZonesZonePerformance
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.capacity:
            self.capacity.validate()
        if self.instance_types:
            self.instance_types.validate()
        if self.performance:
            self.performance.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity.to_map()
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneCapacity()
            self.capacity = temp_model.from_map(m['Capacity'])
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeZonesResponseBodyZonesZoneInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('Performance') is not None:
            temp_model = DescribeZonesResponseBodyZonesZonePerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeZonesResponseBodyZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
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
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The queried zones.
        self.zones = zones  # type: DescribeZonesResponseBodyZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeZonesResponse, self).to_map()
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAndCleanRecycleBinRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAndCleanRecycleBinRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableAndCleanRecycleBinResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableAndCleanRecycleBinResponseBody, self).to_map()
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


class DisableAndCleanRecycleBinResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableAndCleanRecycleBinResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableAndCleanRecycleBinResponse, self).to_map()
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
            temp_model = DisableAndCleanRecycleBinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableNfsAclRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableNfsAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableNfsAclResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableNfsAclResponseBody, self).to_map()
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


class DisableNfsAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableNfsAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableNfsAclResponse, self).to_map()
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
            temp_model = DisableNfsAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSmbAclRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSmbAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DisableSmbAclResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSmbAclResponseBody, self).to_map()
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


class DisableSmbAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableSmbAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableSmbAclResponse, self).to_map()
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
            temp_model = DisableSmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableNfsAclRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableNfsAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class EnableNfsAclResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableNfsAclResponseBody, self).to_map()
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


class EnableNfsAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableNfsAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableNfsAclResponse, self).to_map()
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
            temp_model = EnableNfsAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRecycleBinRequest(TeaModel):
    def __init__(self, file_system_id=None, reserved_days=None):
        # The ID of the file system for which you want to enable the recycle bin feature.
        self.file_system_id = file_system_id  # type: str
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # Valid values: 1 to 180.
        # 
        # Default value: 3.
        self.reserved_days = reserved_days  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRecycleBinRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        return self


class EnableRecycleBinResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRecycleBinResponseBody, self).to_map()
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


class EnableRecycleBinResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableRecycleBinResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableRecycleBinResponse, self).to_map()
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
            temp_model = EnableRecycleBinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSmbAclRequest(TeaModel):
    def __init__(self, file_system_id=None, keytab=None, keytab_md_5=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The string that is generated after the system encodes the keytab file by using Base64.
        self.keytab = keytab  # type: str
        # The string that is generated after the system encodes the keytab file by using MD5.
        self.keytab_md_5 = keytab_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSmbAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.keytab is not None:
            result['Keytab'] = self.keytab
        if self.keytab_md_5 is not None:
            result['KeytabMd5'] = self.keytab_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Keytab') is not None:
            self.keytab = m.get('Keytab')
        if m.get('KeytabMd5') is not None:
            self.keytab_md_5 = m.get('KeytabMd5')
        return self


class EnableSmbAclResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSmbAclResponseBody, self).to_map()
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


class EnableSmbAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableSmbAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableSmbAclResponse, self).to_map()
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
            temp_model = EnableSmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectoryOrFilePropertiesRequest(TeaModel):
    def __init__(self, file_system_id=None, path=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The absolute path of the directory.
        # 
        # The path must start with a forward slash (/) and must be a path that exists in the mount target.
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDirectoryOrFilePropertiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class GetDirectoryOrFilePropertiesResponseBodyEntry(TeaModel):
    def __init__(self, atime=None, ctime=None, has_infrequent_access_file=None, inode=None, mtime=None, name=None,
                 retrieve_time=None, size=None, storage_type=None, type=None):
        # The time when the file was queried.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.atime = atime  # type: str
        # The time when the raw data was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.ctime = ctime  # type: str
        # Indicates whether the directory contains files stored in the IA storage medium.
        # 
        # This parameter is returned only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the IA storage medium.
        # *   false: The directory does not contain files stored in the IA storage medium.
        self.has_infrequent_access_file = has_infrequent_access_file  # type: bool
        # The file or directory inode.
        self.inode = inode  # type: str
        # The time when the file was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.mtime = mtime  # type: str
        # The name of the file or directory.
        self.name = name  # type: str
        # The time when the last data retrieval task was run.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.retrieve_time = retrieve_time  # type: str
        # The size of the file.
        # 
        # Unit: bytes.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.size = size  # type: long
        # The storage type of the file.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   InfrequentAccess: IA storage medium
        self.storage_type = storage_type  # type: str
        # The type of the query result.
        # 
        # Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDirectoryOrFilePropertiesResponseBodyEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atime is not None:
            result['ATime'] = self.atime
        if self.ctime is not None:
            result['CTime'] = self.ctime
        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.mtime is not None:
            result['MTime'] = self.mtime
        if self.name is not None:
            result['Name'] = self.name
        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')
        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')
        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDirectoryOrFilePropertiesResponseBody(TeaModel):
    def __init__(self, entry=None, request_id=None):
        # The details about the file or directory.
        self.entry = entry  # type: GetDirectoryOrFilePropertiesResponseBodyEntry
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.entry:
            self.entry.validate()

    def to_map(self):
        _map = super(GetDirectoryOrFilePropertiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = GetDirectoryOrFilePropertiesResponseBodyEntry()
            self.entry = temp_model.from_map(m['Entry'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectoryOrFilePropertiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDirectoryOrFilePropertiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDirectoryOrFilePropertiesResponse, self).to_map()
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
            temp_model = GetDirectoryOrFilePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecycleBinAttributeRequest(TeaModel):
    def __init__(self, file_system_id=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRecycleBinAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class GetRecycleBinAttributeResponseBodyRecycleBinAttribute(TeaModel):
    def __init__(self, enable_time=None, reserved_days=None, secondary_size=None, size=None, status=None):
        # The time at which the recycle bin was enabled.
        self.enable_time = enable_time  # type: str
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # If the recycle bin is disabled, 0 is returned for this parameter.
        self.reserved_days = reserved_days  # type: long
        # The size of the cold data that is dumped to the recycle bin. Unit: bytes.
        self.secondary_size = secondary_size  # type: long
        # The size of the files that are dumped to the recycle bin. Unit: bytes.
        self.size = size  # type: long
        # The status of the recycle bin.
        # 
        # Valid values:
        # 
        # *   Enable: The recycle bin is enabled.
        # *   Disable: The recycle bin is disabled.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRecycleBinAttributeResponseBodyRecycleBinAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        if self.secondary_size is not None:
            result['SecondarySize'] = self.secondary_size
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        if m.get('SecondarySize') is not None:
            self.secondary_size = m.get('SecondarySize')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRecycleBinAttributeResponseBody(TeaModel):
    def __init__(self, recycle_bin_attribute=None, request_id=None):
        # The description of the recycle bin.
        self.recycle_bin_attribute = recycle_bin_attribute  # type: GetRecycleBinAttributeResponseBodyRecycleBinAttribute
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.recycle_bin_attribute:
            self.recycle_bin_attribute.validate()

    def to_map(self):
        _map = super(GetRecycleBinAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recycle_bin_attribute is not None:
            result['RecycleBinAttribute'] = self.recycle_bin_attribute.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecycleBinAttribute') is not None:
            temp_model = GetRecycleBinAttributeResponseBodyRecycleBinAttribute()
            self.recycle_bin_attribute = temp_model.from_map(m['RecycleBinAttribute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRecycleBinAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRecycleBinAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRecycleBinAttributeResponse, self).to_map()
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
            temp_model = GetRecycleBinAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoriesAndFilesRequest(TeaModel):
    def __init__(self, directory_only=None, file_system_id=None, max_results=None, next_token=None, path=None,
                 storage_type=None):
        # Specifies whether to query only directories.
        # 
        # Valid values:
        # 
        # *   false (default): queries both directories and files
        # *   true: queries only directories
        self.directory_only = directory_only  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The maximum number of directories or files to include in the results of each query.
        # 
        # Valid values: 10 to 128.
        # 
        # Default value: 100.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The absolute path of the directory.
        # 
        # The path must start with a forward slash (/) and must be a path that exists in the mount target.
        self.path = path  # type: str
        # The storage type of the files.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDirectoriesAndFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_only is not None:
            result['DirectoryOnly'] = self.directory_only
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirectoryOnly') is not None:
            self.directory_only = m.get('DirectoryOnly')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ListDirectoriesAndFilesResponseBodyEntries(TeaModel):
    def __init__(self, atime=None, ctime=None, file_id=None, has_infrequent_access_file=None, inode=None, mtime=None,
                 name=None, owner=None, retrieve_time=None, size=None, storage_type=None, type=None):
        # The time when the file was queried.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.atime = atime  # type: str
        # The time when the raw data was modified.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.ctime = ctime  # type: str
        # The ID of the directory or file.
        self.file_id = file_id  # type: str
        # Indicates whether the directory contains files stored in the IA storage medium.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the IA storage medium.
        # *   false: The directory does not contain files stored in the IA storage medium.
        self.has_infrequent_access_file = has_infrequent_access_file  # type: bool
        # The file or directory inode.
        self.inode = inode  # type: str
        # The time when the file was modified.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.mtime = mtime  # type: str
        # The name of the file or directory.
        self.name = name  # type: str
        # The ID of the portable account. This parameter is returned and valid only if the value of the ProtocolType parameter is SMB and RAM-based access control is enabled.
        self.owner = owner  # type: str
        # The time when the last data retrieval task was run.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.retrieve_time = retrieve_time  # type: str
        # The size of the file.
        # 
        # Unit: bytes.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.size = size  # type: long
        # The storage type of the file.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        # 
        # Valid values:
        # 
        # *   InfrequentAccess: IA storage medium
        self.storage_type = storage_type  # type: str
        # The type of the query result.
        # 
        # Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDirectoriesAndFilesResponseBodyEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atime is not None:
            result['Atime'] = self.atime
        if self.ctime is not None:
            result['Ctime'] = self.ctime
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.mtime is not None:
            result['Mtime'] = self.mtime
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Atime') is not None:
            self.atime = m.get('Atime')
        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDirectoriesAndFilesResponseBody(TeaModel):
    def __init__(self, entries=None, next_token=None, request_id=None):
        # The details about the files or directories.
        self.entries = entries  # type: list[ListDirectoriesAndFilesResponseBodyEntries]
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDirectoriesAndFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDirectoriesAndFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDirectoriesAndFilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDirectoriesAndFilesResponse, self).to_map()
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
            temp_model = ListDirectoriesAndFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLifecycleRetrieveJobsRequest(TeaModel):
    def __init__(self, file_system_id=None, page_number=None, page_size=None, status=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: int
        # The status of the data retrieval task. Valid values:
        # 
        # *   active: The task is running.
        # *   canceled: The task is canceled.
        # *   completed: The task is completed.
        # *   failed: The task has failed.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLifecycleRetrieveJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs(TeaModel):
    def __init__(self, create_time=None, discovered_file_count=None, file_system_id=None, job_id=None, paths=None,
                 retrieved_file_count=None, status=None, update_time=None):
        # The time when the task was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time  # type: str
        # The total number of files that are read in the data retrieval task.
        self.discovered_file_count = discovered_file_count  # type: long
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the data retrieval task.
        self.job_id = job_id  # type: str
        self.paths = paths  # type: list[str]
        # The total number of files that are retrieved.
        self.retrieved_file_count = retrieved_file_count  # type: long
        # The status of the data retrieval task. Valid values:
        # 
        # *   active: The task is running.
        # *   canceled: The task is canceled.
        # *   completed: The task is completed.
        # *   failed: The task has failed.
        self.status = status  # type: str
        # The time when the task was updated.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.discovered_file_count is not None:
            result['DiscoveredFileCount'] = self.discovered_file_count
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.retrieved_file_count is not None:
            result['RetrievedFileCount'] = self.retrieved_file_count
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiscoveredFileCount') is not None:
            self.discovered_file_count = m.get('DiscoveredFileCount')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('RetrievedFileCount') is not None:
            self.retrieved_file_count = m.get('RetrievedFileCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListLifecycleRetrieveJobsResponseBody(TeaModel):
    def __init__(self, lifecycle_retrieve_jobs=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        # The details about the data retrieval tasks.
        self.lifecycle_retrieve_jobs = lifecycle_retrieve_jobs  # type: list[ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs]
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of data retrieval tasks.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.lifecycle_retrieve_jobs:
            for k in self.lifecycle_retrieve_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLifecycleRetrieveJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LifecycleRetrieveJobs'] = []
        if self.lifecycle_retrieve_jobs is not None:
            for k in self.lifecycle_retrieve_jobs:
                result['LifecycleRetrieveJobs'].append(k.to_map() if k else None)
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
        self.lifecycle_retrieve_jobs = []
        if m.get('LifecycleRetrieveJobs') is not None:
            for k in m.get('LifecycleRetrieveJobs'):
                temp_model = ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs()
                self.lifecycle_retrieve_jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLifecycleRetrieveJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLifecycleRetrieveJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLifecycleRetrieveJobsResponse, self).to_map()
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
            temp_model = ListLifecycleRetrieveJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecentlyRecycledDirectoriesRequest(TeaModel):
    def __init__(self, file_system_id=None, max_results=None, next_token=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The number of directories to return for each query.
        # 
        # Valid values: 10 to 1000.
        # 
        # Default value: 100.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        # 
        # If not all directories are returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecentlyRecycledDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListRecentlyRecycledDirectoriesResponseBodyEntries(TeaModel):
    def __init__(self, file_id=None, last_delete_time=None, name=None, path=None):
        # The ID of the directory.
        self.file_id = file_id  # type: str
        # The time when the directory was last deleted.
        self.last_delete_time = last_delete_time  # type: str
        # The name of the directory.
        self.name = name  # type: str
        # The absolute path to the directory.
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecentlyRecycledDirectoriesResponseBodyEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.last_delete_time is not None:
            result['LastDeleteTime'] = self.last_delete_time
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('LastDeleteTime') is not None:
            self.last_delete_time = m.get('LastDeleteTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListRecentlyRecycledDirectoriesResponseBody(TeaModel):
    def __init__(self, entries=None, next_token=None, request_id=None):
        # The information about the directories that are recently deleted.
        self.entries = entries  # type: list[ListRecentlyRecycledDirectoriesResponseBodyEntries]
        # A pagination token.
        # 
        # If not all directories are returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRecentlyRecycledDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListRecentlyRecycledDirectoriesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRecentlyRecycledDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRecentlyRecycledDirectoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRecentlyRecycledDirectoriesResponse, self).to_map()
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
            temp_model = ListRecentlyRecycledDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycleBinJobsRequest(TeaModel):
    def __init__(self, file_system_id=None, job_id=None, page_number=None, page_size=None, status=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The job ID.
        self.job_id = job_id  # type: str
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number  # type: long
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size  # type: long
        # The status of the job. Valid values:
        # 
        # *   Running: The job is running.
        # *   Defragmenting: The job is defragmenting data.
        # *   PartialSuccess: The job is partially completed.
        # *   Success: The job is completed.
        # *   Fail: The job failed.
        # *   Cancelled: The job is canceled.
        # *   All: all.Default value:All.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecycleBinJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRecycleBinJobsResponseBodyJobs(TeaModel):
    def __init__(self, create_time=None, error_code=None, error_message=None, file_id=None, file_name=None, id=None,
                 progress=None, status=None, type=None):
        # The time when the job was created.
        self.create_time = create_time  # type: str
        # The error code.
        # 
        # A valid value is returned only if you set the Status parameter to Fail or PartialSuccess.
        self.error_code = error_code  # type: str
        # The error message.
        # 
        # A valid value is returned only if you set the Status parameter to Fail or PartialSuccess.
        self.error_message = error_message  # type: str
        # The ID of the file or directory in the job.
        self.file_id = file_id  # type: str
        # The name of the file or directory that is associated with the job.
        self.file_name = file_name  # type: str
        # The job ID.
        self.id = id  # type: str
        # The progress of the job.
        # 
        # Valid values: 1 to 100.
        self.progress = progress  # type: str
        # The status of the job. Valid values:
        # 
        # *   Running: The job is running.
        # *   Defragmenting: The job is defragmenting data.
        # *   PartialSuccess: The job is partially completed.
        # *   Success: The job is completed.
        # *   Fail: The job failed.
        # *   Cancelled: The job is canceled.
        self.status = status  # type: str
        # The type of the job. Valid values:
        # 
        # *   Restore: a file restoration job
        # *   Delete: a file deletion job
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecycleBinJobsResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecycleBinJobsResponseBody(TeaModel):
    def __init__(self, jobs=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # The information about the jobs of the recycle bin.
        self.jobs = jobs  # type: list[ListRecycleBinJobsResponseBodyJobs]
        # The page number.
        self.page_number = page_number  # type: long
        # The number of jobs returned per page.
        self.page_size = page_size  # type: long
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of jobs.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRecycleBinJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
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
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListRecycleBinJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRecycleBinJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRecycleBinJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRecycleBinJobsResponse, self).to_map()
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
            temp_model = ListRecycleBinJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecycledDirectoriesAndFilesRequest(TeaModel):
    def __init__(self, file_id=None, file_system_id=None, max_results=None, next_token=None):
        # The ID of the directory that you want to query.
        # 
        # You can call the [ListRecycleBinJobs](~~264192~~) operation to query the value of the FileId parameter.
        self.file_id = file_id  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The number of files or directories to return for each query.
        # 
        # Valid values: 10 to 1000.
        # 
        # Default value: 100.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        # 
        # If all the files and directories are incompletely returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecycledDirectoriesAndFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListRecycledDirectoriesAndFilesResponseBodyEntries(TeaModel):
    def __init__(self, atime=None, ctime=None, delete_time=None, file_id=None, inode=None, mtime=None, name=None,
                 size=None, type=None):
        # The time when the file or directory was last accessed.
        self.atime = atime  # type: str
        # The time when the metadata was last modified.
        self.ctime = ctime  # type: str
        # The time when the file or directory was deleted.
        self.delete_time = delete_time  # type: str
        # The IDs of the files or directories.
        self.file_id = file_id  # type: str
        # The inode of the file or directory.
        self.inode = inode  # type: str
        # The time when the file or directory was last modified.
        self.mtime = mtime  # type: str
        # The name of the file or directory before it was deleted.
        self.name = name  # type: str
        # The size of the file. Unit: bytes.
        # 
        # The value 0 is returned for this parameter if Directory is returned for the Type parameter.
        self.size = size  # type: long
        # The type of the returned object. Valid values:
        # 
        # *   File
        # *   Directory
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecycledDirectoriesAndFilesResponseBodyEntries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atime is not None:
            result['ATime'] = self.atime
        if self.ctime is not None:
            result['CTime'] = self.ctime
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.inode is not None:
            result['Inode'] = self.inode
        if self.mtime is not None:
            result['MTime'] = self.mtime
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')
        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Inode') is not None:
            self.inode = m.get('Inode')
        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecycledDirectoriesAndFilesResponseBody(TeaModel):
    def __init__(self, entries=None, next_token=None, request_id=None):
        # The information about files or directories in the recycle bin.
        self.entries = entries  # type: list[ListRecycledDirectoriesAndFilesResponseBodyEntries]
        # A pagination token.
        # 
        # If all the files and directories are incompletely returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.entries:
            for k in self.entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRecycledDirectoriesAndFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Entries'] = []
        if self.entries is not None:
            for k in self.entries:
                result['Entries'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k in m.get('Entries'):
                temp_model = ListRecycledDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRecycledDirectoriesAndFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRecycledDirectoriesAndFilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRecycledDirectoriesAndFilesResponse, self).to_map()
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
            temp_model = ListRecycledDirectoriesAndFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        # 
        # Limits:
        # 
        # *   The tag key cannot be left empty.
        # *   Valid values of N: 1 to 20.
        # *   The tag key must be 1 to 128 characters in length.
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The tag value.
        # 
        # Limits:
        # 
        # *   Valid values of N: 1 to 20.
        # *   The tag value must be 1 to 128 characters in length.
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
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
    def __init__(self, next_token=None, resource_id=None, resource_type=None, tag=None):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The resource type. Set the value to filesystem.
        self.resource_type = resource_type  # type: str
        # The details about the tags.
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


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The resource ID.
        self.resource_id = resource_id  # type: str
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
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
        # A pagination token. It can be used in the next request to retrieve a new page of results. If the value of this parameter is null, no queries are performed after the current query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The list of resources.
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


class ModifyAccessGroupRequest(TeaModel):
    def __init__(self, access_group_name=None, description=None, file_system_type=None):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (\_), and hyphens (-).
        self.access_group_name = access_group_name  # type: str
        # The description of the permission group.
        # 
        # Limits:
        # 
        # *   By default, the description of the permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        return self


class ModifyAccessGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessGroupResponseBody, self).to_map()
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


class ModifyAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccessGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccessGroupResponse, self).to_map()
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
            temp_model = ModifyAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessRuleRequest(TeaModel):
    def __init__(self, access_group_name=None, access_rule_id=None, file_system_type=None,
                 ipv_6source_cidr_ip=None, priority=None, rwaccess_type=None, source_cidr_ip=None, user_access_type=None):
        # The name of the permission group.
        self.access_group_name = access_group_name  # type: str
        # The rule ID.
        self.access_rule_id = access_rule_id  # type: str
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type  # type: str
        # The IPv6 address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IPv6 IP address or CIDR block.
        # 
        # > *   Only Extreme NAS file systems that reside in the China (Hohhot) region support IPv6.
        # >*   Only permission groups that reside in virtual private clouds (VPCs) support IPv6.
        # >*   This parameter is unavailable if you specify the SourceCidrIp parameter.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip  # type: str
        # The priority of the rule.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 1, which indicates the highest priority.
        self.priority = priority  # type: int
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess_type = rwaccess_type  # type: str
        # The IP address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IP address or CIDR block.
        self.source_cidr_ip = source_cidr_ip  # type: str
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash: allows access from root users to the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
        self.user_access_type = user_access_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')
        return self


class ModifyAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessRuleResponseBody, self).to_map()
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


class ModifyAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccessRuleResponse, self).to_map()
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
            temp_model = ModifyAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoSnapshotPolicyRequest(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, auto_snapshot_policy_name=None, repeat_weekdays=None,
                 retention_days=None, time_points=None):
        # The ID of the automatic snapshot policy.
        # 
        # You can call the DescribeAutoSnapshotPolicies operation to view available automatic snapshot policies.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # The name of the automatic snapshot policy. If you do not specify this parameter, the policy name is not changed.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter.
        # *   The name can contain digits, letters, colons (:), underscores (\_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.auto_snapshot_policy_name = auto_snapshot_policy_name  # type: str
        # The days of a week on which auto snapshots are created.
        # 
        # Cycle: week.
        # 
        # Valid values: 1 to 7. The value 1 indicates Monday. If you want to create multiple auto snapshots within a week, you can specify multiple days from Monday to Sunday and separate the days with commas (,). You can specify a maximum of seven days.
        self.repeat_weekdays = repeat_weekdays  # type: str
        # The retention period of auto snapshots.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \-1 (default): Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified number of days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days  # type: int
        # The points in time at which auto snapshots are created.
        # 
        # Unit: hours.
        # 
        # Valid values: 0 to 23. The values from 0 to 23 indicate a total of 24 hours from 00:00 to 23:00. For example, the value 1 indicates 01:00. If you want to create multiple auto snapshots within a day, you can specify multiple points in time and separate the points in time with commas (,). You can specify a maximum of 24 points in time.
        self.time_points = time_points  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAutoSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id
        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name
        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays
        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days
        if self.time_points is not None:
            result['TimePoints'] = self.time_points
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')
        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')
        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')
        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')
        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')
        return self


class ModifyAutoSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        # 
        # Every response returns a unique request ID regardless of whether the request is successful.
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


class ModifyDataFlowRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, description=None, dry_run=None, file_system_id=None,
                 throughput=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with http:// or https://.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The maximum transmission bandwidth for a dataflow. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1,200
        # *   1,500
        # 
        # >  The dataflow throughput must be less than the I/O throughput of the file system.
        self.throughput = throughput  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        return self


class ModifyDataFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataFlowResponseBody, self).to_map()
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


class ModifyDataFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataFlowResponse, self).to_map()
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
            temp_model = ModifyDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataFlowAutoRefreshRequest(TeaModel):
    def __init__(self, auto_refresh_interval=None, auto_refresh_policy=None, client_token=None, data_flow_id=None,
                 dry_run=None, file_system_id=None):
        self.auto_refresh_interval = auto_refresh_interval  # type: long
        self.auto_refresh_policy = auto_refresh_policy  # type: str
        self.client_token = client_token  # type: str
        self.data_flow_id = data_flow_id  # type: str
        self.dry_run = dry_run  # type: bool
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataFlowAutoRefreshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval
        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')
        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ModifyDataFlowAutoRefreshResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataFlowAutoRefreshResponseBody, self).to_map()
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


class ModifyDataFlowAutoRefreshResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDataFlowAutoRefreshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataFlowAutoRefreshResponse, self).to_map()
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
            temp_model = ModifyDataFlowAutoRefreshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileSystemRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None):
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   It must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`. Example: `extreme-0015****`.
        # *   The IDs of Cloud Paralleled File System (CPFS) file systems must start with `cpfs-`. Example: `cpfs-125487****`.
        # >CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ModifyFileSystemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFileSystemResponseBody, self).to_map()
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


class ModifyFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFileSystemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFileSystemResponse, self).to_map()
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
            temp_model = ModifyFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFilesetRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, file_system_id=None, fset_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The fileset description.
        self.description = description  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. 
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The fileset ID.
        self.fset_id = fset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFilesetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.fset_id is not None:
            result['FsetId'] = self.fset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')
        return self


class ModifyFilesetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFilesetResponseBody, self).to_map()
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


class ModifyFilesetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFilesetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFilesetResponse, self).to_map()
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
            temp_model = ModifyFilesetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLDAPConfigRequest(TeaModel):
    def __init__(self, bind_dn=None, file_system_id=None, search_base=None, uri=None):
        self.bind_dn = bind_dn  # type: str
        self.file_system_id = file_system_id  # type: str
        self.search_base = search_base  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLDAPConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_dn is not None:
            result['BindDN'] = self.bind_dn
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.search_base is not None:
            result['SearchBase'] = self.search_base
        if self.uri is not None:
            result['URI'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindDN') is not None:
            self.bind_dn = m.get('BindDN')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SearchBase') is not None:
            self.search_base = m.get('SearchBase')
        if m.get('URI') is not None:
            self.uri = m.get('URI')
        return self


class ModifyLDAPConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLDAPConfigResponseBody, self).to_map()
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


class ModifyLDAPConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyLDAPConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLDAPConfigResponse, self).to_map()
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
            temp_model = ModifyLDAPConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLifecyclePolicyRequest(TeaModel):
    def __init__(self, file_system_id=None, lifecycle_policy_name=None, lifecycle_rule_name=None, path=None,
                 storage_type=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The name of the lifecycle policy.
        # 
        # The name must be 3 to 64 characters in length and can contain letters, digits, underscores (\_), and hyphens (-). The name must start with a letter.
        self.lifecycle_policy_name = lifecycle_policy_name  # type: str
        # The management rule that is associated with the lifecycle policy.
        # 
        # Valid values:
        # 
        # *   DEFAULT_ATIME\_14: Files that are not accessed in the last 14 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_30: Files that are not accessed in the last 30 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_60: Files that are not accessed in the last 60 days are dumped to the IA storage medium.
        # *   DEFAULT_ATIME\_90: Files that are not accessed in the last 90 days are dumped to the IA storage medium.
        self.lifecycle_rule_name = lifecycle_rule_name  # type: str
        # The absolute path of a directory with which the lifecycle policy is associated.
        # 
        # The path must start with a forward slash (/) and must be a path that exists in the mount target.
        self.path = path  # type: str
        # The storage type of the data that is dumped to the IA storage medium.
        # 
        # Default value: InfrequentAccess (IA).
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLifecyclePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name
        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name
        if self.path is not None:
            result['Path'] = self.path
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')
        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class ModifyLifecyclePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLifecyclePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyLifecyclePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyLifecyclePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLifecyclePolicyResponse, self).to_map()
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
            temp_model = ModifyLifecyclePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMountTargetRequest(TeaModel):
    def __init__(self, access_group_name=None, dual_stack_mount_target_domain=None, file_system_id=None,
                 mount_target_domain=None, status=None):
        # The name of the permission group that is attached to the mount target.
        self.access_group_name = access_group_name  # type: str
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # >  Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain  # type: str
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, `extreme-0015****`.
        self.file_system_id = file_system_id  # type: str
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain  # type: str
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyMountTargetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMountTargetResponseBody, self).to_map()
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


class ModifyMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMountTargetResponse, self).to_map()
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
            temp_model = ModifyMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtocolMountTargetRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, export_id=None, file_system_id=None,
                 protocol_service_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the export directory for the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not modify the specified export directory or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request.
        self.dry_run = dry_run  # type: bool
        # The ID of the export directory for the protocol service.
        self.export_id = export_id  # type: str
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtocolMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class ModifyProtocolMountTargetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtocolMountTargetResponseBody, self).to_map()
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


class ModifyProtocolMountTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyProtocolMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtocolMountTargetResponse, self).to_map()
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
            temp_model = ModifyProtocolMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtocolServiceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, file_system_id=None,
                 protocol_service_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. The dry run checks parameter validity and prerequisites. The dry run does not modify a file system or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run and does not modify the protocol service. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, a 200 HTTP status code is returned.
        # *   false (default): performs a dry run and performs the actual request. If the request passes the dry run, the service protocol is modified.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtocolServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')
        return self


class ModifyProtocolServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtocolServiceResponseBody, self).to_map()
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


class ModifyProtocolServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyProtocolServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtocolServiceResponse, self).to_map()
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
            temp_model = ModifyProtocolServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySmbAclRequest(TeaModel):
    def __init__(self, enable_anonymous_access=None, encrypt_data=None, file_system_id=None, home_dir_path=None,
                 keytab=None, keytab_md_5=None, reject_unencrypted_access=None, super_admin_sid=None):
        # Specifies whether to allow anonymous access. Valid values:
        # 
        # *   true: The file system allows anonymous access.
        # *   false (default): The file system denies anonymous access.
        self.enable_anonymous_access = enable_anonymous_access  # type: bool
        # Specifies whether to enable encryption in transit. Valid values:
        # 
        # *   true: enables encryption in transit.
        # *   false (default): disables encryption in transit.
        self.encrypt_data = encrypt_data  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The home directory of each user. Each user-specific home directory must meet the following requirements:
        # 
        # *   Each segment starts with a forward slash (/) or a backward slash (\\).
        # *   Each segment does not contain the following special characters: `<>":|?*`.
        # *   Each segment is 0 to 255 characters in length.
        # *   The total length is 0 to 32,767 characters.
        # 
        # For example, if you create a user named A and the home directory is `/home`, the file system automatically creates a directory named `/home/A` when User A logs on to the file system. If the `/home/A` directory already exists, the file system does not create the directory.
        # 
        # > User A must have the permissions to create folders in the \home directory. Otherwise, the file system cannot create the `/home/A` directory when User A logs on to the file system.
        self.home_dir_path = home_dir_path  # type: str
        # The string that is generated after the system encodes the keytab file by using Base64.
        self.keytab = keytab  # type: str
        # The string that is generated after the system encodes the keytab file by using MD5.
        self.keytab_md_5 = keytab_md_5  # type: str
        # Specifies whether to deny access from non-encrypted clients. Valid values:
        # 
        # *   true: The file system denies access from non-encrypted clients.
        # *   false (default): The file system allows access from non-encrypted clients.
        self.reject_unencrypted_access = reject_unencrypted_access  # type: bool
        # The ID of a super admin. The ID must meet the following requirements:
        # 
        # *   The ID starts with `S` and does not contain letters except S.
        # *   The ID contains at least three hyphens (-) as delimiters.
        # 
        # Examples: `S-1-5-22` and `S-1-5-22-23`.
        self.super_admin_sid = super_admin_sid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySmbAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_anonymous_access is not None:
            result['EnableAnonymousAccess'] = self.enable_anonymous_access
        if self.encrypt_data is not None:
            result['EncryptData'] = self.encrypt_data
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.home_dir_path is not None:
            result['HomeDirPath'] = self.home_dir_path
        if self.keytab is not None:
            result['Keytab'] = self.keytab
        if self.keytab_md_5 is not None:
            result['KeytabMd5'] = self.keytab_md_5
        if self.reject_unencrypted_access is not None:
            result['RejectUnencryptedAccess'] = self.reject_unencrypted_access
        if self.super_admin_sid is not None:
            result['SuperAdminSid'] = self.super_admin_sid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableAnonymousAccess') is not None:
            self.enable_anonymous_access = m.get('EnableAnonymousAccess')
        if m.get('EncryptData') is not None:
            self.encrypt_data = m.get('EncryptData')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('HomeDirPath') is not None:
            self.home_dir_path = m.get('HomeDirPath')
        if m.get('Keytab') is not None:
            self.keytab = m.get('Keytab')
        if m.get('KeytabMd5') is not None:
            self.keytab_md_5 = m.get('KeytabMd5')
        if m.get('RejectUnencryptedAccess') is not None:
            self.reject_unencrypted_access = m.get('RejectUnencryptedAccess')
        if m.get('SuperAdminSid') is not None:
            self.super_admin_sid = m.get('SuperAdminSid')
        return self


class ModifySmbAclResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySmbAclResponseBody, self).to_map()
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


class ModifySmbAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySmbAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySmbAclResponse, self).to_map()
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
            temp_model = ModifySmbAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenNASServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The order ID.
        self.order_id = order_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenNASServiceResponseBody, self).to_map()
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


class OpenNASServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenNASServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenNASServiceResponse, self).to_map()
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
            temp_model = OpenNASServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClientFromBlackListRequest(TeaModel):
    def __init__(self, client_ip=None, client_token=None, file_system_id=None, region_id=None):
        self.client_ip = client_ip  # type: str
        self.client_token = client_token  # type: str
        self.file_system_id = file_system_id  # type: str
        # The ID of the request.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClientFromBlackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveClientFromBlackListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClientFromBlackListResponseBody, self).to_map()
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


class RemoveClientFromBlackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveClientFromBlackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveClientFromBlackListResponse, self).to_map()
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
            temp_model = RemoveClientFromBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key (TagKey) of Tag N. Each tag that you want to remove includes a TagKey and TagValue. You can specify 1 to 10 tags at a time. A TagKey cannot be an empty string, but a TagValue can be an empty string.
        self.key = key  # type: str
        # The value (TagValue) of Tag N. Each tag that you want to remove includes a TagKey and TagValue. You can specify a maximum of 5 tags at a time. A TagKey cannot be an empty string, but a TagValue can be an empty string.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTagsRequestTag, self).to_map()
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


class RemoveTagsRequest(TeaModel):
    def __init__(self, file_system_id=None, tag=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        self.tag = tag  # type: list[RemoveTagsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = RemoveTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class RemoveTagsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveTagsResponseBody, self).to_map()
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


class RemoveTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveTagsResponse, self).to_map()
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
            temp_model = RemoveTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetFileSystemRequest(TeaModel):
    def __init__(self, file_system_id=None, snapshot_id=None):
        # The ID of the advanced Extreme NAS file system.
        self.file_system_id = file_system_id  # type: str
        # The snapshot ID.
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetFileSystemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetFileSystemResponseBody, self).to_map()
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


class ResetFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetFileSystemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetFileSystemResponse, self).to_map()
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
            temp_model = ResetFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryLifecycleRetrieveJobRequest(TeaModel):
    def __init__(self, job_id=None):
        # The ID of the data retrieval task.
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryLifecycleRetrieveJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class RetryLifecycleRetrieveJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryLifecycleRetrieveJobResponseBody, self).to_map()
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


class RetryLifecycleRetrieveJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RetryLifecycleRetrieveJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryLifecycleRetrieveJobResponse, self).to_map()
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
            temp_model = RetryLifecycleRetrieveJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDirQuotaRequest(TeaModel):
    def __init__(self, file_count_limit=None, file_system_id=None, path=None, quota_type=None, size_limit=None,
                 user_id=None, user_type=None):
        # The number of files that a user can create in the directory.
        # 
        # This number includes the number of files, subdirectories, and special files.
        # 
        # If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters.
        self.file_count_limit = file_count_limit  # type: long
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The absolute path of a directory.
        self.path = path  # type: str
        # The type of the quota.
        # 
        # Valid values:
        # 
        # *   Accounting: a statistical quota. If you set this parameter to Accounting, NAS calculates only the storage usage of the directory.
        # *   Enforcement: a restricted quota. If you set this parameter to Enforcement and the storage usage exceeds the quota, you can no longer create files or subdirectories for the directory, or write data to the directory.
        self.quota_type = quota_type  # type: str
        # The size of files that a user can create in the directory.
        # 
        # Unit: GiB.
        # 
        # If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters.
        self.size_limit = size_limit  # type: long
        # The UID or GID of the user for whom you want to set a directory quota.
        # 
        # This parameter is required and valid only if the UserType parameter is set to Uid or Gid.
        # 
        # Examples:
        # 
        # *   If you want to set a directory quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500.
        # *   If you want to set a directory quota for a user group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100.
        self.user_id = user_id  # type: str
        # The type of the user.
        # 
        # Valid values:
        # 
        # *   Uid: user ID
        # *   Gid: user group ID
        # *   AllUsers: all users
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDirQuotaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.path is not None:
            result['Path'] = self.path
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class SetDirQuotaResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDirQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDirQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDirQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDirQuotaResponse, self).to_map()
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
            temp_model = SetDirQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDataFlowRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, dry_run=None, file_system_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. The dry run does not enable the specified dataflow or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, service limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified dataflow is enabled.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDataFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class StartDataFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDataFlowResponseBody, self).to_map()
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


class StartDataFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartDataFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDataFlowResponse, self).to_map()
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
            temp_model = StartDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDataFlowRequest(TeaModel):
    def __init__(self, client_token=None, data_flow_id=None, dry_run=None, file_system_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token  # type: str
        # The dataflow ID.
        self.data_flow_id = data_flow_id  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDataFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class StopDataFlowResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDataFlowResponseBody, self).to_map()
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


class StopDataFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopDataFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDataFlowResponse, self).to_map()
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
            temp_model = StopDataFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the resource.
        # 
        # Limits:
        # 
        # *   The tag key cannot be left empty.
        # *   Valid values of N: 1 to 20.
        # *   The tag key must be 1 to 128 characters in length.
        # *   The tag key cannot start with `aliyun` or `acs:`.
        # *   The tag key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of tag N to add to the resource.
        # 
        # Limits:
        # 
        # *   Valid values of N: 1 to 20.
        # *   The tag value must be 1 to 128 characters in length.
        # *   The tag value cannot start with `aliyun` or `acs:`.
        # *   The tag value cannot contain `http://` or `https://`.
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
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        # The resource IDs. Valid values of N: 1 to 50.
        self.resource_id = resource_id  # type: list[str]
        # The resource type. Set the value to filesystem.
        self.resource_type = resource_type  # type: str
        # The details about the tags.
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
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, resource_id=None, resource_type=None, tag_key=None):
        # Specifies whether to remove all tags from the file system.
        # 
        # This parameter is valid only if the TagKey.N parameter is not specified.
        # 
        # Valid values:
        # 
        # *   true: All tags are removed from the file system. If the file system does not have tags, a success message is returned.
        # *   false (default): No tags are removed from the file system and a success message is returned.
        self.all = all  # type: bool
        # The resource IDs. Valid values of N: 1 to 50.
        self.resource_id = resource_id  # type: list[str]
        # The resource type.
        # 
        # Set the value to filesystem.
        self.resource_type = resource_type  # type: str
        # The tag keys of the resources. Valid values of N: 1 to 20.
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


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecycleBinAttributeRequest(TeaModel):
    def __init__(self, file_system_id=None, reserved_days=None):
        # The ID of the file system.
        self.file_system_id = file_system_id  # type: str
        # The retention period of the files in the recycle bin. Unit: days.
        # 
        # Valid values: 1 to 180.
        # 
        # Default value: 3.
        self.reserved_days = reserved_days  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecycleBinAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.reserved_days is not None:
            result['ReservedDays'] = self.reserved_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('ReservedDays') is not None:
            self.reserved_days = m.get('ReservedDays')
        return self


class UpdateRecycleBinAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecycleBinAttributeResponseBody, self).to_map()
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


class UpdateRecycleBinAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRecycleBinAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRecycleBinAttributeResponse, self).to_map()
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
            temp_model = UpdateRecycleBinAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeFileSystemRequest(TeaModel):
    def __init__(self, capacity=None, client_token=None, dry_run=None, file_system_id=None):
        # The desired capacity of the file system.
        # 
        # The desired capacity of the file system must be greater than the original capacity of the file system. Unit: GiB.
        self.capacity = capacity  # type: long
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](~~25693~~)
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run  # type: bool
        # The ID of the file system.
        # 
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, extreme-0015\*\*\*\*.
        # *   The IDs of CPFS file systems must start with `cpfs-`, for example, cpfs-125487\*\*\*\*.
        # 
        # > CPFS file systems are available only on the China site (aliyun.com).
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class UpgradeFileSystemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeFileSystemResponseBody, self).to_map()
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


class UpgradeFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeFileSystemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeFileSystemResponse, self).to_map()
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
            temp_model = UpgradeFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


